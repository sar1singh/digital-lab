#!/usr/bin/env python3
"""
ThinkLate Video 05 — Documentary Stock B-Roll Downloader (Track 1)
Downloads 100% free, high-definition stock video clips for all 8 narrative scenes.
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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(VIDEO_DIR, "assets", "documentary_broll")
os.makedirs(OUT_DIR, exist_ok=True)

SHOTS = [
    ("city", "scene1_01_city_apartments"),
    ("keys", "scene1_02_apartment_keys"),
    ("credit-card", "scene2_01_credit_card_debt"),
    ("crowd", "scene2_02_convention_crowd"),
    ("business-meeting", "scene3_01_venture_meeting"),
    ("handshake", "scene3_02_partnership_deal"),
    ("camera", "scene4_01_dslr_camera"),
    ("apartment", "scene4_02_bright_interior"),
    ("coding", "scene5_01_python_coding"),
    ("typing", "scene5_02_laptop_terminal"),
    ("airport", "scene6_01_empty_airport"),
    ("stock-market", "scene6_02_wall_street_ticker"),
    ("cleaning", "scene7_01_house_chores"),
    ("protest", "scene7_02_city_protest"),
    ("hotel", "scene8_01_boutique_hotel"),
    ("travel", "scene8_02_luggage_journey")
]

def download_clip(query, out_name):
    target_path = os.path.join(OUT_DIR, f"{out_name}.mp4")
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000000:
        print(f"✅ Already exists: {out_name}.mp4 ({os.path.getsize(target_path)//1024} KB)")
        return target_path

    url = f"https://mixkit.co/free-stock-video/{query}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1', html)
            if not video_ids:
                video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1-thumb', html)
            
            unique_ids = list(dict.fromkeys(video_ids))
            print(f"🔍 Query '{query}': Found {len(unique_ids)} candidates")
            
            for vid in unique_ids[:3]:
                for res in ["720", "1080", "360"]:
                    mp4_url = f"https://assets.mixkit.co/videos/{vid}/{vid}-{res}.mp4"
                    try:
                        req_v = urllib.request.Request(mp4_url, headers=headers)
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
    print(f"🚀 Downloading Documentary B-Roll into: {OUT_DIR}\n")
    downloaded = 0
    for query, name in SHOTS:
        res = download_clip(query, name)
        if res:
            downloaded += 1
    print(f"\n🎉 Finished downloading {downloaded}/{len(SHOTS)} stock video clips.")
