#!/usr/bin/env python3
"""
ThinkLate Gameplay Spine Builder (Track 1 Living Canvas)
========================================================
Autonomously generates a continuous, dynamic, non-repetitive living background
video (Video Track 1) from the creator's master 4K/1080p gameplay footage
(ACBF_Gameplay_2.mp4).

Permanently solves visual dead-air, eliminates manual B-roll hunting bottlenecks,
and enforces Paivio's Law by ensuring active motion beneath evidence cards.

Usage:
    # 1. From exact duration:
    python tools/build_gameplay_spine.py --duration 600 --out track1_spine.mp4

    # 2. From Whisper transcription timestamps:
    python tools/build_gameplay_spine.py --whisper transcription_timestamps.json --out track1_spine.mp4

    # 3. From master audio file:
    python tools/build_gameplay_spine.py --audio full_master_audio.wav --out track1_spine.mp4
"""

import os
import sys
import json
import random
import shutil
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

# Strict Headless Window Suppression for Windows
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

DEFAULT_GAMEPLAY = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"

def get_media_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True, **get_headless_kwargs())
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Error probing duration for {file_path}: {e}")
        return None

def build_gameplay_spine(target_duration, output_path, gameplay_path=DEFAULT_GAMEPLAY, min_shot=6.0, max_shot=12.0, seed=42):
    if not os.path.exists(gameplay_path):
        print(f"Error: Gameplay file not found: {gameplay_path}")
        return False

    output_path = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    source_duration = get_media_duration(gameplay_path)
    if not source_duration or source_duration < 60:
        print(f"Error: Could not retrieve valid source duration ({source_duration}s)")
        return False

    print(f"🎮 Source Gameplay Duration: {source_duration:.1f}s ({source_duration/60:.1f} min)")
    print(f"🎯 Target Living Spine Duration: {target_duration:.1f}s ({target_duration/60:.1f} min)")

    # Build randomized slice schedule across source video
    rng = random.Random(seed)
    current_time = 0.0
    segments = []
    
    # Avoid first 2 minutes (often loading screens/menus) and last 2 minutes
    safe_start = 120.0
    safe_end = max(safe_start + 60, source_duration - 120.0)

    while current_time < target_duration:
        shot_len = min(rng.uniform(min_shot, max_shot), target_duration - current_time)
        # Pick random starting point in safe zone
        start_pt = rng.uniform(safe_start, safe_end - shot_len)
        segments.append((start_pt, shot_len))
        current_time += shot_len

    print(f"✂️ Generated {len(segments)} dynamic action cuts (avg shot: {target_duration/len(segments):.1f}s)")

    # Build concat file for lossless rapid assembly
    temp_dir = os.path.join(os.path.dirname(output_path), "_temp_spine_cuts")
    os.makedirs(temp_dir, exist_ok=True)
    concat_list_path = os.path.join(temp_dir, "concat_list.txt")

    clip_paths = []
    for idx, (s_start, s_dur) in enumerate(segments):
        clip_name = f"spine_cut_{idx:03d}.mp4"
        clip_path = os.path.join(temp_dir, clip_name)
        clip_paths.append(clip_path)

        # Extract sub-clip with center-safe 1080p framing and no audio
        cmd = [
            "ffmpeg", "-y",
            "-ss", f"{s_start:.2f}",
            "-i", gameplay_path,
            "-t", f"{s_dur:.2f}",
            "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30",
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22",
            "-an",
            clip_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
        if res.returncode != 0:
            print(f"Warning: Failed extracting cut {idx}: {res.stderr.decode('utf-8', errors='ignore')[:150]}")

    # Write concat list
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for cp in clip_paths:
            if os.path.exists(cp) and os.path.getsize(cp) > 0:
                f.write(f"file '{cp.replace(os.sep, '/')}'\n")

    # Final concat
    print(f"🎬 Merging living gameplay canvas to: {output_path}...")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c:v", "copy",
        "-an",
        output_path
    ]
    res = subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())

    # Cleanup temp cuts
    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except Exception:
        pass

    if res.returncode == 0 and os.path.exists(output_path):
        out_dur = get_media_duration(output_path)
        out_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"✅ Living Gameplay Spine Assembled Successfully!")
        print(f"   Duration: {out_dur:.1f}s | Size: {out_mb:.1f} MB")
        return True
    else:
        print(f"❌ Concat failed:\n{res.stderr.decode('utf-8', errors='ignore')[:300]}")
        return False

def main():
    parser = argparse.ArgumentParser(description="ThinkLate Track 1 Living Gameplay Spine Builder")
    parser.add_argument("--duration", type=float, default=None, help="Target duration in seconds")
    parser.add_argument("--audio", default=None, help="Path to master audio file to match duration")
    parser.add_argument("--whisper", default=None, help="Path to transcription_timestamps.json")
    parser.add_argument("--gameplay", default=DEFAULT_GAMEPLAY, help="Source gameplay video path")
    parser.add_argument("--out", required=True, help="Output Track 1 MP4 path")
    parser.add_argument("--min_shot", type=float, default=6.0, help="Minimum cut length in seconds")
    parser.add_argument("--max_shot", type=float, default=12.0, help="Maximum cut length in seconds")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for repeatable cut generation")
    args = parser.parse_args()

    target_dur = args.duration

    if target_dur is None and args.audio:
        target_dur = get_media_duration(args.audio)
    elif target_dur is None and args.whisper:
        if os.path.exists(args.whisper):
            try:
                with open(args.whisper, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    segments = data.get("segments", [])
                    if segments:
                        target_dur = float(segments[-1].get("end", 0.0))
            except Exception as e:
                print(f"Error parsing whisper file: {e}")

    if target_dur is None or target_dur <= 0:
        print("Error: Must provide valid --duration, --audio, or --whisper.")
        sys.exit(1)

    success = build_gameplay_spine(
        target_duration=target_dur,
        output_path=args.out,
        gameplay_path=args.gameplay,
        min_shot=args.min_shot,
        max_shot=args.max_shot,
        seed=args.seed
    )
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
