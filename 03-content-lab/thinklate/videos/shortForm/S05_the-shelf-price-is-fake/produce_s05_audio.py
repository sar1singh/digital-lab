#!/usr/bin/env python3
"""
Produce Master Voiceover and Whisper Millisecond Timestamps for Short S05 ("The Shelf Price Is Fake")
"""
import asyncio
import json
import os
import pathlib
import subprocess
import edge_tts
import whisper

SHORT_DIR = pathlib.Path(__file__).resolve().parent
AUDIO_DIR = SHORT_DIR / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

SCRIPT_TEXT = (
    "The price printed on the yellow shelf tag is not what you pay at the register. "
    "In federal court, regulators caught discount giant Dollar General quietly overcharging "
    "customers at checkout across thousands of stores after thirty thousand complaints. "
    "The company blamed manual tag updates. "
    "So why did millions of shoppers never say a word? "
    "Because when you are standing at the register with four tired strangers waiting behind you, "
    "you feel embarrassed to hold up the line over thirty-five cents. "
    "Retailers count on that social shame. "
    "Nobody sues over a quarter. "
    "But when ten million polite shoppers walk away every day, "
    "thirty cents turns into a hundred-million-dollar corporate dividend. "
    "Next time that register screen jumps, do not stay quiet to be polite. "
    "Hold up the line. "
    "Because that extra quarter wasn't an honest mistake. "
    "It was your quiet surrender."
)

VOICE = "en-US-ChristopherNeural"
RATE = "+4%"
PITCH = "-2Hz"

RAW_VOICE = AUDIO_DIR / "voiceover_raw.mp3"
FILTERED_VOICE = AUDIO_DIR / "voiceover_clean.wav"
TIMESTAMPS_JSON = SHORT_DIR / "transcription_timestamps.json"
SUBTITLES_SRT = SHORT_DIR / "subtitles_en.srt"

async def synthesize():
    print(f"[*] Synthesizing voiceover with {VOICE} ({RATE}, {PITCH})...")
    comm = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate=RATE, pitch=PITCH)
    await comm.save(str(RAW_VOICE))
    print("[+] Raw TTS generated:", RAW_VOICE)

def process_audio():
    print("[*] Normalizing vocal master via FFmpeg...")
    # Clean filter chain: gentle silence strip at ends, gentle lowpass at 8.5kHz, standard broadcast loudness
    cmd = [
        "ffmpeg", "-y",
        "-i", str(RAW_VOICE),
        "-af", (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.060:stop_threshold=-44dB,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.0,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
        "-ar", "48000",
        "-ac", "2",
        str(FILTERED_VOICE)
    ]
    subprocess.run(cmd, check=True, creationflags=0x08000000 if os.name == "nt" else 0)
    print("[+] Clean vocal master exported:", FILTERED_VOICE)

def transcribe():
    print("[*] Running Whisper base model for word-accurate alignment...")
    model = whisper.load_model("base")
    result = model.transcribe(str(FILTERED_VOICE), word_timestamps=True, language="en")
    
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
            
            e_h = int(end_sec // 3600)
            e_m = int((end_sec % 3600) // 60)
            e_s = int(end_sec % 60)
            e_ms = int(round((end_sec - int(end_sec)) * 1000))

            f.write(f"{idx}\n")
            f.write(f"{s_h:02d}:{s_m:02d}:{s_s:02d},{s_ms:03d} --> {e_h:02d}:{e_m:02d}:{e_s:02d},{e_ms:03d}\n")
            f.write(f"{seg['text'].strip()}\n\n")
            idx += 1
    print(f"[+] Exported SRT to {SUBTITLES_SRT}")

    probe = subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(FILTERED_VOICE)],
        creationflags=0x08000000 if os.name == "nt" else 0
    )
    dur = float(probe.decode().strip())
    print(f"=== Audio Production Summary ===")
    print(f"  Vocal Track Duration: {dur:.2f} seconds")
    print(f"  Total Words:          {len(words_data)}")
    print(f"  Estimated Pacing:     {len(words_data) / (dur / 60):.1f} WPM")

if __name__ == "__main__":
    asyncio.run(synthesize())
    process_audio()
    transcribe()

