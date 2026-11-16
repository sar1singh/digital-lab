#!/usr/bin/env python3
"""
ThinkLate Episode L07 ("Why You Can't Cancel Anything") — Master Video Compiler
==============================================================================
Compiles the complete 1080p widescreen documentary master:
  1. Composites 5 scenes using living 4K documentary B-roll, noir grade, and 2D forensic plates
  2. Mixes master voiceover with ambient BGM and diegetic Cinema Vault foley (-16.0 LUFS)
  3. Burns in word-synced kinetic ASS broadcast subtitles
  4. Encodes 1080p @ 30fps H.264/AAC MP4 via NVENC
  5. Runs QC audit and exports cover frames + COPY_PASTE_METADATA.txt
"""

import json
import os
import pathlib
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

L07_DIR = pathlib.Path(__file__).resolve().parent
AUDIO_DIR = L07_DIR / "assets" / "audio"
PLATES_DIR = L07_DIR / "assets" / "plates"
SEGMENTS_DIR = L07_DIR / "assets" / "segments"
THUMBNAILS_DIR = L07_DIR / "assets" / "thumbnails"
SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
THUMBNAILS_DIR.mkdir(parents=True, exist_ok=True)

PROJECT_ROOT = L07_DIR.parents[5]
SHARED_BROLL = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "broll"
CINEMA_SFX = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "sfx" / "cinema_vault"
BGM_SRC = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "bgm_vault" / "bgm_dark_tension_free-stock-music_atmospheres.mp3"

VOICE_WAV = AUDIO_DIR / "voiceover_clean.wav"
TIMESTAMPS_JSON = L07_DIR / "transcription_timestamps.json"
MIXED_AUDIO = AUDIO_DIR / "full_mix_master.wav"
ASS_SUBS = L07_DIR / "subtitles_l07_master.ass"
FINAL_MASTER_MP4 = L07_DIR / "ThinkLate_L07_Why_You_Cant_Cancel_1080p_MASTER.mp4"

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

# Scene timeline mapping (derived from Whisper master clock)
SCENES = [
    # (scene_id, start_sec, end_sec, broll_filename, plate_filename)
    (1,   0.00,  37.50, "broll_online_shopping_click.mp4",   "plate_01.png"),
    (2,  37.50,  78.50, "broll_servers.mp4",                 "plate_02.png"),
    (3,  78.50, 138.00, "broll_counting_cash_register.mp4",  "plate_02.png"),
    (4, 138.00, 180.00, "courtroom.mp4",                     "plate_03.png"),
    (5, 180.00, 226.00, "archive_files.mp4",                 "plate_03.png"),
    (6, 226.00, 270.00, "broll_credit_card_payment.mp4",     "plate_04.png"),
    (7, 270.00, 317.29, "broll_customer_card_swipe.mp4",     "plate_05.png"),
]

# -------------------------------------------------------------
# 1. AUDIO MIXING (VOICE + BGM + CINEMA FOLEY)
# -------------------------------------------------------------
def mix_master_audio():
    print("[*] Mixing master audio (Voice + Alternate Dark Tension BGM + Cinema SFX)...")
    sfx_click = CINEMA_SFX / "camera_classic_click.mp3"
    sfx_slam = CINEMA_SFX / "sub_impact_warm_knocking.mp3"
    sfx_paper = CINEMA_SFX / "paper_slide_document.mp3"
    sfx_shutter = CINEMA_SFX / "camera_vintage_shutter.mp3"

    filter_complex = (
        "[0:a]volume=1.0[v];"
        "[1:a]volume=-25dB,equalizer=f=1500:t=q:w=1.5:g=-8,equalizer=f=3000:t=q:w=1.5:g=-6,highpass=f=80,lowpass=f=7500,atrim=0:325[bgm];"
        "[2:a]adelay=100|100,volume=0.20[sfx_c1];"
        "[3:a]adelay=37000|37000,volume=0.25[sfx_s1];"
        "[4:a]adelay=138000|138000,volume=0.25[sfx_s2];"
        "[5:a]adelay=180000|180000,volume=0.22[sfx_shut];"
        "[6:a]adelay=226000|226000,volume=0.25[sfx_p1];"
        "[7:a]adelay=270000|270000,volume=0.28[sfx_s3];"
        "[8:a]adelay=312000|312000,volume=0.32[sfx_climax];"
        "[v][bgm][sfx_c1][sfx_s1][sfx_s2][sfx_shut][sfx_p1][sfx_s3][sfx_climax]amix=inputs=9:duration=first:dropout_transition=0:normalize=0,"
        "loudnorm=I=-16:TP=-1.0:LRA=7[out_a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(VOICE_WAV),
        "-stream_loop", "-1", "-i", str(BGM_SRC),
        "-i", str(sfx_click),
        "-i", str(sfx_slam),
        "-i", str(sfx_slam),
        "-i", str(sfx_shutter),
        "-i", str(sfx_paper),
        "-i", str(sfx_slam),
        "-i", str(sfx_slam),
        "-filter_complex", filter_complex,
        "-map", "[out_a]",
        "-ar", "48000",
        "-c:a", "pcm_s16le",
        str(MIXED_AUDIO)
    ]
    subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)
    print(f"[+] Master audio mixed: {MIXED_AUDIO}")

# -------------------------------------------------------------
# 2. RENDER SCENE SEGMENTS & COMPOSITE
# -------------------------------------------------------------
def render_segments():
    print("[*] Rendering widescreen documentary scene segments...")
    seg_files = []

    for sid, st, en, broll_name, plate_name in SCENES:
        dur = en - st
        broll_path = SHARED_BROLL / broll_name
        plate_path = PLATES_DIR / plate_name
        out_seg = SEGMENTS_DIR / f"seg_{sid:02d}.mp4"
        seg_files.append(str(out_seg))

        # Filter:
        # 1. Scale broll to 1920x1080 with smooth slow zoom/pan
        # 2. Subtle dark noir grade & selective focus blur
        # 3. Composite 2D forensic plate with gentle fade-in
        vf = (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,"
            f"crop=1920:1080:(in_w-1920)/2:(in_h-1080)/2,"
            f"format=yuv420p,colorlevels=rimin=0.03:gimin=0.03:bimin=0.03,"
            f"boxblur=2:1[bg];"
            f"[1:v]fade=t=in:st=0:d=0.4:alpha=1[plate];"
            f"[bg][plate]overlay=0:0[outv]"
        )

        cmd = [
            "ffmpeg", "-y",
            "-stream_loop", "-1",
            "-ss", "0.0",
            "-t", f"{dur:.3f}",
            "-i", str(broll_path),
            "-i", str(plate_path),
            "-filter_complex", vf,
            "-map", "[outv]",
            "-c:v", "h264_nvenc",
            "-preset", "p4",
            "-cq", "20",
            "-pix_fmt", "yuv420p",
            "-r", "30",
            "-an",
            str(out_seg)
        ]
        res = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW)
        if res.returncode != 0:
            cmd[cmd.index("h264_nvenc")] = "libx264"
            cmd[cmd.index("-cq")] = "-crf"
            subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)

    # Concat segments
    concat_txt = SEGMENTS_DIR / "concat_list.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for sf in seg_files:
            f.write(f"file '{sf.replace(os.sep, '/')}'\n")

    concat_raw = SEGMENTS_DIR / "concat_visual_raw.mp4"
    print("[*] Concatenating scene segments...")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c", "copy", str(concat_raw)],
        check=True, creationflags=CREATE_NO_WINDOW
    )

    # Burn in ASS broadcast subtitles & mux master audio
    print("[*] Burning in word-synced ASS subtitles & muxing master audio...")
    ass_escaped = str(ASS_SUBS).replace("\\", "/").replace(":", "\\:")
    final_cmd = [
        "ffmpeg", "-y",
        "-i", str(concat_raw),
        "-i", str(MIXED_AUDIO),
        "-vf", f"ass='{ass_escaped}'",
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "h264_nvenc",
        "-preset", "p5",
        "-cq", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        "-movflags", "+faststart",
        "-shortest",
        str(FINAL_MASTER_MP4)
    ]
    res2 = subprocess.run(final_cmd, creationflags=CREATE_NO_WINDOW)
    if res2.returncode != 0:
        final_cmd[final_cmd.index("h264_nvenc")] = "libx264"
        final_cmd[final_cmd.index("-cq")] = "-crf"
        subprocess.run(final_cmd, check=True, creationflags=CREATE_NO_WINDOW)
    print(f"[+] Master MP4 rendered successfully: {FINAL_MASTER_MP4}")

# -------------------------------------------------------------
# 3. METADATA & COVER FRAMES
# -------------------------------------------------------------
def extract_thumbnails_and_metadata():
    print("[*] Extracting thumbnail preview frames and building metadata...")
    key_times = [5.0, 50.0, 140.0, 240.0]
    for idx, kt in enumerate(key_times, 1):
        cover_out = THUMBNAILS_DIR / f"preview_frame_{idx:02d}.jpg"
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(kt), "-i", str(FINAL_MASTER_MP4),
            "-vframes", "1", "-q:v", "2", str(cover_out)
        ], creationflags=CREATE_NO_WINDOW, check=True)

    meta_text = """================================================================================
THINKLATE EPISODE L07 — 1-CLICK YOUTUBE STUDIO UPLOAD KIT
================================================================================
MASTER VIDEO FILE:   ThinkLate_L07_Why_You_Cant_Cancel_1080p_MASTER.mp4 (1080p @ 30fps)
SUBTITLE TRACK:      subtitles_en.srt (Upload under Subtitles -> English -> With timing)
CATEGORY:            Science & Technology / Education

TITLE CANDIDATES (Pick #1 for Launch, <= 50 chars):
---------------------------------------------------
1. Why You Can't Cancel Anything (28 chars) — [RECOMMENDED]
2. Signing Up: 1 Click. Cancelling: 6 Clicks. (43 chars)
3. The Secret "Iliad Flow" Behind Cancel Buttons (44 chars)

YOUTUBE DESCRIPTION (Copy & Paste Everything Below):
----------------------------------------------------
Signing up for a subscription takes one click and four seconds. Cancelling one takes an Olympic obstacle course.

In internal court documents revealed by federal regulators, tech giants codenamed their cancellation sequence the "Iliad Flow"—named after Homer's 24-book epic poem about an agonizing war. It wasn't an accident. It was an engineered maze of 4 pages, 6 clicks, and 15 different retention roadblocks.

In this deep dive into consumer economics, Eddy Thinklate breaks down:
- Why tech companies spend millions designing cancel buttons you can't find
- The Wall Street churn metric that panics boardrooms if just 3% of users leave
- Why the federal "Click-to-Cancel" rule was killed in court, and the state laws taking over
- The simple banking regulation in India that forced Big Tech to ask permission before touching your money
- Why you are not lazy for forgetting a $12 subscription—you were engineered to surrender

TIMESTAMPS:
0:00 - The One-Click Illusion
0:37 - What Is the "Iliad Flow"?
1:18 - The Churn Math That Panics Wall Street
2:45 - Why the Federal "Click-to-Cancel" Rule Died
3:46 - How India's Central Bank Flipped the Default
4:44 - The $12 Cognitive Tax & Breakage Revenue
5:05 - Evicting the Algorithm from Your Wallet (Climax & Retrospection)

PRIMARY SOURCES VERIFIED IN THIS EPISODE:
1. FTC v. Amazon.com, Inc. (W.D. Wash., Case No. 2:23-cv-00932)
2. FTC 16 CFR Negative Option Marketing Rule & Eighth Circuit Court Ruling
3. Restore Online Shoppers' Confidence Act (ROSCA, 15 U.S.C. §§ 8401–8405)
4. FTC and State Attorneys General v. Toast, Inc. (N.D. Cal., Oct 2026)
5. Reserve Bank of India Circular on e-Mandates for Recurring Transactions (RBI/2019-20/46)
6. California Automatic Renewal Law (Bus. & Prof. Code § 17600 et seq.)

#ThinkLate #ConsumerEconomics #Subscriptions #TheFinePrint #Business #Tech
"""
    (L07_DIR / "COPY_PASTE_METADATA.txt").write_text(meta_text, encoding="utf-8")
    print(f"[+] Saved COPY_PASTE_METADATA.txt")

def audit_final_master():
    print("\n=== Final Master QC Audit ===")
    probe = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(FINAL_MASTER_MP4)],
        creationflags=CREATE_NO_WINDOW
    ))
    v = [s for s in probe["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in probe["streams"] if s["codec_type"] == "audio"][0]
    v_dur = float(v.get("duration", probe["format"]["duration"]))
    a_dur = float(a.get("duration", probe["format"]["duration"]))
    drift = abs(v_dur - a_dur) * 1000.0

    ebu = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(FINAL_MASTER_MP4), "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True, creationflags=CREATE_NO_WINDOW
    ).stderr
    i_lufs = re.findall(r"I:\s*([-\d.]+)\s*LUFS", ebu)
    tp = re.findall(r"Peak:\s*([-\d.]+)\s*dBFS", ebu)

    sz_mb = os.path.getsize(FINAL_MASTER_MP4) / (1024 * 1024)
    print(f"  File:               {FINAL_MASTER_MP4.name}")
    print(f"  Resolution & FPS:   {v['width']}x{v['height']} @ {v['r_frame_rate']} ({sz_mb:.2f} MB)")
    print(f"  Video / Audio Dur:  {v_dur:.2f}s / {a_dur:.2f}s (Sync Drift: {drift:.1f} ms)")
    print(f"  Integrated LUFS:    {i_lufs[-1] if i_lufs else 'N/A'} LUFS (Target: -16.0)")
    print(f"  True Peak:          {tp[-1] if tp else 'N/A'} dBFS")
    print("=" * 50)

if __name__ == "__main__":
    t0 = time.time()
    mix_master_audio()
    render_segments()
    extract_thumbnails_and_metadata()
    audit_final_master()
    print(f"✅ L07 PRODUCTION COMPLETE in {time.time() - t0:.1f}s!")
