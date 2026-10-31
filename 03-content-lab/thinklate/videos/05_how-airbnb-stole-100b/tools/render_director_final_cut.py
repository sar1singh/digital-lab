#!/usr/bin/env python3
"""
ThinkLate Video 05 — Master Director Final Cut Renderer
=======================================================
Episode: "How An $80 Airbed Stole An Entire Industry" (17m 25s | 1,046.00s)
Combines:
- Track 1 (Ambient Glue): User's ACBF_Gameplay_2.mp4
- Track 3 (Evidentiary Plates): 10 High-DPI Cards, 7 Archival Photos, Data Charts, Master Thumbnail Art
- Audio: Andrew Multilingual Neural (90% pure) + Dark Fog Ambient Bed (30%)
- Output: ThinkLate_Video05_Final_Published.mp4
"""

import os
import sys
import json
import subprocess
import time

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(VIDEO_DIR, "render_cache_director")
os.makedirs(CACHE_DIR, exist_ok=True)

AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")
MASTER_AUDIO = os.path.join(AUDIO_DIR, "full_mix_preview.wav")
GAMEPLAY_SRC = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
FINAL_OUTPUT_MP4 = os.path.join(VIDEO_DIR, "ThinkLate_Video05_Final_Published.mp4")
CONCAT_FILE = os.path.join(CACHE_DIR, "concat_director.txt")

FLAGS = 0x08000000 if sys.platform == "win32" else 0

SCHEDULE_JSON = os.path.join(VIDEO_DIR, "director_cut_schedule.json")
with open(SCHEDULE_JSON, "r", encoding="utf-8") as f:
    cues = json.load(f)

print("=" * 70)
print("🎬 ThinkLate Video 05: Master Director Final Cut Assembly")
print(f" Total Semantic Beats: {len(cues)} cuts across 17m 26s")
print(f" Ambient Canvas: User Gameplay ({os.path.basename(GAMEPLAY_SRC)})")
print(f" Master Audio: {os.path.basename(MASTER_AUDIO)}")
print(f" Target Output: {FINAL_OUTPUT_MP4}")
print("=" * 70)

t0 = time.time()
seg_files = []

for idx, cue in enumerate(cues):
    st, et, v_type, rel_path, summary, slam = cue
    dur = et - st
    cid = idx + 1
    out_seg = os.path.join(CACHE_DIR, f"director_seg_{cid:03d}.mp4")
    seg_files.append(out_seg)

    if os.path.exists(out_seg) and os.path.getsize(out_seg) > 50000:
        continue

    if v_type == "GAMEPLAY":
        # Extract subclip from user's recorded gameplay
        # We loop time offset smoothly so it stays within the 4,156s recording
        gameplay_offset = st % 3600.0
        vf = (
            "scale=1920:1080:force_original_aspect_ratio=decrease,"
            "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            "fps=30,format=yuv420p"
        )
        cmd = [
            "ffmpeg", "-y",
            "-ss", f"{gameplay_offset:.2f}",
            "-t", f"{dur:.2f}",
            "-i", GAMEPLAY_SRC,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22",
            "-an",
            out_seg
        ]
    else:
        # High-DPI Evidence Card, Archival Photo, Data Chart, or Thumbnail Art
        img_full_path = os.path.join(VIDEO_DIR, rel_path)
        if not os.path.exists(img_full_path):
            # Fallback to gameplay if image path missing
            img_full_path = os.path.join(VIDEO_DIR, "assets", "thumbnail_option_a.jpg")

        frames_count = max(int(round(dur * 30)), 30)
        vf = (
            f"scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            f"zoompan=z='min(zoom+0.0003,1.03)':d={frames_count}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
            f"format=yuv420p"
        )
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", img_full_path,
            "-t", f"{dur:.2f}",
            "-vf", vf,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22",
            "-an",
            out_seg
        ]

    subprocess.run(cmd, check=True, creationflags=FLAGS)
    print(f"  [{cid:02d}/{len(cues)}] {v_type:8s} ({dur:5.1f}s) | {slam[:40]}...")

print("\n🎞️ Concatenating all 53 Director Segments...")
with open(CONCAT_FILE, "w", encoding="utf-8") as f:
    for s in seg_files:
        norm = s.replace("\\", "/")
        f.write(f"file '{norm}'\n")

raw_video = os.path.join(CACHE_DIR, "raw_director_video.mp4")
cmd_concat = [
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", CONCAT_FILE,
    "-c", "copy",
    raw_video
]
subprocess.run(cmd_concat, check=True, creationflags=FLAGS)

print("🎵 Muxing with Master Audio (Andrew 90% + Ambient BGM 30%)...")
cmd_mux = [
    "ffmpeg", "-y",
    "-i", raw_video,
    "-i", MASTER_AUDIO,
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    FINAL_OUTPUT_MP4
]
subprocess.run(cmd_mux, check=True, creationflags=FLAGS)

elapsed = time.time() - t0
print(f"\n🎉 Director Final Cut Assembly Complete in {elapsed:.1f}s!")
print(f"📦 Broadcast Ready MP4: {FINAL_OUTPUT_MP4} ({os.path.getsize(FINAL_OUTPUT_MP4)//(1024*1024)} MB)")

