import subprocess

src = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
for t in [600, 1200, 1400, 1600, 1800, 2000, 2200, 2400]:
    out_file = f"c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/05_how-airbnb-stole-100b/assets/gameplay_samples/check_{t}s.jpg"
    cmd = ["ffmpeg", "-y", "-ss", str(t), "-i", src, "-vframes", "1", "-q:v", "2", out_file]
    subprocess.run(cmd, creationflags=0x08000000)
print("Done checking action frames")

