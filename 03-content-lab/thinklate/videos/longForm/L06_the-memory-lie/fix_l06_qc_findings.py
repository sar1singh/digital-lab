#!/usr/bin/env python3
"""
Patches transcription_timestamps.json at the root word-level, regenerates subtitles_l06_master.ass
and subtitles_en.srt, and runs the final 25s NVENC subtitle burn-in + audio mux.
"""
import pathlib
import subprocess

VIDEO_DIR = pathlib.Path(__file__).resolve().parent
TS_JSON = VIDEO_DIR / "transcription_timestamps.json"

txt = TS_JSON.read_text(encoding="utf-8")

WORD_FIXES = [
    ('"word": " damn"', '"word": " dim"'),
    ('"word": "damn"', '"word": "dim"'),
    ("a damn refrigerator", "a dim refrigerator"),
    ('"word": " Reconcilitation."', '"word": " Reconsolidation."'),
    ('"word": "Reconcilitation."', '"word": "Reconsolidation."'),
    ("Memory Reconcilitation.", "Memory Reconsolidation."),
    ('"word": " Pride"', '"word": " Cried"'),
    ('"word": "Pride"', '"word": "Cried"'),
    ("Pride for hours", "Cried for hours"),
    ('"word": " safe."', '"word": " save."'),
    ('"word": "safe."', '"word": "save."'),
    ("hit safe.", "hit save."),
    ('"word": " Oh,"', '"word": " Owl,"'),
    ('"word": "Oh,"', '"word": "Owl,"'),
    ("part. Oh, Jennifer", "part, Owl. Jennifer"),
    ('"word": " All."', '"word": " Owl."'),
    ('"word": "All."', '"word": "Owl."'),
    ("pretending. All.", "pretending, Owl."),
    ('"word": " We\'re"', '"word": " Were"'),
    ('"word": "We\'re"', '"word": "Were"'),
    ("We're comforted", "Were comforted"),
    ("We're finally", "Were finally"),
    ('"word": " But"', '"word": " Put"'),
    ('"word": "But"', '"word": "Put"'),
    ("But the ego down.", "Put the ego down."),
]

for old, new in WORD_FIXES:
    txt = txt.replace(old, new)

TS_JSON.write_text(txt, encoding="utf-8")
print("[+] Patched root transcription_timestamps.json")

# Regenerate subtitles_l06_master.ass & subtitles_en.srt
subprocess.run(
    ["python", str(VIDEO_DIR / "generate_l06_master_subtitles.py")],
    check=True, creationflags=0x08000000
)

# Run compile_l06_documentary_master.py (all 23 scenes are cached, so it only runs the final subtitle burn-in!)
subprocess.run(
    ["python", str(VIDEO_DIR / "compile_l06_documentary_master.py")],
    check=True, creationflags=0x08000000
)

# Extract preview 5 at 412.5s to verify "PUT THE"
master_mp4 = VIDEO_DIR / "ThinkLate_L06_The_Memory_Lie_1080p_MASTER.mp4"
subprocess.run(
    ["ffmpeg", "-y", "-ss", "412.5", "-i", str(master_mp4), "-frames:v", "1", "-q:v", "2", str(VIDEO_DIR / "assets" / "master_preview_5.jpg")],
    check=True, creationflags=0x08000000, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)
print("[+] Extracted verified master_preview_5.jpg")
