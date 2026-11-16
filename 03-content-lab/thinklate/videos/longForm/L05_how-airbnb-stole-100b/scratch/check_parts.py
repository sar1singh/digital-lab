import subprocess, json, os

parts = [
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Hook_Final_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part2_Master_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part3_Master_1080p.mp4",
    r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\ThinkLate_Video05_Part4_Master_1080p.mp4",
]

total_dur = 0
for p in parts:
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", p]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    fmt = data.get("format", {})
    dur = float(fmt.get("duration", 0))
    total_dur += dur
    v_stream = next((s for s in data["streams"] if s["codec_type"] == "video"), {})
    a_stream = next((s for s in data["streams"] if s["codec_type"] == "audio"), {})
    name = os.path.basename(p)
    fps = v_stream.get("r_frame_rate")
    print(f"{name}: {dur:.2f}s | Video: {v_stream.get('codec_name')} {v_stream.get('width')}x{v_stream.get('height')} @ {fps} | Audio: {a_stream.get('codec_name')} {a_stream.get('sample_rate')}Hz")

print(f"Total Parts 1-4 Duration: {total_dur:.2f}s ({total_dur/60:.2f} min)")

