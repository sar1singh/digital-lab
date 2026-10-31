#!/usr/bin/env python3
"""
ThinkLate Video 05 — Granular High-Retention Video Assembly Renderer (88 Cues)
Muxes all 88 visual cuts with Andrew 90% + BGM 30% master audio.
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

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(VIDEO_DIR, "assets")
BROLL_DIR = os.path.join(ASSETS_DIR, "documentary_broll")
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")
CACHE_DIR = os.path.join(VIDEO_DIR, "render_cache_granular")
os.makedirs(CACHE_DIR, exist_ok=True)

CUES_JSON = os.path.join(VIDEO_DIR, "ThinkLate_Video05_Granular_Cues.json")
MASTER_AUDIO = os.path.join(AUDIO_DIR, "full_mix_preview.wav")
FINAL_MP4 = os.path.join(VIDEO_DIR, "ThinkLate_Video05_Final_High_Retention.mp4")
CONCAT_FILE = os.path.join(CACHE_DIR, "concat_88.txt")

FLAGS = 0x08000000 if sys.platform == "win32" else 0

with open(CUES_JSON, "r", encoding="utf-8") as f:
    cues = json.load(f)

print(f"🎬 Starting Granular 88-Cue Assembly Render ({len(cues)} cues | 17m 26s)...")
t0 = time.time()

seg_files = []
for c in cues:
    cid = c["id"]
    dur = c["dur"]
    clip_name = c["v1_clip"]
    
    # Path resolution
    clip_path = os.path.join(BROLL_DIR, clip_name)
    if not os.path.exists(clip_path):
        clip_path = os.path.join(ASSETS_DIR, clip_name)
    if not os.path.exists(clip_path):
        # Fallback to base stock video
        clip_path = os.path.join(BROLL_DIR, "scene1_01_city_apartments.mp4")

    out_seg = os.path.join(CACHE_DIR, f"seg_{cid:03d}.mp4")
    seg_files.append(out_seg)

    if os.path.exists(out_seg) and os.path.getsize(out_seg) > 50000:
        continue

    is_image = clip_path.lower().endswith(('.jpg', '.jpeg', '.png'))
    
    if is_image:
        # 3% Ken Burns slow push on static stills
        vf = (
            f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            f"zoompan=z='min(zoom+0.0003,1.03)':d={int(round(dur*30))}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
            f"format=yuv420p"
        )
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", clip_path,
            "-t", f"{dur:.2f}",
            "-vf", vf,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23",
            "-an",
            out_seg
        ]
    else:
        vf = (
            f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            f"fps=30,format=yuv420p"
        )
        cmd = [
            "ffmpeg", "-y",
            "-stream_loop", "-1",
            "-i", clip_path,
            "-t", f"{dur:.2f}",
            "-vf", vf,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23",
            "-an",
            out_seg
        ]
    
    subprocess.run(cmd, check=True, creationflags=FLAGS)
    if cid % 10 == 0:
        print(f"  --> Rendered {cid}/{len(cues)} visual cues...")

print("🎞️ Concatenating all 88 visual segments...")
with open(CONCAT_FILE, "w", encoding="utf-8") as f:
    for s in seg_files:
        norm = s.replace("\\", "/")
        f.write(f"file '{norm}'\n")

raw_video = os.path.join(CACHE_DIR, "raw_88_video.mp4")
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
    FINAL_MP4
]
subprocess.run(cmd_mux, check=True, creationflags=FLAGS)

elapsed = time.time() - t0
print(f"\n🎉 88-Cue High-Retention Assembly Complete in {elapsed:.1f}s!")
print(f"📦 Final Output: {FINAL_MP4} ({os.path.getsize(FINAL_MP4)//(1024*1024)} MB)")
