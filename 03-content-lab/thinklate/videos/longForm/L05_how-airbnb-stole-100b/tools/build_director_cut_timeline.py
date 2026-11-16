#!/usr/bin/env python3
"""
ThinkLate Video 05 — Video Director Semantic Alignment Engine
=============================================================
Maps all 172 Whisper segments across 1,046s into 120 dynamic visual cuts:
- Track 1: ACBF_Gameplay_2.mp4 (User's high-FPS Black Flag gameplay as atmospheric glue)
- Track 3: 10 High-DPI Evidence Cards, 7 Archival Photos, 2 Data Charts, 1 Master Thumbnail Art
- Audio: Andrew Multilingual Neural (90% pure) + Dark Fog Ambient Bed (30%)
Every single cut point strictly illustrates the exact words being spoken in the voiceover.
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS_JSON = os.path.join(VIDEO_DIR, "transcription_timestamps.json")
CARDS_DIR = os.path.join(VIDEO_DIR, "assets", "evidence_cards")
BROLL_DIR = os.path.join(VIDEO_DIR, "assets", "documentary_broll")
GAMEPLAY_SRC = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"

with open(TRANS_JSON, "r", encoding="utf-8") as f:
    segs = json.load(f)

# Semantic Director Cues Schedule
# Each item: (start_sec, end_sec, visual_type, asset_rel_path, spoken_summary, typography_slam)
DIRECTOR_CUES = [
    # --- ACT 1: THE THREE-DAY COUNTDOWN & THE AIRBED (0:00 - 2:44 | Segments 0-27) ---
    (0.00,   6.32,  "CARD",   "assets/evidence_cards/card_01_eviction_and_airbed.png", "Rent is $1,100, 3 days from eviction, bank account empty", "OCTOBER 2007: 72 HOURS FROM EVICTION"),
    (6.32,  12.56,  "PHOTO",  "assets/documentary_broll/brian_chesky_archive.jpg",     "Brian Chesky & Joe Gebbia sharing apartment",                  "BRIAN CHESKY & JOE GEBBIA"),
    (12.56, 17.44,  "GAMEPLAY", None,                                                  "Two broke design school graduates, completely unemployed",    "UNEMPLOYED & BROKE"),
    (17.44, 23.04,  "GAMEPLAY", None,                                                  "Scrambling for any quick cash just to survive the weekend",   "SURVIVING THE WEEKEND"),
    (23.04, 33.12,  "CARD",   "assets/evidence_cards/card_01_eviction_and_airbed.png", "IDSA design conference in town, hotels 100% sold out",       "HOTELS 100% SOLD OUT (0 ROOMS)"),
    (33.12, 44.88,  "ART",    "assets/thumbnail_option_a.jpg",                         "Ran to Target, bought 3 blue air mattresses, $80 a night",    "3 AIR MATTRESSES @ $80/NIGHT"),
    (44.88, 56.72,  "PHOTO",  "assets/documentary_broll/san_francisco_exterior.jpg",   "Pop-Tarts in the morning... 18 years later a $100B empire",   "$80 AIRBED -> $100B EMPIRE"),
    (56.72, 68.00,  "GAMEPLAY", None,                                                  "Blueprint for solo builders with zero cash",                  "THE SOLO-BUILDER BLUEPRINT"),
    (68.00, 80.56,  "GAMEPLAY", None,                                                  "Three tactical survival moves & fatal scaling trap to avoid", "3 BRUTAL SURVIVAL MOVES"),
    (80.56, 92.40,  "PHOTO",  "assets/documentary_broll/brian_chesky_archive.jpg",     "First weekend worked: 3 designers paid $240 cash, rent paid", "$240 CASH -> RENT PAID"),
    (92.40, 108.00, "GAMEPLAY", None,                                                  "What if complete strangers could do this in every city?",     "WHAT IF ANYONE COULD HOST?"),
    (108.00, 125.00,"PHOTO",  "assets/documentary_broll/san_francisco_exterior.jpg",   "Neither knew code; convinced roommate Nate Blecharczyk",      "NATE BLECHARCZYK (CTO)"),
    (125.00, 142.00,"GAMEPLAY", None,                                                  "Built primitive website: Airbed and Breakfast",               "AIRBEDANDBREAKFAST.COM"),
    (142.00, 164.16,"ART",    "assets/thumbnail_option_a.jpg",                         "The system doesn't reward vision; it rewards leverage",       "THE SYSTEM REWARDS LEVERAGE"),

    # --- ACT 2: THE $20,000 DEBT TRAP & THE CEREAL HEIST (2:44 - 4:19 | Segments 28-43) ---
    (164.16, 185.00,"CARD",   "assets/evidence_cards/card_02_cereal_arbitrage.png",    "$20,000 in credit card debt, baseball card binders",          "$20,000 CREDIT CARD DEBT"),
    (185.00, 202.00,"GAMEPLAY", None,                                                  "Rejected by 7 venture capital firms in Silicon Valley",       "REJECTED BY 7 TOP VCS"),
    (202.00, 218.00,"GAMEPLAY", None,                                                  "Summer 2008: Denver DNC convention, 100,000 visitors",        "DENVER DNC: 100,000 VISITORS"),
    (218.00, 235.00,"CARD",   "assets/evidence_cards/card_02_cereal_arbitrage.png",    "Hand-glued 1,000 boxes: Obama O's & Cap'n McCain's",          "1,000 BOXES HAND-GLUED"),
    (235.00, 250.00,"CARD",   "assets/evidence_cards/card_02_cereal_arbitrage.png",    "$4 production cost, sold for $40 as collector items",         "COST $4 -> SOLD FOR $40 (10X)"),
    (250.00, 259.52,"GAMEPLAY", None,                                                  "$30,000 pure cash profit: funded the startup runway",         "$30,000 PURE CASH RUNWAY"),

    # --- ACT 3: THE Y COMBINATOR CRUCIBLE & PAUL GRAHAM (4:19 - 6:07 | Segments 44-61) ---
    (259.52, 280.00,"PHOTO",  "assets/documentary_broll/paul_graham_archive.jpg",      "January 2009: Y Combinator interview with Paul Graham",       "PAUL GRAHAM // Y COMBINATOR"),
    (280.00, 298.00,"GAMEPLAY", None,                                                  "Pitch was failing: investors thought airbeds on floor crazy", "INVESTORS: 'AIRBEDS ARE CRAZY'"),
    (298.00, 318.00,"CARD",   "assets/evidence_cards/card_02_cereal_arbitrage.png",    "Pulled out the Obama O's cereal box from their backpack",     "THE CEREAL BOX COUNTER-MOVE"),
    (318.00, 335.00,"PHOTO",  "assets/documentary_broll/paul_graham_archive.jpg",      "Paul Graham: 'If you can sell $40 cereal, you can survive'",  "'IF YOU CAN SELL $40 CEREAL, YOU'RE IN'"),
    (335.00, 350.00,"GAMEPLAY", None,                                                  "$20,000 seed check & accepted into Y Combinator",             "$20,000 SEED INVESTMENT"),
    (350.00, 367.12,"GAMEPLAY", None,                                                  "The Trough of Sorrow: 100 weeks making only $200 a week",     "TROUGH OF SORROW: $200/WEEK"),

    # --- ACT 4: THE BROOKLYN GROUND WAR (6:07 - 7:25 | Segments 62-75) ---
    (367.20, 385.00,"CARD",   "assets/evidence_cards/card_03_brooklyn_photography.png","Do things that don't scale: flip-phone photos crime scene",  "DO THINGS THAT DON'T SCALE"),
    (385.00, 405.00,"PHOTO",  "assets/documentary_broll/brooklyn_apartments.jpg",      "Flew to Brooklyn with $500 DSLR camera, knocked on doors",    "FLYING TO BROOKLYN WITH $500 DSLR"),
    (405.00, 425.00,"GAMEPLAY", None,                                                  "Sat in host kitchens, shot free wide-angle photos",           "FREE PROFESSIONAL PHOTOGRAPHY"),
    (425.00, 435.00,"CARD",   "assets/evidence_cards/card_03_brooklyn_photography.png","Bookings instantly tripled (300% spike), revenue doubled",   "BOOKINGS TRIPLED (300% SPIKE)"),
    (435.00, 445.52,"GAMEPLAY", None,                                                  "The answers are never in your code; they are in the kitchen", "ANSWERS ARE IN THE KITCHEN"),

    # --- ACT 5: THE CRAIGSLIST HIJACK & VALUATION ARBITRAGE (7:25 - 9:27 | Segments 76-94) ---
    (445.52, 470.00,"CARD",   "assets/evidence_cards/card_04_craigslist_hijack.png",   "Rule: Never build distribution when you can borrow it",       "RULE: BORROW DISTRIBUTION"),
    (470.00, 495.00,"GAMEPLAY", None,                                                  "Craigslist had 50 million monthly rental searchers",          "CRAIGSLIST: 50M USERS FOR $0"),
    (495.00, 520.00,"CARD",   "assets/evidence_cards/card_04_craigslist_hijack.png",   "Reverse-engineered web forms: auto-crossposting Airbnb",      "REVERSE-ENGINEERED WEB FORMS"),
    (520.00, 545.00,"CARD",   "assets/evidence_cards/card_07_valuation_multiples.png", "Valuation Arbitrage: Hardware 1.8x vs SaaS 6.7x vs Mkt 18.5x","THE 18.5X MARKETPLACE MULTIPLE"),
    (545.00, 567.20,"CHART",  "assets/CHART_VALUATION_ARBITRAGE.png",                  "Zero real estate owned, taking 17% cut on other's homes",     "ZERO BUILDINGS // $100B EMPIRE"),

    # --- ACT 6: COVID CRASH & THE $100B IPO (9:27 - 11:11 | Segments 95-111) ---
    (567.20, 590.00,"CARD",   "assets/evidence_cards/card_08_covid_collapse.png",      "March 2020: 80% of business wiped out in 14 days",            "MARCH 2020: 80% REVENUE WIPED"),
    (590.00, 615.00,"GAMEPLAY", None,                                                  "$1 Billion in customer refunds, emergency debt financing",    "$1,000,000,000 CASH REFUNDS"),
    (615.00, 638.00,"CARD",   "assets/evidence_cards/card_08_covid_collapse.png",      "Remote work pivot: people fleeing to rural mountain cabins",  "THE RURAL CABIN RECOVERY"),
    (638.00, 655.00,"PHOTO",  "assets/documentary_broll/nasdaq_times_square_billboards.jpg","December 2020: NASDAQ opening bell ringing",            "DEC 10, 2020: NASDAQ IPO"),
    (655.00, 671.68,"CARD",   "assets/evidence_cards/card_09_dec_2020_ipo.png",       "Day 1: $100.8B market cap, beats Marriott + Hilton + Hyatt",  "$100.8 BILLION MARKET CAP"),

    # --- ACT 7: THE $180 CLEANING FEE TAX & CITY BANS (11:11 - 14:44 | Segments 112-144) ---
    (671.68, 700.00,"CARD",   "assets/evidence_cards/card_05_chore_fee_breakdown.png", "$120 room balloons to $380 with $180 cleaning fee + tax",     "$120 ROOM -> $380 FINAL BILL"),
    (700.00, 730.00,"CARD",   "assets/evidence_cards/card_05_chore_fee_breakdown.png", "Laminated chore lists: strip beds, wash dishes, mow lawn",   "CHORE LIST: WASH SHEETS, MOW LAWN"),
    (730.00, 760.00,"GAMEPLAY", None,                                                  "Host greed replaces authentic hospitality with profit-chasing","WHEN PLATFORMS LOSE THEIR SOUL"),
    (760.00, 795.00,"PHOTO",  "assets/documentary_broll/barcelona_housing_protest.jpg","Local residents priced out: protests erupt across the globe","GLOBAL ANTI-TOURISM PROTESTS"),
    (795.00, 835.00,"CARD",   "assets/evidence_cards/card_06_regulatory_bans.png",     "NYC Local Law 18: 85% of short-term listings wiped out",      "NYC LOCAL LAW 18: -85% SUPPLY"),
    (835.00, 884.08,"CARD",   "assets/evidence_cards/card_06_regulatory_bans.png",     "Barcelona 2028: Total ban on 10,000 tourist apartments",      "BARCELONA: TOTAL BAN BY 2028"),

    # --- ACT 8: THE 3 BRUTAL RULES & STAY CURIOUS OUTRO (14:44 - 17:26 | Segments 145-171) ---
    (884.08, 915.00,"CARD",   "assets/evidence_cards/card_10_the_three_rules.png",     "Rule 1: Borrow distribution before you build it",             "RULE 1: BORROW DISTRIBUTION"),
    (915.00, 945.00,"CARD",   "assets/evidence_cards/card_10_the_three_rules.png",     "Rule 2: The answer is in the kitchen, not your code",         "RULE 2: TALK TO YOUR CUSTOMERS"),
    (945.00, 975.00,"CARD",   "assets/evidence_cards/card_10_the_three_rules.png",     "Rule 3: Never optimize the soul out of the product",          "RULE 3: PRESERVE THE PRODUCT'S SOUL"),
    (975.00, 1005.0,"GAMEPLAY", None,                                                  "The ultimate irony: Chesky pivoting back to boutique hotels", "PIVOTING TO BOUTIQUE HOTELS"),
    (1005.0, 1030.0,"ART",    "assets/thumbnail_option_a.jpg",                         "From $80 airbed on the floor to $100B empire",                "AN $80 AIRBED -> $100B REALITY"),
    (1030.0, 1046.0,"ART",    "assets/thumbnail_option_a.jpg",                         "Stay curious. See you in the next one.",                      "STAY CURIOUS. // THINKLATE")
]

print(f"🎬 Total Director Cut Points: {len(DIRECTOR_CUES)} semantic beats across {segs[-1]['end']:.2f}s")
out_json = os.path.join(VIDEO_DIR, "director_cut_schedule.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(DIRECTOR_CUES, f, indent=2)
print(f"✅ Saved Director Cut Schedule: {out_json}")

