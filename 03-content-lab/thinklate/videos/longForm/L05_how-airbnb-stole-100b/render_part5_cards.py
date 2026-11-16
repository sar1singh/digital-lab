#!/usr/bin/env python3
"""
Render ProRes 4444 MOV Alpha Cards for ThinkLate Video 05 Part 5 (13:27 - 15:57 | 150s)
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
PART5_CARDS_DIR = os.path.join(BASE_DIR, "assets", "part5_cards")
os.makedirs(PART5_CARDS_DIR, exist_ok=True)

DOC_BROLL = os.path.join(BASE_DIR, "assets", "documentary_broll")
BRIAN_IMG = os.path.join(DOC_BROLL, "brian_chesky_archive.jpg")

CARDS_TO_RENDER = [
    {
        "filename": "card_p5_01_ladder_3laws.mov",
        "template": "KineticScrollLadder",
        "props": {
            "channel": "thinklate",
            "title": "THE 3 BRUTAL LAWS OF SOLO ENTREPRENEURSHIP",
            "items": [
                {"title": "LAW 1: BORROW DISTRIBUTION BEFORE YOU OWN IT", "subtitle": "Hijack congregating high-intent traffic with $0 ad spend"},
                {"title": "LAW 2: THE ANSWER IS IN THE USER'S KITCHEN", "subtitle": "48 hours of manual unscalable legwork beats 6 months of data"},
                {"title": "LAW 3: NEVER OPTIMIZE THE SOUL OUT OF PRODUCT", "subtitle": "The moment you squeeze via spreadsheets, competitors destroy you"}
            ],
            "footerNote": "THE SOLO-BUILDER PLAYBOOK // 18-YEAR WAR LESSONS"
        }
    },
    {
        "filename": "card_p5_02_comparison_distribution.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "LAW 1 // DISTRIBUTION ARBITRAGE",
            "leftTag": "STANDARD AD PLAYBOOK",
            "leftStat": "$50,000",
            "leftStatUnit": "burned",
            "leftTitle": "PAID ADS & WAITING",
            "leftItems": [
                "Bidding wars on saturated Google/FB ads",
                "Passive SEO waiting for algorithm indexing",
                "Runway expires before finding product-market fit"
            ],
            "rightTag": "CONTRARIAN HIJACK",
            "rightStat": "$0.00",
            "rightStatUnit": "spent",
            "rightTitle": "AGGRESSIVE SIPHONING",
            "rightItems": [
                "Find where users are already desperately congregating",
                "Reverse engineer ethical siphoning mechanisms",
                "Acquire first 10,000 customers with zero capital"
            ],
            "footerNote": "✦ BORROW DISTRIBUTION UNTIL YOU ARE BIG ENOUGH TO OWN IT"
        }
    },
    {
        "filename": "card_p5_03_comparison_kitchen.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "LAW 2 // THE KITCHEN DOCTRINE",
            "leftTag": "ACADEMIC DESK TRAP",
            "leftStat": "0%",
            "leftStatUnit": "growth",
            "leftTitle": "STARING AT ANALYTICS",
            "leftItems": [
                "Rewriting backend database algorithms",
                "Endlessly tweaking UI gradients & logos",
                "Guessing customer pain points from a laptop"
            ],
            "rightTag": "MANUAL LEGWORK",
            "rightStat": "300%",
            "rightStatUnit": "surge",
            "rightTitle": "DO THINGS THAT DON'T SCALE",
            "rightItems": [
                "Fly to user city & knock directly on doors",
                "Drink tea in kitchens & watch real behavior",
                "Learn more in 48 hours than 6 months of metrics"
            ],
            "footerNote": "✦ THE ANSWER IS ALWAYS IN YOUR USER'S KITCHEN, NOT YOUR CODE"
        }
    },
    {
        "filename": "card_p5_04_evidence_soul.mov",
        "template": "EvidenceCard",
        "props": {
            "channel": "thinklate",
            "badgeText": "LAW 3 // ANTI-EXTRACTION DIRECTIVE",
            "badgeType": "warning",
            "title": "NEVER OPTIMIZE THE SOUL OUT OF PRODUCT",
            "quote": "The moment your customer feels like they are being squeezed by a spreadsheet instead of served by a human, you create the exact crack your competitors will use to destroy you.",
            "highlightWords": "squeezed by a spreadsheet instead of served by a human",
            "sourceDoc": "CORE BRAND INTEGRITY MANDATE",
            "dateStr": "PERPETUAL PRINCIPLE"
        }
    },
    {
        "filename": "card_p5_05_character_chesky.mov",
        "template": "CharacterProfileCard",
        "props": {
            "channel": "thinklate",
            "characterName": "BRIAN CHESKY",
            "roleTitle": "THE RELENTLESS BUILDER",
            "photoUrl": BRIAN_IMG,
            "badgeText": "ANATOMY OF A $100B SOLO BUILDER",
            "stats": [
                {"label": "Resourcefulness", "value": "Turned $80 airbed into rent cash"},
                {"label": "Stubbornness", "value": "Hand-glued $40 cereal to clear debt"},
                {"label": "Humility", "value": "Knocked on user doors with rented DSLR"}
            ],
            "quote": "He didn't build a $100B empire with a visionary master plan. He built it with unglamorous execution nobody else was willing to do."
        }
    },
    {
        "filename": "card_p5_06_typography_action.mov",
        "template": "TypographySlam",
        "props": {
            "channel": "thinklate",
            "line1": "FIND AN ANNOYING PROBLEM.",
            "line2": "DO THE UNGLAMOROUS WORK.",
            "badgeText": "THE ENTREPRENEUR'S CALL TO ACTION",
            "subtext": "Every massive industry is hiding a broken friction someone is desperately waiting for you to solve."
        }
    },
    {
        "filename": "card_p5_07_headline_outro.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "THINKLATE CONTRARIAN BRIEF",
            "category": "EPISODE 05 // FINAL VERDICT",
            "headline": "From An $80 Airbed On A Living Room Rug To A $100 Billion Travel Empire",
            "excerpt": "What is an everyday annoyance you think someone should turn into a business right now? Tell us in the comments below. Stay curious.",
            "highlightWords": "From An $80 Airbed To A $100 Billion Empire",
            "dateStr": "EPISODE 05 WRAP",
            "authorOrRef": "@WETHINKLATE // DISPATCH"
        }
    }
]

def render_part5_cards():
    CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW

    print(f"Rendering {len(CARDS_TO_RENDER)} ProRes 4444 MOV Alpha Cards for Part 5...")
    for i, item in enumerate(CARDS_TO_RENDER, 1):
        out_path = os.path.join(PART5_CARDS_DIR, item["filename"])
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
    render_part5_cards()

