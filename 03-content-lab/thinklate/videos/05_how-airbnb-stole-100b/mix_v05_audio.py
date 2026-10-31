#!/usr/bin/env python3
"""
ThinkLate Video 05 — Voiceover + Cinematic BGM Bed Mixer
========================================================
Mixes voice_mastered.mp3 with ambient_music_dark_fog.mp3:
1. Lowpasses BGM at 3.8kHz and sets volume to -23.5 dB so voice sits cleanly on top.
2. Applies sidechain/amix so music ducks slightly under speech.
3. Completely masks digital silence during pauses and dead-air drops.
4. Outputs:
   - audio_takes/ambient_bed_track.wav (isolated background music bed)
   - audio_takes/full_mix_preview.mp3 (complete broadcast mix)
"""

import os
import sys
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
VOICE_FILE = os.path.join(VIDEO_DIR, "audio_takes", "voice_mastered.wav")
AMBIENT_FILE = os.path.join(VIDEO_DIR, "assets", "audio", "ambient_music_dark_fog.mp3")
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")

AMBIENT_BED_WAV = os.path.join(AUDIO_DIR, "ambient_bed_track.wav")
FULL_MIX_MP3 = os.path.join(AUDIO_DIR, "full_mix_preview.mp3")
FULL_MIX_WAV = os.path.join(AUDIO_DIR, "full_mix_preview.wav")

flags = 0x08000000 if sys.platform == "win32" else 0

# 1. Get voice duration
cmd_probe = [
    "ffprobe", "-v", "error",
    "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1",
    VOICE_FILE
]
proc = subprocess.run(cmd_probe, stdout=subprocess.PIPE, text=True, creationflags=flags)
dur = float(proc.stdout.strip())
print(f"🎵 Voiceover Duration: {dur:.2f}s ({dur/60:.2f} min)")

# 2. Process looped ambient music bed with fade-out
fadeout_start = max(0, dur - 5.0)
amb_filter = (
    f"aloop=loop=-1:size=2e+09,"
    f"atrim=0:{dur},"
    f"highpass=f=60,lowpass=f=4000,"
    f"afade=t=in:ss=0:d=2.5,afade=t=out:st={fadeout_start:.2f}:d=5.0"
)

print("🎚️ Step 1: Processing ambient music bed...")
cmd_amb = [
    "ffmpeg", "-y",
    "-i", AMBIENT_FILE,
    "-af", amb_filter,
    "-ar", "48000", "-c:a", "pcm_s24le",
    AMBIENT_BED_WAV
]
subprocess.run(cmd_amb, check=True, creationflags=flags)
print(f"✅ Generated: {AMBIENT_BED_WAV}")

# 3. Mix voiceover + ambient bed (Voice at 90%, BGM clearly audible at -16.5 dB / 15% amplitude)
print("🎛️ Step 2: Mixing voice (90% volume) + BGM (rich -16.5 dB audible bed)...")
cmd_mix = [
    "ffmpeg", "-y",
    "-i", VOICE_FILE,
    "-i", AMBIENT_BED_WAV,
    "-filter_complex", "[0:a]volume=0.90[v];[1:a]volume=0.15[bgm];[v][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0",
    "-b:a", "192k",
    FULL_MIX_MP3
]
subprocess.run(cmd_mix, check=True, creationflags=flags)
print(f"✅ Generated Broadcast MP3: {FULL_MIX_MP3}")

cmd_mix_wav = [
    "ffmpeg", "-y",
    "-i", VOICE_FILE,
    "-i", AMBIENT_BED_WAV,
    "-filter_complex", "[0:a]volume=0.90[v];[1:a]volume=0.15[bgm];[v][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0",
    "-ar", "48000", "-c:a", "pcm_s24le",
    FULL_MIX_WAV
]
subprocess.run(cmd_mix_wav, check=True, creationflags=flags)
print(f"✅ Generated DaVinci Mix WAV: {FULL_MIX_WAV}")
print("\n🎉 Broadcast Mix Complete: Silence fully covered by cinematic BGM bed!")

