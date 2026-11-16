import json

path = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\transcription_timestamps.json"
with open(path, "r", encoding="utf-8") as f:
    segs = json.load(f)

# Let's inspect where key phrases occur
keywords = [
    ("twenty thousand", "debt"),
    ("cereal", "obama"),
    ("paul graham", "y combinator"),
    ("trough of sorrow", "ramen"),
    ("do things that", "scale"),
    ("brooklyn", "dslr"),
    ("craigslist", "reverse"),
    ("multiple", "valuation"),
    ("march 2020", "covid"),
    ("nasdaq", "ipo"),
    ("cleaning fee", "chore"),
    ("city", "ban"),
    ("rule 1", "survival"),
    ("rule 2", "unfair"),
    ("rule 3", "scaling"),
    ("stay curious", "thinklate")
]

for kw in keywords:
    matches = []
    for i, s in enumerate(segs):
        text = s['text'].lower()
        if any(k in text for k in kw):
            matches.append((i, s['start'], s['end'], s['text']))
    print(f"=== KEYWORD: {kw} (matches: {len(matches)}) ===")
    for m in matches[:2]:
        print(f"  [{m[0]:03d}] {m[1]:6.2f} - {m[2]:6.2f}: {m[3]}")

