import json

with open('digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/transcription_timestamps.json') as f:
    segs = json.load(f)

for s in segs:
    st = s['start']
    et = s['end']
    txt = s['text']
    if 335 <= st <= 370 or 335 <= et <= 370:
        print(f"[{st:.2f}s - {et:.2f}s] {txt}")
