"""
Transcribe ThinkLate Video 03 Master Voiceover using Whisper.
Extracts millisecond-accurate timestamps for speech-to-visual alignment.
"""

import os
import sys
import json
import time

AUDIO_PATH = r"videos\03_death_of_ownership\audio_takes\voiceover_raw_mastered.wav"
OUT_JSON   = r"videos\03_death_of_ownership\transcription_timestamps.json"
OUT_MD     = r"videos\03_death_of_ownership\transcription_timestamps.md"
OUT_SRT    = r"videos\03_death_of_ownership\subtitles_en.srt"

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

    print(f"Transcribing {AUDIO_PATH} (10m 07s)...")
    result = model.transcribe(AUDIO_PATH, language="en", verbose=False)

    segments = result.get("segments", [])
    print(f"Extracted {len(segments)} spoken segments.")

    json_records = []
    md_lines = [
        "# ThinkLate Video 03 Spoken Audio Timestamps",
        f"**Source Audio:** `voiceover_raw_mastered.wav`  ",
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
            "duration": round(e - s, 2),
            "timecode": tc,
            "text": txt
        })

        md_lines.append(f"| {i} | `{tc}` | `{s:06.2f}` | `{e:06.2f}` | {txt} |")

        # SRT format
        srt_lines.append(f"{i}")
        srt_lines.append(f"{format_srt_time(s)} --> {format_srt_time(e)}")
        srt_lines.append(f"{txt}\n")

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_records, f, indent=2)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    with open(OUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"\n[SUCCESS] Transcription completed in {time.time()-t0:.2f}s!")
    print(f"Exported JSON: {OUT_JSON}")
    print(f"Exported MD:   {OUT_MD}")
    print(f"Exported SRT:  {OUT_SRT}")

if __name__ == '__main__':
    transcribe()
