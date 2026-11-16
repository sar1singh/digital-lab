"""
ThinkLate Video 04: Kinetic Typography & UI Evidence Badge Generator
Renders high-DPI transparent PNG cards (1920x1080) for Track 4 typography slams.
Adheres strictly to the Cinematic Graphic Noir color token standard.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\brand_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_BOLD = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG  = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO = os.path.join(FONTS_DIR, 'consola.ttf')

# Brand Color Tokens
GOLD   = (245, 158, 11, 255)   # #F59E0B
CYAN   = (6, 182, 212, 255)    # #06B6D4
RED    = (239, 68, 68, 255)    # #EF4444
WHITE  = (241, 245, 249, 255)  # #F1F5F9
MUTED  = (148, 163, 184, 255)  # #94A3B8
CARD_BG = (12, 18, 32, 230)    # #0C1220 (90% alpha)
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

    # Estimate height
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
        # Drop shadow
        draw.rounded_rectangle([bx - 2, start_y + 2, bx + bw + 2, start_y + bh + 4], radius=8, fill=(0, 0, 0, 160))
        draw.rounded_rectangle([bx, start_y, bx + bw, start_y + bh], radius=8, fill=accent_color)
        draw.text((bx + 16, start_y + 8), badge.upper(), font=font_badge, fill=(8, 12, 20, 255))
        start_y += bh + 24

    # Headline with high-contrast shadow
    h_bbox = draw.textbbox((0, 0), headline, font=font_head)
    hx = (1920 - (h_bbox[2] - h_bbox[0])) // 2

    # Shadow
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
    """Render a broadcast-style lower-left or lower-center evidence card."""
    img = make_canvas()
    draw = ImageDraw.Draw(img)

    card_w, card_h = 1000, 260
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
    print("Generating Video 04 Kinetic Typography & UI Badges...")

    cards = [
        # Cue 01
        ("card_cue01_60k_car.png", "center", {"headline": "THE $60,000 CAR", "subtext": "FROZEN AT DAWN", "accent_color": WHITE}),
        # Cue 02
        ("card_cue02_global_rollout.png", "lower", {"badge": "GLOBAL ROLLOUT", "headline": "UK • GERMANY • SOUTH AFRICA", "body_items": ["BMW ConnectedDrive Feature-on-Demand"], "accent_color": CYAN}),
        # Cue 04
        ("card_cue04_bolted_factory.png", "center", {"headline": "BOLTED AT THE FACTORY", "subtext": "COPPER • RELAYS • SWITCHES ALREADY INSTALLED", "accent_color": GOLD}),
        # Cue 05
        ("card_cue05_cloud_lock.png", "lower", {"badge": "CLOUD LOCK", "headline": "\"NOT UNLESS YOUR CARD BILLS\"", "body_items": ["Remotely Disabled via Over-the-Air Telematics"], "accent_color": RED}),
        # Cue 06
        ("card_cue06_hostage_seat.png", "center", {"headline": "A HOSTAGE IN YOUR SEAT", "subtext": "Hardware You Paid For. Software You Must Rent.", "accent_color": RED}),
        # Cue 08
        ("card_cue08_not_a_prank.png", "center", {"headline": "IT WAS NOT A PRANK", "subtext": "IT WAS A TEST OF CUSTOMER COMPLIANCE", "accent_color": GOLD}),
        # Cue 10
        ("card_cue10_overnight_brick.png", "lower", {"badge": "OVERNIGHT BRICK", "headline": "THIRD-PARTY INK BLOCKED", "body_items": ["Dynamic Security Firmware Update Dispatched Worldwide"], "accent_color": RED}),
        # Cue 11
        ("card_cue11_audits_ink.png", "center", {"headline": "YOU BOUGHT A PRINTER", "subtext": "THAT AUDITS YOUR INK SUPPLY DAILY", "accent_color": CYAN}),
        # Cue 12
        ("card_cue12_fine_penalty.png", "lower", {"badge": "REGULATORY PENALTY", "headline": "€10,000,000 FINE", "body_items": ["Italian Antitrust Authority (AGCM) Ruling Against HP"], "accent_color": GOLD}),
        # Cue 14
        ("card_cue14_hp_investment.png", "center", {"headline": "\"A PRINTER IS AN INVESTMENT FOR HP\"", "subtext": "HP CEO Enrique Lores on CNBC Squawk Box", "accent_color": GOLD}),
        # Cue 15
        ("card_cue15_cheap_ink_target.png", "center", {"headline": "CHEAP INK = BAD INVESTMENT", "subtext": "YOU ARE THE SUBSCRIPTION ASSET", "accent_color": RED}),
        # Cue 16
        ("card_cue16_cold_seat_tractor.png", "center", {"headline": "A COLD SEAT IS AN INSULT", "subtext": "A FROZEN TRACTOR FEEDS NOBODY", "accent_color": GOLD}),
        # Cue 17
        ("card_cue17_nebraska_testimony.png", "lower", {"badge": "LEGISLATIVE TESTIMONY", "headline": "NEBRASKA UNICAMERAL 2017", "body_items": ["Danny Kluthe Sworn Testimony on Right to Repair"], "accent_color": CYAN}),
        # Cue 18
        ("card_cue18_john_deere_trip.png", "lower", {"badge": "JOHN DEERE SERVICE CALL", "headline": "$230 TRIP CHARGE + $130/HOUR", "body_items": ["Mandatory Dealer Service Call Just to Connect Diagnostic Tool"], "accent_color": GOLD}),
        # Cue 19
        ("card_cue19_whose_tractor.png", "center", {"headline": "WHOSE TRACTOR WAS IT?", "subtext": "THE SPREADSHEET CLAIMED FULL OWNERSHIP", "accent_color": RED}),
        # Cue 21
        ("card_cue21_copyright_weapon.png", "center", {"headline": "COPYRIGHT AS A WEAPON", "subtext": "DMCA Section 1201 Used to Criminalize Basic Repairs", "accent_color": RED}),
        # Cue 22
        ("card_cue22_spreadsheet_villain.png", "center", {"headline": "NOT A VILLAIN IN A CAPE", "subtext": "A WALL STREET SPREADSHEET", "accent_color": WHITE}),
        # Cue 25
        ("card_cue25_cannot_leave.png", "center", {"headline": "A PRISONER CANNOT CANCEL", "subtext": "Hardware Lock-In Generates Guaranteed Recurring Cash Flow", "accent_color": RED}),
        # Cue 26
        ("card_cue26_valuation_surge.png", "lower", {"badge": "VALUATION MULTIPLIER", "headline": "$1.5B ➔ $6.7B OVERNIGHT", "body_items": ["From 1.5x Hardware Revenue to 6.7x SaaS Multiples"], "accent_color": GOLD}),
        # Cue 27
        ("card_cue27_ceo_scoreboard.png", "center", {"headline": "THE CEO STOCK SCOREBOARD", "subtext": "Executives Paid in Options to Liquidate Customer Ownership", "accent_color": GOLD}),
        # Cue 29
        ("card_cue29_secret_pact.png", "lower", {"badge": "THE SECRET PACT", "headline": "GENEVA • CHRISTMAS 1924", "body_items": ["Osram • Philips • General Electric • Associated Electrical"], "accent_color": CYAN}),
        # Cue 30
        ("card_cue30_livermore_bulb.png", "lower", {"badge": "CENTENNIAL LIGHT (1901)", "headline": "BURNING 120+ YEARS NON-STOP", "body_items": ["Livermore, California Fire Station • The 2,500hr Industrial Baseline"], "accent_color": GOLD}),
        # Cue 31
        ("card_cue31_phoebus_limit.png", "center", {"badge": "PHOEBUS CARTEL", "headline": "THE 1,000-HOUR MANDATE", "subtext": "Fined Heavy Penalties for Engineering Bulbs That Lasted Longer", "accent_color": RED}),
        # Cue 32
        ("card_cue32_same_incentive.png", "center", {"headline": "SAME CENTURY-OLD CON", "subtext": "Just Better Silicon and Legalese", "accent_color": WHITE}),
        # Cue 34
        ("card_cue34_job_hostage.png", "lower", {"badge": "FINANCIAL LOCKOUT", "headline": "ONE LATE EMI = PHONE BRICKED", "body_items": ["Food Delivery Rider • GPS & Order Route Instantly Disabled"], "accent_color": RED}),
        # Cue 35
        ("card_cue35_ftc_lawsuit.png", "lower", {"badge": "JUNE 2024 • DOJ & FTC ENFORCEMENT", "headline": "U.S. SUES ADOBE: ANNUAL SUBSCRIPTION TRAP", "body_items": ["Undisclosed Early Termination Fees • 50% Cancellation Penalty"], "accent_color": CYAN}),
        # Cue 36
        ("card_cue36_bmw_drops_rent.png", "center", {"headline": "SEPTEMBER 2023", "subtext": "BMW Officially Drops the Heated Seat Subscription", "accent_color": GOLD}),
        # Cue 37
        ("card_cue37_repair_wins.png", "lower", {"badge": "RIGHT TO REPAIR WINS", "headline": "COLORADO • MINNESOTA • CALIFORNIA", "body_items": ["Statutory Protections for Agricultural & Consumer Hardware"], "accent_color": CYAN}),
        # Cue 38
        ("card_cue38_one_update_lease.png", "center", {"headline": "ONE UPDATE FROM A LEASE", "subtext": "A Seat • A Printer • A Tractor", "accent_color": RED}),
        # Cue 39
        ("card_cue39_holding_key.png", "center", {"headline": "\"REMEMBER WHO HOLDS THE KEY\"", "subtext": "ThinkLate (@wethinklate)", "accent_color": GOLD}),
    ]

    for fname, ctype, kwargs in cards:
        if ctype == "center":
            p = render_center_slam(fname, **kwargs)
        else:
            p = render_lower_card(fname, **kwargs)
        print(f"Generated: {fname}")

    print(f"All {len(cards)} typography cards generated successfully in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

