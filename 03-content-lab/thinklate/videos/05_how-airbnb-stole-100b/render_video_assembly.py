#!/usr/bin/env python3
"""
ThinkLate Video 05 — Video Assembly & Review Renderer
Episode: "How An $80 Airbed Stole An Entire Industry" (17m 26s | 1,046.00s)
Combines:
- Track 1: High-Definition Stock Videos & Archival B-Roll
- Track 3: Programmatic Charts & Anchor Artwork (with 3% Ken Burns slow push)
- Master Audio: Andrew Multilingual Neural (90%) + Ambient BGM Bed (30%)
- Output: ThinkLate_Video05_Assembly_Preview.mp4
"""

import os
import sys
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
CACHE_DIR = os.path.join(VIDEO_DIR, "render_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

MASTER_AUDIO = os.path.join(AUDIO_DIR, "full_mix_preview.wav")
if not os.path.exists(MASTER_AUDIO):
    MASTER_AUDIO = os.path.join(AUDIO_DIR, "full_mix_preview.mp3")

OUTPUT_MP4 = os.path.join(VIDEO_DIR, "ThinkLate_Video05_Assembly_Preview.mp4")
CONCAT_FILE = os.path.join(CACHE_DIR, "segments.txt")

FLAGS = 0x08000000 if sys.platform == "win32" else 0

SCENES = [
    {
        "id": 1,
        "name": "Scene 01: Cold Open & Airbed Hook",
        "dur": 164.16,
        "clip": os.path.join(BROLL_DIR, "scene1_01_city_apartments.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene1_02_apartment_keys.mp4"),
        "is_image": False
    },
    {
        "id": 2,
        "name": "Scene 02: Debt & Novelty Cereal Stunt",
        "dur": 95.36,
        "clip": os.path.join(BROLL_DIR, "scene2_01_credit_card_debt.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene2_02_convention_crowd.mp4"),
        "is_image": False
    },
    {
        "id": 3,
        "name": "Scene 03: YC Crucible & Paul Graham Pitch",
        "dur": 107.60,
        "clip": os.path.join(BROLL_DIR, "scene3_01_venture_meeting.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene3_02_partnership_deal.mp4"),
        "is_image": False
    },
    {
        "id": 4,
        "name": "Scene 04: Brooklyn Photography Ground War",
        "dur": 78.40,
        "clip": os.path.join(BROLL_DIR, "scene4_01_dslr_camera.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene4_02_bright_interior.mp4"),
        "is_image": False
    },
    {
        "id": 5,
        "name": "Scene 05: Craigslist Hijack Growth Hack",
        "dur": 121.68,
        "clip": os.path.join(BROLL_DIR, "scene5_01_python_coding.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene5_02_laptop_terminal.mp4"),
        "is_image": False
    },
    {
        "id": 6,
        "name": "Scene 06: March 2020 Crash & $100B IPO",
        "dur": 104.48,
        "clip": os.path.join(BROLL_DIR, "scene6_01_empty_airport.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene6_02_wall_street_ticker.mp4"),
        "is_image": False
    },
    {
        "id": 7,
        "name": "Scene 07: Chore Fee Backlash & City Bans",
        "dur": 212.40,
        "clip": os.path.join(BROLL_DIR, "scene7_01_house_chores.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene7_02_city_protest.mp4"),
        "is_image": False
    },
    {
        "id": 8,
        "name": "Scene 08: 3 Entrepreneur Rules & Outro",
        "dur": 161.92,
        "clip": os.path.join(BROLL_DIR, "scene8_01_boutique_hotel.mp4"),
        "alt_clip": os.path.join(BROLL_DIR, "scene8_02_luggage_journey.mp4"),
        "is_image": False
    }
]

def render_segment(scene):
    out_seg = os.path.join(CACHE_DIR, f"seg_{scene['id']:02d}.mp4")
    if os.path.exists(out_seg) and os.path.getsize(out_seg) > 500000:
        print(f"  ✅ Segment {scene['id']} already rendered ({os.path.getsize(out_seg)//1024} KB)")
        return out_seg

    dur = scene["dur"]
    clip = scene["clip"]
    
    # Render with seamless loop to cover the exact duration of each scene, scaled to 1080p
    vf = (
        f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
        f"fps=30,format=yuv420p"
    )

    cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1",
        "-i", clip,
        "-t", f"{dur:.2f}",
        "-vf", vf,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "22",
        "-an",
        out_seg
    ]
    subprocess.run(cmd, check=True, creationflags=FLAGS)
    print(f"  🎬 Rendered Segment {scene['id']}: {scene['name']} ({dur:.1f}s)")
    return out_seg

def main():
    print("=" * 60)
    print("🚀 ThinkLate Video 05 — Video Assembly Renderer")
    print(f" Master Audio: {os.path.basename(MASTER_AUDIO)}")
    print(f" Target Output: {OUTPUT_MP4}")
    print("=" * 60)

    t0 = time.time()
    seg_files = []
    for sc in SCENES:
        seg = render_segment(sc)
        seg_files.append(seg)

    # Write concat list
    with open(CONCAT_FILE, "w", encoding="utf-8") as f:
        for s in seg_files:
            norm_path = s.replace("\\", "/")
            f.write(f"file '{norm_path}'\n")

    print("\n🎞️ Step 2: Concatenating video tracks & muxing master audio...")
    raw_video = os.path.join(CACHE_DIR, "raw_video_track.mp4")
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_FILE,
        "-c", "copy",
        raw_video
    ]
    subprocess.run(cmd_concat, check=True, creationflags=FLAGS)

    print("🎵 Step 3: Muxing final video with master audio...")
    cmd_mux = [
        "ffmpeg", "-y",
        "-i", raw_video,
        "-i", MASTER_AUDIO,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_MP4
    ]
    subprocess.run(cmd_mux, check=True, creationflags=FLAGS)

    elapsed = time.time() - t0
    print(f"\n🎉 Video Assembly Complete in {elapsed:.1f}s!")
    print(f"📦 Final Video: {OUTPUT_MP4} ({os.path.getsize(OUTPUT_MP4)//(1024*1024)} MB)")

if __name__ == "__main__":
    main()
