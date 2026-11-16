#!/usr/bin/env python3
"""
Render 3x3 Test & Compare Thumbnail Package for ThinkLate Video 05:
"How An $80 Airbed Stole An Entire Industry"
==================================================================
Strictly compliant with:
- Rule 8 (3x3 A/B/C Test & Compare Matrix)
- Rule 15 (Anti-Dark Mode Blending, Swiss Brutalist Typography)
- packaging-director skill (4-Layer Plot Tableau, 150ms mobile feed test)
"""

import os
import sys
import subprocess
import json
import shutil

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SHARED_TOOLS = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\tools"
RENDER_MOTION = os.path.join(SHARED_TOOLS, "render_motion.py")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

THUMBNAILS = [
    {
        "filename": "thumbnail_variant_a_tactical_weapon.png",
        "title": "Option A (Tactical Heist): How An $80 Airbed Stole An Industry",
        "props": {
            "channel": "thinklate",
            "style": "vox_forensic",
            "headlineTop": "THE $80",
            "headlineBottom": "WEAPON",
            "badgeText": "TACTICAL ARBITRAGE",
            "badgeColor": "#06B6D4",
            "brandLogoType": "dollar",
            "statPins": [
                {"label": "CRAIGSLIST SIPHON", "value": "50M USERS"},
                {"label": "CEREAL HUSTLE", "value": "$30,000"},
                {"label": "HOTEL IMPACT", "value": "-$100B"}
            ],
            "accentStamp": "50M USERS // $0 ADS"
        }
    },
    {
        "filename": "thumbnail_variant_b_consumer_greed_trap.png",
        "title": "Option B (Consumer Greed Trap): The $100B Trap Behind Your Airbnb",
        "props": {
            "channel": "thinklate",
            "style": "magnates_brand",
            "headlineTop": "THE $100B",
            "headlineBottom": "GREED TRAP",
            "badgeText": "CONSUMER EXPOSÉ",
            "badgeColor": "#FF2A4B",
            "brandLogoType": "airbnb",
            "statPins": [
                {"label": "CLEANING FEE", "value": "$300"},
                {"label": "CHORE LIST", "value": "8 TASKS"},
                {"label": "HOTEL SAVINGS", "value": "$0"}
            ],
            "accentStamp": "FRAUD // $100B"
        }
    },
    {
        "filename": "thumbnail_variant_c_regulatory_war.png",
        "title": "Option C (Regulatory War): Why Cities Are Banning Airbnb",
        "props": {
            "channel": "thinklate",
            "style": "vox_forensic",
            "headlineTop": "NOW",
            "headlineBottom": "ILLEGAL",
            "badgeText": "LOCAL LAW 18",
            "badgeColor": "#E11D48",
            "brandLogoType": "hazard",
            "statPins": [
                {"label": "NYC FINES", "value": "$5,000/DAY"},
                {"label": "LISTINGS PURGED", "value": "85%"},
                {"label": "BARCELONA BAN", "value": "100% OUTLAWED"}
            ],
            "accentStamp": "OUTLAWED BY CITIES"
        }
    }
]

def render_all():
    print("=" * 70)
    print("RENDERING 3X3 TEST & COMPARE THUMBNAIL MATRIX (1280X720)")
    print("=" * 70)

    for i, item in enumerate(THUMBNAILS, 1):
        out_path = os.path.join(ASSETS_DIR, item["filename"])
        art_path = os.path.join(ARTIFACT_DIR, item["filename"])
        print(f"\n[{i}/3] Rendering {item['filename']}...")

        cmd = [
            sys.executable, RENDER_MOTION,
            "--template", "ThumbnailStudio",
            "--frame", "15",
            "--out", out_path,
            "--props", json.dumps(item["props"])
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(out_path):
            shutil.copy2(out_path, art_path)
            sz_kb = os.path.getsize(out_path) / 1024
            print(f"  [OK] Success: {item['filename']} ({sz_kb:.1f} KB)")
        else:
            print(f"  [FAIL] Error rendering {item['filename']}:\n{res.stderr[:400]}")

if __name__ == "__main__":
    render_all()

