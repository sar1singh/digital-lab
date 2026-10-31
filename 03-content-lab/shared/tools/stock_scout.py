#!/usr/bin/env python3
"""
Universal Media, B-Roll & Meme Scout (Rule 9 & Rule 17)
========================================================
Autonomously searches and downloads 100% free royalty-free B-roll stock footage,
viral memes, and archival video without requiring broken or paused API keys.

Primary Free Sources (Zero API Keys Needed):
  1. Mixkit (mixkit.co) - Direct 1080p MP4 stock footage
  2. Coverr (coverr.co) - Direct MP4 stock footage & community AI plates
  3. YouTube Memes & Clips (via yt-dlp) - Exact 3-5s pop-culture reaction clips
  4. Wikimedia Commons - Historical documentary photos & public domain media

Optional Sources (If free keys exist):
  5. Pexels & Pixabay (via .env)

Usage:
    # 1. Search & download 1080p stock video (Mixkit / Coverr - zero keys needed):
    python tools/stock_scout.py --query "money" --limit 2

    # 2. Search & download a reaction meme into shared meme vault:
    python tools/stock_scout.py --meme "steve carell no god" --name steve_carell_no

    # 3. Search public domain historical archives:
    python tools/stock_scout.py --query "san francisco street" --source wikimedia
"""

import os
import sys
import json
import re
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_ASSET_DIR = os.path.join(SHARED_DIR, "assets", "broll")
MEME_VAULT_DIR = os.path.join(SHARED_DIR, "assets", "memes")

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def get_headless_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

def download_file_stream(url, out_path):
    print(f"  [Downloading] {url[:85]}...")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as response, open(out_path, 'wb') as out_file:
            chunk_size = 32768
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
        size_mb = os.path.getsize(out_path) / (1024 * 1024)
        print(f"  ✅ [Saved] -> {os.path.basename(out_path)} ({size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"  ❌ [Failed] Error downloading: {e}")
        return False

# -------------------------------------------------------------
# 1. MIXKIT (100% Free 1080p Stock Video - Zero API Keys)
# -------------------------------------------------------------
def search_mixkit_videos(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🎬 Searching Mixkit (Free 1080p Stock) for '{query}'...")
    
    clean_q = urllib.parse.quote(query.lower().replace(" ", "-"))
    url = f"https://mixkit.co/free-stock-video/{clean_q}/"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    
    downloaded = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        
        # Match all mp4 links
        matches = re.findall(r'https://assets\.mixkit\.co/videos/[^"\'\s]+\.mp4', html)
        unique_matches = list(dict.fromkeys(matches))
        
        # Prefer 1080p or 720p
        hd_links = [m for m in unique_matches if "-1080.mp4" in m]
        if not hd_links:
            hd_links = [m for m in unique_matches if "-720.mp4" in m or ".mp4" in m]
            
        for target_url in hd_links[:limit]:
            fname = os.path.basename(urllib.parse.urlparse(target_url).path)
            out_file = os.path.join(output_dir, f"mixkit_{query.replace(' ', '_')}_{fname}")
            if download_file_stream(target_url, out_file):
                downloaded.append(out_file)
    except Exception as e:
        print(f"  Mixkit notice: {e}")
    return downloaded

# -------------------------------------------------------------
# 2. COVERR (100% Free Stock Video & AI Plates - Zero API Keys)
# -------------------------------------------------------------
def search_coverr_videos(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🎬 Searching Coverr (Free Stock & AI Plates) for '{query}'...")
    
    clean_q = urllib.parse.quote_plus(query)
    url = f"https://coverr.co/s?q={clean_q}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    
    downloaded = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        
        matches = re.findall(r'https://cdn\.coverr\.co/videos/[^"\'\s]+\.mp4', html)
        unique_matches = list(dict.fromkeys(matches))
        
        # Prefer 1080p or 720p
        hd_links = [m for m in unique_matches if "1080p" in m or "720p" in m]
        if not hd_links:
            hd_links = unique_matches
            
        for target_url in hd_links[:limit]:
            fname = os.path.basename(urllib.parse.urlparse(target_url).path)
            out_file = os.path.join(output_dir, f"coverr_{query.replace(' ', '_')}_{fname}")
            if download_file_stream(target_url, out_file):
                downloaded.append(out_file)
    except Exception as e:
        print(f"  Coverr notice: {e}")
    return downloaded

# -------------------------------------------------------------
# 3. YOUTUBE REACTION MEMES & CLIPS (via yt-dlp)
# -------------------------------------------------------------
def search_and_download_meme(query, name=None, duration=5, output_dir=MEME_VAULT_DIR):
    os.makedirs(output_dir, exist_ok=True)
    if not name:
        name = re.sub(r'[^a-zA-Z0-9_]', '_', query.lower()).strip('_')[:35]
    out_file = os.path.join(output_dir, f"{name}.mp4")
    
    print(f"\n🎭 Sourcing Reaction Meme for '{query}' -> {name}.mp4...")
    target = f"ytsearch1:{query} meme short"
    cmd = [
        "yt-dlp",
        target,
        "-f", "mp4[height<=720]/best[height<=720]/best",
        "--download-sections", f"*00:00-00:{int(duration):02d}",
        "-o", out_file,
        "--no-playlist",
        "--force-overwrites"
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **get_headless_kwargs())
        if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
            size_kb = os.path.getsize(out_file) / 1024
            print(f"  ✅ [Meme Vaulted] -> {out_file} ({size_kb:.1f} KB)")
            return [out_file]
        else:
            print(f"  ❌ Meme download failed: {res.stderr[:200]}")
            return []
    except Exception as e:
        print(f"  yt-dlp exception: {e}")
        return []

# -------------------------------------------------------------
# 4. WIKIMEDIA COMMONS (Free Historical / Documentary Media)
# -------------------------------------------------------------
def search_wikimedia_commons(query, limit=2, output_dir=DEFAULT_ASSET_DIR):
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
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    downloaded = []
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        for _, page in pages.items():
            info_list = page.get("imageinfo", [])
            if not info_list:
                continue
            media_url = info_list[0].get("url")
            parsed_path = urllib.parse.urlparse(media_url).path
            ext = os.path.splitext(parsed_path)[1] or ".jpg"
            title_clean = page.get("title", "wikimedia_asset").replace("File:", "").replace(" ", "_")
            title_clean = "".join(c for c in title_clean if c.isalnum() or c in ("_", "-")).rstrip()
            out_filename = f"{title_clean}{ext}"
            out_filepath = os.path.join(output_dir, out_filename)
            if download_file_stream(media_url, out_filepath):
                downloaded.append(out_filepath)
    except Exception as e:
        print(f"Wikimedia API Error: {e}")
    return downloaded

def scout_media(query, limit=2, output_dir=DEFAULT_ASSET_DIR, source="all", meme_name=None):
    print("=" * 70)
    print("🔍 ThinkLate Zero-Key Media, B-Roll & Meme Scout")
    print(f"  Target:     '{query}'")
    print(f"  Output Dir: {output_dir}")
    print(f"  Source:     {source}")
    print("=" * 70)

    results = []
    if source == "meme":
        return search_and_download_meme(query, name=meme_name, duration=limit)

    # 1. Primary Zero-Key Free Sources
    if source in ("all", "mixkit"):
        results.extend(search_mixkit_videos(query, limit, output_dir))
    if source in ("all", "coverr") and len(results) < limit:
        results.extend(search_coverr_videos(query, limit - len(results), output_dir))
    if source in ("all", "wikimedia") and len(results) < limit:
        results.extend(search_wikimedia_commons(query, limit - len(results), output_dir))

    print(f"\n🎉 Sourced {len(results)} high-quality asset(s) ready for production.")
    return results

def main():
    parser = argparse.ArgumentParser(description="Zero-Key Free Stock Video & Meme Scout")
    parser.add_argument("--query", required=True, help="Search query (e.g. 'luxury hotel', 'money', 'pointing')")
    parser.add_argument("--limit", type=int, default=2, help="Number of assets to download (default: 2)")
    parser.add_argument("--out", default=DEFAULT_ASSET_DIR, help="Destination directory")
    parser.add_argument("--source", default="all", choices=["all", "mixkit", "coverr", "wikimedia", "meme"], help="Source engine")
    parser.add_argument("--name", help="Custom filename base for memes")
    args = parser.parse_args()

    scout_media(args.query, args.limit, args.out, args.source, args.name)

if __name__ == "__main__":
    main()
