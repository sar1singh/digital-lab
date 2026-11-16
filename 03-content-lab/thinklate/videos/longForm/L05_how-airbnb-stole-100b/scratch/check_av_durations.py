import subprocess, json

parts = [
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Hook_Final_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part2_Master_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part3_Master_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part4_Master_1080p.mp4",
]

for p in parts:
    cmd_v = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "default=noprint_wrappers=1:nokey=1", p]
    dur_v = float(subprocess.check_output(cmd_v).decode().strip())
    cmd_a = ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration", "-of", "default=noprint_wrappers=1:nokey=1", p]
    dur_a = float(subprocess.check_output(cmd_a).decode().strip())
    name = p.split("\\")[-1]
    print(f"{name} -> Video: {dur_v:.3f}s | Audio: {dur_a:.3f}s | Diff: {dur_v - dur_a:.3f}s")

