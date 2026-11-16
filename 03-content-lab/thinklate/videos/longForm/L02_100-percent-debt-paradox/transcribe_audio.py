"""
Transcribe ThinkLate Video 2 Master Audio using faster-whisper.
Extracts exact word-level and sentence-level timestamps for the spoken audio.
"""

import os
import json
import time
from faster_whisper import WhisperModel

AUDIO_PATH = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\audio_takes\voice_mastered_balanced.wav"
OUT_JSON   = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\transcription_timestamps.json"
OUT_MD     = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\transcription_timestamps.md"

def transcribe():
    print(f"Loading faster-whisper model ('base')...")
    t0 = time.time()
    # Use CPU or CUDA if available
    # Use CPU int8 for reliable universal execution
    model = WhisperModel("base", device="cpu", compute_type="int8")
    print("Using CPU (int8 quantization) for Whisper transcription...")

    print(f"Transcribing {AUDIO_PATH}...")
    segments, info = model.transcribe(AUDIO_PATH, beam_size=5, language="en")
    print(f"Detected language: {info.language} with probability {info.language_probability:.2f}")

    results = []
    lines_md = [
        "# Spoken Audio Transcription with Exact Timecodes",
        f"**File:** `voice_mastered_balanced.wav`  ",
        f"**Duration:** {info.duration:.2f}s  \n",
        "| Timecode | Start (s) | End (s) | Spoken Words |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for seg in segments:
        m_s, s_s = divmod(int(seg.start), 60)
        m_e, s_e = divmod(int(seg.end), 60)
        timecode = f"{m_s:02d}:{s_s:02d} - {m_e:02d}:{s_e:02d}"
        text = seg.text.strip()
        results.append({
            "id": seg.id,
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "duration": round(seg.end - seg.start, 2),
            "timecode": timecode,
            "text": text
        })
        lines_md.append(f"| `{timecode}` | `{seg.start:06.2f}` | `{seg.end:06.2f}` | {text} |")
        print(f"[{timecode}] {text}")

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_md))

    print(f"\n[DONE] Transcribed {len(results)} segments in {time.time()-t0:.2f}s!")
    print(f"Saved to: {OUT_JSON} and {OUT_MD}")

if __name__ == '__main__':
    transcribe()
