import os
import subprocess

OUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\audio_takes\voice_shootout"
PYTHON_EXE = r"C:\Users\sar1s\AppData\Local\Programs\Python\Python312\python.exe"

# 1. Hindi test (matching Rian's text)
rian_text = "जब मैंने इस प्रोडक्ट को करीब से देखा, तो मुझे एहसास हुआ कि यह एक नकली प्रोडक्ट है।"
rian_txt_path = os.path.join(OUT_DIR, "rian_text.txt")
with open(rian_txt_path, "w", encoding="utf-8") as f:
    f.write(rian_text)

madhur_raw = os.path.join(OUT_DIR, "replicate_madhur_raw.mp3")
madhur_mastered = os.path.join(OUT_DIR, "replicate_madhur_mastered.mp3")

subprocess.run([
    PYTHON_EXE, "-m", "edge_tts",
    "--voice", "hi-IN-MadhurNeural",
    "--rate", "+8%",
    "-f", rian_txt_path,
    "--write-media", madhur_raw
])

# 2. English test (matching Adam's text)
adam_text = "Hey, Adam here. Let's create something that feels real, sounds human, and connects every time."
adam_txt_path = os.path.join(OUT_DIR, "adam_text.txt")
with open(adam_txt_path, "w", encoding="utf-8") as f:
    f.write(adam_text)

andrew_raw = os.path.join(OUT_DIR, "replicate_andrew_raw.mp3")
andrew_mastered = os.path.join(OUT_DIR, "replicate_andrew_mastered.mp3")
subprocess.run([
    PYTHON_EXE, "-m", "edge_tts",
    "--voice", "en-US-AndrewMultilingualNeural",
    "--rate", "+12%",
    "-f", adam_txt_path,
    "--write-media", andrew_raw
])

brian_raw = os.path.join(OUT_DIR, "replicate_brian_raw.mp3")
brian_mastered = os.path.join(OUT_DIR, "replicate_brian_mastered.mp3")
subprocess.run([
    PYTHON_EXE, "-m", "edge_tts",
    "--voice", "en-US-BrianMultilingualNeural",
    "--rate", "+12%",
    "-f", adam_txt_path,
    "--write-media", brian_raw
])

# Master both with Studio Sharp DSP
dsp = (
    "highpass=f=90,"
    "equalizer=f=220:t=q:w=1.2:g=-3.5,"
    "equalizer=f=340:t=q:w=1.4:g=-2.0,"
    "equalizer=f=3500:t=q:w=1.5:g=3.5,"
    "equalizer=f=5200:t=q:w=1.8:g=2.0,"
    "treble=g=2.5:f=11000,"
    "speechnorm=e=4:r=0.0001:l=1,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=120:makeup=2.5,"
    "loudnorm=I=-16.0:LRA=7.0:TP=-1.5"
)

for raw, out in [(madhur_raw, madhur_mastered), (andrew_raw, andrew_mastered), (brian_raw, brian_mastered)]:
    if os.path.exists(raw):
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", dsp,
            "-c:a", "libmp3lame", "-b:a", "320k",
            out
        ], capture_output=True)
        print(f"Generated {out}: {os.path.exists(out)}")

