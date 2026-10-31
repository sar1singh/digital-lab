#!/usr/bin/env python3
"""
Stock Video & Media Asset Scout (Rule 9 & Rule 17)
===================================================
Searches and downloads free royalty-free B-roll stock footage, archival images,
and audio from Pexels, Pixabay, and Wikimedia Commons directly into the shared asset vault.

Usage:
    # 1. Search & download 1080p stock videos from Pexels / Pixabay:
    python tools/stock_scout.py --query "luxury hotel skyline" --limit 2 --type video

    # 2. Search & download public domain archival media from Wikimedia Commons:
    python tools/stock_scout.py --query "san francisco street 2000s" --limit 3 --source wikimedia

    # 3. Download to custom destination:
    python tools/stock_scout.py --query "money counting cash" --out assets/broll/
"""

import os
import sys
import json
import urllib.parse
import urllib.request
import argparse
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr.encoding != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def get_headless_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_ASSET_DIR = os.path.join(SHARED_DIR, "assets", "broll")

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY", "")

def download_file_stream(url, out_path):
    print(f"  [Downloading] {url[:80]}...")
    headers = {"User-Agent": "ThinkLate-Scout/1.0 (contact@thinklate.internal)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response, open(out_path, 'wb') as out_file:
            chunk_size = 16384
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
        size_mb = os.path.getsize(out_path) / (1024 * 1024)
        print(f"  [Saved] -> {os.path.basename(out_path)} ({size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"  [Failed] Error downloading: {e}")
        return False

def search_wikimedia_commons(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
    """Searches Wikimedia Commons API (no API key required)."""
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🏛️ Searching Wikimedia Commons for '{query}'...")
    
    endpoint = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": "6",
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|mime|size",
        "format": "json"
    }
    url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    headers = {"User-Agent": "ThinkLate-AssetScout/1.0"}
    req = urllib.request.Request(url, headers=headers)

    downloaded = []
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        for page_id, page in pages.items():
            info = page.get("imageinfo", [{}])[0]
            media_url = info.get("url")
            if media_url:
                title = page.get("title", f"wiki_{page_id}").replace("File:", "").replace(" ", "_")
                parsed_path = urllib.parse.urlparse(media_url).path
                ext = os.path.splitext(parsed_path)[1] or ".jpg"
                clean_name = "".join(c for c in title if c.isalnum() or c in "._-")
                if not clean_name.lower().endswith(ext.lower()):
                    clean_name += ext
                save_path = os.path.join(output_dir, clean_name)
                if download_file_stream(media_url, save_path):
                    downloaded.append(save_path)
    except Exception as e:
        print(f"Wikimedia API Error: {e}")
    return downloaded

def search_pexels_videos(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
    """Searches Pexels Videos API (requires PEXELS_API_KEY)."""
    if not PEXELS_API_KEY:
        print("  [Notice] PEXELS_API_KEY environment variable not set. Skipping Pexels.")
        return []

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🎬 Searching Pexels Videos for '{query}'...")
    url = f"https://api.pexels.com/videos/search?query={urllib.parse.quote(query)}&per_page={limit}&orientation=landscape"
    headers = {
        "Authorization": PEXELS_API_KEY,
        "User-Agent": "ThinkLate-Scout/1.0"
    }
    req = urllib.request.Request(url, headers=headers)
    downloaded = []
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        videos = data.get("videos", [])
        for vid in videos:
            vid_id = vid.get("id")
            files = vid.get("video_files", [])
            # Sort by width to get 1080p / highest available
            sorted_files = sorted(files, key=lambda f: f.get("width") or 0, reverse=True)
            if sorted_files:
                target_url = sorted_files[0].get("link")
                save_name = f"pexels_{vid_id}_1080p.mp4"
                save_path = os.path.join(output_dir, save_name)
                if download_file_stream(target_url, save_path):
                    downloaded.append(save_path)
    except Exception as e:
        print(f"Pexels API Error: {e}")
    return downloaded

def search_pixabay_videos(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
    """Searches Pixabay Videos API (requires PIXABAY_API_KEY)."""
    if not PIXABAY_API_KEY:
        print("  [Notice] PIXABAY_API_KEY environment variable not set. Skipping Pixabay.")
        return []

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🎬 Searching Pixabay Videos for '{query}'...")
    url = f"https://pixabay.com/api/videos/?key={PIXABAY_API_KEY}&q={urllib.parse.quote(query)}&per_page={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "ThinkLate-Scout/1.0"})
    downloaded = []
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        hits = data.get("hits", [])
        for hit in hits:
            hit_id = hit.get("id")
            vids = hit.get("videos", {})
            target = vids.get("large", {}) or vids.get("medium", {})
            target_url = target.get("url")
            if target_url:
                save_name = f"pixabay_{hit_id}.mp4"
                save_path = os.path.join(output_dir, save_name)
                if download_file_stream(target_url, save_path):
                    downloaded.append(save_path)
    except Exception as e:
        print(f"Pixabay API Error: {e}")
    return downloaded

def scout_media(query, limit=2, output_dir=DEFAULT_ASSET_DIR, source="all"):
    print("=" * 70)
    print("🔍 ThinkLate Universal Media & B-Roll Scout")
    print(f"  Query:      '{query}'")
    print(f"  Target Dir: {output_dir}")
    print(f"  Source:     {source}")
    print("=" * 70)

    results = []
    if source in ("all", "pexels"):
        results.extend(search_pexels_videos(query, limit, output_dir))
    if source in ("all", "pixabay"):
        results.extend(search_pixabay_videos(query, limit, output_dir))
    if source in ("all", "wikimedia"):
        results.extend(search_wikimedia_commons(query, limit, output_dir))

    print(f"\n🎉 Sourced {len(results)} media asset(s) ready for production.")
    return results

def main():
    parser = argparse.ArgumentParser(description="Stock Video & Media Asset Scout")
    parser.add_argument("--query", required=True, help="Search query (e.g. 'luxury hotel', 'san francisco 2008')")
    parser.add_argument("--limit", type=int, default=2, help="Number of assets to download (default: 2)")
    parser.add_argument("--out", default=DEFAULT_ASSET_DIR, help="Destination directory")
    parser.add_argument("--source", default="all", choices=["all", "pexels", "pixabay", "wikimedia"], help="Media source")
    args = parser.parse_args()

    scout_media(args.query, args.limit, args.out, args.source)

if __name__ == "__main__":
    main()
