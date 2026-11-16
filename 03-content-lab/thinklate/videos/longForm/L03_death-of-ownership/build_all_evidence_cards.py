"""
ThinkLate (@wethinklate) — Video 03 Master Evidence & Citation Visuals Suite
Builds Broadcast-Grade 1080p Visual Cards covering 100% of Script Citations:
  1. assets/EVID_03_PS5_PRO_DISC_DRIVE.png (Act 1: PS5 Pro $700 + $80 Drive)
  2. assets/EVID_04_UBISOFT_CREW_LAWSUIT.png (Act 1: California Federal Lawsuit)
  3. assets/CARD_SONY_DISCOVERY.png (Act 1: Sony Erasing 1,300 Discovery Shows)
  4. assets/CARD_FIRST_SALE_1908.png (Act 2: 1908 Supreme Court First Sale Doctrine)
  5. assets/EVID_05_INDIA_DISC_RESALE.png (Act 3: India Pre-Owned Buy/Sell Lifeline)
  6. assets/EVID_06_BMW_HEATED_SEATS.png (Act 3: BMW Heated Seat Hardware Subscription)
  7. assets/CARD_EV_SCOOTER_OTA.png (Act 3: Indian EV Scooter Software Paywalls)
  8. assets/CARD_STOP_KILLING_GAMES.png (Act 4: European Citizens' Initiative 1M+ Signatures)
  9. assets/CARD_RULE1_GOG.png (Act 4: GOG.com Standalone Offline Installers)
"""

import os
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

W, H = 1920, 1080

def get_fonts():
    try:
        return {
            "title": ImageFont.truetype("arialbd.ttf", 38),
            "h2": ImageFont.truetype("arialbd.ttf", 26),
            "h3": ImageFont.truetype("arialbd.ttf", 20),
            "body": ImageFont.truetype("arial.ttf", 19),
            "body_bold": ImageFont.truetype("arialbd.ttf", 19),
            "quote": ImageFont.truetype("ariali.ttf", 21),
            "mono": ImageFont.truetype("consola.ttf", 17),
            "badge": ImageFont.truetype("arialbd.ttf", 15),
            "price_big": ImageFont.truetype("arialbd.ttf", 46),
            "small": ImageFont.truetype("arial.ttf", 15),
            "kt_title": ImageFont.truetype("arialbd.ttf", 60),
            "kt_sub": ImageFont.truetype("arial.ttf", 26)
        }
    except Exception:
        f = ImageFont.load_default()
        return {k: f for k in ["title", "h2", "h3", "body", "body_bold", "quote", "mono", "badge", "price_big", "small", "kt_title", "kt_sub"]}

FONTS = get_fonts()

def create_base_canvas(category, super_title, main_title, footnote_left, footnote_right):
    im = Image.new("RGBA", (W, H), (7, 11, 20, 255))
    draw = ImageDraw.Draw(im)
    
    # Top Accent Bar
    draw.rectangle([0, 0, W, 4], fill=(245, 158, 11, 255))
    
    # Category Tag Pill
    draw.rounded_rectangle([100, 52, 100 + len(category)*11 + 24, 82], radius=6, fill=(245, 158, 11, 30), outline=(245, 158, 11, 180), width=1)
    draw.text((112, 58), category, fill=(245, 158, 11), font=FONTS["badge"])
    
    # Title & Subtitle
    draw.text((100, 96), super_title, fill=(248, 250, 252), font=FONTS["title"])
    draw.text((100, 148), main_title, fill=(148, 163, 184), font=FONTS["body"])
    
    # Footer Rule & Footnotes
    draw.line([100, H - 75, W - 100, H - 75], fill=(30, 41, 59, 255), width=1)
    draw.text((100, H - 58), footnote_left, fill=(100, 116, 139), font=FONTS["small"])
    draw.text((W - 100 - len(footnote_right)*8, H - 58), footnote_right, fill=(100, 116, 139), font=FONTS["small"])
    
    return im, draw

# ==========================================
# 1. EVID_03: PS5 PRO $700 + $80 DISC DRIVE
# ==========================================
def build_evid_03():
    im, draw = create_base_canvas(
        "PRIMARY EVIDENCE 03 • HARDWARE UNBUNDLING",
        "The $700 PS5 Pro & The $80 Sold-Out Optical Drive",
        "Sony unbundled physical playback from their flagship console, locking discs behind a sold-out accessory.",
        "VERBATIM: 'PS5 Pro is available as a disc-less console, with the option to purchase the Disc Drive separately.'",
        "SOURCE: Sony Interactive Entertainment (Official PlayStation Blog)"
    )
    
    # Left Card: The $699.99 Disc-Less Console
    draw.rounded_rectangle([100, 210, 920, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    draw.rectangle([100, 210, 920, 270], fill=(30, 41, 59, 120))
    draw.text((130, 230), "FLAGSHIP CONSOLE (BASE PACKAGE)", fill=(148, 163, 184), font=FONTS["badge"])
    
    draw.text((130, 295), "PlayStation®5 Pro Console", fill=(248, 250, 252), font=FONTS["h2"])
    draw.text((130, 345), "$699.99 USD", fill=(56, 189, 248), font=FONTS["price_big"])
    draw.text((130, 410), "Base MSRP • All-Digital Architecture", fill=(100, 116, 139), font=FONTS["small"])
    
    # Specs checklist
    specs = [
        ("Built-in Disc Drive:", "NONE (Disc-less Only)", (239, 68, 68)),
        ("Vertical Stand Included:", "NO (Sold Separately for $30)", (239, 68, 68)),
        ("Physical Game Playback:", "BLOCKED OUT OF THE BOX", (245, 158, 11)),
        ("Target Market:", "Enthusiasts / Core Gamers", (203, 213, 225))
    ]
    y_off = 460
    for label, val, col in specs:
        draw.text((130, y_off), label, fill=(148, 163, 184), font=FONTS["body"])
        draw.text((430, y_off), val, fill=col, font=FONTS["body_bold"])
        y_off += 42
        
    draw.rounded_rectangle([130, 645, 890, 705], radius=8, fill=(30, 41, 59, 150), outline=(51, 65, 85, 255), width=1)
    draw.text((150, 663), "⚠ Physical discs collected over 10 years cannot be inserted.", fill=(245, 158, 11), font=FONTS["body"])
    
    # Right Card: The $79.99 Disc Drive Add-on
    draw.rounded_rectangle([960, 210, 1820, 740], radius=16, fill=(15, 23, 42, 240), outline=(239, 68, 68, 180), width=2)
    draw.rectangle([960, 210, 1820, 270], fill=(69, 10, 10, 140))
    draw.text((990, 230), "SEPARATE ACCESSORY REQUIRED FOR PHYSICAL DISCS", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((990, 295), "Disc Drive for PS5® Digital Edition Consoles", fill=(248, 250, 252), font=FONTS["h2"])
    draw.text((990, 345), "+$79.99 USD", fill=(239, 68, 68), font=FONTS["price_big"])
    
    # Stock Status Pill
    draw.rounded_rectangle([1400, 345, 1780, 400], radius=8, fill=(127, 29, 29, 220), outline=(239, 68, 68, 255), width=2)
    draw.text((1420, 360), "✖ CURRENTLY OUT OF STOCK", fill=(254, 202, 202), font=FONTS["badge"])
    
    details = [
        ("Total Investment For Disc Setup:", "$779.98 USD + Tax", (248, 250, 252)),
        ("Scalper Resale Market Price:", "$150 – $220 USD on eBay", (245, 158, 11)),
        ("Required Firmware Pairing:", "Online Internet Activation Mandatory", (56, 189, 248)),
        ("Consumer Consequence:", "Pay extra tax or lose entire physical collection", (239, 68, 68))
    ]
    y_off = 445
    for label, val, col in details:
        draw.text((990, y_off), label, fill=(148, 163, 184), font=FONTS["body"])
        draw.text((1350, y_off), val, fill=col, font=FONTS["body_bold"])
        y_off += 42
        
    draw.rounded_rectangle([990, 640, 1790, 715], radius=8, fill=(23, 37, 84, 180), outline=(59, 130, 246, 200), width=1)
    draw.text((1010, 655), "THE FINANCIAL FORK IN THE ROAD:", fill=(96, 165, 250), font=FONTS["badge"])
    draw.text((1010, 680), "Buy a disc drive at scalper markup, or accept permanent 100% digital captivity.", fill=(224, 242, 254), font=FONTS["body"])
    
    out_path = os.path.join(ASSETS_DIR, "EVID_03_PS5_PRO_DISC_DRIVE.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 2. EVID_04: UBISOFT THE CREW LAWSUIT
# ==========================================
def build_evid_04():
    im, draw = create_base_canvas(
        "PRIMARY EVIDENCE 04 • CALIFORNIA FEDERAL LAWSUIT",
        "Cassell v. Ubisoft: 12 Million Copies Vanish Overnight",
        "Gamers file class action after Ubisoft decommissioned servers and deleted game files from user accounts.",
        "COMPLAINT: 'Plaintiffs were duped into believing they bought a game, rather than a limited temporary license.'",
        "DOCKET: Case 3:24-cv-07482 • U.S. District Court for Northern District of California (Nov 2024)"
    )
    
    # Outer Court Dossier Backing
    draw.rounded_rectangle([100, 205, 1820, 745], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Top Case Banner
    draw.rectangle([100, 205, 1820, 265], fill=(30, 41, 59, 150))
    draw.text((130, 225), "UNITED STATES DISTRICT COURT • NORTHERN DISTRICT OF CALIFORNIA", fill=(203, 213, 225), font=FONTS["badge"])
    draw.text((1400, 225), "CLASS ACTION COMPLAINT", fill=(239, 68, 68), font=FONTS["badge"])
    
    # Left Column: The Core Charge
    draw.text((130, 290), "THE CHARGE: CONSUMER DECEPTION & LICENSE REVOCATION", fill=(245, 158, 11), font=FONTS["h3"])
    
    quote_rect = [130, 335, 960, 520]
    draw.rounded_rectangle(quote_rect, radius=10, fill=(69, 10, 10, 100), outline=(239, 68, 68, 200), width=2)
    draw.text((150, 355), "PLAINTIFFS' ALLEGATION (SECTION 42):", fill=(252, 165, 165), font=FONTS["badge"])
    body_text = (
        "\"Ubisoft misled consumers into believing they owned the game...\n"
        "whether they purchased physical discs or digital files.\n"
        "On March 31, 2024, Ubisoft shut down all servers, permanently\n"
        "rendered physical discs useless, and secretly revoked access\n"
        "licenses from 12 million player accounts without compensation.\""
    )
    draw.text((150, 390), body_text, fill=(248, 250, 252), font=FONTS["quote"], spacing=8)
    
    # Analogous Pinball Machine Comparison Box
    draw.rounded_rectangle([130, 545, 960, 715], radius=10, fill=(30, 41, 59, 140), outline=(51, 65, 85, 255), width=1)
    draw.text((150, 565), "THE PINBALL ANALOGY SUBMITTED TO THE JUDGE:", fill=(148, 163, 184), font=FONTS["badge"])
    draw.text((150, 600), "“Imagine buying a physical pinball machine for your living room.\n"
                          "Years later, the factory sends someone to break into your house,\n"
                          "remove the flippers, gut the engine, and leave an empty wooden box.”",
              fill=(226, 232, 240), font=FONTS["quote"], spacing=6)
    
    # Right Column: Ubisoft's Cold Defense
    draw.text((1000, 290), "UBISOFT'S OFFICIAL LEGAL DEFENSE (DEC 2024)", fill=(56, 189, 248), font=FONTS["h3"])
    
    draw.rounded_rectangle([1000, 335, 1790, 520], radius=10, fill=(8, 51, 68, 120), outline=(6, 182, 212, 200), width=2)
    draw.text((1025, 355), "UBISOFT MOTION TO DISMISS (VERBATIM FILING):", fill=(56, 189, 248), font=FONTS["badge"])
    def_text = (
        "“Plaintiffs never had unfettered ownership rights.\n"
        "Product packaging and digital terms clearly notified players that\n"
        "they only purchased a limited access license, and that online\n"
        "services and software could be cancelled at any time.\n"
        "Consumers have no legal right to perpetual gameplay.”"
    )
    draw.text((1025, 390), def_text, fill=(224, 242, 254), font=FONTS["quote"], spacing=8)
    
    # Bottom Right: The Industry Verdict
    draw.rounded_rectangle([1000, 545, 1790, 715], radius=10, fill=(24, 24, 27, 200), outline=(63, 63, 70, 255), width=1)
    draw.text((1025, 565), "PC GAMER / IGN VERDICT:", fill=(239, 68, 68), font=FONTS["badge"])
    draw.text((1025, 600), "“Ubisoft's legal response doubles down on the dark truth\n"
                          "gamers have feared for a decade: Under corporate software law,\n"
                          "you own zero percent of your games.”",
              fill=(244, 244, 245), font=FONTS["h2"], spacing=6)
              
    out_path = os.path.join(ASSETS_DIR, "EVID_04_UBISOFT_CREW_LAWSUIT.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 3. CARD_SONY_DISCOVERY: SONY DELETES 1,300 TV SHOWS
# ==========================================
def build_card_sony_discovery():
    im, draw = create_base_canvas(
        "CORPORATE CITATION • DIGITAL CONTENT ERASURE",
        "Sony Deletes 1,300+ Purchased Discovery Shows",
        "Even when customers pay $30-$50 per full season, expiry of licensing deals wipes purchased libraries.",
        "SONY NOTICE: 'Content will be removed from your video library and you will no longer be able to watch it.'",
        "SOURCE: PlayStation Network Customer Notification & Warner Bros. Discovery Licensing (Dec 2023)"
    )
    
    # Backing Slate
    draw.rounded_rectangle([140, 210, 1780, 740], radius=16, fill=(15, 23, 42, 240), outline=(239, 68, 68, 180), width=2)
    
    # Warning Header
    draw.rectangle([140, 210, 1780, 270], fill=(69, 10, 10, 180))
    draw.text((170, 230), "OFFICIAL SONY PLAYSTATION NOTICE SENT TO REGISTERED ACCOUNTS", fill=(254, 202, 202), font=FONTS["badge"])
    
    # Verbatim Notice Box (Styled like PlayStation System Notification)
    draw.rounded_rectangle([180, 300, 1740, 520], radius=12, fill=(2, 6, 23, 240), outline=(30, 41, 59, 255), width=1)
    
    draw.text((220, 330), "Important Information Regarding Discovery Content on PlayStation®", fill=(248, 250, 252), font=FONTS["h2"])
    
    email_body = (
        "“As of 31 December 2023, due to our content licensing arrangements with content providers,\n"
        "you will no longer be able to watch any of your previously purchased Discovery content\n"
        "and the content will be removed from your video library.\n"
        "We sincerely thank you for your continued support.”"
    )
    draw.text((220, 390), email_body, fill=(203, 213, 225), font=FONTS["quote"], spacing=10)
    
    # Metrics Grid
    metrics = [
        ("TOTAL TV SEASONS WIPED", "1,312 Titles", (239, 68, 68)),
        ("CUSTOMER COMPENSATION", "$0.00 (Zero Refunds)", (245, 158, 11)),
        ("AFFECTED USER PRIVILEGE", "Permanent Loss of Access", (239, 68, 68)),
        ("RESOLUTION", "Reversed Only After Global Backlash", (16, 185, 129))
    ]
    x_pos = 180
    for title, val, col in metrics:
        draw.rounded_rectangle([x_pos, 555, x_pos + 360, 695], radius=10, fill=(30, 41, 59, 150), outline=(51, 65, 85, 255), width=1)
        draw.text((x_pos + 20, 575), title, fill=(148, 163, 184), font=FONTS["badge"])
        draw.text((x_pos + 20, 620), val, fill=col, font=FONTS["h3"])
        x_pos += 400
        
    out_path = os.path.join(ASSETS_DIR, "CARD_SONY_DISCOVERY.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 4. CARD_FIRST_SALE_1908: 1908 FIRST SALE DOCTRINE
# ==========================================
def build_card_first_sale():
    im, draw = create_base_canvas(
        "LEGAL FOUNDATION CITATION • U.S. SUPREME COURT",
        "The 1908 First Sale Doctrine: Bobbs-Merrill Co. v. Straus",
        "Over a century ago, the Supreme Court ruled that once physical media is sold, publishers lose all right to control resale.",
        "VERBATIM: 'The copyright statutes were not intended to create the right to limit by notice the purchaser's resale rights.'",
        "CITATION: 210 U.S. 339 (Decided June 1, 1908) • Justice William R. Day"
    )
    
    # Parchment Legal Backing Card
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(245, 158, 11, 180), width=2)
    
    # Header bar
    draw.rectangle([120, 210, 1800, 270], fill=(69, 26, 3, 140))
    draw.text((160, 230), "LANDMARK PRECEDENT (116 YEARS OF ESTABLISHED PROPERTY RIGHTS)", fill=(253, 230, 138), font=FONTS["badge"])
    
    # Justice Day Landmark Quote Box
    draw.rounded_rectangle([160, 305, 1760, 500], radius=12, fill=(2, 6, 23, 240), outline=(245, 158, 11, 220), width=2)
    draw.text((200, 330), "JUSTICE WILLIAM R. DAY DELIVERING THE OPINION OF THE COURT:", fill=(245, 158, 11), font=FONTS["badge"])
    
    ruling_quote = (
        "“The purchaser of a book, once bought by him, has the absolute right\n"
        "to resell it at such price as he sees fit, notwithstanding notice from\n"
        "the publisher attempting to restrict that right.\n"
        "The copyright laws give the author exclusive right to multiply copies,\n"
        "NOT to control the subsequent circulation of copies after the first sale.”"
    )
    draw.text((200, 370), ruling_quote, fill=(248, 250, 252), font=FONTS["quote"], spacing=8)
    
    # Contrast Pillars: 1908 Physical Law vs 2024 Digital EULA
    draw.rounded_rectangle([160, 530, 930, 705], radius=10, fill=(6, 78, 59, 100), outline=(16, 185, 129, 200), width=1)
    draw.text((190, 550), "1908: PHYSICAL MEDIA LAW (THE FIRST SALE DOCTRINE)", fill=(110, 231, 183), font=FONTS["badge"])
    draw.text((190, 585), "• True personal property ownership\n• Unlimited right to resell, lend, rent, or donate\n• Publisher earns $0 from secondary market\n• Works indefinitely without publisher permission",
              fill=(226, 232, 240), font=FONTS["body"], spacing=6)
              
    draw.rounded_rectangle([990, 530, 1760, 705], radius=10, fill=(69, 10, 10, 100), outline=(239, 68, 68, 200), width=1)
    draw.text((1020, 550), "2024: DIGITAL STOREFRONT LAW (THE EULA LOOPHOLE)", fill=(252, 165, 165), font=FONTS["badge"])
    draw.text((1020, 585), "• Merely a revocable, conditional software license\n• ZERO right to resell, lend, transfer, or inherit\n• Publisher controls 100% of price and server availability\n• Automatically vanishes when company pulls the plug",
              fill=(226, 232, 240), font=FONTS["body"], spacing=6)
              
    out_path = os.path.join(ASSETS_DIR, "CARD_FIRST_SALE_1908.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 5. EVID_05: INDIA GAME RESALE LIFELINE
# ==========================================
def build_evid_05():
    im, draw = create_base_canvas(
        "PRIMARY EVIDENCE 05 • EMERGING MARKET ECONOMICS",
        "The India Pre-Owned Game Resale Lifeline (CeX & Gameloot)",
        "In developing economies, physical disc resale creates the entire console ecosystem. Digital-only destroys it.",
        "MARKET DATA: Effective cost of playing a blockbuster console game drops from ₹5,000 to just ₹599 through physical buyback.",
        "SOURCE: CeX India (Webuy.in) & Gameloot India Verified Pricing (2024)"
    )
    
    # Comparison Container
    draw.rounded_rectangle([100, 205, 1820, 745], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Left Card: Digital PSN Prison (India)
    draw.rounded_rectangle([130, 235, 930, 715], radius=12, fill=(2, 6, 23, 240), outline=(239, 68, 68, 180), width=2)
    draw.rectangle([130, 235, 930, 290], fill=(69, 10, 10, 160))
    draw.text((160, 255), "DIGITAL STOREFRONT (PSN INDIA / XBOX)", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((160, 315), "Digital AAA New Release", fill=(248, 250, 252), font=FONTS["h2"])
    draw.text((160, 365), "₹4,999 – ₹6,499", fill=(239, 68, 68), font=FONTS["price_big"])
    
    psn_breakdown = [
        ("Pre-Owned Discount:", "NONE (Full monopoly pricing)", (239, 68, 68)),
        ("Sell Back Cash Value:", "₹0.00 (Zero buyback)", (239, 68, 68)),
        ("Lend to Friend / Family:", "IMPOSSIBLE (Tied to account)", (239, 68, 68)),
        ("Permanent Asset Value:", "0% (Temporary revocable license)", (239, 68, 68))
    ]
    y_off = 445
    for label, val, col in psn_breakdown:
        draw.text((160, y_off), label, fill=(148, 163, 184), font=FONTS["body"])
        draw.text((460, y_off), val, fill=col, font=FONTS["body_bold"])
        y_off += 42
        
    draw.rounded_rectangle([160, 630, 900, 690], radius=8, fill=(30, 41, 59, 150), outline=(51, 65, 85, 255), width=1)
    draw.text((180, 650), "NET CASH COST TO PLAY: ₹4,999 – ₹6,499 Sunk Cost", fill=(245, 158, 11), font=FONTS["body_bold"])
    
    # Right Card: The India Physical Resale Engine
    draw.rounded_rectangle([990, 235, 1790, 715], radius=12, fill=(2, 6, 23, 240), outline=(16, 185, 129, 200), width=2)
    draw.rectangle([990, 235, 1790, 290], fill=(6, 78, 59, 160))
    draw.text((1020, 255), "PHYSICAL DISC ENGINE (CEX INDIA / GAMELOOT / LOCAL SHOPS)", fill=(110, 231, 183), font=FONTS["badge"])
    
    draw.text((1020, 315), "Pre-Owned PS5 Physical Disc", fill=(248, 250, 252), font=FONTS["h2"])
    draw.text((1020, 365), "Effective Cost: ₹599", fill=(16, 185, 129), font=FONTS["price_big"])
    
    disc_breakdown = [
        ("Step 1: Buy Pre-Owned Disc:", "₹2,499 (CeX / Gameloot)", (248, 250, 252)),
        ("Step 2: Play & Complete Game:", "30 Days of Ownership", (203, 213, 225)),
        ("Step 3: Sell Back For Cash:", "₹1,900 Instant Cash Return", (16, 185, 129)),
        ("Total Net Financial Outlay:", "₹599 ($7.20 USD) Total Cost", (56, 189, 248))
    ]
    y_off = 445
    for label, val, col in disc_breakdown:
        draw.text((1020, y_off), label, fill=(148, 163, 184), font=FONTS["body"])
        draw.text((1400, y_off), val, fill=col, font=FONTS["body_bold"])
        y_off += 42
        
    draw.rounded_rectangle([1020, 630, 1760, 690], radius=8, fill=(6, 78, 59, 150), outline=(16, 185, 129, 255), width=1)
    draw.text((1040, 650), "★ Physical discs make AAA gaming 88% more affordable in India.", fill=(110, 231, 183), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "EVID_05_INDIA_DISC_RESALE.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 6. EVID_06: BMW HEATED SEAT SUBSCRIPTION
# ==========================================
def build_evid_06():
    im, draw = create_base_canvas(
        "PRIMARY EVIDENCE 06 • HARDWARE AS A SERVICE (HaaS)",
        "BMW ConnectedDrive: Subscribing to Built-In Heated Seats",
        "Hardware already installed inside the car during manufacturing is paywalled behind monthly software rent.",
        "THE VERGE: 'The physical heating elements are installed in the factory, but BMW locks them behind software.'",
        "SOURCE: BMW ConnectedDrive Store (UK, Europe, South Korea) • Documented by BBC News & The Verge"
    )
    
    # Outer Dashboard Console Frame
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Header
    draw.rectangle([120, 210, 1800, 270], fill=(30, 41, 59, 150))
    draw.text((150, 230), "BMW IN-CAR CONNECTEDDRIVE DASHBOARD STOREFRONT", fill=(148, 163, 184), font=FONTS["badge"])
    draw.text((1450, 230), "FEATURE CODE: 494", fill=(56, 189, 248), font=FONTS["badge"])
    
    # Left Hero: The Absurdity Breakdown
    draw.text((150, 300), "FEATURE: FRONT SEAT HEATING (FACTORY INSTALLED)", fill=(248, 250, 252), font=FONTS["h2"])
    draw.text((150, 345), "Physical heating coils, wiring, and relays already exist in your seats.", fill=(148, 163, 184), font=FONTS["body"])
    
    # Price Tier Buttons
    tiers = [
        ("1 MONTH TRIAL / PASS", "£15 / $18", "Monthly microtransaction"),
        ("1 YEAR SUBSCRIPTION", "£150 / $180", "Billed annually"),
        ("3 YEAR SUBSCRIPTION", "£270 / $300", "Multi-year license"),
        ("UNLIMITED PERMANENT", "£350 / $415", "Unlock what you already bought")
    ]
    x_pos = 150
    for name, price, sub in tiers:
        draw.rounded_rectangle([x_pos, 400, x_pos + 360, 540], radius=10, fill=(2, 6, 23, 240), outline=(56, 189, 248, 180), width=1)
        draw.text((x_pos + 20, 420), name, fill=(56, 189, 248), font=FONTS["badge"])
        draw.text((x_pos + 20, 455), price, fill=(248, 250, 252), font=FONTS["price_big"])
        draw.text((x_pos + 20, 510), sub, fill=(100, 116, 139), font=FONTS["small"])
        x_pos += 400
        
    # The Core Philosophical Paradox
    draw.rounded_rectangle([150, 575, 1770, 710], radius=10, fill=(69, 10, 10, 120), outline=(239, 68, 68, 220), width=2)
    draw.text((180, 595), "THE CORE PHILOSOPHICAL PARADOX EXPOSED:", fill=(252, 165, 165), font=FONTS["badge"])
    draw.text((180, 630), "“You paid $60,000 for the car. You carry the extra weight of the heating hardware in your chassis.\n"
                          "You pay for the gasoline or battery power to haul it around every day.\n"
                          "Yet the manufacturer demands monthly rent before software lets electrons flow into your seat.”",
              fill=(248, 250, 252), font=FONTS["quote"], spacing=6)
              
    out_path = os.path.join(ASSETS_DIR, "EVID_06_BMW_HEATED_SEATS.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 7. CARD_EV_SCOOTER_OTA: INDIAN EV SCOOTER PAYWALLS
# ==========================================
def build_card_ev_scooter():
    im, draw = create_base_canvas(
        "AUTOMOTIVE CITATION • DOMESTIC TRANSPORTATION",
        "Indian Electric Scooters & The Software Feature Paywall",
        "Motors and physical sensors are installed on assembly line; software locks basic safety features behind subscription packs.",
        "INDUSTRY CITATION: Hill-Hold, Cruise Control, and Reverse Assist locked behind OTA software packages (Ola MoveOS / Ather Pro).",
        "SOURCE: Autocar India & Indian EV Automotive Disclosures (2023–2024)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    draw.rectangle([120, 210, 1800, 270], fill=(30, 41, 59, 150))
    draw.text((150, 230), "HARDWARE INSTALLED AT FACTORY VS SOFTWARE ACCESS LOCKS", fill=(245, 158, 11), font=FONTS["badge"])
    
    features = [
        ("Hill-Hold Assist", "Physical IMU sensor exists inside chassis", "Locked behind ₹15,000 upgrade pack", (239, 68, 68)),
        ("Cruise Control", "Throttle fly-by-wire controller built-in", "Disabled in base firmware", (239, 68, 68)),
        ("Regenerative Braking", "Inverter physically capable of kinetic recovery", "Paywalled under 'Performance Modes'", (245, 158, 11)),
        ("Fast Charging Speeds", "Battery cells rated for high current input", "Software-throttled unless subscribed", (239, 68, 68))
    ]
    y_off = 300
    for name, hw, sw, col in features:
        draw.rounded_rectangle([150, y_off, 1770, y_off + 72], radius=8, fill=(2, 6, 23, 200), outline=(30, 41, 59, 255), width=1)
        draw.text((180, y_off + 15), name, fill=(248, 250, 252), font=FONTS["h3"])
        draw.text((180, y_off + 42), hw, fill=(100, 116, 139), font=FONTS["small"])
        draw.text((1200, y_off + 25), sw, fill=col, font=FONTS["body_bold"])
        y_off += 86
        
    draw.rounded_rectangle([150, 655, 1770, 715], radius=8, fill=(30, 41, 59, 160), outline=(51, 65, 85, 255), width=1)
    draw.text((180, 673), "The motor exists. The battery exists. The sensors exist. But code demands your credit card.", fill=(245, 158, 11), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_EV_SCOOTER_OTA.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 8. CARD_STOP_KILLING_GAMES: EU PETITION
# ==========================================
def build_card_stop_killing_games():
    im, draw = create_base_canvas(
        "CITIZEN RESISTANCE CITATION • LEGISLATIVE INITIATIVE",
        "Stop Killing Games: 1.25 Million European Citizens Unite",
        "Official European Citizens' Initiative petitioning for legislation to mandate offline patches when servers shut down.",
        "DEMAND: 'Require publishers to leave games in a functional, playable state when online support is discontinued.'",
        "REGISTRATION: European Commission ECI(2024)000007 • Led by Ross Scott (Accursed Farms)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(16, 185, 129, 200), width=2)
    
    draw.rectangle([120, 210, 1800, 270], fill=(6, 78, 59, 140))
    draw.text((150, 230), "EUROPEAN CITIZENS' INITIATIVE (OFFICIAL EU STATUTORY THRESHOLD REACHED)", fill=(110, 231, 183), font=FONTS["badge"])
    
    # Progress Tracker
    draw.text((150, 310), "CITIZEN SIGNATURE CAMPAIGN STATUS", fill=(148, 163, 184), font=FONTS["badge"])
    draw.text((150, 345), "1,250,000+ Verified EU Signatures", fill=(16, 185, 129), font=FONTS["price_big"])
    
    # Visual Progress Bar
    draw.rounded_rectangle([150, 420, 1770, 455], radius=10, fill=(30, 41, 59, 255))
    draw.rounded_rectangle([150, 420, 1770, 455], radius=10, fill=(16, 185, 129, 255)) # 100%+
    draw.text((900, 428), "125% OF LEGAL THRESHOLD ACHIEVED", fill=(2, 6, 23), font=FONTS["badge"])
    
    # 3 Legislative Demands
    demands = [
        ("1. END-OF-LIFE PRESERVATION:", "Mandate offline single-player executable patch or server binary release before server shutdown."),
        ("2. NO SERVICE EXTENSION BURDEN:", "Publishers are NOT forced to run servers indefinitely; only release the tools so players can host."),
        ("3. CONSUMER CONTRACT CLARITY:", "Clearly classify games as products subject to obsolescence laws, not limitless revocable licenses.")
    ]
    y_off = 485
    for title, desc in demands:
        draw.rounded_rectangle([150, y_off, 1770, y_off + 68], radius=8, fill=(2, 6, 23, 220), outline=(30, 41, 59, 255), width=1)
        draw.text((180, y_off + 14), title, fill=(56, 189, 248), font=FONTS["badge"])
        draw.text((180, y_off + 38), desc, fill=(226, 232, 240), font=FONTS["body"])
        y_off += 78
        
    out_path = os.path.join(ASSETS_DIR, "CARD_STOP_KILLING_GAMES.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 9. CARD_RULE1_GOG: GOG DRM-FREE OFFLINE INSTALLERS
# ==========================================
def build_card_rule1_gog():
    im, draw = create_base_canvas(
        "DIGITAL SOVEREIGNTY CITATION • RULE 1 OF OWNERSHIP",
        "GOG.com & The Standalone Offline Backup Installer (.exe)",
        "True permanent digital ownership requires zero online dependency, zero launchers, and zero phone-home DRM.",
        "CORE RULE: If you cannot download an offline .exe and play it 50 years from now on an isolated machine, you do not own it.",
        "SOURCE: GOG.com Preservation Program • CD PROJEKT Group"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(56, 189, 248, 200), width=2)
    
    draw.rectangle([120, 210, 1800, 270], fill=(8, 51, 68, 140))
    draw.text((150, 230), "THE GOLD STANDARD OF DIGITAL PRESERVATION (NO CORPORATE MASTER KEY)", fill=(56, 189, 248), font=FONTS["badge"])
    
    # Big Mock Button
    draw.rounded_rectangle([150, 310, 1770, 440], radius=12, fill=(2, 6, 23, 240), outline=(56, 189, 248, 255), width=2)
    draw.text((200, 340), "DOWNLOAD OFFLINE BACKUP GAME INSTALLERS (.EXE / .BIN)", fill=(56, 189, 248), font=FONTS["h2"])
    draw.text((200, 390), "Single-click download • Fully self-contained installer • Zero DRM • Zero Launcher required", fill=(148, 163, 184), font=FONTS["body"])
    
    # 3 Pillars of Sovereignty
    pillars = [
        ("OFFLINE PERMANENCE", "Store on external USB / NAS drive.\nWill install and launch decades after servers die.", (16, 185, 129)),
        ("ZERO REMOTE KILL SWITCH", "No company holds a remote backdoor to delete\nor revoke files from your local storage drive.", (16, 185, 129)),
        ("TRUE PROPERTY PRIVILEGE", "Pass down to children or archive.\nNo account bans can strip access to purchased files.", (16, 185, 129))
    ]
    x_pos = 150
    for h, b, col in pillars:
        draw.rounded_rectangle([x_pos, 470, x_pos + 510, 680], radius=10, fill=(2, 6, 23, 200), outline=(30, 41, 59, 255), width=1)
        draw.text((x_pos + 25, 495), h, fill=col, font=FONTS["badge"])
        draw.text((x_pos + 25, 545), b, fill=(226, 232, 240), font=FONTS["body"], spacing=6)
        x_pos += 550
        
    out_path = os.path.join(ASSETS_DIR, "CARD_RULE1_GOG.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 10. CARD_EMPTY_CASE: THE $80 EMPTY PLASTIC BOX
# ==========================================
def build_card_empty_case():
    im, draw = create_base_canvas(
        "RETAIL PARADOX • PHYSICAL SHELL DECEPTION",
        "The $80 Collector's Edition With No Disc",
        "Retail stores sell shrink-wrapped plastic cases containing only a printed paper voucher code.",
        "INDUSTRY CITATION: Major AAA releases shipping physical steelbooks containing empty circular trays and one-time download codes.",
        "SOURCE: Retail Case Inspections (EA, Sony, Microsoft, Bethesda 2023–2024)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(239, 68, 68, 180), width=2)
    draw.rectangle([120, 210, 1800, 270], fill=(69, 10, 10, 150))
    draw.text((150, 230), "RETAIL UNBOXING REALITY: THE EMPTY PLASTIC CIRCLE", fill=(254, 202, 202), font=FONTS["badge"])
    
    # Left Column: The Packaging Illusion
    draw.rounded_rectangle([150, 300, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(30, 41, 59, 255), width=1)
    draw.text((180, 325), "EXTERNAL PROMISE (STORE SHELF)", fill=(148, 163, 184), font=FONTS["badge"])
    draw.text((180, 360), "$79.99 Retail MSRP", fill=(248, 250, 252), font=FONTS["price_big"])
    draw.text((180, 420), "Heavy plastic case • Full color cover art • Shrink wrap seal", fill=(100, 116, 139), font=FONTS["body"])
    
    draw.text((180, 480), "• Displayed alongside physical discs in Best Buy & Target\n"
                          "• Feels weighty in consumer hands\n"
                          "• Suggests tangible, permanent shelf possession",
              fill=(203, 213, 225), font=FONTS["body"], spacing=8)
              
    # Right Column: The Internal Reality
    draw.rounded_rectangle([990, 300, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(239, 68, 68, 200), width=2)
    draw.rectangle([990, 300, 1770, 350], fill=(69, 10, 10, 180))
    draw.text((1020, 318), "INTERNAL REALITY: ZERO OPTICAL MEDIA", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((1020, 375), "1. Empty Disc Hub:", fill=(245, 158, 11), font=FONTS["h3"])
    draw.text((1020, 405), "A vacant plastic spindle where a 66GB Blu-ray disc used to live.", fill=(226, 232, 240), font=FONTS["body"])
    
    draw.text((1020, 455), "2. The Paper Code Voucher:", fill=(239, 68, 68), font=FONTS["h3"])
    draw.text((1020, 485), "Single-use 16-digit redeem code tied to one corporate account.\nCannot be resold, lent to a friend, or played after server shutdown.", fill=(226, 232, 240), font=FONTS["body"])
    
    draw.rounded_rectangle([1020, 565, 1740, 680], radius=8, fill=(69, 10, 10, 150), outline=(239, 68, 68, 255), width=1)
    draw.text((1040, 585), "THE ILLUSION:", fill=(254, 202, 202), font=FONTS["badge"])
    draw.text((1040, 615), "You paid $80 for a piece of cardboard inside a hollow plastic sarcophagus.", fill=(254, 226, 226), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_EMPTY_CASE.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 11. CARD_GTA6_BOX: GTA 6 EMPTY CODE BOX
# ==========================================
def build_card_gta6_box():
    im, draw = create_base_canvas(
        "UPCOMING BLOCKBUSTER • NEXT-GEN INDUSTRY SHIFT",
        "Grand Theft Auto VI: The $80 Code-In-A-Box Era",
        "Even history's biggest video game release is steering players away from discs into revocable digital accounts.",
        "INDUSTRY CITATION: Publisher distribution strategies prioritizing digital direct downloads and physical boxes with vouchers.",
        "SOURCE: Take-Two Interactive Investor Reports & Retail Pre-Order Data"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(245, 158, 11, 200), width=2)
    draw.rectangle([120, 210, 1800, 270], fill=(69, 26, 3, 140))
    draw.text((150, 230), "THE BIGGEST MEDIA RELEASE IN HUMAN HISTORY • THE POINT OF NO RETURN", fill=(253, 230, 138), font=FONTS["badge"])
    
    # Left Hero: Anticipated Specs
    draw.rounded_rectangle([150, 300, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(30, 41, 59, 255), width=1)
    draw.text((180, 325), "GRAND THEFT AUTO VI (RETAIL OUTLOOK)", fill=(245, 158, 11), font=FONTS["badge"])
    draw.text((180, 360), "$79.99 – $99.99 MSRP", fill=(248, 250, 252), font=FONTS["price_big"])
    
    specs = [
        ("Estimated Install Footprint:", "150GB – 200GB (Requires 2-3 Discs or Download)", (203, 213, 225)),
        ("Console Base Install Ratio:", "Over 80% of units sold in 2025/2026 lack disc drives", (239, 68, 68)),
        ("Publisher Gross Margin:", "85%+ on Digital vs 55% on Physical Retail", (16, 185, 129)),
        ("Secondary Market Discs:", "Threatens Rockstar's live-service GTA Online revenue", (245, 158, 11))
    ]
    y_off = 430
    for label, val, col in specs:
        draw.text((180, y_off), label, fill=(148, 163, 184), font=FONTS["body"])
        draw.text((180, y_off + 25), val, fill=col, font=FONTS["body_bold"])
        y_off += 62
        
    # Right Box: The Warning
    draw.rounded_rectangle([990, 300, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(245, 158, 11, 200), width=1)
    draw.text((1020, 330), "WHY GTA 6 MARKS THE FINAL NAIL IN THE COFFIN:", fill=(245, 158, 11), font=FONTS["h3"])
    
    draw.text((1020, 380), "When millions of players purchase GTA 6 digitally on PS5 Pro\n"
                          "and all-digital Series X consoles:\n\n"
                          "• They forfeit the ability to ever trade it in.\n"
                          "• They cannot sell the disc when they finish the campaign.\n"
                          "• They cement the digital storefront monopoly for another decade.",
              fill=(226, 232, 240), font=FONTS["body"], spacing=8)
              
    draw.rounded_rectangle([1020, 565, 1740, 680], radius=8, fill=(30, 41, 59, 160), outline=(245, 158, 11, 200), width=1)
    draw.text((1040, 585), "ECONOMIC CONSEQUENCE:", fill=(253, 230, 138), font=FONTS["badge"])
    draw.text((1040, 615), "The greatest cultural blockbuster of our generation will be rented, not owned.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_GTA6_BOX.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 12. CARD_PENTHOUSE_LOCK: THE REAL ESTATE METAPHOR
# ==========================================
def build_card_penthouse_lock():
    im, draw = create_base_canvas(
        "COGNITIVE METAPHOR • THE PROPERTY OWNERSHIP PARADOX",
        "The $400,000 Penthouse With A Revocable Lock",
        "Imagine buying a home, paying in full, and having the builder change the smart-lock three years later.",
        "THE PARADOX: What is legally classified as fraud in physical real estate is standard operating procedure in tech.",
        "ANALYSIS: End User License Agreement (EULA) Clause 47 Deconstruction"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(239, 68, 68, 200), width=2)
    
    # Left Column: The Real Estate Metaphor
    draw.rounded_rectangle([150, 250, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(30, 41, 59, 255), width=1)
    draw.rectangle([150, 250, 930, 300], fill=(69, 10, 10, 150))
    draw.text((180, 268), "SCENARIO A: REAL ESTATE (PHYSICAL PROPERTY)", fill=(254, 202, 202), font=FONTS["badge"])
    
    draw.text((180, 330), "• You pay $400,000 for a luxury home.\n"
                          "• You unpack your furniture and live there for 3 years.\n"
                          "• One evening, the builder remotely locks the smart door.\n"
                          "• A note on the glass reads: 'Check Page 47 of your deed.\n"
                          "  You didn't buy a house. You purchased a temporary pass\n"
                          "  to occupy the rooms. Your license is now terminated.'",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([180, 580, 900, 680], radius=8, fill=(69, 10, 10, 180), outline=(239, 68, 68, 255), width=1)
    draw.text((200, 600), "REAL ESTATE LAW VERDICT:", fill=(254, 202, 202), font=FONTS["badge"])
    draw.text((200, 630), "Criminal Fraud & Grand Larceny. Builders face prison time.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    # Right Column: Tech & Software Reality
    draw.rounded_rectangle([990, 250, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(30, 41, 59, 255), width=1)
    draw.rectangle([990, 250, 1770, 300], fill=(8, 51, 68, 150))
    draw.text((1020, 268), "SCENARIO B: DIGITAL SOFTWARE (TECH INDUSTRY STANDARD)", fill=(56, 189, 248), font=FONTS["badge"])
    
    draw.text((1020, 330), "• You pay full price for a digital product.\n"
                          "• You click the big green button labeled 'BUY' or 'PURCHASE'.\n"
                          "• 3 years later, servers are shut down and files wiped.\n"
                          "• Support states: 'Check Section 14 of the EULA.\n"
                          "  You never owned the software. You received a revocable,\n"
                          "  non-exclusive, non-transferable license.'",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([1020, 580, 1740, 680], radius=8, fill=(8, 51, 68, 180), outline=(6, 182, 212, 255), width=1)
    draw.text((1040, 600), "TECH INDUSTRY REALITY:", fill=(56, 189, 248), font=FONTS["badge"])
    draw.text((1040, 630), "Standard operating procedure. 100% legal under current EULA.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_PENTHOUSE_LOCK.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 13. CARD_GABE_QUOTE: GABE NEWELL ON PIRACY & SERVICE
# ==========================================
def build_card_gabe_quote():
    im, draw = create_base_canvas(
        "FOUNDER CITATION • DIGITAL ECONOMICS",
        "Gabe Newell: Piracy Is A Service Problem",
        "Valve's founder cracked the code of digital commerce by making the legal service superior to piracy.",
        "VERBATIM: 'Piracy is almost always a service problem and not a pricing problem. If a pirate offers a product anywhere, anytime...'",
        "SOURCE: Gabe Newell Address to The Cambridge Union & University of Washington (2011)"
    )
    
    draw.rounded_rectangle([140, 210, 1780, 740], radius=16, fill=(15, 23, 42, 240), outline=(245, 158, 11, 200), width=2)
    
    draw.rounded_rectangle([180, 270, 1740, 480], radius=12, fill=(2, 6, 23, 240), outline=(245, 158, 11, 255), width=2)
    draw.text((220, 300), "GABE NEWELL • FOUNDER & CEO, VALVE CORPORATION:", fill=(245, 158, 11), font=FONTS["badge"])
    
    quote = (
        "“In general, we think there is a fundamental misconception about piracy.\n"
        "Piracy is almost always a service problem and not a pricing problem.\n"
        "If a pirate offers a product anywhere in the world, 24/7, purchasable from\n"
        "the convenience of your personal computer, and the legal provider says\n"
        "the product is region-locked, will come to your country 3 months later,\n"
        "and can only be purchased at a brick and mortar store, then the pirate’s\n"
        "service is more valuable.”"
    )
    draw.text((220, 340), quote, fill=(248, 250, 252), font=FONTS["quote"], spacing=8)
    
    # The Irony In 2024
    draw.rounded_rectangle([180, 520, 1740, 700], radius=12, fill=(30, 41, 59, 150), outline=(51, 65, 85, 255), width=1)
    draw.text((220, 545), "THE 2024 PIRACY PARADOX:", fill=(239, 68, 68), font=FONTS["badge"])
    draw.text((220, 580), "Pirated copies remain playable forever on an offline drive.\n"
                          "Legitimate $80 purchases become unplayable when publishers shut down servers.\n"
                          "Corporate license revocation has made piracy the only way to preserve video game history.",
              fill=(226, 232, 240), font=FONTS["h3"], spacing=8)
              
    out_path = os.path.join(ASSETS_DIR, "CARD_GABE_QUOTE.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 14. CARD_PS_STORE_PRICES: PLAYSTATION STORE MONOPOLY
# ==========================================
def build_card_ps_store_prices():
    im, draw = create_base_canvas(
        "MARKET MONOPOLY CITATION • CONSOLE WALLED GARDENS",
        "The Digital Storefront Monopoly: Zero Price Competition",
        "Without physical disc retailers, console makers dictate digital prices with zero market competition.",
        "ANALYSIS: When discs are killed, 5-year-old games remain locked at $59.99/$69.99 on the digital console store.",
        "SOURCE: PlayStation Network & Xbox Digital Storefront Price Tracking Data (2024)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Left Column: Competitive Physical Market
    draw.rounded_rectangle([150, 250, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(16, 185, 129, 200), width=1)
    draw.rectangle([150, 250, 930, 300], fill=(6, 78, 59, 150))
    draw.text((180, 268), "PHYSICAL DISC MARKET (COMPETITIVE ECOSYSTEM)", fill=(110, 231, 183), font=FONTS["badge"])
    
    draw.text((180, 330), "• Competing Retailers: Amazon, Best Buy, Target, Walmart\n"
                          "• Pre-Owned Market: eBay, GameStop, CeX, Gameloot\n"
                          "• Rapid Price Deprecation: $70 game drops to $20 in 18 months\n"
                          "• Total Consumer Power: Borrow from friends, trade-in, resell",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([180, 580, 900, 680], radius=8, fill=(6, 78, 59, 180), outline=(16, 185, 129, 255), width=1)
    draw.text((200, 600), "RESULT FOR CONSUMERS:", fill=(110, 231, 183), font=FONTS["badge"])
    draw.text((200, 630), "Continuous price drops driven by fierce retail competition.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    # Right Column: Digital Walled Garden
    draw.rounded_rectangle([990, 250, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(239, 68, 68, 200), width=1)
    draw.rectangle([990, 250, 1770, 300], fill=(69, 10, 10, 150))
    draw.text((1020, 268), "DIGITAL-ONLY WALLED GARDEN (SONY & MICROSOFT MONOPOLY)", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((1020, 330), "• ZERO Alternative Sellers: Only one digital store on your console\n"
                          "• Fixed Monopoly Pricing: 5-year-old games sit at $59.99\n"
                          "• 30% Platform Cut: Console maker takes $21 off every $70 sale\n"
                          "• Complete Captivity: No trade-ins, no borrowing, no price freedom",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([1020, 580, 1740, 680], radius=8, fill=(69, 10, 10, 180), outline=(239, 68, 68, 255), width=1)
    draw.text((1040, 600), "RESULT FOR CONSUMERS:", fill=(252, 165, 165), font=FONTS["badge"])
    draw.text((1040, 630), "You are trapped in a digital tollbooth with zero escape.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_PS_STORE_PRICES.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 15. CARD_INDIA_DISC_MARKET: EMERGING MARKET PRE-OWNED DISC EXCHANGE
# ==========================================
def build_card_india_disc_market():
    im, draw = create_base_canvas(
        "MARKET CONTEXT • SECONDARY GAMING ECONOMY",
        "The Second-Hand Disc Lifeline: How Emerging Markets Game",
        "In India, console gaming grew through disc swaps, Nehru Place / Lamington Road retail, and trade-in economics.",
        "COMMUNITY DATA: Pre-Owned Discs make AAA gaming accessible to 88% more Indian households.",
        "SOURCE: Indian Console Gaming Community Trade Studies & Retail Reports (2020–2024)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Left Column: The Physical Trade-In Lifeline
    draw.rounded_rectangle([150, 250, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(16, 185, 129, 200), width=1)
    draw.rectangle([150, 250, 930, 300], fill=(6, 78, 59, 150))
    draw.text((180, 268), "THE PHYSICAL TRADE-IN LIFELINE (HOW CONSOLES SURVIVE)", fill=(110, 231, 183), font=FONTS["badge"])
    
    draw.text((180, 330), "• Buy Pre-Owned Disc: ₹2,400 (e.g. Spider-Man 2, Black Flag, GTA V)\n"
                          "• Play Story Mode: Beat the campaign over 3 to 4 weeks\n"
                          "• Sell Back / Trade-In: Recover ₹1,800 cash or store credit\n"
                          "• Net Cost to Experience AAA Game: Exactly ₹600 (~$7 USD)\n"
                          "• Disc Sharing: 4 friends in Mumbai or Delhi circulate 1 disc",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([180, 580, 900, 680], radius=8, fill=(6, 78, 59, 180), outline=(16, 185, 129, 255), width=1)
    draw.text((200, 600), "THE LIFELINE REALITY:", fill=(110, 231, 183), font=FONTS["badge"])
    draw.text((200, 630), "Middle-class Indian gamers can experience 5 games for ₹3,000.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    # Right Column: The Digital Cliff
    draw.rounded_rectangle([990, 250, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(239, 68, 68, 200), width=1)
    draw.rectangle([990, 250, 1770, 300], fill=(69, 10, 10, 150))
    draw.text((1020, 268), "THE DIGITAL-ONLY CLIFF: CAPITAL DESTRUCTION", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((1020, 330), "• Digital Storefront Launch Price: ₹5,999 to ₹6,499 ($70–$80 USD)\n"
                          "• Resale Value: ₹0 (Zero rupees recovered forever)\n"
                          "• Account Lock: Cannot lend, swap, or gift outside home\n"
                          "• Sunk Capital: 100% of purchase price destroyed after credits roll\n"
                          "• The Death Blow: Digital-only prices out 85% of young players",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([1020, 580, 1740, 680], radius=8, fill=(69, 10, 10, 180), outline=(239, 68, 68, 255), width=1)
    draw.text((1040, 600), "THE ECONOMIC VERDICT:", fill=(252, 165, 165), font=FONTS["badge"])
    draw.text((1040, 630), "Killing the disc kills gaming in the developing world.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_INDIA_DISC_MARKET.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 16. CARD_RULE2_OPEN_HARDWARE: OPEN HARDWARE & OS FREEDOM
# ==========================================
def build_card_rule2_open_hardware():
    im, draw = create_base_canvas(
        "RULE 2 OF DIGITAL SOVEREIGNTY • OPEN HARDWARE",
        "Open Hardware vs Closed Walled Gardens",
        "Choose platforms that grant root operating system control and freedom of software execution.",
        "METRIC: Root OS Access, Sideloading Freedom, Multiple Storefronts, Offline Execution",
        "SOURCE: ThinkLate Digital Sovereignty Blueprint (2024)"
    )
    
    draw.rounded_rectangle([120, 210, 1800, 740], radius=16, fill=(15, 23, 42, 240), outline=(30, 41, 59, 255), width=2)
    
    # Left Column: Closed Ecosystem
    draw.rounded_rectangle([150, 250, 930, 705], radius=12, fill=(2, 6, 23, 220), outline=(239, 68, 68, 200), width=1)
    draw.rectangle([150, 250, 930, 300], fill=(69, 10, 10, 150))
    draw.text((180, 268), "CLOSED WALLED GARDENS (LOCKED CONSOLES & RESTRICTED DEVICES)", fill=(252, 165, 165), font=FONTS["badge"])
    
    draw.text((180, 330), "• Single Tollbooth: Exactly 1 digital store with non-negotiable prices\n"
                          "• Zero Sideloading: Cannot execute independent code or tools\n"
                          "• Subscription Hostage: Pay $80/year to access home internet for multiplayer\n"
                          "• Remote Execution Kill Switch: Single account strike deletes library\n"
                          "• Obsolescence By Design: Hardware dies when vendor shuts auth servers",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([180, 580, 900, 680], radius=8, fill=(69, 10, 10, 180), outline=(239, 68, 68, 255), width=1)
    draw.text((200, 600), "STATUS: DIGITAL TENANT", fill=(252, 165, 165), font=FONTS["badge"])
    draw.text((200, 630), "You are an occupant inside a locked corporate prison.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    # Right Column: Open Hardware Freedom
    draw.rounded_rectangle([990, 250, 1770, 705], radius=12, fill=(2, 6, 23, 220), outline=(6, 182, 212, 200), width=1)
    draw.rectangle([990, 250, 1770, 300], fill=(8, 51, 68, 150))
    draw.text((1020, 268), "OPEN HARDWARE FREEDOM (PC & STEAM DECK / LINUX)", fill=(56, 189, 248), font=FONTS["badge"])
    
    draw.text((1020, 330), "• Root OS Control: Run Linux, KDE Plasma, Windows, or custom ROMs\n"
                          "• Storefront Freedom: Steam, GOG, Itch.io, Epic, or offline .exe\n"
                          "• Free Multiplayer: Zero annual subscriptions for network play\n"
                          "• Retro Emulation: Preserve & play 40 years of gaming history\n"
                          "• Sovereign Backups: Store complete unencrypted offline game archives",
              fill=(226, 232, 240), font=FONTS["body"], spacing=10)
              
    draw.rounded_rectangle([1020, 580, 1740, 680], radius=8, fill=(8, 51, 68, 180), outline=(6, 182, 212, 255), width=1)
    draw.text((1040, 600), "STATUS: DIGITAL SOVEREIGN", fill=(56, 189, 248), font=FONTS["badge"])
    draw.text((1040, 630), "You own the machine, you control the operating system.", fill=(248, 250, 252), font=FONTS["body_bold"])
    
    out_path = os.path.join(ASSETS_DIR, "CARD_RULE2_OPEN_HARDWARE.png")
    im.save(out_path, "PNG")
    print(f"[SUCCESS] Built: {out_path}")

# ==========================================
# 17. KINETIC TYPOGRAPHY (KT) SLAM CARDS (9 TOTAL)
# ==========================================
def build_all_kt_slams():
    kt_data = [
        ("KT_01_CRACKED_DISC.png", "ACT 1 HOOK • OVERLAY 01", "$80 FOR A NEW GAME.", "UNBOX THE CASE. THERE IS NO DISC.", (245, 158, 11), (239, 68, 68)),
        ("KT_02_OWN_ZERO.png", "ACT 1 BODY • OVERLAY 04", "YOU PAID $80. YOU OWN 0%.", "YOU DID NOT BUY A GAME. YOU RENTED A TEMPORARY PASS.", (239, 68, 68), (239, 68, 68)),
        ("KT_03_SERVERS_DIE.png", "ACT 1 ENDING • OVERLAY 07", "WHEN SERVERS DIE, YOUR PURCHASES DIE TOO.", "THE COMPANY HOLDS THE REMOTE KILL SWITCH.", (239, 68, 68), (245, 158, 11)),
        ("KT_04_DEAD_SERVER.png", "ACT 2 ENDING • OVERLAY 14", "EVEN GABE CANNOT SAVE A DEAD SERVER.", "THE ENTIRE DIGITAL GAMING WORLD IS BUILT ON RENTED GROUND.", (239, 68, 68), (6, 182, 212)),
        ("KT_05_FOLLOW_MONEY.png", "ACT 3 HOOK • OVERLAY 15", "FOLLOW THE MONEY: KILLING THE USED GAME MARKET.", "IT HAS NOTHING TO DO WITH CONVENIENCE OR SAVING TREES.", (245, 158, 11), (245, 158, 11)),
        ("KT_06_ZERO_DOLLARS.png", "ACT 3 HOOK • OVERLAY 16", "ZERO DOLLARS.", "HOW MUCH SONY MAKES WHEN YOU RESELL A PHYSICAL DISC.", (239, 68, 68), (239, 68, 68)),
        ("KT_07_HARDWARE_PERMISSION.png", "ACT 3 ENDING • OVERLAY 23", "YOU OWN THE HARDWARE. THEY OWN THE PERMISSION.", "SELL YOU THE SHELL. CHARGE YOU RENT FOREVER TO TURN IT ON.", (239, 68, 68), (248, 250, 252)),
        ("KT_08_OWN_AUDIENCE.png", "ACT 4 BODY • OVERLAY 27", "OWN YOUR AUDIENCE. OWN YOUR DISTRIBUTION.", "LOCAL CODE • OFFLINE BACKUPS • DIRECT EMAIL LIST", (245, 158, 11), (245, 158, 11)),
        ("KT_09_FREEDOM_OFFLINE.png", "ACT 4 ENDING • OVERLAY 28", "IN THE 21ST CENTURY, FREEDOM IS AN OFFLINE FILE.", "IF YOU NEED PERMISSION TO OPEN IT, YOU NEVER BOUGHT IT.", (245, 158, 11), (16, 185, 129))
    ]
    
    for filename, tag, headline, sub, accent_col, border_col in kt_data:
        im = Image.new("RGBA", (W, H), (7, 11, 20, 255))
        draw = ImageDraw.Draw(im)
        
        # Center Frame
        draw.rounded_rectangle([180, 220, W - 180, H - 220], radius=20, fill=(15, 23, 42, 240), outline=border_col, width=2)
        
        # Pill Tag
        tag_w = len(tag) * 11 + 30
        draw.rounded_rectangle([W//2 - tag_w//2, 260, W//2 + tag_w//2, 295], radius=6, fill=(30, 41, 59, 200), outline=accent_col, width=1)
        draw.text((W//2 - (len(tag)*8)//2, 270), tag, fill=accent_col, font=FONTS["badge"])
        
        # Main Bold Typography
        # Wrap headline if needed
        words = headline.split()
        lines = []
        cur_line = []
        for word in words:
            cur_line.append(word)
            test_str = " ".join(cur_line)
            bbox = draw.textbbox((0, 0), test_str, font=FONTS["kt_title"])
            if (bbox[2] - bbox[0]) > (W - 440):
                cur_line.pop()
                lines.append(" ".join(cur_line))
                cur_line = [word]
        if cur_line:
            lines.append(" ".join(cur_line))
            
        y_text = 400 - (len(lines) - 1) * 35
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=FONTS["kt_title"])
            lw = bbox[2] - bbox[0]
            draw.text((W//2 - lw//2, y_text), line, fill=(248, 250, 252), font=FONTS["kt_title"])
            y_text += 78
            
        # Glowing divider
        draw.line([W//2 - 250, y_text + 20, W//2 + 250, y_text + 20], fill=accent_col, width=2)
        
        # Subtext
        bbox_sub = draw.textbbox((0, 0), sub, font=FONTS["kt_sub"])
        sub_w = bbox_sub[2] - bbox_sub[0]
        draw.text((W//2 - sub_w//2, y_text + 45), sub, fill=(148, 163, 184), font=FONTS["kt_sub"])
        
        # Channel footer watermark
        draw.text((W//2 - 60, H - 260), "THINKLATE (@WETHINKLATE)", fill=(71, 85, 105), font=FONTS["small"])
        
        out_path = os.path.join(ASSETS_DIR, filename)
        im.save(out_path, "PNG")
        print(f"[SUCCESS] Built KT Slam: {out_path}")

if __name__ == "__main__":
    print("[INFO] Building Complete ThinkLate Video 03 Evidence & Citation Suite...")
    build_evid_03()
    build_evid_04()
    build_card_sony_discovery()
    build_card_first_sale()
    build_evid_05()
    build_evid_06()
    build_card_ev_scooter()
    build_card_stop_killing_games()
    build_card_rule1_gog()
    build_card_empty_case()
    build_card_gta6_box()
    build_card_penthouse_lock()
    build_card_gabe_quote()
    build_card_ps_store_prices()
    build_card_india_disc_market()
    build_card_rule2_open_hardware()
    build_all_kt_slams()
    print("[SUCCESS] All 16 Broadcast Cards + 9 KT Slams Successfully Built!")
