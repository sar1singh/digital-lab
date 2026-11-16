#!/usr/bin/env python3
"""
Compile Final Master Video for ThinkLate Episode 05:
"How An $80 Airbed Stole An Entire Industry" (15m 57s | 957.0s)
==============================================================
Frame-accurate concatenation of all 5 modular parts:
  Part 1: The Hook (00:00 - 01:16 | 76.0s)
  Part 2: Rejection & Cereal Hustle (01:16 - 05:58 | 282.0s)
  Part 3: Craigslist Hijack & $100B IPO (05:58 - 10:15 | 257.0s)
  Part 4: Hotelification Trap & Regulatory War (10:15 - 13:27 | 192.0s)
  Part 5: Solo-Builder Playbook & 3 Contrarian Laws (13:27 - 15:57 | 150.0s)

Audio Track: Master continuous broadcast mix (pegged VO at -1.0dB, -26dB BGM with 1.5kHz notch filter).
Video Track: 1080p 30fps x264 CRF 18 Commercial Master + Fast-start web optimization.
"""

import os
import sys
import subprocess
import time

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

PART_FILES = [
    {"name": "Part 1 (The Hook)", "file": os.path.join(BASE_DIR, "ThinkLate_Video05_Hook_Final_1080p.mp4"), "dur": 76.0},
    {"name": "Part 2 (Rejection & Hustle)", "file": os.path.join(BASE_DIR, "ThinkLate_Video05_Part2_Master_1080p.mp4"), "dur": 282.0},
    {"name": "Part 3 (Craigslist Hijack & IPO)", "file": os.path.join(BASE_DIR, "ThinkLate_Video05_Part3_Master_1080p.mp4"), "dur": 257.0},
    {"name": "Part 4 (Hotelification Trap)", "file": os.path.join(BASE_DIR, "ThinkLate_Video05_Part4_Master_1080p.mp4"), "dur": 192.0},
    {"name": "Part 5 (Solo-Builder Playbook)", "file": os.path.join(BASE_DIR, "ThinkLate_Video05_Part5_Master_1080p.mp4"), "dur": 150.0},
]

OUTPUT_EPISODE_MASTER = os.path.join(BASE_DIR, "ThinkLate_Episode05_Final_Master_1080p.mp4")
OUTPUT_EPISODE_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Episode05_Final_Review_Light.mp4")

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def get_headless_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

def compile_master():
    print("=" * 70)
    print("THINKLATE EPISODE 05 // FINAL MASTER ASSEMBLY (15M 57S)")
    print("=" * 70)

    # 1. Verify existence of all parts and continuous audio master
    total_planned = sum(p["dur"] for p in PART_FILES)
    print(f"Total planned timeline: {total_planned:.1f}s ({total_planned/60:.2f} minutes)")

    for p in PART_FILES:
        if not os.path.exists(p["file"]):
            print(f"[FAIL] Missing part file: {p['file']}")
            return False
        sz = os.path.getsize(p["file"]) / (1024 * 1024)
        print(f"  [OK] Found {p['name']}: {sz:.1f}MB ({p['dur']:.1f}s)")

    if not os.path.exists(AUDIO_SRC):
        print(f"[FAIL] Missing master audio: {AUDIO_SRC}")
        return False
    print(f"  [OK] Found Master Audio: {os.path.basename(AUDIO_SRC)}")

    # 2. Build FFmpeg command with frame-accurate video trimming and concat
    cmd = ["ffmpeg", "-y"]

    # Inputs 0..4: The 5 Part video files trimmed exactly to intended duration
    for p in PART_FILES:
        cmd.extend(["-t", f"{p['dur']:.2f}", "-i", p["file"]])

    # Input 5: Master continuous audio track (957.0s)
    cmd.extend(["-t", f"{total_planned:.2f}", "-i", AUDIO_SRC])

    # Filter graph: normalize fps, timebase, and concatenate video streams
    filter_chains = []
    for i in range(len(PART_FILES)):
        filter_chains.append(f"[{i}:v]fps=30,settb=AVTB,setpts=PTS-STARTPTS[v{i}]")

    concat_inputs = "".join(f"[v{i}]" for i in range(len(PART_FILES)))
    filter_chains.append(f"{concat_inputs}concat=n={len(PART_FILES)}:v=1:a=0[v_master]")

    filter_complex_str = ";\n".join(filter_chains)
    audio_idx = len(PART_FILES)  # Input 5

    full_cmd = cmd + [
        "-filter_complex", filter_complex_str,
        "-map", "[v_master]",
        "-map", f"{audio_idx}:a",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "320k",
        "-ar", "44100",
        "-shortest",
        "-movflags", "+faststart",
        OUTPUT_EPISODE_MASTER
    ]

    print(f"\nEncoding Final Episode Master (CRF 18 broadcast standard)...")
    t0 = time.time()
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    t_master = time.time() - t0

    if res.returncode == 0 and os.path.exists(OUTPUT_EPISODE_MASTER):
        sz = os.path.getsize(OUTPUT_EPISODE_MASTER) / (1024 * 1024)
        print(f"[SUCCESS] Final Episode 05 Master Compiled: {OUTPUT_EPISODE_MASTER}")
        print(f"  Size: {sz:.2f} MB | Time: {t_master:.1f}s")
    else:
        print(f"[FAIL] Master compilation failed:\n{res.stderr.decode('utf-8', errors='ignore')[-800:]}")
        return False

    # 3. Render light review cut for instant in-IDE playback and artifacts inspection
    print(f"\nRendering In-IDE Review Light Cut (CRF 24 fast)...")
    t0 = time.time()
    light_cmd = [
        "ffmpeg", "-y",
        "-i", OUTPUT_EPISODE_MASTER,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "24",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        OUTPUT_EPISODE_LIGHT
    ]
    res_light = subprocess.run(light_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    t_light = time.time() - t0

    if res_light.returncode == 0 and os.path.exists(OUTPUT_EPISODE_LIGHT):
        sz_light = os.path.getsize(OUTPUT_EPISODE_LIGHT) / (1024 * 1024)
        print(f"[SUCCESS] In-IDE Review Cut Ready: {OUTPUT_EPISODE_LIGHT}")
        print(f"  Size: {sz_light:.2f} MB | Time: {t_light:.1f}s")
    else:
        print(f"[WARN] Light cut creation had warning:\n{res_light.stderr.decode('utf-8', errors='ignore')[-400:]}")

    return True

if __name__ == "__main__":
    compile_master()

