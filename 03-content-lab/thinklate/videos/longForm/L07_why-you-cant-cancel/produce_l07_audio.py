#!/usr/bin/env python3
"""
ThinkLate Episode L07 ("Why You Can't Cancel Anything") — Master Voiceover & Whisper Pipeline
=============================================================================================
1. Parses script_final.md for spoken lines (ignoring [VISUAL/SFX/DEAD AIR] and markdown headers)
2. Synthesizes voiceover via Edge-TTS (Eddy Thinklate: en-US-ChristopherNeural @ +4%, -2Hz)
3. Normalizes audio to broadcast standard (-16 LUFS, -1.0 True Peak)
4. Transcribes audio via Whisper to create transcription_timestamps.json, subtitles_en.srt, and subtitles_l07_master.ass
"""

import asyncio
import json
import os
import pathlib
import re
import subprocess
import sys
import edge_tts
import whisper

sys.stdout.reconfigure(encoding="utf-8")

L07_DIR = pathlib.Path(__file__).resolve().parent
SCRIPT_MD = L07_DIR / "script_final.md"
AUDIO_DIR = L07_DIR / "assets" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

RAW_MP3 = AUDIO_DIR / "voiceover_raw.mp3"
CLEAN_WAV = AUDIO_DIR / "voiceover_clean.wav"
TIMESTAMPS_JSON = L07_DIR / "transcription_timestamps.json"
SUBTITLES_SRT = L07_DIR / "subtitles_en.srt"
SUBTITLES_ASS = L07_DIR / "subtitles_l07_master.ass"

VOICE = "en-US-ChristopherNeural"
RATE = "+4%"
PITCH = "-2Hz"

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def extract_spoken_text():
    with open(SCRIPT_MD, "r", encoding="utf-8") as f:
        lines = f.readlines()

    spoken_lines = []
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith("#") or line_str.startswith("["):
            continue
        # Clean breath markers for TTS pronunciation
        # Replace /// with full stop pause, // with comma pause
        clean = line_str.replace("///", ".").replace("//", ",")
        # Remove any internal brackets if present
        clean = re.sub(r'\[.*?\]', '', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()
        if clean:
            spoken_lines.append(clean)

    full_text = " ".join(spoken_lines)
    # Clean up double periods or spaces
    full_text = re.sub(r'\.\s*\.', '.', full_text)
    full_text = re.sub(r',\s*,', ',', full_text)
    return full_text

async def synthesize(text: str):
    print(f"[*] Synthesizing {len(text.split())} words with {VOICE} ({RATE}, {PITCH})...")
    comm = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await comm.save(str(RAW_MP3))
    print(f"[+] Raw TTS generated: {RAW_MP3}")

def process_audio():
    print("[*] Normalizing vocal master via FFmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(RAW_MP3),
        "-af", (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.060:stop_threshold=-44dB,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.0,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
        "-ar", "48000",
        "-ac", "2",
        str(CLEAN_WAV)
    ]
    subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)
    print(f"[+] Broadcast-clean voiceover: {CLEAN_WAV}")

def transcribe():
    print("[*] Running Whisper model for millisecond word alignment...")
    model = whisper.load_model("base")
    result = model.transcribe(str(CLEAN_WAV), word_timestamps=True, language="en")

    words_data = []
    for segment in result["segments"]:
        for w in segment.get("words", []):
            words_data.append({
                "word": w["word"].strip(),
                "start": round(w["start"], 3),
                "end": round(w["end"], 3),
                "probability": round(w.get("probability", 1.0), 3)
            })

    with open(TIMESTAMPS_JSON, "w", encoding="utf-8") as f:
        json.dump(words_data, f, indent=2)
    print(f"[+] Saved {len(words_data)} aligned word tokens to {TIMESTAMPS_JSON}")

    # Generate standard SRT
    with open(SUBTITLES_SRT, "w", encoding="utf-8") as f:
        idx = 1
        for seg in result["segments"]:
            start_sec = seg["start"]
            end_sec = seg["end"]
            
            s_h = int(start_sec // 3600)
            s_m = int((start_sec % 3600) // 60)
            s_s = int(start_sec % 60)
            s_ms = int(round((start_sec - int(start_sec)) * 1000))
            if s_ms >= 1000: s_ms = 999
            
            e_h = int(end_sec // 3600)
            e_m = int((end_sec % 3600) // 60)
            e_s = int(end_sec % 60)
            e_ms = int(round((end_sec - int(end_sec)) * 1000))
            if e_ms >= 1000: e_ms = 999

            f.write(f"{idx}\n")
            f.write(f"{s_h:02d}:{s_m:02d}:{s_s:02d},{s_ms:03d} --> {e_h:02d}:{e_m:02d}:{e_s:02d},{e_ms:03d}\n")
            f.write(f"{seg['text'].strip()}\n\n")
            idx += 1
    print(f"[+] Exported SRT to {SUBTITLES_SRT}")

    # Generate word-synced ASS kinetic subtitles (widescreen 1920x1080)
    generate_widescreen_ass(words_data, result["segments"][-1]["end"])

def fmt_ass_time(sec: float) -> str:
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def generate_widescreen_ass(words: list, total_dur: float):
    hl_color = "&H0000FFE2&"  # Acid Lime #E2FF00 in BGR

    chunks = []
    cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= 5 or w["word"].endswith((".", "!", "?", ",", ":")):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)

    ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: BroadcastSub,Segoe UI,42,&H00FFFFFF,&H0000FFFF,&H00080D1A,&HB404070F,-1,0,0,0,100,100,1.2,0,3,3,0,2,80,80,48,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_events = []
    for chunk in chunks:
        for i, active in enumerate(chunk):
            w_st = active["start"]
            w_en = chunk[i + 1]["start"] if i + 1 < len(chunk) else active["end"]
            if w_en <= w_st:
                w_en = w_st + 0.08
            tokens = []
            for j, tok in enumerate(chunk):
                raw = tok["word"].upper()
                if j == i:
                    tokens.append(f"{{\\c{hl_color}\\b1}}{raw}{{\\c&H00FFFFFF&\\b0}}")
                else:
                    tokens.append(raw)
            line_str = " ".join(tokens)
            ass_events.append(f"Dialogue: 0,{fmt_ass_time(w_st)},{fmt_ass_time(w_en)},BroadcastSub,,0,0,0,,{line_str}")

    SUBTITLES_ASS.write_text(ass_header + "\n".join(ass_events) + "\n", encoding="utf-8")
    print(f"[+] Exported word-synced ASS subtitles to {SUBTITLES_ASS}")

    # Duration probe
    probe = subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(CLEAN_WAV)],
        creationflags=CREATE_NO_WINDOW
    )
    dur = float(probe.decode().strip())
    mins = int(dur // 60)
    secs = int(dur % 60)
    print("=" * 60)
    print(f"✅ VOICE & MASTER CLOCK SUMMARY")
    print(f"   Audio Duration: {mins}m {secs:02d}s ({dur:.2f} seconds)")
    print(f"   Total Tokens:   {len(words)} words")
    print(f"   Vocal Cadence:  {len(words) / (dur / 60):.1f} WPM")
    print("=" * 60)

if __name__ == "__main__":
    text = extract_spoken_text()
    print(f"[*] Extracted spoken text: {len(text.split())} words")
    asyncio.run(synthesize(text))
    process_audio()
    transcribe()
