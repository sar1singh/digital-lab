#!/usr/bin/env python3
"""
Render ProRes 4444 MOV Alpha Cards for ThinkLate Video 05 Part 3 (05:58 - 10:15 | 257s)
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
PART3_CARDS_DIR = os.path.join(BASE_DIR, "assets", "part3_cards")
os.makedirs(PART3_CARDS_DIR, exist_ok=True)

DOC_BROLL = os.path.join(BASE_DIR, "assets", "documentary_broll")
BROOKLYN_IMG = os.path.join(DOC_BROLL, "brooklyn_apartments.jpg")
NASDAQ_IMG = os.path.join(DOC_BROLL, "nasdaq_times_square_billboards.jpg")

CARDS_TO_RENDER = [
    {
        "filename": "card_p3_01_polaroid_camera.mov",
        "template": "PhotoPolaroidPin",
        "props": {
            "channel": "thinklate",
            "photoUrl": BROOKLYN_IMG,
            "exhibitBadge": "UNSCALABLE HUSTLE // BROOKLYN EXHIBIT #101",
            "title": "THE $500 RENTED DSLR HACK",
            "handwrittenNote": "Knocking on user doors in Brooklyn. Drinking tea in kitchens, taking free interior photos.",
            "dateStr": "SUMMER 2009",
            "stampText": "DO THINGS THAT DON'T SCALE",
            "tiltDeg": -2.0
        }
    },
    {
        "filename": "card_p3_02_comparison_photos.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "THE VISUAL PROBLEM // LISTING AUDIT",
            "leftTag": "2008 FLIP PHONE",
            "leftStat": "0.3 MP",
            "leftStatUnit": "blurry",
            "leftTitle": "DARK BASEMENT CRIME SCENE",
            "leftItems": [
                "Dim, grainy lighting from flip phones",
                "Hostage video aesthetic repelled travelers",
                "Zero bookings for 10 consecutive months"
            ],
            "rightTag": "DSLR WIDE-ANGLE",
            "rightStat": "300%",
            "rightStatUnit": "bookings",
            "rightTitle": "BRIGHT STAGED HOSPITALITY",
            "rightItems": [
                "Natural daylight wide-angle photography",
                "Clean staged bedding and living spaces",
                "Immediate visual trust and credibility"
            ],
            "footerNote": "THE DIRTY SECRET: AIRBNB DID NOT HAVE A TECH PROBLEM — IT HAD A PHOTO PROBLEM"
        }
    },
    {
        "filename": "card_p3_03_metric_nyc_spike.mov",
        "template": "MetricCounter",
        "props": {
            "badgeText": "TRACTION VELOCITY // NYC EXPERIMENT",
            "startVal": 0,
            "endVal": 300,
            "prefix": "+",
            "suffix": "%",
            "label": "NYC BOOKING REVENUE SURGE",
            "subtext": "Within 30 days of founder photography, weekly New York revenue doubled, then tripled."
        }
    },
    {
        "filename": "card_p3_04_headline_craigslist.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "CLASSIFIED MONOPOLY AUDIT",
            "category": "AUDACIOUS GROWTH HIJACK",
            "headline": "Craigslist Controls 50 Million Housing Seekers With Zero Public Developer API",
            "excerpt": "With zero capital to buy Google ads or national billboards, Airbnb engineers targeted the largest real estate classified network on the planet.",
            "highlightWords": "50 Million Housing Seekers",
            "dateStr": "SPRING 2010",
            "authorOrRef": "CLASSIFIEDS DATA INTELLIGENCE"
        }
    },
    {
        "filename": "card_p3_05_terminal_bot.mov",
        "template": "TerminalCodeBlock",
        "props": {
            "channel": "thinklate",
            "windowTitle": "airbed_daemon: /opt/growth/craigslist_syndicate.py",
            "commands": [
                "python craigslist_auto_poster.py --bypass-spam --spoof-session",
                "inject_backlink --url 'https://airbnb.com/rooms/8821' --track 'organic_siphon'"
            ],
            "outputLines": [
                {"text": "[SESSION] Craigslist form token extracted via reverse engineering", "tag": "AUTH", "color": "#10B981"},
                {"text": "[BYPASS] Anti-spam filters & IP rate-limiters neutralized", "tag": "BYPASS", "color": "#06B6D4"},
                {"text": "[INJECT] Clean backlink: 'Check availability & book securely on Airbnb'", "tag": "INJECT", "color": "#E2FF00"},
                {"text": "[SYNDICATE] Published live to 50,000,000 monthly apartment hunters", "tag": "SUCCESS", "color": "#10B981"}
            ],
            "statusText": "THE LEGALLY GRAY GROWTH ENGINE // ACTIVE SYNDICATION",
            "executionTime": "12.4ms"
        }
    },
    {
        "filename": "card_p3_06_comparison_siphon.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "DISTRIBUTION ARBITRAGE // $0 AD SPEND",
            "leftTag": "TRADITIONAL AD SPEND",
            "leftStat": "$100,000+",
            "leftStatUnit": "/ month",
            "leftTitle": "GOOGLE ADS & BILLBOARDS",
            "leftItems": [
                "Brutal bidding wars on keywords",
                "Burned precious seed runway in weeks",
                "Zero viral compounding loop"
            ],
            "rightTag": "UNAUTHORIZED BOT",
            "rightStat": "$0.00",
            "rightStatUnit": "spent",
            "rightTitle": "CRAIGSLIST REVERSE-ENGINEERING",
            "rightItems": [
                "Free piggyback on 50M high-intent users",
                "Automated 1-click cross-posting checkbox",
                "Siphoned entire customer base before CL noticed"
            ],
            "footerNote": "UNSTOPPABLE JUGGERNAUT: BY THE TIME CRAIGSLIST PATCHED IT, AIRBNB HAD WON"
        }
    },
    {
        "filename": "card_p3_07_barchart_supply.mov",
        "template": "AnimatedBarChart",
        "props": {
            "channel": "thinklate",
            "badgeText": "GLOBAL SCALE // 2011 - 2019",
            "title": "ROOM SUPPLY: HOTEL CARTEL VS AIRBNB",
            "subtitle": "Global Active Accommodation Inventory (Millions of Rooms)",
            "bars": [
                {"label": "Hyatt Hotels", "value": 0.3, "displayValue": "300K", "highlight": False},
                {"label": "Hilton Worldwide", "value": 1.0, "displayValue": "1.0M", "highlight": False},
                {"label": "Marriott Int.", "value": 1.4, "displayValue": "1.4M", "highlight": False},
                {"label": "Airbnb Platform", "value": 7.0, "displayValue": "7.0M", "highlight": True}
            ],
            "footerNote": "✦ 0 Buildings Owned. 7,000,000 Listings Across 80,000 Cities Worldwide."
        }
    },
    {
        "filename": "card_p3_08_headline_covid.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "GLOBAL CRISIS REPORT",
            "category": "CATASTROPHIC SHOCK",
            "headline": "Global Travel Industry Vanishes: Airbnb Bookings Collapse 80% in 8 Weeks",
            "excerpt": "Over $1 Billion in cash refunds issued from corporate reserves as borders close worldwide and Wall Street analysts declare company dead.",
            "highlightWords": "Collapse 80% in 8 Weeks",
            "dateStr": "MARCH 2020",
            "authorOrRef": "FINANCIAL RESERVES AUDIT"
        }
    },
    {
        "filename": "card_p3_09_redaction_layoffs.mov",
        "template": "DocumentRedaction",
        "props": {
            "docketNumber": "CASE #20-CORP-RESTRUCTURING // MAY 5, 2020",
            "classification": "EXECUTIVE RESTRUCTURING ORDER",
            "title": "CONFIDENTIAL RESTRUCTURING ALL-HANDS MEMO",
            "clausePreamble": "Due to unprecedented global cessation of commercial travel, ",
            "redactedPhrase": "we must lay off 1,900 employees, representing 25% of our global workforce",
            "clausePostamble": ", stripping company operations down to bare metal and cutting all moonshots.",
            "revealText": "BRIAN CHESKY VIDEO ALL-HANDS DEPOSITION",
            "footerNote": "THE MOST PAINFUL DAY IN COMPANY HISTORY // SURVIVAL RESET"
        }
    },
    {
        "filename": "card_p3_10_comparison_staycation.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "THE CRISIS PIVOT // SUMMER 2020",
            "leftTag": "INTERNATIONAL FLIGHTS",
            "leftStat": "0%",
            "leftStatUnit": "travel",
            "leftTitle": "EUROPEAN AIR TRAVEL",
            "leftItems": [
                "Terrified of crowded commercial airplanes",
                "Mandatory 14-day government quarantines",
                "Total collapse of urban business travel"
            ],
            "rightTag": "DRIVE-TO CABINS",
            "rightStat": "RECORD",
            "rightStatUnit": "cash flow",
            "rightTitle": "THE STAYCATION BOOM",
            "rightItems": [
                "2-hour drive into mountains and woods",
                "High-speed Wi-Fi remote-work sanctuaries",
                "Booked for months by remote tech workers"
            ],
            "footerNote": "FROM NEAR-BANKRUPTCY TO RECORD CASH FLOW IN UNDER SIX MONTHS"
        }
    },
    {
        "filename": "card_p3_11_linechart_ipo.mov",
        "template": "AnimatedLineChart",
        "props": {
            "channel": "thinklate",
            "badgeText": "CAPITAL MARKET TRAJECTORY // 2008 - 2020",
            "title": "VALUATION: FROM $80 AIRBED TO $100B NASDAQ IPO",
            "subtitle": "Market Capitalization Trajectory ($ Billions)",
            "points": [
                {"xLabel": "2008", "yValue": 0.0},
                {"xLabel": "2011", "yValue": 1.0},
                {"xLabel": "2015", "yValue": 25.5},
                {"xLabel": "2019", "yValue": 38.0},
                {"xLabel": "Mar 20", "yValue": 18.0},
                {"xLabel": "Dec 20", "yValue": 100.0}
            ],
            "milestoneText": "DECEMBER 10, 2020: $100B IPO",
            "milestoneSubtext": "Stock doubles on day 1. Broke design graduate running the most valuable travel company on Earth.",
            "footerNote": "SOURCE: NASDAQ EXCHANGE COMPOSITE // SEC FORM S-1"
        }
    }
]

def render_part3_cards():
    CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW

    print(f"Rendering {len(CARDS_TO_RENDER)} ProRes 4444 MOV Alpha Cards for Part 3...")
    for i, item in enumerate(CARDS_TO_RENDER, 1):
        out_path = os.path.join(PART3_CARDS_DIR, item["filename"])
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
    render_part3_cards()
