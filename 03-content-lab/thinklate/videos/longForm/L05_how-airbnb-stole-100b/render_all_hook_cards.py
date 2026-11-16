#!/usr/bin/env python3
"""
Render ProRes 4444 MOV Alpha Cards for ThinkLate Video 05 Hook (00:00 - 01:16)
Strictly compliant with Rule 17 (Headless CREATE_NO_WINDOW) and Rule 23.
"""

import os
import sys
import json
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr.encoding != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
SHARED_TOOLS = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\tools"
RENDER_MOTION = os.path.join(SHARED_TOOLS, "render_motion.py")
HOOK_CARDS_DIR = os.path.join(BASE_DIR, "assets", "hook_cards")
os.makedirs(HOOK_CARDS_DIR, exist_ok=True)

CHESKY_IMG = os.path.join(BASE_DIR, "assets", "documentary_broll", "brian_chesky_archive.jpg")

CARDS_TO_RENDER = [
    {
        "filename": "card_01_evidence_eviction.mov",
        "template": "EvidenceCard",
        "props": {
            "channel": "thinklate",
            "badgeText": "PRIMARY EVIDENCE // EVICTION NOTICE",
            "badgeType": "warning",
            "title": "OCTOBER 2007: 72 HOURS FROM STREET",
            "quote": "Your rent is $1,100. You have three days before your landlord kicks you out and your bank account is empty.",
            "highlightWords": "three days before your landlord kicks you out",
            "sourceDoc": "SAN FRANCISCO HOUSING DOCKET #07-8891",
            "dateStr": "OCTOBER 14, 2007"
        }
    },
    {
        "filename": "card_02_character_founders.mov",
        "template": "CharacterProfileCard",
        "props": {
            "channel": "thinklate",
            "characterName": "BRIAN CHESKY & JOE GEBBIA",
            "designation": "CO-FOUNDERS // BROKE DESIGN SCHOOL GRADUATES",
            "photoUrl": CHESKY_IMG,
            "statusBadge": "SUBJECT DOSSIER // $0 BANK BALANCE",
            "stampTag": "VERIFIED FOUNDERS",
            "stats": [
                {"label": "RENT DUE IN 72H", "value": "$1,100 CASH", "color": "#EF4444"},
                {"label": "BANK BALANCE", "value": "$0.00 EMPTY", "color": "#F59E0B"},
                {"label": "EMPLOYMENT STATUS", "value": "UNEMPLOYED", "color": "#06B6D4"},
                {"label": "SURVIVAL STRATEGY", "value": "INFLATABLE RUG", "color": "#E2FF00"}
            ],
            "quoteSnippet": "Two broke design school graduates sharing an apartment, completely unemployed and scrambling for quick cash."
        }
    },
    {
        "filename": "card_03_typography_scrambling.mov",
        "template": "TypographySlam",
        "props": {
            "channel": "thinklate",
            "line1": "EMPTY LIVING ROOM",
            "line2": "$0 INCOME // 72H TO EVICTION",
            "subtext": "THE EMBARRASSING DESPERATE HUSTLE THAT HIJACKED AN INDUSTRY",
            "line2Color": "#EF4444"
        }
    },
    {
        "filename": "card_04_headline_hotels_sold_out.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "SAN FRANCISCO CHRONICLE",
            "category": "CONVENTION HOUSING BOTTLENECK",
            "headline": "Massive Design Conference Floods City: Every Hotel Room 100% Sold Out",
            "excerpt": "Over 40,000 industrial designers descended upon San Francisco, triggering an artificial supply bottleneck across all commercial lodging.",
            "highlightWords": "100% Sold Out",
            "dateStr": "OCTOBER 2007",
            "authorOrRef": "CITY TOURISM & LODGING RECORDS"
        }
    },
    {
        "filename": "card_05_comparison_hotel_vs_airbed.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "leftTag": "RIGID MONOPOLY",
            "leftStat": "$280",
            "leftStatUnit": "/ night",
            "leftTitle": "SAN FRANCISCO HOTEL CARTEL",
            "leftItems": [
                "Standard room rate during design conference",
                "100% sold-out citywide capacity in 48 hours",
                "Mandatory resort fees + parking overhead"
            ],
            "rightTag": "SYSTEM ARBITRAGE",
            "rightStat": "$80",
            "rightStatUnit": "/ night",
            "rightTitle": "THE $80 AIRBED EXPERIMENT",
            "rightItems": [
                "Inflatable air mattress on living room rug",
                "Free Wi-Fi + homemade breakfast pop-tarts",
                "Zero hotel infrastructure, instant cash flow"
            ],
            "footerNote": "PRICE SPREAD: 71.4% DISCOUNT FOR ATTENDEES  ✦  $240 CASH REVENUE FOR FOUNDERS"
        }
    },
    {
        "filename": "card_06_typography_blueprint.mov",
        "template": "TypographySlam",
        "props": {
            "channel": "thinklate",
            "line1": "3 AIR MATTRESSES ON BARE WOOD",
            "line2": "$100 BILLION EMPIRE",
            "subtext": "THE ASSET-LIGHT PLAYBOOK THAT COMPLETELY BROKE THE HOTEL CARTEL",
            "line2Color": "#E2FF00"
        }
    },
    {
        "filename": "card_07_timeline_moves.mov",
        "template": "TimelineMilestoneFlow",
        "props": {
            "channel": "thinklate",
            "title": "THE 3 TACTICAL SURVIVAL MOVES",
            "currentStep": 1,
            "steps": [
                {"label": "OCT 2007", "title": "AIRBED RUG", "desc": "3 Airbeds on living room rug"},
                {"label": "AUG 2008", "title": "CEREAL HUSTLE", "desc": "$30,000 in election breakfast cereal"},
                {"label": "JAN 2009", "title": "YC CRUCIBLE", "desc": "$20,000 seed round with Paul Graham"},
                {"label": "2010+", "title": "GLOBAL EMPIRE", "desc": "100M+ guests across 220 countries"}
            ]
        }
    },
    {
        "filename": "card_08_receipt_240_cash.mov",
        "template": "TornPaperReceipt",
        "props": {
            "channel": "thinklate",
            "receiptTitle": "FIRST GUEST CHECKOUT RECEIPT",
            "storeLocation": "54 RUSSIAN HILL APARTMENT // LIVING ROOM FLOOR",
            "dateStr": "OCTOBER 19, 2007 // 72-HOUR DEADLINE",
            "lineItems": [
                {"name": "Guest 1 (Living Room Airbed)", "amount": "$80.00 CASH"},
                {"name": "Guest 2 (Living Room Airbed)", "amount": "$80.00 CASH"},
                {"name": "Guest 3 (Living Room Airbed)", "amount": "$80.00 CASH"}
            ],
            "subtotal": "$240.00",
            "total": "$240.00 CASH",
            "stampText": "RENT PAID IN CASH",
            "footerMessage": "OCTOBER RENT: $1,100  ✦  EMERGENCY HUSTLE WORKED"
        }
    }
]

def render_cards():
    CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW

    for i, item in enumerate(CARDS_TO_RENDER, 1):
        out_path = os.path.join(HOOK_CARDS_DIR, item["filename"])
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000000:
            print(f"[{i}/{len(CARDS_TO_RENDER)}] Exists: {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f}MB)")
            continue

        print(f"[{i}/{len(CARDS_TO_RENDER)}] Rendering {item['template']} -> {item['filename']}...")
        cmd = [
            sys.executable, RENDER_MOTION,
            "--template", item["template"],
            "--out", out_path,
            "--props", json.dumps(item["props"])
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
        if res.returncode == 0 and os.path.exists(out_path):
            print(f"  [OK] Success: {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f}MB)")
        else:
            print(f"  [FAIL] Error: {res.stderr.decode('utf-8', errors='ignore')[:300]}")

if __name__ == "__main__":
    render_cards()
