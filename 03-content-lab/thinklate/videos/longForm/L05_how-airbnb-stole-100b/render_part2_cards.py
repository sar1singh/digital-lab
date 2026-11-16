#!/usr/bin/env python3
"""
Render ProRes 4444 MOV Alpha Cards for ThinkLate Video 05 Part 2 (01:16 - 05:36 | 260s)
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
PART2_CARDS_DIR = os.path.join(BASE_DIR, "assets", "part2_cards")
os.makedirs(PART2_CARDS_DIR, exist_ok=True)

DOC_BROLL = os.path.join(BASE_DIR, "assets", "documentary_broll")
NATE_IMG = os.path.join(DOC_BROLL, "nate_blecharczyk_archive.jpg")
PAULG_IMG = os.path.join(DOC_BROLL, "paul_graham_archive.jpg")
CEREAL_IMG = os.path.join(BASE_DIR, "assets", "evidence_cards", "card_02_cereal_arbitrage.png")

CARDS_TO_RENDER = [
    {
        "filename": "card_p2_01_character_nate.mov",
        "template": "CharacterProfileCard",
        "props": {
            "channel": "thinklate",
            "characterName": "NATHAN BLECHARCZYK",
            "designation": "CO-FOUNDER & CTO // SOFTWARE ARCHITECT",
            "photoUrl": NATE_IMG,
            "statusBadge": "SUBJECT DOSSIER // TECHNICAL CO-FOUNDER",
            "stampTag": "VERIFIED FOUNDER",
            "stats": [
                {"label": "BACKGROUND", "value": "HARVARD CS GRAD", "color": "#06B6D4"},
                {"label": "FIRST TASK", "value": "CODE AIRBED MVP", "color": "#E2FF00"},
                {"label": "EQUITY SHARE", "value": "EQUAL 1/3 CO-FOUNDER", "color": "#10B981"},
                {"label": "INITIAL SALARY", "value": "$0.00 RUNWAY", "color": "#EF4444"}
            ],
            "quoteSnippet": "Industrial designers who drew sketches, not programmers. So they called up former roommate Nate Blecharczyk."
        }
    },
    {
        "filename": "card_p2_02_architecture_mvp.mov",
        "template": "RoughSketchChart",
        "props": {
            "channel": "thinklate",
            "title": "ORIGINAL 2008 AIRBED MVP STACK",
            "subtitle": "PHYSICAL HOTEL SOFTWARE OVERHEAD VS NATE'S RAW PHP SCRIPT",
            "leftLabel": "HOTEL IT OVERHEAD (18 LAYERS)",
            "leftAmount": "$50,000+ SOFTWARE STACK",
            "leftHeightPercent": 85,
            "rightLabel": "NATE'S RAW PHP MVP (1 MAP)",
            "rightAmount": "$0 CAPITAL / 3 WEEKS",
            "rightHeightPercent": 40,
            "handwrittenNote": "✦ Built in 3 weeks. 1 Google map. 1 PayPal button. 0 full-time staff."
        }
    },
    {
        "filename": "card_p2_03_headline_vc_pass.mov",
        "template": "ForensicHeadline",
        "props": {
            "channel": "thinklate",
            "publication": "SAND HILL ROAD DISPATCH",
            "category": "VENTURE CAPITAL SEED GATE",
            "headline": "Top Silicon Valley VCs Reject Airbed: 'Dangerous & Unscalable Gimmick'",
            "excerpt": "Renowned venture capitalists walked out of coffee shops or stared at the founders like they were completely insane. Why would anyone pay to sleep on dirty airbeds?",
            "highlightWords": "Dangerous & Unscalable Gimmick",
            "dateStr": "SPRING 2008",
            "authorOrRef": "INVESTOR REJECTION DOSSIER // 100% REJECTION RATE"
        }
    },
    {
        "filename": "card_p2_04_redaction_seed_memo.mov",
        "template": "DocumentRedaction",
        "props": {
            "docketNumber": "CASE #08-VC-ANGELS // SEED ROUND",
            "classification": "DECLASSIFIED VENTURE PASS MEMO",
            "title": "CONFIDENTIAL VC PARTNER PASS MEMO",
            "clausePreamble": "After careful partner review of Airbed & Breakfast, ",
            "redactedPhrase": "we could not see how strangers on airbeds scaled to a venture-scale business",
            "clausePostamble": ", therefore passing on the $150,000 seed investment for 10% equity.",
            "revealText": "FRED WILSON / UNION SQUARE VENTURES ARCHIVES",
            "footerNote": "THE GREATEST MISS IN MODERN VENTURE CAPITAL HISTORY"
        }
    },
    {
        "filename": "card_p2_05_comparison_sxsw.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "SXSW 2008 // EXPECTATIONS VS BRUTAL REALITY",
            "leftTag": "FOUNDER PROJECTIONS",
            "leftStat": "1,000+",
            "leftStatUnit": "bookings",
            "leftTitle": "WHAT FOUNDERS ANTICIPATED",
            "leftItems": [
                "National tech press viral explosion",
                "10,000+ festival attendees looking for lodging",
                "Self-sustaining word-of-mouth growth"
            ],
            "rightTag": "BRUTAL TRACTION",
            "rightStat": "2",
            "rightStatUnit": "bookings",
            "rightTitle": "WHAT ACTUALLY HAPPENED",
            "rightItems": [
                "Booking #1: Unidentified attendee",
                "Booking #2: Brian Chesky himself",
                "Net platform revenue generated: $18.00"
            ],
            "footerNote": "MONTHLY SERVER BILL: $450.00  ✦  ZERO PRODUCT-MARKET FIT"
        }
    },
    {
        "filename": "card_p2_06_ladder_debt.mov",
        "template": "KineticScrollLadder",
        "props": {
            "channel": "thinklate",
            "items": [
                "MAY 2008: $5,000 (Card 1 & 2 Maxed)",
                "JUNE 2008: $12,400 (Card 3 & 4 Maxed)",
                "JULY 2008: $18,200 (Baseball Binder Filled)",
                "AUGUST 2008: $20,000+ (Collection Calls Daily)"
            ],
            "selectedIndex": 3,
            "subtitle": "10 CREDIT CARDS MAXED // $20,000 FOUNDER DEBT"
        }
    },
    {
        "filename": "card_p2_07_polaroid_cereal.mov",
        "template": "PhotoPolaroidPin",
        "props": {
            "channel": "thinklate",
            "photoUrl": CEREAL_IMG,
            "exhibitBadge": "EVIDENCE ARCHIVE // EXHIBIT #104",
            "title": "THE $40 CEREAL ARBITRAGE",
            "handwrittenNote": "1,000 numbered boxes hand-assembled at 2 AM in kitchen to fund server costs.",
            "dateStr": "AUGUST 2008",
            "stampText": "BOOTSTRAP SURVIVAL",
            "tiltDeg": -2.0
        }
    },
    {
        "filename": "card_p2_08_comparison_cereal.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "DENVER DNC 2008 // POLITICAL CEREAL ARBITRAGE",
            "leftTag": "BARACK OBAMA",
            "leftStat": "$40",
            "leftStatUnit": "/ box",
            "leftTitle": "OBAMA O'S: BREAKFAST OF CHANGE",
            "leftItems": [
                "500 numbered collector's edition boxes",
                "100% sold out in 72 hours at Denver DNC",
                "Covered on CNN, MSNBC & national blogs"
            ],
            "rightTag": "JOHN MCCAIN",
            "rightStat": "$40",
            "rightStatUnit": "/ box",
            "rightTitle": "CAP'N MCCAIN'S: MAVERICK IN EVERY BITE",
            "rightItems": [
                "500 numbered collector's edition boxes",
                "Slow seller; founders ate surplus boxes for dinner",
                "Hand-glued with hot glue guns at 2 AM in kitchen"
            ],
            "footerNote": "UNIT ECONOMICS: $4.00 PRODUCTION COST  ✦  $36.00 GROSS MARGIN PER BOX"
        }
    },
    {
        "filename": "card_p2_09_metric_cereal_cash.mov",
        "template": "MetricCounter",
        "props": {
            "badgeText": "DEBT CLEARED // 0% EQUITY DILUTION",
            "startVal": 0,
            "endVal": 38000,
            "prefix": "$",
            "suffix": " CASH",
            "label": "POLITICAL CEREAL REVENUE",
            "subtext": "1,000 custom cereal boxes funded 4 months of runway without surrendering a single share of stock."
        }
    },
    {
        "filename": "card_p2_10_character_paulg.mov",
        "template": "CharacterProfileCard",
        "props": {
            "channel": "thinklate",
            "characterName": "PAUL GRAHAM",
            "designation": "Y COMBINATOR CO-FOUNDER // SEED INVESTOR",
            "photoUrl": PAULG_IMG,
            "statusBadge": "INTERVIEW BOARD // THE COCKROACH TEST",
            "stampTag": "VERIFIED INVESTOR",
            "stats": [
                {"label": "INITIAL VERDICT", "value": "100% FATAL IDEA", "color": "#EF4444"},
                {"label": "ACCELERATOR BATCH", "value": "W09 (WINTER 2009)", "color": "#06B6D4"},
                {"label": "SEED INVESTMENT", "value": "$20,000 FOR 6%", "color": "#E2FF00"},
                {"label": "PRIMARY FEAR", "value": "ROBBERY & LIABILITY", "color": "#F59E0B"}
            ],
            "quoteSnippet": "Graham listened to the pitch and hated it: 'People are going to get murdered, nobody will pay for this.'"
        }
    },
    {
        "filename": "card_p2_11_citation_paulg.mov",
        "template": "SocialCitation",
        "props": {
            "authorName": "Paul Graham",
            "authorHandle": "@paulg",
            "avatarText": "PG",
            "avatarColor": "#F59E0B",
            "dateStr": "JANUARY 2009 · Y COMBINATOR W09",
            "content": "We thought Airbnb was a terrible idea. Who wants to sleep on an airbed in a stranger's apartment? But we funded them because if you can convince people to pay $40 for a $4 box of cereal, you can survive. You guys are cockroaches — you just won't die.",
            "highlightWords": "if you can convince people to pay $40 for a $4 box of cereal, you can survive",
            "repostsTarget": 18400,
            "likesTarget": 94200,
            "viewsTarget": 5100000,
            "footerNote": "THE COCKROACH PRINCIPLE // Y COMBINATOR WINTER 2009"
        }
    },
    {
        "filename": "card_p2_12_comparison_rebrand.mov",
        "template": "ComparisonSplit",
        "props": {
            "channel": "thinklate",
            "badgeText": "MARCH 2009 // PSYCHOLOGICAL PIVOT",
            "leftTag": "SUFFOCATING GIMMICK",
            "leftStat": "AIRBED",
            "leftStatUnit": "& breakfast",
            "leftTitle": "LEGACY IDENTITY (2007 - 2009)",
            "leftItems": [
                "Rubber pool mattress on living room floor",
                "Awkward budget backpacking connotation",
                "Hosts with actual spare bedrooms refused to list"
            ],
            "rightTag": "GLOBAL MARKETPLACE",
            "rightStat": "AIRBNB",
            "rightStatUnit": ".com",
            "rightTitle": "MODERN REBRAND (MARCH 2009)",
            "rightItems": [
                "Purchased 3-letter domain during YC batch",
                "Expanded to private rooms, apartments, villas",
                "Psychological leap to legitimate hospitality"
            ],
            "footerNote": "THE 3-LETTER DOMAIN PURCHASE: EXPANDED TAM FROM $100K TO $100B"
        }
    },
    {
        "filename": "card_p2_13_linechart_flatline.mov",
        "template": "RoughSketchChart",
        "props": {
            "channel": "thinklate",
            "title": "WEEKLY NET REVENUE (JUNE 2009)",
            "subtitle": "Y COMBINATOR COHORT ENDING // ZERO TRACTION",
            "leftLabel": "INVESTOR TARGET (30% WEEKLY)",
            "leftAmount": "$25,000 / WEEK",
            "leftHeightPercent": 80,
            "rightLabel": "ACTUAL REVENUE PULSE",
            "rightAmount": "$200 / WEEK FLATLINE",
            "rightHeightPercent": 25,
            "handwrittenNote": "✦ Flat as a dead man's pulse. 3 founders living in windowless office on ramen."
        }
    },
    {
        "filename": "card_p2_14_typography_nyc.mov",
        "template": "TypographySlam",
        "props": {
            "channel": "thinklate",
            "line1": "\"GO TO YOUR USERS.\"",
            "line2": "DO THINGS THAT DON'T SCALE",
            "subtext": "PAUL GRAHAM'S COMMANDMENT THAT SAVED AIRBNB FROM EXTINCTION",
            "line2Color": "#06B6D4"
        }
    }
]

def render_part2_cards():
    CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW

    print(f"Rendering {len(CARDS_TO_RENDER)} ProRes 4444 MOV Alpha Cards for Part 2...")
    for i, item in enumerate(CARDS_TO_RENDER, 1):
        out_path = os.path.join(PART2_CARDS_DIR, item["filename"])
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
    render_part2_cards()

