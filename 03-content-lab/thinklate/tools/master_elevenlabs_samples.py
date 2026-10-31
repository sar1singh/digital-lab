import os
import subprocess

DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\audio_takes\voice_shootout"

samples = [
    "elevenlabs_adam_sample",
    "elevenlabs_chris_sample",
    "elevenlabs_brian_sample",
    "elevenlabs_will_sample",
    "elevenlabs_george_sample"
]

filter_chain = (
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

for name in samples:
    raw_file = os.path.join(DIR, f"{name}.mp3")
    mastered_file = os.path.join(DIR, f"{name}_mastered.mp3")
    if os.path.exists(raw_file):
        cmd = [
            "ffmpeg", "-y", "-i", raw_file,
            "-af", filter_chain,
            "-c:a", "libmp3lame", "-b:a", "320k",
            mastered_file
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Mastered: {mastered_file} ({os.path.getsize(mastered_file)} bytes)")
        else:
            print(f"Error mastering {name}: {res.stderr}")
