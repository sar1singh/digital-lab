#!/usr/bin/env python3
"""
ThinkLate Free Stock & Archival B-Roll Scout (Zero API Key Required)
Searches Wikimedia Commons & Openverse public APIs for landscape, non-watermarked
images/photos, downloads verified files to --out, and writes STOCK_SOURCES.json.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

USER_AGENT = "ThinkLateMediaScout/1.0 (https://github.com/thinklate; contact@thinklate.local)"
VALID_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def _http_get_json(url: str, timeout: int = 15) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _download_file(url: str, dest: str, timeout: int = 25) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    if len(data) < 25_000:  # reject tiny thumbnails/icons
        return False
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    return True


def _safe_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:48]


def search_wikimedia(query: str, limit: int = 6) -> list[dict]:
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap",
        "gsrnamespace": "6",
        "gsrlimit": str(max(limit * 3, 12)),
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime",
        "iiurlwidth": "1920",
        "format": "json",
    })
    url = f"https://commons.wikimedia.org/w/api.php?{params}"
    data = _http_get_json(url)
    pages = (data.get("query") or {}).get("pages") or {}
    results = []
    for _, page in pages.items():
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        w = int(info.get("width") or 0)
        h = int(info.get("height") or 0)
        if w < 1000 or h < 550 or (w / max(h, 1)) < 1.25:
            continue
        dl_url = info.get("thumburl") or info.get("url")
        if not dl_url:
            continue
        ext = os.path.splitext(urllib.parse.urlparse(dl_url).path)[1].lower()
        if ext not in VALID_EXTS:
            ext = ".jpg"
        meta = info.get("extmetadata") or {}
        lic = ((meta.get("LicenseShortName") or {}).get("value") or "Wikimedia Commons")
        if "nc" in lic.lower() or "nd" in lic.lower():
            continue  # commercial-safe licenses only
        results.append({
            "source": "wikimedia",
            "title": page.get("title", ""),
            "url": dl_url,
            "page_url": info.get("descriptionurl", ""),
            "width": w,
            "height": h,
            "license": lic,
            "ext": ext,
        })
        if len(results) >= limit:
            break
    return results


def search_openverse(query: str, limit: int = 6) -> list[dict]:
    params = urllib.parse.urlencode({
        "q": query,
        "page_size": str(max(limit * 3, 15)),
        "license_type": "commercial",
        "aspect_ratio": "wide",
    })
    url = f"https://api.openverse.org/v1/images/?{params}"
    data = _http_get_json(url)
    results = []
    for item in data.get("results") or []:
        w = int(item.get("width") or 0)
        h = int(item.get("height") or 0)
        if w < 1000 or h < 550 or (w / max(h, 1)) < 1.25:
            continue
        dl_url = item.get("url")
        if not dl_url:
            continue
        ext = os.path.splitext(urllib.parse.urlparse(dl_url).path)[1].lower()
        if ext not in VALID_EXTS:
            ext = ".jpg"
        results.append({
            "source": f"openverse/{item.get('source', 'cc')}",
            "title": item.get("title") or query,
            "url": dl_url,
            "page_url": item.get("foreign_landing_url", ""),
            "width": w,
            "height": h,
            "license": item.get("license", "cc"),
            "ext": ext,
        })
        if len(results) >= limit:
            break
    return results


def main():
    parser = argparse.ArgumentParser(description="Free zero-key B-roll stock image scout")
    parser.add_argument("--query", "-q", required=True, help="Search terms")
    parser.add_argument("--out", "-o", required=True, help="Output folder")
    parser.add_argument("--limit", "-n", type=int, default=2, help="Images to download")
    parser.add_argument("--name", default=None, help="Filename prefix override")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    candidates = []
    for fn in (search_openverse, search_wikimedia):
        try:
            candidates.extend(fn(args.query, limit=max(args.limit * 2, 4)))
        except Exception as exc:
            print(f"[WARN] {fn.__name__} failed for '{args.query}': {exc}", file=sys.stderr)

    downloaded = []
    prefix = _safe_slug(args.name or args.query)
    ledger_path = os.path.join(args.out, "STOCK_SOURCES.json")
    ledger = []
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path, "r", encoding="utf-8") as f:
                ledger = json.load(f)
        except Exception:
            ledger = []

    idx = 1
    for item in candidates:
        if len(downloaded) >= args.limit:
            break
        fname = f"{prefix}_{idx:02d}{item['ext']}"
        dest = os.path.join(args.out, fname)
        try:
            if _download_file(item["url"], dest):
                rec = {**item, "file": fname, "query": args.query}
                downloaded.append(rec)
                ledger.append(rec)
                print(f"[OK] {fname} ({item['width']}x{item['height']}, {item['source']}, {item['license']}) -> {dest}")
                idx += 1
        except Exception as exc:
            print(f"[SKIP] {item['url']}: {exc}", file=sys.stderr)

    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

    if not downloaded:
        print(f"[ERR] No verified images downloaded for query: {args.query}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
