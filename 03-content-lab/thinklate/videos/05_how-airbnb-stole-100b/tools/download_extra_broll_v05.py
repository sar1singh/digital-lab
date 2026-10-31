#!/usr/bin/env python3
"""
ThinkLate Video 05 — Additional Documentary Stock B-Roll Downloader (Track 1 Expansion)
Downloads 16 additional 1080p/720p stock video clips to give every scene 4 distinct B-roll cuts.
"""

import os
import sys
import re
import urllib.request

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(VIDEO_DIR, "assets", "documentary_broll")
os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

ADDITIONAL_SHOTS = [
    ("clock", "scene1_03_clock_ticking"),
    ("boxes", "scene1_04_moving_boxes"),
    ("printing", "scene2_03_printing_press"),
    ("cash", "scene2_04_dollar_bills"),
    ("contract", "scene3_03_business_contract"),
    ("whiteboard", "scene3_04_whiteboard_strategy"),
    ("photography", "scene4_03_photo_studio"),
    ("door", "scene4_04_doorway_entry"),
    ("server", "scene5_03_server_datacenter"),
    ("internet", "scene5_04_web_browsing"),
    ("airplane", "scene6_03_airplane_tarmac"),
    ("trading", "scene6_04_financial_trading"),
    ("vacuum", "scene7_03_cleaning_chores"),
    ("city-hall", "scene7_04_city_protest_street"),
    ("stage", "scene8_03_conference_keynote"),
    ("passport", "scene8_04_travel_passport")
]

def download_clip(query, out_name):
    target_path = os.path.join(OUT_DIR, f"{out_name}.mp4")
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000000:
        print(f"✅ Already exists: {out_name}.mp4 ({os.path.getsize(target_path)//1024} KB)")
        return target_path

    url = f"https://mixkit.co/free-stock-video/{query}/"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1', html)
            if not video_ids:
                video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1-thumb', html)
            
            unique_ids = list(dict.fromkeys(video_ids))
            
            for vid in unique_ids[:3]:
                for res in ["720", "1080", "360"]:
                    mp4_url = f"https://assets.mixkit.co/videos/{vid}/{vid}-{res}.mp4"
                    try:
                        req_v = urllib.request.Request(mp4_url, headers=HEADERS)
                        with urllib.request.urlopen(req_v, timeout=15) as v_resp:
                            data = v_resp.read()
                            if len(data) > 500000:
                                with open(target_path, "wb") as f:
                                    f.write(data)
                                print(f"  📥 Saved: {out_name}.mp4 ({len(data)//(1024*1024)} MB) [{res}p]")
                                return target_path
                    except Exception:
                        continue
    except Exception as e:
        print(f"❌ Error fetching {query}: {e}")
    return None

if __name__ == "__main__":
    print(f"🚀 Downloading 16 Additional B-Roll Clips into: {OUT_DIR}\n")
    downloaded = 0
    for query, name in ADDITIONAL_SHOTS:
        res = download_clip(query, name)
        if res:
            downloaded += 1
    print(f"\n🎉 Additional B-Roll Finished: {downloaded}/{len(ADDITIONAL_SHOTS)} clips.")
