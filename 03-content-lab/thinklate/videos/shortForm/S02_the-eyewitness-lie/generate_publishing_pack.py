import os
import json
import subprocess

SHORT_DIR = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/shortForm/S02_the-eyewitness-lie")
PUB_DIR = os.path.join(SHORT_DIR, "publishing_pack")
os.makedirs(PUB_DIR, exist_ok=True)

MASTER_MP4 = os.path.join(SHORT_DIR, "ThinkLate_Short02_The_Eyewitness_Lie_1080x1920_MASTER.mp4")

# 1. Extract 4 High-CTR Cover Frames
frames = [
    ("cover_01_sworn_affidavit.png", "00:00:03.500"),
    ("cover_02_certainty_meter.png", "00:00:08.500"),
    ("cover_03_dna_exoneration.png", "00:00:19.500"),
    ("cover_04_70_percent_stat.png", "00:00:26.500"),
]

for name, ts in frames:
    out_path = os.path.join(PUB_DIR, name)
    cmd = [
        "ffmpeg", "-y",
        "-ss", ts,
        "-i", MASTER_MP4,
        "-vframes", "1",
        "-q:v", "2",
        out_path
    ]
    subprocess.run(cmd, creationflags=0x08000000, check=True)
    print(f"[+] Extracted cover frame: {name}")

# 2. Generate SRT subtitles
TS_PATH = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/longForm/L06_the-memory-lie/transcription_timestamps.json")
with open(TS_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

short_words = []
for s in data["segments"]:
    if s["end"] <= 38.0:
        for w in s.get("words", []):
            short_words.append(w)

def fmt_srt(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

srt_path = os.path.join(PUB_DIR, "subtitles_en.srt")
with open(srt_path, "w", encoding="utf-8") as f:
    idx = 1
    for i in range(0, len(short_words), 2):
        grp = short_words[i:i+2]
        st = grp[0]["start"]
        en = max(grp[-1]["end"], st + 0.35)
        txt = " ".join(w["word"] for w in grp).strip()
        f.write(f"{idx}\n{fmt_srt(st)} --> {fmt_srt(en)}\n{txt}\n\n")
        idx += 1
print(f"[+] Subtitles generated: {srt_path}")

# 3. Copy-Paste Metadata
meta_txt = """=== YOUTUBE SHORTS PUBLISHING METADATA ===

TITLE (Test & Compare 3 Variations):
A: Why Eyewitnesses Lie Without Knowing (36 chars)
B: The Woman Who Jailed an Innocent Man (36 chars)
C: Your Memories Never Happened (27 chars)

DESCRIPTION:
In 1984, Jennifer Thompson looked straight at a judge and swore on a Bible she recognized her attacker. She was 100% certain. 

11 years later, DNA testing proved Ronald Cotton was completely innocent.

Over 70% of wrongful convictions overturned by DNA evidence share this exact flaw: an eyewitness who was calm, totally confident, and dead wrong. 

Your brain does not record video files. Every memory is a fresh hallucination. Full documentary breakdown on ThinkLate.

#ThinkLate #Neuroscience #Psychology #TrueCrime #Science #Shorts #Mindset
"""

with open(os.path.join(PUB_DIR, "COPY_PASTE_METADATA.txt"), "w", encoding="utf-8") as f:
    f.write(meta_txt)
print(f"[+] Metadata written: COPY_PASTE_METADATA.txt")
