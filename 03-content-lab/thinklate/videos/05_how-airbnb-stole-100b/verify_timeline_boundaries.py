import json
import os

video_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(video_dir, "transcription_timestamps.json")

with open(json_path, "r", encoding="utf-8") as f:
    segs = json.load(f)

scenes = [
    ("Scene 1: Eviction & Airbed Hook", 0, 27),
    ("Scene 2: Cereal Stunt & Debt", 28, 43),
    ("Scene 3: YC & Paul Graham", 44, 61),
    ("Scene 4: Brooklyn Photography", 62, 75),
    ("Scene 5: Craigslist Hack", 76, 94),
    ("Scene 6: COVID Crash & IPO", 95, 111),
    ("Scene 7: Greed Trap & Backlash", 112, 144),
    ("Scene 8: Rules & Outro", 145, 171)
]

for title, s_idx, e_idx in scenes:
    s_time = segs[s_idx]["start"]
    e_time = segs[e_idx]["end"]
    print(f"{title}: {s_time:6.2f}s ({s_time/60:4.1f}m) -> {e_time:6.2f}s ({e_time/60:4.1f}m) | dur: {e_time - s_time:.1f}s")
