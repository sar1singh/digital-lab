import json

path = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\transcription_timestamps.json"
with open(path, "r", encoding="utf-8") as f:
    segs = json.load(f)

for i in range(125, len(segs)):
    s = segs[i]
    print(f"[{i:03d}] {s['start']:6.2f} - {s['end']:6.2f}: {s['text']}")

