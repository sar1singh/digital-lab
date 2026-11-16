"""
ThinkLate Video 2 Graphic Asset Generator
Generates High-DPI 1080p Evidence Cards, Kinetic Typography Plates,
Lower-Third Citations, and the YouTube Thumbnail for 'The 100% Debt Paradox'.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\assets"
BRAND_DIR  = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\brand"
FONTS_DIR  = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

FONT_BOLD = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG  = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO = os.path.join(FONTS_DIR, 'consola.ttf')
FONT_IMPACT = os.path.join(FONTS_DIR, 'impact.ttf')

# Brand Color Tokens
BG_DARK    = (8, 12, 20, 255)      # #080C14
CARD_BG    = (15, 22, 38, 240)     # #0F1626
BORDER_COL = (30, 44, 72, 255)     # #1E2C48
GOLD       = (245, 158, 11, 255)   # #F59E0B
CYAN       = (6, 182, 212, 255)    # #06B6D4
RED        = (239, 68, 68, 255)    # #EF4444
WHITE      = (241, 245, 249, 255)  # #F1F5F9
MUTED      = (148, 163, 184, 255)  # #94A3B8

def create_card_canvas():
    """Create a 1920x1080 transparent canvas."""
    return Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))

def draw_evidence_card(filename, title, subtitle, rows, highlight_note=None, color_accent=GOLD):
    """Draw a clean right-aligned evidence card (1920x1080 transparent overlay)."""
    img = create_card_canvas()
    draw = ImageDraw.Draw(img)

    # Card dimensions: right 45% (width 780, height 700)
    card_x0, card_y0 = 1040, 190
    card_x1, card_y1 = 1820, 890

    # Drop shadow
    shadow = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([card_x0 - 4, card_y0 + 10, card_x1 + 10, card_y1 + 18], radius=24, fill=(0, 0, 0, 140))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)

    # Card Background & Border
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=20, fill=CARD_BG, outline=BORDER_COL, width=2)

    # Header Accent bar
    draw.rounded_rectangle([card_x0 + 40, card_y0 + 40, card_x0 + 48, card_y0 + 100], radius=4, fill=color_accent)

    # Title & Subtitle
    font_title = ImageFont.truetype(FONT_BOLD, 36)
    font_sub   = ImageFont.truetype(FONT_MONO, 18)
    draw.text((card_x0 + 64, card_y0 + 38), title, font=font_title, fill=WHITE)
    draw.text((card_x0 + 64, card_y0 + 82), subtitle.upper(), font=font_sub, fill=color_accent)

    # Divider
    draw.line([card_x0 + 40, card_y0 + 120, card_x1 - 40, card_y0 + 120], fill=BORDER_COL, width=1)

    # Rows of data
    curr_y = card_y0 + 145
    font_label = ImageFont.truetype(FONT_REG, 20)
    font_val   = ImageFont.truetype(FONT_BOLD, 32)
    font_sub_v = ImageFont.truetype(FONT_REG, 16)

    for item in rows:
        label, value, subtext = item[0], item[1], item[2] if len(item) > 2 else ""
        draw.text((card_x0 + 40, curr_y), label, font=font_label, fill=MUTED)
        draw.text((card_x0 + 40, curr_y + 26), value, font=font_val, fill=WHITE)
        if subtext:
            draw.text((card_x0 + 40, curr_y + 68), subtext, font=font_sub_v, fill=color_accent)
            curr_y += 115
        else:
            curr_y += 95
        draw.line([card_x0 + 40, curr_y - 12, card_x1 - 40, curr_y - 12], fill=(25, 36, 60, 180), width=1)

    if highlight_note:
        font_note = ImageFont.truetype(FONT_MONO, 16)
        draw.rounded_rectangle([card_x0 + 40, card_y1 - 75, card_x1 - 40, card_y1 - 25], radius=8, fill=(10, 16, 28, 220), outline=BORDER_COL, width=1)
        draw.text((card_x0 + 56, card_y1 - 62), f">> {highlight_note}", font=font_note, fill=color_accent)

    out_path = os.path.join(ASSETS_DIR, filename)
    img.save(out_path, "PNG")
    print(f"Generated Evidence Card: {filename}")

def draw_kinetic_typography(filename, text_lines, color_accent=GOLD, kicker="THINKLATE INTEL"):
    """Generate bold, high-contrast Kinetic Typography plate (1920x1080)."""
    img = Image.new('RGBA', (1920, 1080), (8, 12, 20, 240))
    draw = ImageDraw.Draw(img)

    # Subtle background grid & gradient lines
    for y in range(0, 1080, 80):
        draw.line([0, y, 1920, y], fill=(15, 24, 40, 60), width=1)

    # Kicker
    font_kicker = ImageFont.truetype(FONT_MONO, 22)
    k_w = draw.textlength(kicker, font=font_kicker)
    draw.rounded_rectangle([960 - (k_w//2) - 20, 320, 960 + (k_w//2) + 20, 365], radius=6, fill=(15, 26, 45, 255), outline=color_accent, width=1)
    draw.text((960 - (k_w//2), 332), kicker, font=font_kicker, fill=color_accent)

    # Big Impact Lines
    font_main = ImageFont.truetype(FONT_IMPACT, 72)
    total_h = len(text_lines) * 90
    start_y = 500 - (total_h // 2)

    for i, line in enumerate(text_lines):
        line_w = draw.textlength(line, font=font_main)
        # Drop shadow
        draw.text((960 - (line_w // 2) + 4, start_y + (i * 90) + 4), line, font=font_main, fill=(0, 0, 0, 180))
        # Text fill (alternate accent on last line if multiple)
        fill_col = color_accent if i == len(text_lines) - 1 else WHITE
        draw.text((960 - (line_w // 2), start_y + (i * 90)), line, font=font_main, fill=fill_col)

    out_path = os.path.join(ASSETS_DIR, filename)
    img.save(out_path, "PNG")
    print(f"Generated Kinetic Typography: {filename}")

def draw_lower_third(filename, source_name, details):
    """Draw clean broadcast lower-third citation (Track 5 overlay)."""
    img = create_card_canvas()
    draw = ImageDraw.Draw(img)

    x0, y0 = 120, 920
    x1, y1 = 1100, 1010

    # Drop shadow
    shadow = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([x0 - 2, y0 + 4, x1 + 4, y1 + 6], radius=10, fill=(0, 0, 0, 120))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)

    # Background plate
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=(12, 18, 30, 245), outline=BORDER_COL, width=1)
    # Accent indicator
    draw.rounded_rectangle([x0 + 12, y0 + 14, x0 + 18, y1 - 14], radius=3, fill=GOLD)

    font_src = ImageFont.truetype(FONT_BOLD, 22)
    font_det = ImageFont.truetype(FONT_MONO, 16)

    draw.text((x0 + 34, y0 + 18), source_name, font=font_src, fill=WHITE)
    draw.text((x0 + 34, y0 + 54), details, font=font_det, fill=CYAN)

    out_path = os.path.join(ASSETS_DIR, filename)
    img.save(out_path, "PNG")
    print(f"Generated Lower Third: {filename}")

def generate_youtube_thumbnail():
    """Generate high-CTR 1280x720 YouTube Thumbnail."""
    thumb = Image.new('RGBA', (1280, 720), (8, 12, 20, 255))
    draw = ImageDraw.Draw(thumb)

    # Background mood glow
    for r in range(400, 0, -20):
        alpha = int(25 * (1 - r / 400))
        draw.ellipse([700 - r, 360 - r, 700 + r, 360 + r], fill=(239, 68, 68, alpha))

    # Add master avatar if present
    avatar_path = os.path.join(BRAND_DIR, "00_MASTER_avatar.png")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA")
        # Scale avatar to fit left side
        av = av.resize((540, 540), Image.Resampling.LANCZOS)
        thumb.paste(av, (40, 140), av)

    # Right side typography
    font_badge = ImageFont.truetype(FONT_MONO, 22)
    font_num   = ImageFont.truetype(FONT_IMPACT, 102)
    font_hook  = ImageFont.truetype(FONT_IMPACT, 68)

    # Top Tag
    draw.rounded_rectangle([590, 110, 830, 155], radius=6, fill=RED)
    draw.text((615, 120), "OFFICIAL 2026", font=font_badge, fill=WHITE)

    # Huge $40.1 TRILLION
    draw.text((594, 184), "$40.1 TRILLION", font=font_num, fill=(0, 0, 0, 200))
    draw.text((590, 180), "$40.1 TRILLION", font=font_num, fill=RED)

    # Second Hook Line
    draw.text((594, 304), "THE 100% DEBT CON", font=font_hook, fill=(0, 0, 0, 200))
    draw.text((590, 300), "THE 100% DEBT CON", font=font_hook, fill=GOLD)

    # Sub-kicker
    font_sub = ImageFont.truetype(FONT_BOLD, 28)
    draw.text((590, 400), "WHY SAVERS LOSE EVERYTHING.", font=font_sub, fill=WHITE)

    out_path = os.path.join(ASSETS_DIR, "thumbnail_video02_40t_debt.png")
    thumb.save(out_path, "PNG")
    print(f"Generated YouTube Thumbnail: thumbnail_video02_40t_debt.png")

if __name__ == '__main__':
    print("=== GENERATING THINKLATE VIDEO 2 GRAPHIC ASSETS ===")
    os.makedirs(ASSETS_DIR, exist_ok=True)

    # 1. Evidence Cards
    draw_evidence_card(
        "card_act1_realestate_paradox.png",
        "The Housing Paradox",
        "Asset Pricing Distortion",
        [
            ("Gurgaon / Manhattan Condos", "$15,000,000 USD", "400 AQI Smog / Concrete Gridlock"),
            ("European Chateau (500-yr old)", "$15,000,000 USD", "Stone Towers, Moats, Historic Acreage"),
            ("Market Reality", "Supply/Demand Broken", "Capital Pools in Liquid Assets")
        ],
        highlight_note="Diluted capital pools into urban penthouses",
        color_accent=GOLD
    )

    draw_evidence_card(
        "card_act2_debt_benchmarks.png",
        "The Global Debt Ledger",
        "Verified 2026 Sovereign Data",
        [
            ("Total Global Debt", "$365 Trillion", ">311% of Global GDP (IIF Record)"),
            ("United States Debt", "$40.10 Trillion", "Breached Milestone in 2026"),
            ("Annual Net Interest", ">$1.0 Trillion / yr", "Surpasses Total US Defense Budget"),
            ("Japan Debt-to-GDP", "~260%", "Central Bank Artificially Anchored")
        ],
        highlight_note="Sources: US Treasury, CBO, IIF Global Monitor",
        color_accent=RED
    )

    draw_evidence_card(
        "card_act3_denarius_purity.png",
        "Roman Coin Debasement",
        "The 3rd Century AD Silver Collapse",
        [
            ("Augustan Era (1st Century)", "90%+ Pure Silver", "Universal Mediterranean Trust"),
            ("Crisis Era (270 AD)", "<5% Silver Alloy", "Diluted with Cheap Copper & Zinc"),
            ("Real-World Consequence", "Baker Charged 10x", "Same count of coins, 1/10th the bread")
        ],
        highlight_note="Empires dilute currency before they fall",
        color_accent=CYAN
    )

    draw_evidence_card(
        "card_act4_institutional_housing.png",
        "The Institutional Land Grab",
        "2020-2022 Central Bank Credit Flow",
        [
            ("Single-Family Home Buyouts", "300,000+ Homes", "Acquired by Private Equity in 2021 Alone"),
            ("Cost of Borrowing (Mega-funds)", "Near-Zero Interest", "Unmatched Capital Advantage"),
            ("First-Time Homebuyers", "Systematically Outbid", "Competing against Fed-Funded Giants")
        ],
        highlight_note="Money flows up. Inflation flows down.",
        color_accent=GOLD
    )

    draw_evidence_card(
        "card_act5_median_home_vs_income.png",
        "The Generational Divide",
        "Median Home Price to Median Income",
        [
            ("1970 (Single Income)", "3.2x Annual Salary", "Modest desk job easily bought family plot"),
            ("2026 (Elite Tech Talent)", "7.8x - 11.5x Salary", "Top engineers priced out of land"),
            ("Purchasing Power", "-64% Human Labor Value", "Human sweat buys less physical reality")
        ],
        highlight_note="Resolution: Stop swimming. Build a boat.",
        color_accent=CYAN
    )

    # 2. Kinetic Typography Plates
    draw_kinetic_typography("kt_act1_what_if_nation.png", ["BUT WHAT HAPPENS", "WHEN A NATION DOES IT?"], color_accent=CYAN)
    draw_kinetic_typography("kt_act1_debt_con.png", ["THE 100% DEBT CON", "THE RIGGED PARADOX"], color_accent=GOLD)
    draw_kinetic_typography("kt_act2_villain_dilution.png", ["THE VILLAIN", "IS DILUTION."], color_accent=RED)
    draw_kinetic_typography("kt_act2_who_touches_first.png", ["WHO TOUCHES THE", "MONEY FIRST?"], color_accent=GOLD)
    draw_kinetic_typography("kt_act3_same_coins_half_meal.png", ["SAME COUNT OF COINS.", "HALF THE MEAL."], color_accent=RED)
    draw_kinetic_typography("kt_act3_cantillon_effect.png", ["CANTILLON EFFECT:", "WHO GETS IT FIRST?"], color_accent=CYAN)
    draw_kinetic_typography("kt_act3_same_con.png", ["SAME CON.", "DIFFERENT MILLENNIUM."], color_accent=GOLD)
    draw_kinetic_typography("kt_act4_trillions_created.png", ["TRILLIONS CREATED", "FROM NOTHING."], color_accent=CYAN)
    draw_kinetic_typography("kt_act4_money_flows_up.png", ["CHEAP CASH FLOWS UP.", "INFLATION FLOWS DOWN."], color_accent=RED)
    draw_kinetic_typography("kt_act4_startup_dies.png", ["THE TECH OUTFIT DIES.", "THE PLANT WINS."], color_accent=GOLD)
    draw_kinetic_typography("kt_act5_own_tangible_assets.png", ["ACQUIRE", "TANGIBLE ASSETS."], color_accent=CYAN)
    draw_kinetic_typography("kt_act5_build_a_boat.png", ["STOP SWIMMING.", "BUILD A BOAT."], color_accent=GOLD)

    # 3. Lower Third Citations
    draw_lower_third("lt_us_treasury.png", "U.S. DEPARTMENT OF THE TREASURY", "Fiscal Data & Congressional Budget Office (CBO) 2026")
    draw_lower_third("lt_peterson_foundation.png", "PETER G. PETERSON FOUNDATION", "Net Annual Interest Exceeds National Defense Budget ($1.05T)")
    draw_lower_third("lt_iif_global.png", "INSTITUTE OF INTERNATIONAL FINANCE", "Global Debt Monitor: Worldwide Debt Exceeds $365 Trillion")
    draw_lower_third("lt_roman_debasement.png", "HISTORICAL EVIDENCE: ROMAN EMPIRE", "Antoninianus & Denarius Debasement (Caracalla to Gallienus)")
    draw_lower_third("lt_cantillon_essay.png", "RICHARD CANTILLON (1730)", "Essay on the Nature of Commerce in General: Money Injection Mechanics")

    # 4. YouTube Thumbnail
    generate_youtube_thumbnail()

    print("\nAll Video 2 Visual Assets Generated Successfully!")
