"""
Convert Whisper Transcription JSON into Broadcast-Standard SubRip Subtitle (.srt)
"""

import os
import json

JSON_FILE = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\transcription_timestamps.json"
SRT_FILE  = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\subtitles_en.srt"

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def convert():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    srt_lines = []
    for idx, item in enumerate(data, start=1):
        start_tc = format_timestamp(item["start"])
        end_tc   = format_timestamp(item["end"])
        text     = item["text"].strip()
        srt_lines.append(str(idx))
        srt_lines.append(f"{start_tc} --> {end_tc}")
        srt_lines.append(text)
        srt_lines.append("")

    with open(SRT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"Generated SubRip SRT file with {len(data)} cues: {SRT_FILE}")

if __name__ == '__main__':
    convert()
