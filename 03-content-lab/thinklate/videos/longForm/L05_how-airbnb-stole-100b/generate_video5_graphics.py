"""
ThinkLate Video 05: Kinetic Typography & UI Evidence Badge Generator
Renders high-DPI transparent PNG cards (1920x1080) for Track 4 typography slams.
Adheres strictly to the Cinematic Graphic Noir color token standard of Video 04.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(VIDEO_DIR, "brand_assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_BOLD = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG  = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO = os.path.join(FONTS_DIR, 'consola.ttf')

# Brand Color Tokens
GOLD   = (245, 158, 11, 255)   # #F59E0B
AMBER  = (245, 158, 11, 255)   # #F59E0B
CYAN   = (6, 182, 212, 255)    # #06B6D4
RED    = (239, 68, 68, 255)    # #EF4444
WHITE  = (241, 245, 249, 255)  # #F1F5F9
MUTED  = (148, 163, 184, 255)  # #94A3B8
LIME   = (226, 255, 0, 255)    # #E2FF00
CARD_BG = (12, 18, 32, 230)    # #0C1220 (90% alpha glassmorphism)
BORDER_COL = (30, 48, 80, 255) # #1E3050

def make_canvas():
    return Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))

def render_center_slam(filename, headline, subtext=None, badge=None, accent_color=GOLD):
    """Render a bold, cinematic center-screen typography slam with drop shadow."""
    img = make_canvas()
    draw = ImageDraw.Draw(img)

    font_badge = ImageFont.truetype(FONT_BOLD, 22)
    font_head = ImageFont.truetype(FONT_BOLD, 54)
    font_sub  = ImageFont.truetype(FONT_REG, 28)

    total_h = 100
    if badge: total_h += 50
    if subtext: total_h += 60

    start_y = (1080 - total_h) // 2

    # Draw Badge if exists
    if badge:
        bbox = draw.textbbox((0, 0), badge.upper(), font=font_badge)
        bw = bbox[2] - bbox[0] + 32
        bh = bbox[3] - bbox[1] + 16
        bx = (1920 - bw) // 2
        draw.rounded_rectangle([bx - 2, start_y + 2, bx + bw + 2, start_y + bh + 4], radius=8, fill=(0, 0, 0, 160))
        draw.rounded_rectangle([bx, start_y, bx + bw, start_y + bh], radius=8, fill=accent_color)
        draw.text((bx + 16, start_y + 8), badge.upper(), font=font_badge, fill=(8, 12, 20, 255))
        start_y += bh + 24

    # Headline with high-contrast shadow
    h_bbox = draw.textbbox((0, 0), headline, font=font_head)
    hx = (1920 - (h_bbox[2] - h_bbox[0])) // 2

    for dx, dy in [(-2, 2), (2, 2), (0, 3)]:
        draw.text((hx + dx, start_y + dy), headline, font=font_head, fill=(0, 0, 0, 200))
    draw.text((hx, start_y), headline, font=font_head, fill=WHITE)
    start_y += (h_bbox[3] - h_bbox[1]) + 20

    # Subtext if exists
    if subtext:
        s_bbox = draw.textbbox((0, 0), subtext, font=font_sub)
        sx = (1920 - (s_bbox[2] - s_bbox[0])) // 2
        draw.text((sx + 1, start_y + 2), subtext, font=font_sub, fill=(0, 0, 0, 180))
        draw.text((sx, start_y), subtext, font=font_sub, fill=MUTED)

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    return filepath

def render_lower_card(filename, badge, headline, body_items=[], accent_color=CYAN):
    """Render a broadcast-style lower-center evidence card."""
    img = make_canvas()
    draw = ImageDraw.Draw(img)

    card_w, card_h = 1040, 260
    card_x = (1920 - card_w) // 2
    card_y = 740

    # Shadow
    shadow = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([card_x - 4, card_y + 6, card_x + card_w + 6, card_y + card_h + 12], radius=16, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)

    # Card Body
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=16, fill=CARD_BG, outline=BORDER_COL, width=2)

    # Left accent vertical bar
    draw.rounded_rectangle([card_x + 28, card_y + 28, card_x + 36, card_y + card_h - 28], radius=4, fill=accent_color)

    font_badge = ImageFont.truetype(FONT_BOLD, 20)
    font_head  = ImageFont.truetype(FONT_BOLD, 36)
    font_body  = ImageFont.truetype(FONT_REG, 24)

    curr_y = card_y + 32
    if badge:
        draw.text((card_x + 56, curr_y), badge.upper(), font=font_badge, fill=accent_color)
        curr_y += 36

    draw.text((card_x + 56, curr_y), headline, font=font_head, fill=WHITE)
    curr_y += 48

    for item in body_items:
        draw.text((card_x + 56, curr_y), item, font=font_body, fill=MUTED)
        curr_y += 32

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    return filepath

def main():
    print("Generating Video 05 Kinetic Typography & UI Evidence Badges...")

    cards = [
        # --- ACT 1: THE THREE-DAY COUNTDOWN & THE AIRBED (0:00 - 2:44) ---
        ("card_cue01_overdue_rent.png", "center", {
            "badge": "OCTOBER 2007 • SAN FRANCISCO",
            "headline": "RENT: $1,150 OVERDUE",
            "subtext": "72 HOURS BEFORE POLICE EVICTION • BANK ACCOUNT: $0.00",
            "accent_color": RED
        }),
        ("card_cue02_broke_founders.png", "lower", {
            "badge": "THE DESPERATE FOUNDERS",
            "headline": "BRIAN CHESKY & JOE GEBBIA",
            "body_items": [
                "Two Unemployed Design School Graduates (RISD)",
                "Scrambling for Any Quick Cash to Survive the Weekend"
            ],
            "accent_color": GOLD
        }),
        ("card_cue03_hotels_sold_out.png", "center", {
            "badge": "IDSA DESIGN CONFERENCE",
            "headline": "HOTELS: 100% SOLD OUT",
            "subtext": "ZERO VACANCIES ACROSS SAN FRANCISCO • TOURISTS STRANDED",
            "accent_color": AMBER
        }),
        ("card_cue04_the_airbed_hustle.png", "lower", {
            "badge": "THE MAKESHIFT HUSTLE",
            "headline": "3 BLUE AIR MATTRESSES",
            "body_items": [
                "$80 a Night on the Living Room Floor",
                "Thrown-in Homemade Pop-Tarts for Breakfast"
            ],
            "accent_color": CYAN
        }),
        ("card_cue05_empire_transformation.png", "center", {
            "badge": "THE 18-YEAR TRANSFORMATION",
            "headline": "$80 AIRBED ➔ $100,000,000,000",
            "subtext": "From Desperate Rug Rental to Global Travel Empire",
            "accent_color": LIME
        }),
        ("card_cue06_solo_blueprint.png", "lower", {
            "badge": "THE FOUNDER BLUEPRINT",
            "headline": "STARTING WITH ZERO CASH",
            "body_items": [
                "3 Tactical Survival Moves to Hijack an Industry",
                "The Fatal Scaling Trap You Must Avoid After Winning"
            ],
            "accent_color": CYAN
        }),
        ("card_cue07_rent_paid_cash.png", "center", {
            "badge": "VALIDATION IN 72 HOURS",
            "headline": "$240 CASH COLLECTED",
            "subtext": "3 Guests Paid Cash • Rent Paid • The Lightbulb Moment",
            "accent_color": GOLD
        }),
        ("card_cue08_the_lightbulb.png", "lower", {
            "badge": "THE SYSTEMIC THESIS",
            "headline": "\"WHAT IF ANYONE COULD HOST?\"",
            "body_items": [
                "Unlocking Empty Living Space Across Every Major City",
                "Turning Ordinary Renters into Micro-Hoteliers"
            ],
            "accent_color": CYAN
        }),
        ("card_cue09_no_code_problem.png", "center", {
            "badge": "THE TECHNICAL BOTTLENECK",
            "headline": "NEITHER FOUNDER KNEW CODE",
            "subtext": "Industrial Designers Who Drew Sketches • Called Roommate Nate",
            "accent_color": RED
        }),
        ("card_cue10_airbed_launch.png", "lower", {
            "badge": "THE FIRST DEPLOYMENT",
            "headline": "AIRBEDANDBREAKFAST.COM",
            "body_items": [
                "3 Air Mattresses • Free Wifi • $80 Per Night",
                "Sounded Insane to Every Investor in Silicon Valley"
            ],
            "accent_color": LIME
        }),

        # --- ACT 2: THE $20,000 DEBT TRAP & THE CEREAL STUNT (2:44 - 4:19) ---
        ("card_cue11_twenty_k_debt.png", "center", {
            "badge": "THE DEBT CRUCIBLE",
            "headline": "$20,000 IN CREDIT CARD DEBT",
            "subtext": "A Baseball Card Binder of Maxed-Out Credit Cards",
            "accent_color": RED
        }),
        ("card_cue12_cereal_arbitrage.png", "lower", {
            "badge": "SUMMER 2008 • NOVELTY CEREAL STUNT",
            "headline": "1,000 BOXES: OBAMA O'S & CAP'N MCCAIN'S",
            "body_items": [
                "Production Cost: $4.00 / box (Cheerios + Cardboard)",
                "Collector Sale Price: $40.00 / box (10x Margin)",
                "Total Cash Runway Raised: $30,000 Cold Hard Cash"
            ],
            "accent_color": GOLD
        }),

        # --- ACT 3: THE Y COMBINATOR CRUCIBLE (4:19 - 6:07) ---
        ("card_cue13_paul_graham_quote.png", "center", {
            "badge": "PAUL GRAHAM • Y COMBINATOR 2009",
            "headline": "\"IF YOU CAN SELL $40 CEREAL, YOU CAN SURVIVE\"",
            "subtext": "Accepted Into Y Combinator • $20,000 Seed Investment",
            "accent_color": GOLD
        }),
        ("card_cue14_trough_of_sorrow.png", "center", {
            "badge": "THE TROUGH OF SORROW",
            "headline": "100 WEEKS AT $200 A WEEK",
            "subtext": "Growth Flatlined • Survival on Ramen and Maxed Debt",
            "accent_color": RED
        }),

        # --- ACT 4: THE BROOKLYN GROUND WAR (6:07 - 7:25) ---
        ("card_cue15_dont_scale.png", "center", {
            "badge": "THE SURVIVAL LAW",
            "headline": "DO THINGS THAT DON'T SCALE",
            "subtext": "The Answers Are Never in Code; They Are in the Kitchen",
            "accent_color": GOLD
        }),
        ("card_cue16_brooklyn_photos.png", "lower", {
            "badge": "THE BROOKLYN INTERVENTION",
            "headline": "FREE $500 DSLR PHOTOGRAPHY",
            "body_items": [
                "Replaced Dark Flip-Phone 'Crime Scene' Photos",
                "Bookings Tripled Instantly (300% Spike)",
                "Weekly Revenue Doubled to $400 / Week"
            ],
            "accent_color": CYAN
        }),

        # --- ACT 5: THE CRAIGSLIST HIJACK & VALUATION (7:25 - 9:27) ---
        ("card_cue17_craigslist_hijack.png", "lower", {
            "badge": "DISTRIBUTION ARBITRAGE",
            "headline": "THE CRAIGSLIST HIJACK",
            "body_items": [
                "Reverse-Engineered Craigslist Web Forms",
                "One-Click Cross-Posting for Airbnb Hosts",
                "Hijacked 50,000,000 Monthly Users for Exactly $0"
            ],
            "accent_color": LIME
        }),
        ("card_cue18_valuation_multiplier.png", "center", {
            "badge": "THE ASSET-LIGHT MULTIPLIER",
            "headline": "18.5x REVENUE MULTIPLE",
            "subtext": "Zero Buildings Owned • 17% Fee on Other People's Homes",
            "accent_color": LIME
        }),

        # --- ACT 6: COVID CRASH & THE $100B IPO (9:27 - 11:11) ---
        ("card_cue19_covid_collapse.png", "center", {
            "badge": "MARCH 2020 • THE NEAR-DEATH EVENT",
            "headline": "80% OF REVENUE WIPED IN 14 DAYS",
            "subtext": "$1,000,000,000 in Cash Refunds • Valuation Cut $31B ➔ $18B",
            "accent_color": RED
        }),
        ("card_cue20_nasdaq_ipo.png", "lower", {
            "badge": "DECEMBER 10, 2020 • NASDAQ: ABNB",
            "headline": "$100.8 BILLION DAY 1 MARKET CAP",
            "body_items": [
                "More Valuable Than Marriott ($44B), Hilton ($29B), and Hyatt ($7B) Combined",
                "Achieved Without Owning a Single Physical Brick"
            ],
            "accent_color": LIME
        }),

        # --- ACT 7: THE $180 CLEANING FEE TAX & CITY BANS (11:11 - 14:44) ---
        ("card_cue21_cleaning_fee_tax.png", "center", {
            "badge": "THE CONSUMER REVOLT",
            "headline": "$120 ROOM ➔ $380 FINAL BILL",
            "subtext": "$180 Cleaning Fee + Service Taxes + Laminated Chore Lists",
            "accent_color": RED
        }),
        ("card_cue22_city_bans.png", "lower", {
            "badge": "REGULATORY BACKLASH",
            "headline": "NYC & BARCELONA STRIKE BACK",
            "body_items": [
                "NYC Local Law 18: 85% of Short-Term Listings Wiped Out",
                "Barcelona: Total Ban on 10,000 Tourist Apartments by 2028"
            ],
            "accent_color": RED
        }),

        # --- ACT 8: 3 BRUTAL RULES (14:44 - 17:26) ---
        ("card_cue23_rule1.png", "center", {
            "badge": "RULE 1 FOR SOLO BUILDERS",
            "headline": "BORROW DISTRIBUTION FIRST",
            "subtext": "Never Build an Audience from Scratch When You Can Hijack an Existing Giant",
            "accent_color": GOLD
        }),
        ("card_cue24_rule2.png", "center", {
            "badge": "RULE 2 FOR SOLO BUILDERS",
            "headline": "THE ANSWER IS IN THE KITCHEN",
            "subtext": "Stop Tweaking Code in Isolation. Go Sit with Your First 10 Customers.",
            "accent_color": CYAN
        }),
        ("card_cue25_rule3.png", "center", {
            "badge": "RULE 3 FOR SOLO BUILDERS",
            "headline": "NEVER OPTIMIZE THE SOUL OUT",
            "subtext": "The Moment Wall Street Multiples Replace Hospitality, the Market Revolts.",
            "accent_color": RED
        }),
        ("card_cue26_stay_curious.png", "center", {
            "badge": "THINKLATE • CONVERSATIONAL INFOTAINMENT",
            "headline": "STAY CURIOUS. SEE YOU IN THE NEXT ONE.",
            "subtext": "@wethinklate",
            "accent_color": LIME
        })
    ]

    for fname, ctype, kwargs in cards:
        if ctype == "center":
            p = render_center_slam(fname, **kwargs)
        else:
            p = render_lower_card(fname, **kwargs)
        print(f"Generated: {fname}")

    print(f"\nAll {len(cards)} Video 05 brand graphics generated in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
