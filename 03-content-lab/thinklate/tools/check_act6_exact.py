import json

with open('digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/transcription_timestamps.json') as f:
    segs = json.load(f)

for s in segs:
    st = s['start']
    et = s['end']
    txt = s['text']
    if st >= 330:
        print(f"[{st:06.2f}s - {et:06.2f}s] {txt}")
