#!/usr/bin/env python3
"""
Generate Word-Synced SRT and ASS Broadcast Subtitles for ThinkLate L06 (1920x1080)
===================================================================================
Uses `transcription_timestamps.json` and `takes_timing.json` to build:
  1. `subtitles_en.srt` (for YouTube Studio manual upload)
  2. `subtitles_l06_master.ass` (for widescreen lower-third broadcast burn-in)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TS_PATH = os.path.join(BASE_DIR, "transcription_timestamps.json")
TAKES_PATH = os.path.join(BASE_DIR, "takes_timing.json")
SRT_OUT = os.path.join(BASE_DIR, "subtitles_en.srt")
ASS_OUT = os.path.join(BASE_DIR, "subtitles_l06_master.ass")

with open(TS_PATH, "r", encoding="utf-8") as f:
    ts_data = json.load(f)

with open(TAKES_PATH, "r", encoding="utf-8") as f:
    takes_data = json.load(f)

def get_speaker_at_time(t):
    for tk in takes_data:
        if tk["start"] - 0.1 <= t <= tk["end"] + 0.1:
            return "OWL" if "owl" in tk["file"].lower() else "FALCON"
    return "OWL"

def fmt_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def fmt_ass_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int(round((seconds - int(seconds)) * 100))
    if cs >= 100:
        cs = 99
    return f"{h:01d}:{m:02d}:{s:02d}.{cs:02d}"

all_words = []
for seg in ts_data.get("segments", []):
    for w in seg.get("words", []):
        word_str = w["word"].strip()
        if word_str:
            all_words.append({
                "word": word_str,
                "start": float(w["start"]),
                "end": float(w["end"])
            })

# 1. Generate clean 6-word chunked SRT for YouTube upload
with open(SRT_OUT, "w", encoding="utf-8") as f:
    idx = 1
    for i in range(0, len(all_words), 6):
        grp = all_words[i:i+6]
        st = grp[0]["start"]
        en = max(grp[-1]["end"], st + 0.4)
        txt = " ".join(w["word"] for w in grp)
        f.write(f"{idx}\n{fmt_srt_time(st)} --> {fmt_srt_time(en)}\n{txt}\n\n")
        idx += 1

# 2. Generate Broadcast Widescreen ASS (1920x1080) with Speaker Color & Active Word Highlight
ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: BroadcastSub,Segoe UI,42,&H00FFFFFF,&H0000FFFF,&H00080D1A,&HB404070F,-1,0,0,0,100,100,1.2,0,3,3,0,2,80,80,38,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

ass_events = []
chunk_size = 5
for i in range(0, len(all_words), chunk_size):
    grp = all_words[i:i+chunk_size]
    chunk_st = grp[0]["start"]
    chunk_en = grp[-1]["end"]
    speaker = get_speaker_at_time(chunk_st)
    # ASS BGR color format:
    # Acid Lime (#E2FF00) -> &H0000FFE2&
    # Electric Cyan (#00F0FF) -> &H00FFF000&
    active_col = "\\c&H0000FFE2&" if speaker == "OWL" else "\\c&H00FFF000&"

    for j, active_w in enumerate(grp):
        w_st = active_w["start"]
        w_en = grp[j+1]["start"] if j + 1 < len(grp) else max(active_w["end"], w_st + 0.25)
        if w_en <= w_st:
            w_en = w_st + 0.18

        rendered_words = []
        for k, token in enumerate(grp):
            w_upper = token["word"].upper()
            if k == j:
                rendered_words.append(f"{{{active_col}\\b1}}{w_upper}{{\\c&H00FFFFFF&}}")
            else:
                rendered_words.append(w_upper)

        line_text = " ".join(rendered_words)
        ass_events.append(
            f"Dialogue: 0,{fmt_ass_time(w_st)},{fmt_ass_time(w_en)},BroadcastSub,,0,0,0,,{line_text}"
        )

with open(ASS_OUT, "w", encoding="utf-8") as f:
    f.write(ass_header + "\n".join(ass_events) + "\n")

print(f"[+] Generated SRT ({SRT_OUT}) and ASS ({ASS_OUT}) with {len(ass_events)} word-synced events!")

