import subprocess
import json

files = [
    ("Rian", r"C:/Users/sar1s/.gemini/antigravity/brain/fa6cc279-b4cc-4a52-9629-aff42dfd0eb7/.user_uploaded/uploaded_media_0_1793373089125.mp3"),
    ("Adam", r"C:/Users/sar1s/.gemini/antigravity/brain/fa6cc279-b4cc-4a52-9629-aff42dfd0eb7/.user_uploaded/uploaded_media_1_1793373089125.mp3")
]

for label, p in files:
    # Get loudness and dynamic range
    cmd = [
        "ffmpeg", "-i", p, "-af", "ebur128=framelog=verbose", "-f", "null", "-"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = res.stderr
    print(f"\n--- {label} Loudness Analysis ---")
    for line in out.splitlines():
        if "I:" in line or "LRA:" in line or "Threshold:" in line:
            print(line.strip())

