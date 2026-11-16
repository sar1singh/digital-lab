#!/usr/bin/env python3
"""
Pop-Culture & Cinema Footage Scout (ThinkLate Content Lab)
==========================================================
Scouts, downloads, and post-processes iconic movie scenes, executive soundbites,
and meme reaction clips for ThinkLate infotainment pacing.
"""

import os
import sys
import json
import subprocess
import argparse

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
POP_CULTURE_DIR = os.path.join(SHARED_DIR, "assets", "pop_culture")

def run_cmd(cmd):
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **kwargs)

def search_candidates(query, limit=3):
    cmd = ["yt-dlp", f"ytsearch{limit}:{query}", "--dump-json", "--flat-playlist"]
    res = run_cmd(cmd)
    results = []
    for line in res.stdout.strip().splitlines():
        if line:
            try:
                data = json.loads(line)
                results.append({
                    "id": data.get("id"),
                    "title": data.get("title"),
                    "duration": data.get("duration"),
                    "url": data.get("url") or f"https://www.youtube.com/watch?v={data.get('id')}"
                })
            except Exception:
                pass
    return results

def main():
    queries = [
        ("Clip 1 (Wolf of Wall Street)", "wolf of wall street chest thump scene"),
        ("Clip 2 (The Big Short)", "they are not confessing they are bragging the big short"),
        ("Clip 3 (Succession)", "logan roy you are not serious people scene"),
        ("Clip 4 (Jensen Huang)", "jensen huang the more you buy the more you save"),
        ("Clip 5 (Pedro Pascal / Oppenheimer)", "pedro pascal laughing crying green screen")
    ]
    for tag, q in queries:
        print(f"=== {tag}: '{q}' ===")
        items = search_candidates(q, limit=3)
        for i, it in enumerate(items):
            print(f"  [{i+1}] {it['title']} ({it['duration']}s)")
            print(f"      URL: {it['url']}")

if __name__ == "__main__":
    main()
