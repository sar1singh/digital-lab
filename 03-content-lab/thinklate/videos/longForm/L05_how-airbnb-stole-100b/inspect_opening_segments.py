import json
import os

video_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(video_dir, "transcription_timestamps.json"), "r", encoding="utf-8") as f:
    segs = json.load(f)

for i, s in enumerate(segs[:15]):
    print(f"Seg {i:02d} ({s['start']:5.2f}s - {s['end']:5.2f}s): {s['text']}")
