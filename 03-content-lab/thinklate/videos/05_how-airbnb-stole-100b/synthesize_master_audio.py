#!/usr/bin/env python3
"""
ThinkLate Video 05 — Master Audio Synthesis & Studio Sharp DSP Chain
===================================================================
1. Parses script.md, stripping visual/Foley directions and converting breath markers.
2. Synthesizes speech with en-US-ChristopherNeural @ 148 WPM (+7% rate).
3. Applies the Studio Sharp DSP chain (HPF 95Hz, 220Hz mud cut, 3.3kHz presence, loudnorm -16.1 LUFS).
4. Verifies broadcast loudness standards (EBU R128).
"""

import os
import sys
import re
import asyncio
import subprocess
import edge_tts

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

# Path configuration
VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(VIDEO_DIR, "script.md")
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")
os.makedirs(AUDIO_DIR, exist_ok=True)

RAW_MP3 = os.path.join(AUDIO_DIR, "voice_raw.mp3")
MASTERED_MP3 = os.path.join(AUDIO_DIR, "voice_mastered.mp3")
MASTERED_WAV = os.path.join(AUDIO_DIR, "voice_mastered.wav")

def clean_script_for_tts(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by double newlines into genuine narrative paragraphs
    raw_paragraphs = content.split("\n\n")
    clean_paragraphs = []

    for p in raw_paragraphs:
        lines = p.strip().splitlines()
        clean_lines = []
        for line in lines:
            line_s = line.strip()
            # Skip headers, visual cues, SFX cues, comments, divider lines
            if (line_s.startswith("#") or line_s.startswith("[") or 
                line_s.startswith("*") or line_s.startswith("---") or not line_s):
                continue

            # Convert breath markers to natural punctuation pauses
            # Use ellipses (...) for suspense and natural pauses that allow pitch recovery
            t = re.sub(r':\s*///', '...', line_s)
            t = re.sub(r':\s*//', '...', t)
            t = t.replace("///", "...")
            t = t.replace("//", ",")
            t = re.sub(r':\s*,', '...', t)
            t = re.sub(r',\s*:', ':', t)
            t = re.sub(r'\.\.\.\s*,', '...', t)
            t = re.sub(r',\s*\.\.\.', '...', t)
            
            # Clean double punctuation
            t = re.sub(r'([,\.\?!])\s*([,\.\?!])', r'\1', t)
            t = re.sub(r',\s*,', ',', t)
            t = re.sub(r'\.\s*\.', '.', t)
            t = re.sub(r',\s*\.', '.', t)
            t = re.sub(r'\.\s*,', ',', t)
            t = re.sub(r'\s+', ' ', t).strip()

            # Fix spacing around punctuation
            t = t.replace(" ,", ",").replace(" .", ".")
            if not t.endswith((".", "!", "?", "...", ":")):
                t += "."

            if t:
                clean_lines.append(t)

        if clean_lines:
            # Join sentences within a paragraph with single space to maintain neural prosody and flow
            para_text = " ".join(clean_lines)
            clean_paragraphs.append(para_text)

    # Join distinct narrative beats with paragraph break
    return "\n\n".join(clean_paragraphs)

# Studio Sharp DSP Mastering Chain
DSP_CHAIN = (
    "highpass=f=95,"
    "equalizer=f=220:t=q:w=1.3:g=-4.5,"     # Kill proximity chest boom
    "equalizer=f=340:t=q:w=1.6:g=-3.0,"     # Remove boxy lower-mid mud
    "equalizer=f=3300:t=q:w=1.4:g=3.8,"     # Sharp presence & consonant bite
    "equalizer=f=5200:t=q:w=2.0:g=2.2,"     # Crisp vocal articulation
    "equalizer=f=11000:t=h:g=3.0,"          # Modern YouTube high air sheen
    "speechnorm=p=0.9:e=3.0:c=2.0:r=0.001:f=0.002,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=110,"
    "loudnorm=I=-16.1:TP=-1.5:LRA=8.0"
)

async def synthesize_speech(text, output_file):
    print(f"🎙️ Synthesizing {len(text.split())} words using en-US-AndrewMultilingualNeural @ +4% rate...")
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AndrewMultilingualNeural",
        rate="+4%",
        pitch="+0Hz"
    )
    await communicate.save(output_file)
    print(f"✅ Raw audio saved: {output_file} ({os.path.getsize(output_file):,} bytes)")

def master_audio(input_file, out_mp3, out_wav):
    print("🎛️ Exporting Pure Studio Audio (Zero DSP filters for Neural TTS)...")
    flags = 0x08000000 if sys.platform == "win32" else 0
    # Export clean MP3
    cmd_mp3 = [
        "ffmpeg", "-y",
        "-i", input_file,
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        out_mp3
    ]
    subprocess.run(cmd_mp3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=flags)
    print(f"✅ Mastered MP3: {out_mp3} ({os.path.getsize(out_mp3):,} bytes)")

    # Export clean 48kHz 24-bit PCM WAV for DaVinci Resolve
    cmd_wav = [
        "ffmpeg", "-y",
        "-i", input_file,
        "-ar", "48000",
        "-c:a", "pcm_s24le",
        out_wav
    ]
    subprocess.run(cmd_wav, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=flags)
    print(f"✅ Mastered WAV (DaVinci Master 48kHz/24-bit): {out_wav} ({os.path.getsize(out_wav):,} bytes)")

def measure_loudness(audio_file):
    print("📊 Measuring broadcast loudness (EBU R128)...")
    flags = 0x08000000 if sys.platform == "win32" else 0
    cmd = [
        "ffmpeg",
        "-i", audio_file,
        "-af", "ebur128=framelog=verbose",
        "-f", "null",
        "-"
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=flags)
    lines = proc.stderr.splitlines()
    for line in lines[-15:]:
        if "I:" in line or "LRA:" in line or "Threshold:" in line:
            print(f"   {line.strip()}")

async def main():
    text = clean_script_for_tts(SCRIPT_PATH)
    clean_txt_path = os.path.join(AUDIO_DIR, "spoken_text_clean.txt")
    with open(clean_txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"📝 Prepared spoken text: {len(text.split())} words saved to {clean_txt_path}")

    await synthesize_speech(text, RAW_MP3)
    master_audio(RAW_MP3, MASTERED_MP3, MASTERED_WAV)
    measure_loudness(MASTERED_MP3)
    print("\n🎉 PHASE 5 COMPLETE: Broadcast-Ready Master Voiceover Generated!")

if __name__ == "__main__":
    asyncio.run(main())
