import subprocess

# Extract last 10 seconds of Take 1 and Take 2 to check how they end
t1 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take1.mp3"
t2 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take2.mp3"
p2 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part2.mp3"

for name, f, ss, t in [
    ("Take1_end", t1, "185", "11"),
    ("Take2_end", t2, "190", "12"),
    ("Part2_start", p2, "0", "10"),
    ("Part2_end", p2, "189", "11"),
]:
    out_f = f"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/{name}.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-ss", ss, "-t", t, "-i", f, "-c", "copy", out_f
    ], capture_output=True)
    print(f"Created {out_f}")

