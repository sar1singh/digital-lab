import os
import subprocess
from PIL import Image

src = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
out_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\assets\gameplay_frames"
os.makedirs(out_dir, exist_ok=True)

# Sample every 60 seconds from 0 to 3600
timestamps = list(range(10, 3600, 60))
print(f"Sampling {len(timestamps)} frames...")

for t in timestamps:
    out_file = os.path.join(out_dir, f"frame_{t:04d}s.jpg")
    if not os.path.exists(out_file):
        cmd = ["ffmpeg", "-y", "-ss", str(t), "-i", src, "-vframes", "1", "-vf", "scale=640:360", "-q:v", "3", out_file]
        subprocess.run(cmd, creationflags=0x08000000, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Frames extracted. Now analyzing brightness and color profiles...")
results = []
for t in timestamps:
    f = os.path.join(out_dir, f"frame_{t:04d}s.jpg")
    if os.path.exists(f):
        im = Image.open(f)
        # resize to 1x1 or calculate averages
        stat = im.resize((1, 1)).getpixel((0, 0))
        # stat is (r, g, b)
        results.append((t, stat))

for t, (r, g, b) in results:
    # Check if high contrast / ocean / combat (not pure black menus or cutscenes)
    # Sea combat in ACBF usually has nice sky/water (blue/cyan) or sunset/storm
    desc = "Dark/Night/Menu"
    if r > 40 and g > 50 and b > 60:
        desc = "Day Sea / Sailing / Sky"
    elif r > 80 and g > 60 and b > 40:
        desc = "Sun / Town / Combat"
    elif (r + g + b) / 3 > 50:
        desc = "Action / Exterior"
    print(f"{t:04d}s: RGB=({r:3d},{g:3d},{b:3d}) -> {desc}")

