import os
import subprocess

video_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = os.path.join(video_dir, "assets", "gameplay_samples")
os.makedirs(out_dir, exist_ok=True)

src = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"

# Sample every 120 seconds across 69 minutes
timestamps = range(120, 3900, 180)

for t in timestamps:
    out_file = os.path.join(out_dir, f"sample_{t:04d}s.jpg")
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(t),
        "-i", src,
        "-vframes", "1",
        "-q:v", "2",
        out_file
    ]
    subprocess.run(cmd, creationflags=0x08000000)

print(f"Sampled {len(timestamps)} frames into {out_dir}")

