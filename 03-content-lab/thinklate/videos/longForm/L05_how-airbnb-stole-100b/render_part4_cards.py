#!/usr/bin/env python3
"""
Render ProRes 4444 MOV Alpha Cards for ThinkLate Video 05 Part 4 (10:15 - 13:27 | 192s)
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
PART4_CARDS_DIR = os.path.join(BASE_DIR, "assets", "part4_cards")
os.makedirs(PART4_CARDS_DIR, exist_ok=True)

CARDS_TO_RENDER = [
    {
        "filename": "card_p4_01_headline_shadow_hotels.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "HOUSING EQUITY AUDIT",
            "category": "CORPORATE HORROR MOVIE",
            "headline": "Wall Street & Predatory Landlords Convert 100,000 Everyday Homes Into Unlicensed Shadow Hotels",
            "excerpt": "Private equity funds bought entire apartment buildings, evicted local families, and weaponized the platform into an extractive hotel cartel.",
            "highlightWords": "Unlicensed Shadow Hotels",
            "dateStr": "SPRING 2022",
            "authorOrRef": "HOUSING MARKET INVESTIGATION"
        }
    },
    {
        "filename": "card_p4_02_receipt_exploding_bill.mov",
        "template": "TornPaperReceipt",
        "props": {
            "channel": "thinklate",
            "receiptTitle": "AIRBNB CHECKOUT EXPLOSION",
            "storeLocation": "APARTMENT BOOKING // 1-NIGHT STAY",
            "dateStr": "SUMMER 2023 // GUEST BILLING DOCKET",
            "lineItems": [
                {"name": "Advertised Nightly Rate", "amount": "$150.00"},
                {"name": "Airbnb Platform Service Fee", "amount": "$70.00"},
                {"name": "Municipal Occupancy Tax", "amount": "$40.00"},
                {"name": "Mandatory Host Cleaning Fee", "amount": "$180.00"}
            ],
            "subtotal": "$150.00",
            "total": "$440.00 CASH",
            "stampText": "+193% CHECKOUT AMBUSH",
            "footerMessage": "BASE PRICE: $150 ✦ ACTUAL CHARGE: $440 ✦ PLUS YOU DO THE LAUNDRY"
        }
    },
    {
        "filename": "card_p4_03_redaction_chore_list.mov",
        "template": "DocumentRedaction",
        "props": {
            "docketNumber": "HOST CONTRACT // CHECKOUT PROTOCOL",
            "classification": "MANDATORY GUEST CHORES",
            "title": "CONFIDENTIAL GUEST CHECKOUT REQUIREMENTS",
            "clausePreamble": "Prior to 10:00 AM departure, guest must strip all linens, wash bed sheets, wipe baseboards, and ",
            "redactedPhrase": "drive all bagged trash four miles away to the local municipal dump",
            "clausePostamble": " or incur an immediate $250 non-compliance penalty.",
            "revealText": "LAMENS-LAMINATED CHORE CONTRACT // ABSENTEE LANDLORD",
            "footerNote": "PAYING LUXURY HOTEL RATES TO PERFORM UNPAID MANUAL LABOR"
        }
    },
    {
        "filename": "card_p4_04_citation_hotels_won.mov",
        "template": "SocialCitation",
        "props": {
            "authorName": "Traveler Revolt",
            "authorHandle": "@airbnb_hostage",
            "avatarText": "TR",
            "avatarColor": "#EF4444",
            "dateStr": "OCTOBER 2023 · VIRAL TIKTOK DISPATCH",
            "content": "Hotels won. Because a hotel never hands you a mop after an 8-hour flight, or charges you a hidden $180 cleaning fee just to sleep in their bed.",
            "highlightWords": "Hotels won because a hotel never hands you a mop",
            "repostsTarget": 48200,
            "likesTarget": 320000,
            "viewsTarget": 14200000,
            "footerNote": "#AIRBNBBOYCOTT // 14.2 MILLION VIEWS"
        }
    },
    {
        "filename": "card_p4_05_redaction_nyc_law18.mov",
        "template": "DocumentRedaction",
        "props": {
            "docketNumber": "NYC INT. NO. 2208-A // LOCAL LAW 18",
            "classification": "STATUTORY REGULATORY INJUNCTION",
            "title": "NYC SHORT-TERM RENTAL REGISTRATION LAW",
            "clausePreamble": "Effective September 5, 2023, all unhosted short-term rentals are declared unlawful, ",
            "redactedPhrase": "wiping out over 80% of Airbnb's active New York City listings overnight",
            "clausePostamble": ", imposing civil penalties up to $5,000 per violation.",
            "revealText": "NYC OFFICE OF SPECIAL ENFORCEMENT DECREE",
            "footerNote": "THE REGULATORY GUILLOTINE // NYC HOUSING CLAMPDOWN"
        }
    },
    {
        "filename": "card_p4_06_comparison_global_bans.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "THE GLOBAL CLAMPDOWN // 2023 - 2028",
            "leftTag": "NEW YORK CITY",
            "leftStat": "80%",
            "leftStatUnit": "wiped out",
            "leftTitle": "LOCAL LAW 18 HAMMER",
            "leftItems": [
                "Unhosted rentals under 30 days banned",
                "Over 80% of NYC listings erased",
                "Fines up to $5,000 per violation"
            ],
            "rightTag": "BARCELONA",
            "rightStat": "100%",
            "rightStatUnit": "ban by 2028",
            "rightTitle": "TOTAL TOURIST BAN",
            "rightItems": [
                "All 10,000 tourist apartments revoked",
                "Strict zero-tolerance housing zoning",
                "Housing returned to local residents"
            ],
            "footerNote": "FROM RENT RELIEF IN 2007 TO MAKING HOUSING UNAFFORDABLE WORLDWIDE"
        }
    },
    {
        "filename": "card_p4_07_barchart_mature_machine.mov",
        "template": "AnimatedBarChart",
        "props": {
            "channel": "thinklate",
            "badgeText": "FINANCIAL SNAPSHOT // 2024 - 2026",
            "title": "THE MATURE CASH MACHINE",
            "subtitle": "Annual Performance Metrics ($ Billions / Millions)",
            "bars": [
                {"label": "Net Profit ($B)", "value": 2.5, "displayValue": "$2.5B", "highlight": False},
                {"label": "Global Supply (M)", "value": 8.0, "displayValue": "8.0M", "highlight": False},
                {"label": "Annual Rev ($B)", "value": 12.0, "displayValue": "$12.0B", "highlight": True}
            ],
            "footerNote": "✦ Hyper-Growth Officially Dead: Expansion Cooled to Low Single Digits"
        }
    },
    {
        "filename": "card_p4_08_comparison_boutique_hotels.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "THE COMEDIC FULL CIRCLE // 18-YEAR IRONY",
            "leftTag": "2007 REBELLION",
            "leftStat": "$80",
            "leftStatUnit": "airbed",
            "leftTitle": "KILL THE HOTEL CARTEL",
            "leftItems": [
                "Sterile lobbies & stiff front desks",
                "Three cheap rubber airbeds on floor",
                "Pure anti-establishment counterculture"
            ],
            "rightTag": "2026 SURVIVAL",
            "rightStat": "#1",
            "rightStatUnit": "growth category",
            "rightTitle": "BECOME THE HOTEL CARTEL",
            "rightItems": [
                "Total price display enforced by decree",
                "Unreasonable chore lists outlawed",
                "Fastest growing category: Boutique Hotels"
            ],
            "footerNote": "✦ THE ULTIMATE PUNCHLINE: AIRBNB'S SURVIVAL DEPENDS ON SELLING HOTEL ROOMS"
        }
    }
]

def render_part4_cards():
    CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW

    print(f"Rendering {len(CARDS_TO_RENDER)} ProRes 4444 MOV Alpha Cards for Part 4...")
    for i, item in enumerate(CARDS_TO_RENDER, 1):
        out_path = os.path.join(PART4_CARDS_DIR, item["filename"])
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000000:
            print(f"[{i:02d}/{len(CARDS_TO_RENDER)}] Already rendered: {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f}MB)")
            continue

        print(f"[{i:02d}/{len(CARDS_TO_RENDER)}] Rendering {item['template']} -> {item['filename']}...")
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
            print(f"  [FAIL] Error rendering {item['filename']}:\n{res.stderr.decode('utf-8', errors='ignore')[:400]}")

if __name__ == "__main__":
    render_part4_cards()

