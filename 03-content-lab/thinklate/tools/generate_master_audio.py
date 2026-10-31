#!/usr/bin/env python3
"""
ThinkLate - Universal Automated Broadcast Voiceover Generator & Mastering Engine
Uses en-US-GuyNeural (Naturally Lean, Bright, Articulate) + Studio Sharp Mastering EQ
Usage:
    python tools/generate_master_audio.py [video_folder_path]
"""

import asyncio
import os
import sys
import re
import subprocess
import edge_tts

DEFAULT_VIDEO_DIR = r"C:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap"

VOICE = "en-US-BrianMultilingualNeural"
RATE = "+12%"

# Studio Sharp EQ Mastering Chain (Tuned specifically for Brian Multilingual)
EQ_STUDIO_SHARP = (
    "highpass=f=90,"
    "equalizer=f=220:t=q:w=1.2:g=-3.5,"     # Kills chest boom & proximity mud
    "equalizer=f=340:t=q:w=1.4:g=-2.0,"     # Removes boxy lower-mid resonance
    "equalizer=f=3500:t=q:w=1.5:g=3.5,"     # Sharp presence & consonant bite
    "equalizer=f=5200:t=q:w=1.8:g=2.0,"     # Speech articulation
    "treble=g=2.5:f=11000,"                 # Crystalline modern YouTube air
    "speechnorm=e=4:r=0.0001:l=1,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=120:makeup=2.5,"
    "loudnorm=I=-16.0:LRA=7.0:TP=-1.5"
)

def extract_spoken_script(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    spoken_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("["):
            continue
        if stripped.startswith("*"):
            continue
        if stripped.startswith("---"):
            continue

        # Replace breath markers with natural punctuation pauses
        text = stripped.replace("///", ".")
        text = text.replace("//", ",")

        # Clean spaces and double punctuation
        text = re.sub(r'\s*,\s*', ', ', text)
        text = re.sub(r'\s*\.\s*', '. ', text)
        text = re.sub(r',\s*\.', '.', text)
        text = re.sub(r'\.{2,}', '.', text)
        text = re.sub(r'\s+', ' ', text).strip()

        if text:
            spoken_lines.append(text)

    return " \n".join(spoken_lines)

async def generate_and_master(video_dir):
    script_file = os.path.join(video_dir, "script_final.md")
    audio_dir = os.path.join(video_dir, "assets", "audio")
    temp_raw = os.path.join(audio_dir, "temp_raw_guy.mp3")
    output_mp3 = os.path.join(audio_dir, "voiceover_mastered.mp3")

    if not os.path.exists(script_file):
        print(f"Error: Script not found: {script_file}")
        return False

    os.makedirs(audio_dir, exist_ok=True)
    full_text = extract_spoken_script(script_file)
    words = full_text.split()
    print(f"[1/3] Spoken dialogue extracted: {len(words)} words, {len(full_text)} characters.")
    print(f"[2/3] Synthesizing raw voice with {VOICE} (rate: {RATE})...")

    # Step 1: Synthesize Raw Audio via direct CLI invocation
    temp_txt = os.path.join(audio_dir, "temp_spoken_text.txt")
    with open(temp_txt, "w", encoding="utf-8") as f:
        f.write(full_text)

    cmd_tts = [
        sys.executable, "-m", "edge_tts",
        "--voice", VOICE,
        "--rate", RATE,
        "-f", temp_txt,
        "--write-media", temp_raw
    ]
    res_tts = subprocess.run(cmd_tts, capture_output=True, text=True)
    if res_tts.returncode != 0:
        print("TTS Synthesis Error:\n", res_tts.stderr)
        return False
    print(f"  Raw audio saved: {temp_raw}")

    # Step 2: Apply Broadcast Studio Sharp Mastering Filter Chain in FFmpeg
    print(f"[3/3] Applying Studio Sharp Broadcast Mastering EQ Chain...")
    cmd = [
        "ffmpeg", "-y",
        "-i", temp_raw,
        "-af", EQ_STUDIO_SHARP,
        "-b:a", "192k",
        output_mp3
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("FFmpeg Mastering Error:\n", res.stderr)
        return False

    # Cleanup temp raw file
    if os.path.exists(temp_raw):
        os.remove(temp_raw)

    file_size_mb = os.path.getsize(output_mp3) / (1024 * 1024)
    print(f"\n=======================================================")
    print(f" [SUCCESS] Master Broadcast Audio Live!")
    print(f" Target: {os.path.basename(video_dir)}")
    print(f" File: {output_mp3}")
    print(f" Voice: {VOICE} | Profile: Studio Sharp")
    print(f" File Size: {file_size_mb:.2f} MB")
    print(f"=======================================================")
    return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VIDEO_DIR
    target_path = os.path.abspath(target)
    asyncio.run(generate_and_master(target_path))
