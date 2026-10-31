"""
Transcribe ThinkLate Video 05 Master Voiceover using Whisper.
Extracts millisecond-accurate timestamps for speech-to-visual alignment.
"""

import os
import sys
import json
import time

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = os.path.join(VIDEO_DIR, "audio_takes", "dual_voice_mastered.wav")
OUT_JSON   = os.path.join(VIDEO_DIR, "transcription_timestamps.json")
OUT_MD     = os.path.join(VIDEO_DIR, "transcription_timestamps.md")
OUT_SRT    = os.path.join(VIDEO_DIR, "subtitles_en.srt")

def format_srt_time(sec):
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    millis = int((sec - int(sec)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def transcribe():
    import whisper

    if not os.path.exists(AUDIO_PATH):
        print(f"Error: Audio file not found: {AUDIO_PATH}")
        sys.exit(1)

    print(f"Loading Whisper model ('base')...")
    t0 = time.time()
    model = whisper.load_model("base")
    print(f"Model loaded in {time.time()-t0:.2f}s.")

    print(f"Transcribing {AUDIO_PATH} (~10m 07s)...")
    result = model.transcribe(AUDIO_PATH, language="en", verbose=False)

    segments = result.get("segments", [])
    print(f"Extracted {len(segments)} spoken segments.")

    json_records = []
    md_lines = [
        "# ThinkLate Video 05 Spoken Audio Timestamps",
        f"**Source Audio:** `voice_mastered.mp3`  ",
        f"**Total Segments:** {len(segments)}  \n",
        "| ID | Timecode | Start (s) | End (s) | Spoken Words |",
        "| :-: | :--- | :-: | :-: | :--- |"
    ]
    srt_lines = []

    for i, seg in enumerate(segments, 1):
        s = round(seg["start"], 2)
        e = round(seg["end"], 2)
        m_s, sec_s = divmod(int(s), 60)
        m_e, sec_e = divmod(int(e), 60)
        tc = f"{m_s:02d}:{sec_s:02d} - {m_e:02d}:{sec_e:02d}"
        txt = seg["text"].strip()

        json_records.append({
            "id": i,
            "start": s,
            "end": e,
            "timecode": tc,
            "text": txt
        })

        md_lines.append(f"| {i} | `{tc}` | {s:.2f} | {e:.2f} | {txt} |")

        srt_lines.append(f"{i}")
        srt_lines.append(f"{format_srt_time(s)} --> {format_srt_time(e)}")
        srt_lines.append(txt)
        srt_lines.append("")

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_records, f, indent=2, ensure_ascii=False)
    print(f"Saved: {OUT_JSON}")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Saved: {OUT_MD}")

    with open(OUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))
    print(f"Saved: {OUT_SRT}")

    print("\nTranscription complete! Ground truth speech boundaries generated.")

if __name__ == "__main__":
    transcribe()

