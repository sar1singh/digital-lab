"""
ThinkLate Gameplay B-Roll Extractor CLI Tool
Extracts lossless/upscaled clips from source gameplay recordings into reusable_vault.

Usage:
  python tools/extract_gameplay_broll.py --start 00:24:45 --duration 10 --name havana_pan --cues V36
"""

import os
import sys
import json
import argparse
import subprocess

DEFAULT_INPUT = r"C:\Users\sar1s\Videos\obs\2026-10-12 22-44-03.mkv"
VAULT_DIR = r"reusable_vault\gameplay_broll\ac_black_flag"
MANIFEST_FILE = os.path.join(VAULT_DIR, "manifest.json")

def main():
    parser = argparse.ArgumentParser(description="Extract gameplay B-roll clips into reusable vault.")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Source video file path")
    parser.add_argument("--start", required=True, help="Start timestamp (e.g. 00:15:30 or seconds)")
    parser.add_argument("--duration", type=float, default=8.0, help="Duration in seconds (default: 8.0)")
    parser.add_argument("--name", required=True, help="Output clip filename without extension")
    parser.add_argument("--cues", default="", help="Comma-separated script cues (e.g. V36,V55)")
    parser.add_argument("--tags", default="gameplay,ac_black_flag", help="Comma-separated tags")
    parser.add_argument("--scale_1080p", action="store_true", default=True, help="Upscale to 1920x1080 (default: True)")
    
    args = parser.parse_args()

    os.makedirs(VAULT_DIR, exist_ok=True)
    out_filename = f"{args.name}.mp4" if not args.name.endswith(".mp4") else args.name
    out_path = os.path.join(VAULT_DIR, out_filename)

    scale_filter = "scale=1920:1080:flags=lanczos" if args.scale_1080p else "copy"

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(args.start),
        "-i", args.input,
        "-t", str(args.duration),
    ]

    if args.scale_1080p:
        cmd.extend(["-vf", scale_filter, "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an"])
    else:
        cmd.extend(["-c:v", "copy", "-an"])

    cmd.append(out_path)

    print(f"🎬 Extracting clip to: {out_path}...")
    result = subprocess.run(cmd)

    if result.returncode == 0 and os.path.exists(out_path):
        print(f"✅ Extraction SUCCESS: {out_filename} ({os.path.getsize(out_path) / (1024*1024):.2f} MB)")
        
        # Update manifest
        manifest = {"game": "Assassin's Creed IV: Black Flag", "clips": []}
        if os.path.exists(MANIFEST_FILE):
            try:
                with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                    manifest = json.load(f)
            except Exception:
                pass
        
        cues_list = [c.strip() for c in args.cues.split(",") if c.strip()]
        tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]

        # Check if clip already in manifest
        existing = [c for c in manifest.get("clips", []) if c["filename"] == out_filename]
        if not existing:
            manifest.setdefault("clips", []).append({
                "filename": out_filename,
                "timestamp_in": str(args.start),
                "duration_sec": args.duration,
                "tags": tags_list,
                "video_cues": cues_list,
                "description": f"Extracted clip from Black Flag recording at {args.start}"
            })
            with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
            print(f"📋 Manifest updated in: {MANIFEST_FILE}")
    else:
        print(f"❌ Extraction failed with code {result.returncode}")

if __name__ == "__main__":
    main()
