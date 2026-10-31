import json
import os

TIMESTAMPS_FILE = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\transcription_timestamps.json"

with open(TIMESTAMPS_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

print(f"Total Whisper segments: {len(segments)}")
total_dur = segments[-1]["end"]
print(f"Total duration: {total_dur}s")

# Let's find segments matching the 39 cue narrative points
targets = [
    ("BMW announcement", "BMW started charging"),
    ("Global rollout", "South Korea, the United Kingdom"),
    ("Furious wires", "Here is what made people furious"),
    ("Bolted in", "Copper, relays, switches"),
    ("Software flag", "Not unless your car keeps billing"),
    ("Hostage seat", "They installed a hostage"),
    ("Who cares", "fair. It is a seat warmer"),
    ("Not a prank", "Except this was not a prank"),
    ("Meet HP", "Meet HP"),
    ("Dynamic security", "Dynamic Security"),
    ("Dead machine", "Owners woke up to a dead machine"),
    ("Audits ink", "You bought a printer that audits your ink"),
    ("Italy fine", "Italy's competition regulator"),
    ("HP CEO quote", "HP's own CEO said the quiet part"),
    ("Investment", "Every time a customer buys a printer"),
    ("Bad investment", "the moment you buy cheaper ink"),
    ("Cold seat insult", "A cold seat is an insult"),
    ("Nebraska farmer", "A hog farmer in Nebraska"),
    ("Dealer laptop", "until a dealer plugged in a laptop"),
    ("Price", "Two hundred thirty dollars to show up"),
    ("Whose tractor", "Whose tractor was it"),
    ("Outlaws / hackers", "Hackers in Eastern Europe"),
    ("Backwards", "Think about how backwards that is"),
    ("License agreement", "John Deere's license agreement"),
    ("Spreadsheet villain", "Wall Street prices every company"),
    ("Sell once", "Sell a tractor once"),
    ("Watch the trick", "Now watch the trick"),
    ("Same tractor", "Same tractor, same factory"),
    ("Recurring", "The accountants give the revenue a new name"),
    ("Multiplier", "Software gets six, seven"),
    ("Scoreboard", "It is a scoreboard that pays executives"),
    ("Geneva 1924", "Winter, 1924, Geneva"),
    ("Lightbulbs too good", "Their light bulbs were too good"),
    ("Phoebus pact", "They called it Phoebus"),
    ("100 years later", "100 years later, nobody needs a secret meeting"),
    ("India delivery rider", "Go to a small town in India"),
    ("Screen dark / padlock", "The screen goes dark"),
    ("Adobe lawsuit", "In June 2024, the government sued Adobe"),
    ("Colorado right to repair", "Colorado, 2023"),
    ("Outro / key", "remember who is holding the key"),
]

for label, phrase in targets:
    found = False
    for s in segments:
        if phrase.lower() in s["text"].lower():
            print(f"[{s['start']:.2f}s - {s['end']:.2f}s] {label}: {s['text'][:50]}...")
            found = True
            break
    if not found:
        print(f"MISSING: {label} ({phrase})")

