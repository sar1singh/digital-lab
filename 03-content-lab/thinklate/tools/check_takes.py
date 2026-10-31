import subprocess, json

files = [
    ("Take1", r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take1.mp3"),
    ("Take2", r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take2.mp3"),
    ("Part2", r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part2.mp3"),
]

for label, f in files:
    cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', f]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    print(f"{label}: duration={data['format']['duration']}s, size={data['format']['size']} bytes")

