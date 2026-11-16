#!/usr/bin/env python3
"""
Meme & Satirical Reaction Clip Scout (ThinkLate Infotainment Engine)
=====================================================================
Autonomously searches and downloads viral pop-culture memes, movie reaction clips,
and comedy B-roll into the shared vault for witty, satirical infotainment pacing.

Usage:
    # 1. Download a meme by search query:
    python tools/meme_scout.py --query "steve carell no god please no" --name steve_carell_no

    # 2. List all available local reaction memes:
    python tools/meme_scout.py --list

    # 3. Download a 4-second clip from any YouTube URL:
    python tools/meme_scout.py --url "https://www.youtube.com/watch?v=..." --start 00:02 --duration 4 --name my_clip
"""

import os
import sys
import argparse
import subprocess
import re

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
MEME_VAULT_DIR = os.path.join(SHARED_DIR, "assets", "memes")

def download_meme_clip(query=None, url=None, name=None, duration=None, start_sec=0, full=False):
    os.makedirs(MEME_VAULT_DIR, exist_ok=True)
    
    if not name:
        clean_base = re.sub(r'[^a-zA-Z0-9_]', '_', (query or "meme_clip").lower()).strip('_')
        name = clean_base[:35]
    
    out_file = os.path.join(MEME_VAULT_DIR, f"{name}.mp4")
    temp_file = os.path.join(MEME_VAULT_DIR, f"{name}_raw.mp4")
    
    target_target = url if url else f"ytsearch1:{query} meme template"
    
    cmd = [
        "yt-dlp",
        target_target,
        "-f", "bestvideo[height<=1080]+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", temp_file,
        "--no-playlist",
        "--force-overwrites"
    ]
    
    # Complete sentence rule: Only slice if duration is explicitly specified AND not full
    if duration is not None and not full:
        start_time = f"{int(start_sec//60):02d}:{int(start_sec%60):02d}"
        end_sec = start_sec + duration
        end_time = f"{int(end_sec//60):02d}:{int(end_sec%60):02d}"
        cmd.extend(["--download-sections", f"*{start_time}-{end_time}"])
    
    print(f"🎬 Sourcing full meme clip: '{query or url}' -> {name}.mp4...")
    try:
        kwargs = {}
        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 0
            kwargs["startupinfo"] = startupinfo
            kwargs["creationflags"] = CREATE_NO_WINDOW

        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **kwargs)
        if os.path.exists(temp_file) and os.path.getsize(temp_file) > 1000:
            # Remux to AAC audio for full editor compatibility
            remux_cmd = [
                "ffmpeg", "-y", "-i", temp_file,
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                out_file
            ]
            subprocess.run(remux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
            try:
                os.remove(temp_file)
            except:
                pass
            if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
                size_kb = os.path.getsize(out_file) / 1024
                print(f"✅ Meme successfully vaulted with complete audio: {out_file} ({size_kb:.1f} KB)")
                return out_file
        print(f"❌ Failed to download meme: {res.stderr[:200]}")
        return None
    except Exception as e:
        print(f"Exception during meme download: {e}")
        return None

def list_memes():
    if not os.path.exists(MEME_VAULT_DIR):
        print("No memes vaulted yet.")
        return []
    
    files = [f for f in os.listdir(MEME_VAULT_DIR) if f.endswith(('.mp4', '.gif', '.webm'))]
    print(f"\n🎭 Curated Satirical Meme Vault ({len(files)} clips available):")
    for f in sorted(files):
        fpath = os.path.join(MEME_VAULT_DIR, f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"  • {f} ({size_kb:.1f} KB)")
    print()
    return files

def main():
    parser = argparse.ArgumentParser(description="Meme & Satirical Reaction Clip Scout")
    parser.add_argument("--query", help="Search query for meme (e.g. 'steve carell no god')")
    parser.add_argument("--url", help="Direct video URL")
    parser.add_argument("--name", help="Output filename base (e.g. 'steve_carell_no')")
    parser.add_argument("--duration", type=int, default=None, help="Clip duration in seconds (optional, default: full complete dialogue)")
    parser.add_argument("--start", type=float, default=0.0, help="Start offset in seconds")
    parser.add_argument("--full", action="store_true", help="Download complete clip without cutting mid-sentence")
    parser.add_argument("--list", action="store_true", help="List all available memes in vault")
    parser.add_argument("--harvest", action="store_true", help="Run full viral vault harvester")
    args = parser.parse_args()

    if args.harvest:
        harvester = os.path.join(SCRIPT_DIR, "harvest_viral_vault.py")
        res = subprocess.run([sys.executable, harvester, "--all"], creationflags=CREATE_NO_WINDOW)
        sys.exit(res.returncode)

    if args.list:
        list_memes()
        return

    if not args.query and not args.url:
        print("Error: must provide --query, --url, --list, or --harvest")
        sys.exit(1)

    download_meme_clip(args.query, args.url, args.name, args.duration, args.start, full=args.full)

if __name__ == "__main__":
    main()
