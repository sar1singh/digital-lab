import json

path = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\transcription_timestamps.json"
with open(path, "r", encoding="utf-8") as f:
    segs = json.load(f)

print(f"Total segments: {len(segs)}, duration: {segs[-1]['end']:.2f}s")
for i, s in enumerate(segs[:35]):
    print(f"[{i:03d}] {s['start']:6.2f} - {s['end']:6.2f}: {s['text']}")

