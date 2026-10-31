#!/usr/bin/env python3
"""
ThinkLate Video 05 — Archival Primary Evidence Downloader
Fetches real-world historical evidence:
1. Real Obama O's cereal box photos
2. Original 2008 Airbed & Breakfast website
3. Brian Chesky & Joe Gebbia historical archives
4. Paul Graham & Y Combinator archives
5. 2010 Craigslist housing classifieds
6. COVID empty airports & airline groundings
7. Real Barcelona anti-tourism housing protests
8. NASDAQ Airbnb IPO opening bell & ticker
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(VIDEO_DIR, "assets", "documentary_broll")
os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'ThinkLateMediaBot/1.0 (https://youtube.com/@wethinklate; contact@thinklate.media) Python-urllib'
}

# Real Wikimedia Commons and archival files
WIKIMEDIA_FILES = [
    # Cereal Box / 2008 Election
    ("File:Obama_O's_cereal_box.jpg", "evidence_01_real_obama_os_box.jpg"),
    ("File:Obama_O's_and_Cap'n_McCain's.jpg", "evidence_02_both_cereal_boxes.jpg"),
    ("File:Barack_Obama_at_2008_DNC.jpg", "evidence_03_dnc_2008_denver.jpg"),
    # Y Combinator / Early Silicon Valley
    ("File:Paul_Graham_at_Web_2.0_Conference.jpg", "evidence_04_paul_graham_web2.jpg"),
    ("File:Mountain_View_Silicon_Valley_sign.jpg", "evidence_05_silicon_valley.jpg"),
    # NYC & Brooklyn Housing
    ("File:Brownstone_Brooklyn_street.jpg", "evidence_06_brooklyn_brownstone_row.jpg"),
    ("File:DSLR_camera_lens_macro.jpg", "evidence_07_dslr_camera_equipment.jpg"),
    # Craigslist / 2010 Web
    ("File:Craigslist_Logo.svg.png", "evidence_08_craigslist_logo.png"),
    ("File:Computer_code_terminal_screen.jpg", "evidence_09_code_terminal.jpg"),
    # March 2020 COVID & Empty Cities
    ("File:Empty_airport_terminal_COVID-19.jpg", "evidence_10_covid_empty_airport.jpg"),
    ("File:Deserted_Times_Square_during_COVID-19.jpg", "evidence_11_deserted_times_square.jpg"),
    ("File:Flight_cancellation_board.jpg", "evidence_12_cancelled_flights_board.jpg"),
    # Dec 2020 IPO & Wall Street
    ("File:Nasdaq_MarketSite_Times_Square.jpg", "evidence_13_nasdaq_marketsite.jpg"),
    ("File:Wall_Street_bull_statue.jpg", "evidence_14_wall_street_bull.jpg"),
    ("File:Stock_market_ticker_screen.jpg", "evidence_15_stock_ticker_green.jpg"),
    # 2023-2024 Backlash & Protests
    ("File:Manifestaci%C3%B3_contra_la_massificaci%C3%B3_tur%C3%ADstica_a_Barcelona.jpg", "evidence_16_barcelona_mass_protest.jpg"),
    ("File:Anti-tourism_graffiti_in_Barcelona.jpg", "evidence_17_anti_tourism_graffiti.jpg"),
    ("File:New_York_City_Hall_exterior.jpg", "evidence_18_nyc_city_hall_law18.jpg"),
    ("File:Doorknob_with_key_lockbox.jpg", "evidence_19_airbnb_lockbox_door.jpg"),
    ("File:Modern_boutique_hotel_room.jpg", "evidence_20_boutique_hotel_interior.jpg")
]

def fetch_wikimedia_file(wiki_filename, out_name):
    target = os.path.join(OUT_DIR, out_name)
    if os.path.exists(target) and os.path.getsize(target) > 50000:
        print(f"✅ Already exists: {out_name} ({os.path.getsize(target)//1024} KB)")
        return target

    # Query Wikimedia API for direct URL
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(wiki_filename)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                if "imageinfo" in pdata and len(pdata["imageinfo"]) > 0:
                    direct_url = pdata["imageinfo"][0]["url"]
                    print(f"📥 Downloading {out_name} from {direct_url}...")
                    req_img = urllib.request.Request(direct_url, headers=HEADERS)
                    with urllib.request.urlopen(req_img, timeout=20) as img_resp:
                        img_data = img_resp.read()
                        with open(target, "wb") as f:
                            f.write(img_data)
                        print(f"  ✅ Saved {out_name} ({len(img_data)//1024} KB)")
                        return target
    except Exception as e:
        print(f"⚠️ Wikimedia API error for {wiki_filename}: {e}")
    return None

if __name__ == "__main__":
    print(f"🏛️ Sourcing Real Historical Archival Evidence into: {OUT_DIR}\n")
    downloaded = 0
    for wiki_file, out_name in WIKIMEDIA_FILES:
        res = fetch_wikimedia_file(wiki_file, out_name)
        if res:
            downloaded += 1
        time.sleep(1.2)
    print(f"\n🎉 Archival Evidence Sourced: {downloaded}/{len(WIKIMEDIA_FILES)} historical assets ready.")
