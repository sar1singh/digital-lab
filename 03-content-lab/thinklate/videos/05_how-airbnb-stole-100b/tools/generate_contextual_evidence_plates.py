#!/usr/bin/env python3
"""
Generate High-DPI Contextual Evidence Plates for ThinkLate Video 05
Every plate strictly illustrates the exact spoken dialogue in the script.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(VIDEO_DIR, "assets", "evidence_cards")
os.makedirs(OUT_DIR, exist_ok=True)

# Colors
BG_COLOR = (8, 12, 20)          # Slate Navy #080C14
CARD_BG = (15, 22, 38)          # Card background #0F1626
BORDER_COLOR = (30, 41, 59)     # Slate border
WHITE = (248, 250, 252)         # Chalk White
LIME = (226, 255, 0)            # Electric Acid Lime #E2FF00
RED = (239, 68, 68)             # Crimson Red #EF4444
AMBER = (245, 158, 11)          # Warm Amber #F59E0B
MUTED = (148, 163, 184)         # Slate text

def get_font(size):
    # Try system fonts
    font_names = ["arialbd.ttf", "segoeuib.ttf", "calibrib.ttf", "arial.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_header(draw, title, category="PRIMARY EVIDENCE // PRIMARY SOURCE"):
    draw.text((80, 70), category, font=get_font(24), fill=AMBER)
    draw.text((80, 110), title, font=get_font(44), fill=WHITE)
    draw.line([(80, 175), (1840, 175)], fill=BORDER_COLOR, width=2)

def create_card_01_eviction():
    # Card 01: 72 Hours from Eviction Notice
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "OCTOBER 2007: THE THREE-DAY COUNTDOWN", "SAN FRANCISCO // HOUSING CRISIS")

    # Left Box: Eviction Notice
    draw.rounded_rectangle([(120, 240), (900, 940)], radius=20, fill=CARD_BG, outline=RED, width=3)
    draw.rectangle([(120, 240), (900, 310)], fill=(60, 15, 15))
    draw.text((160, 260), "⚠️  FINAL NOTICE TO VACATE", font=get_font(32), fill=RED)
    
    draw.text((160, 350), "PROPERTY:", font=get_font(24), fill=MUTED)
    draw.text((160, 385), "Rausch Street Apartment, San Francisco", font=get_font(30), fill=WHITE)

    draw.text((160, 450), "STATUS:", font=get_font(24), fill=MUTED)
    draw.text((160, 485), "72 HOURS BEFORE POLICE LOCKOUT", font=get_font(30), fill=RED)

    draw.text((160, 560), "OVERDUE RENT AMOUNT:", font=get_font(24), fill=MUTED)
    draw.text((160, 600), "$1,150.00", font=get_font(72), fill=WHITE)

    draw.text((160, 720), "TENANTS:", font=get_font(24), fill=MUTED)
    draw.text((160, 755), "Brian Chesky & Joe Gebbia (Unemployed)", font=get_font(28), fill=WHITE)
    draw.text((160, 820), "BANK ACCOUNT BALANCE: $0.00", font=get_font(32), fill=RED)

    # Right Box: The Design Conference Solution
    draw.rounded_rectangle([(1020, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=LIME, width=3)
    draw.rectangle([(1020, 240), (1800, 310)], fill=(20, 40, 15))
    draw.text((1060, 260), "⚡ THE ACCIDENTAL OPENING", font=get_font(32), fill=LIME)

    draw.text((1060, 350), "OCTOBER 2007 EVENT:", font=get_font(24), fill=MUTED)
    draw.text((1060, 385), "IDSA International Design Conference", font=get_font(32), fill=WHITE)

    draw.text((1060, 460), "SAN FRANCISCO HOTELS:", font=get_font(24), fill=MUTED)
    draw.text((1060, 500), "100% SOLD OUT (0 ROOMS)", font=get_font(42), fill=RED)

    draw.text((1060, 580), "THE MAKESHIFT OFFER:", font=get_font(24), fill=MUTED)
    draw.text((1060, 620), "3 Blue Air Mattresses on Floor", font=get_font(36), fill=LIME)
    draw.text((1060, 680), "+ Homemade Pop-Tarts Breakfast", font=get_font(28), fill=WHITE)

    draw.text((1060, 760), "PRICE PER NIGHT:", font=get_font(24), fill=MUTED)
    draw.text((1060, 800), "$80 / NIGHT", font=get_font(64), fill=LIME)
    draw.text((1060, 880), "WEEKEND CASH: $240 -> RENT SAVED", font=get_font(28), fill=WHITE)

    out_path = os.path.join(OUT_DIR, "card_01_eviction_and_airbed.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

def create_card_02_cereal_arbitrage():
    # Card 02: Cereal Stunt Unit Economics
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "SUMMER 2008: THE NOVELTY CEREAL ARBITRAGE", "UNIT ECONOMICS // DEBT SURVIVAL")

    # Left: Credit Card Debt Trap
    draw.rounded_rectangle([(120, 240), (900, 940)], radius=20, fill=CARD_BG, outline=RED, width=3)
    draw.text((160, 280), "THE DEBT CRUCIBLE", font=get_font(32), fill=RED)
    draw.text((160, 350), "MAXED CREDIT CARDS:", font=get_font(24), fill=MUTED)
    draw.text((160, 390), "Kept in Baseball Card Binders", font=get_font(30), fill=WHITE)

    draw.text((160, 470), "TOTAL UNSECURED DEBT:", font=get_font(24), fill=MUTED)
    draw.text((160, 510), "$20,000+", font=get_font(72), fill=RED)

    draw.text((160, 630), "VENTURE CAPITAL STATUS:", font=get_font(24), fill=MUTED)
    draw.text((160, 670), "Rejected by 7 Top VC Firms", font=get_font(32), fill=WHITE)
    draw.text((160, 730), "Zero Investors Believed in Airbeds", font=get_font(26), fill=MUTED)

    # Right: Obama O's Math
    draw.rounded_rectangle([(1020, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=LIME, width=3)
    draw.text((1060, 280), "THE POLITICAL CEREAL HUSTLE", font=get_font(32), fill=LIME)

    draw.text((1060, 350), "2008 DNC DENVER EVENT:", font=get_font(24), fill=MUTED)
    draw.text((1060, 390), "100,000 Visitors & Zero Rooms", font=get_font(30), fill=WHITE)

    draw.text((1060, 470), "BOXES HAND-GLUED IN KITCHEN:", font=get_font(24), fill=MUTED)
    draw.text((1060, 510), "1,000 Boxes (Obama O's & McCain's)", font=get_font(32), fill=WHITE)

    draw.text((1060, 590), "UNIT PRODUCTION COST:", font=get_font(24), fill=MUTED)
    draw.text((1060, 625), "$4.00 / box (Cheerios + Cardboard)", font=get_font(28), fill=MUTED)

    draw.text((1060, 680), "COLLECTOR SALE PRICE:", font=get_font(24), fill=MUTED)
    draw.text((1060, 715), "$40.00 / box (10x Margin)", font=get_font(42), fill=LIME)

    draw.text((1060, 800), "NET CASH RUNWAY RAISED:", font=get_font(24), fill=MUTED)
    draw.text((1060, 840), "$30,000 COLD CASH", font=get_font(60), fill=LIME)

    out_path = os.path.join(OUT_DIR, "card_02_cereal_arbitrage.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

def create_card_03_brooklyn_photos():
    # Card 03: Do Things That Don't Scale (Brooklyn DSLR)
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "SPRING 2009: DO THINGS THAT DON'T SCALE", "THE BROOKLYN GROUND WAR // PAUL GRAHAM RULE")

    draw.rounded_rectangle([(120, 240), (900, 940)], radius=20, fill=CARD_BG, outline=RED, width=2)
    draw.text((160, 280), "THE FLIP-PHONE BLUNDER", font=get_font(32), fill=RED)
    draw.text((160, 360), "Host Photos: 2009 Flip-Phones", font=get_font(28), fill=MUTED)
    draw.text((160, 410), "Dark, blurry, uninviting living rooms", font=get_font(26), fill=WHITE)
    draw.text((160, 480), "Looked like basement crime scenes", font=get_font(26), fill=MUTED)
    draw.text((160, 580), "WEEKLY REVENUE:", font=get_font(24), fill=MUTED)
    draw.text((160, 620), "$200 / WEEK", font=get_font(64), fill=RED)
    draw.text((160, 720), "Flatlined in the 'Trough of Sorrow'", font=get_font(28), fill=MUTED)

    draw.rounded_rectangle([(1020, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=LIME, width=3)
    draw.text((1060, 280), "THE HANDS-ON INTERVENTION", font=get_font(32), fill=LIME)
    draw.text((1060, 360), "Tactic: Flew to Brooklyn with $500 DSLR", font=get_font(28), fill=WHITE)
    draw.text((1060, 410), "Knocked on doors & shot free professional photos", font=get_font(26), fill=MUTED)
    draw.text((1060, 480), "Sat in hosts' kitchens & discovered bugs", font=get_font(26), fill=WHITE)
    draw.text((1060, 580), "THE EMPIRICAL RESULT:", font=get_font(24), fill=MUTED)
    draw.text((1060, 620), "BOOKINGS TRIPLED (3X)", font=get_font(60), fill=LIME)
    draw.text((1060, 720), "Revenue Doubled Instantly to $400/wk", font=get_font(32), fill=WHITE)
    draw.text((1060, 800), "Taught Silicon Valley: 'Do Things That Don't Scale'", font=get_font(26), fill=AMBER)

    out_path = os.path.join(OUT_DIR, "card_03_brooklyn_photography.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

def create_card_04_craigslist_hack():
    # Card 04: The Craigslist Hijack
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "2010: THE CRAIGSLIST DISTRIBUTION HIJACK", "BORROWING DISTRIBUTION // ZERO CUSTOMER ACQUISITION COST")

    draw.rounded_rectangle([(120, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=LIME, width=2)
    draw.text((160, 280), "THE GROWTH MECHANISM:", font=get_font(28), fill=AMBER)
    draw.text((160, 320), "Reverse-Engineering Craigslist Rental Classifieds", font=get_font(42), fill=WHITE)

    # 3-step pipeline
    boxes = [
        ("1. HOST CREATES LISTING", "Host uploads apartment photos & price on Airbnb website", WHITE),
        ("2. AUTOMATED SCRIPT INJECTION", "Python bot fills out Craigslist forms & bypasses captcha", LIME),
        ("3. 50M USERS HIJACKED FOR $0", "Craigslist searchers click link back to Airbnb platform", LIME)
    ]
    for idx, (b_title, b_desc, col) in enumerate(boxes):
        y = 430 + (idx * 150)
        draw.rounded_rectangle([(160, y), (1760, y + 120)], radius=12, fill=(20, 28, 48), outline=BORDER_COLOR, width=2)
        draw.text((200, y + 25), b_title, font=get_font(30), fill=col)
        draw.text((200, y + 70), b_desc, font=get_font(24), fill=MUTED)

    draw.text((160, 890), "MARKET TAKEAWAY: Never build distribution from scratch when you can borrow an existing giant's.", font=get_font(26), fill=AMBER)

    out_path = os.path.join(OUT_DIR, "card_04_craigslist_hijack.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

def create_card_05_chore_fee():
    # Card 05: The $180 Cleaning Fee & Chore List Tax
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "2023–2024: THE $180 CLEANING FEE TAX", "THE CORPORATE GREED TRAP // CONSUMER BACKLASH")

    # Left: The Bill Shock
    draw.rounded_rectangle([(120, 240), (950, 940)], radius=20, fill=CARD_BG, outline=RED, width=3)
    draw.text((160, 280), "THE INVOICE EXPLOSION", font=get_font(32), fill=RED)
    
    draw.text((160, 360), "ADVERTISED NIGHTLY ROOM:", font=get_font(24), fill=MUTED)
    draw.text((700, 360), "$120.00", font=get_font(30), fill=WHITE)

    draw.text((160, 420), "MANDATORY CLEANING FEE:", font=get_font(24), fill=MUTED)
    draw.text((700, 420), "$180.00", font=get_font(32), fill=RED)

    draw.text((160, 480), "AIRBNB SERVICE FEE (14%):", font=get_font(24), fill=MUTED)
    draw.text((700, 480), "$42.00", font=get_font(30), fill=WHITE)

    draw.text((160, 540), "LOCAL OCCUPANCY TAXES:", font=get_font(24), fill=MUTED)
    draw.text((700, 540), "$38.00", font=get_font(30), fill=WHITE)
    draw.line([(160, 600), (910, 600)], fill=BORDER_COLOR, width=2)

    draw.text((160, 630), "TOTAL FINAL CHARGE:", font=get_font(28), fill=WHITE)
    draw.text((630, 630), "$380.00", font=get_font(44), fill=RED)
    draw.text((160, 710), "Price Inflation: 3.16x advertised rate!", font=get_font(26), fill=AMBER)

    # Right: Host Chore List
    draw.rounded_rectangle([(1030, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=AMBER, width=2)
    draw.text((1070, 280), "LAMINATED HOST CHORE LIST", font=get_font(32), fill=AMBER)
    draw.text((1070, 330), "Required Guest Tasks Before Checkout (10:00 AM):", font=get_font(24), fill=MUTED)

    chores = [
        "1. Strip all bed linens & start laundry cycle",
        "2. Wash, dry, and put away all kitchen dishes",
        "3. Take all trash & recycling to alley bins (100m away)",
        "4. Sweep front patio & turn off thermostat",
        "5. $75 Fine per uncompleted chore item"
    ]
    for idx, c in enumerate(chores):
        y = 390 + (idx * 85)
        draw.rounded_rectangle([(1070, y), (1760, y + 65)], radius=8, fill=(25, 20, 15), outline=(60, 40, 20), width=1)
        draw.text((1100, y + 18), c, font=get_font(24), fill=WHITE if idx < 4 else RED)

    draw.text((1070, 840), "THE CONSUMER REVOLT: 'Why am I paying $180 cleaning to do manual labor?'", font=get_font(22), fill=MUTED)

    out_path = os.path.join(OUT_DIR, "card_05_chore_fee_breakdown.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

def create_card_06_city_bans():
    # Card 06: NYC Local Law 18 & Barcelona 2028 Ban
    im = Image.new("RGB", (1920, 1080), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_header(draw, "2023–2028: THE REGULATORY BACKLASH", "CITIES STRIKE BACK // HOUSING CRISIS RETALIATION")

    # Left: NYC Local Law 18
    draw.rounded_rectangle([(120, 240), (950, 940)], radius=20, fill=CARD_BG, outline=RED, width=3)
    draw.text((160, 280), "NEW YORK CITY (LOCAL LAW 18)", font=get_font(32), fill=RED)
    draw.text((160, 350), "ACTIVE LISTINGS (AUG 2023):", font=get_font(24), fill=MUTED)
    draw.text((160, 390), "22,000 SHORT-TERM UNITS", font=get_font(36), fill=WHITE)

    draw.text((160, 470), "ACTIVE LISTINGS (JAN 2024):", font=get_font(24), fill=MUTED)
    draw.text((160, 510), "3,000 REGISTERED UNITS", font=get_font(36), fill=RED)

    draw.text((160, 600), "TOTAL SUPPLY WIPED OUT:", font=get_font(24), fill=MUTED)
    draw.text((160, 640), "-85% ELIMINATED", font=get_font(64), fill=RED)
    draw.text((160, 750), "Rule: Host must live on site, max 2 guests", font=get_font(26), fill=MUTED)

    # Right: Barcelona Total Ban
    draw.rounded_rectangle([(1030, 240), (1800, 940)], radius=20, fill=CARD_BG, outline=RED, width=3)
    draw.text((1070, 280), "BARCELONA: THE 2028 TOTAL BAN", font=get_font(32), fill=RED)
    draw.text((1070, 350), "CURRENT TOURIST APARTMENTS:", font=get_font(24), fill=MUTED)
    draw.text((1070, 390), "10,101 LICENSED UNITS", font=get_font(36), fill=WHITE)

    draw.text((1070, 470), "NOVEMBER 2028 MANDATE:", font=get_font(24), fill=MUTED)
    draw.text((1070, 510), "100% LICENSES REVOKED", font=get_font(44), fill=RED)

    draw.text((1070, 600), "LOCAL RENT INFLATION (10 YRS):", font=get_font(24), fill=MUTED)
    draw.text((1070, 640), "+68% SURGE IN RENTS", font=get_font(52), fill=AMBER)
    draw.text((1070, 750), "Mayor Jaume Collboni: 'Homes are for residents, not tourists.'", font=get_font(24), fill=WHITE)

    out_path = os.path.join(OUT_DIR, "card_06_regulatory_bans.png")
    im.save(out_path)
    print(f"✅ Generated: {out_path}")

if __name__ == "__main__":
    create_card_01_eviction()
    create_card_02_cereal_arbitrage()
    create_card_03_brooklyn_photos()
    create_card_04_craigslist_hack()
    create_card_05_chore_fee()
    create_card_06_city_bans()
    print("\n🎉 All 6 High-DPI Evidence Plates generated!")
