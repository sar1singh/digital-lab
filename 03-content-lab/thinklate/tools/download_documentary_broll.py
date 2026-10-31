import urllib.request
import re
import os
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

OUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets\documentary_broll"
os.makedirs(OUT_DIR, exist_ok=True)

CATEGORIES = [
    ("car", "broll_01_bmw_car"),
    ("driving", "broll_02_car_driving"),
    ("printer", "broll_03_hp_printer"),
    ("office", "broll_04_office_corp"),
    ("tractor", "broll_05_nebraska_tractor"),
    ("farming", "broll_06_farm_combine"),
    ("hacker", "broll_07_hacker_firmware"),
    ("code", "broll_08_diagnostic_code"),
    ("finance", "broll_09_wall_street_finance"),
    ("server", "broll_10_server_room"),
    ("light-bulb", "broll_11_tungsten_bulb"),
    ("delivery", "broll_12_delivery_rider"),
    ("smartphone", "broll_13_phone_lock"),
]

def get_mp4_for_query(query, out_name):
    target_path = os.path.join(OUT_DIR, f"{out_name}.mp4")
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000000:
        print(f"Already exists: {out_name}.mp4 ({os.path.getsize(target_path)//1024} KB)")
        return target_path

    url = f"https://mixkit.co/free-stock-video/{query}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract video numbers
            video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1-thumb', html)
            if not video_ids:
                # Try finding direct 360/720/1080 mp4s
                video_ids = re.findall(r'assets\.mixkit\.co/videos/(\d+)/\1', html)
            
            unique_ids = list(dict.fromkeys(video_ids))
            print(f"Query '{query}': Found video IDs: {unique_ids[:5]}")
            
            for vid in unique_ids[:3]:
                for res in ["720", "1080", "360"]:
                    mp4_url = f"https://assets.mixkit.co/videos/{vid}/{vid}-{res}.mp4"
                    try:
                        req_v = urllib.request.Request(mp4_url, headers=headers)
                        with urllib.request.urlopen(req_v) as v_resp:
                            data = v_resp.read()
                            if len(data) > 500000:
                                with open(target_path, "wb") as f:
                                    f.write(data)
                                print(f"  --> Downloaded {out_name}.mp4 from {mp4_url} ({len(data)//(1024*1024)} MB)")
                                return target_path
                    except Exception as e:
                        continue
    except Exception as e:
        print(f"Error querying {query}: {e}")
    return None

manifest = {}
for q, name in CATEGORIES:
    p = get_mp4_for_query(q, name)
    if p:
        manifest[name] = p

print(f"\nSuccessfully sourced {len(manifest)} documentary B-roll clips!")
with open(os.path.join(OUT_DIR, "broll_manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2)

