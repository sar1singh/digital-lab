"""
ThinkLate Video 2 Procedural Scene Plate Generator
Creates stunning 1080p Dark Academic Anime-Vector backdrops for all video scenes.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\assets"
BRAND_DIR  = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\brand"
FONTS_DIR  = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

FONT_BOLD   = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG    = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO   = os.path.join(FONTS_DIR, 'consola.ttf')
FONT_IMPACT = os.path.join(FONTS_DIR, 'impact.ttf')

BG_DARK     = (8, 12, 20, 255)      # #080C14
NAVY_MID    = (15, 24, 42, 255)     # #0F182A
NAVY_LIGHT  = (27, 42, 74, 255)     # #1B2A4A
GOLD        = (245, 158, 11, 255)   # #F59E0B
CYAN        = (6, 182, 212, 255)    # #06B6D4
RED         = (239, 68, 68, 255)    # #EF4444
WHITE       = (241, 245, 249, 255)  # #F1F5F9
MUTED       = (148, 163, 184, 255)  # #94A3B8

def create_base_canvas(color_top=(12, 18, 30), color_bot=(6, 10, 16)):
    """Create 1920x1080 base canvas with subtle vertical gradient & grid."""
    img = Image.new('RGBA', (1920, 1080), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # Vertical gradient
    for y in range(1080):
        t = y / 1080.0
        r = int(color_top[0] * (1 - t) + color_bot[0] * t)
        g = int(color_top[1] * (1 - t) + color_bot[1] * t)
        b = int(color_top[2] * (1 - t) + color_bot[2] * t)
        draw.line([(0, y), (1920, y)], fill=(r, g, b, 255))
        
    # Grid lines
    for x in range(0, 1920, 96):
        draw.line([(x, 0), (x, 1080)], fill=(255, 255, 255, 7), width=1)
    for y in range(0, 1080, 72):
        draw.line([(0, y), (1920, y)], fill=(255, 255, 255, 7), width=1)
        
    return img

def add_radial_glow(img, cx, cy, radius, color, max_alpha=120):
    """Add smooth atmospheric radial glow."""
    glow = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow)
    steps = 40
    for i in range(steps):
        r = int(radius * (1 - i / steps))
        alpha = int(max_alpha * (i / steps))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(color[0], color[1], color[2], alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(radius // 8))
    return Image.alpha_composite(img, glow)

def add_header_badge(draw, text, act_text, color_accent=GOLD):
    """Clean documentary header stamp."""
    font_badge = ImageFont.truetype(FONT_MONO, 18)
    font_act   = ImageFont.truetype(FONT_BOLD, 18)
    draw.rounded_rectangle([80, 50, 480, 95], radius=6, fill=(12, 18, 32, 220), outline=(30, 44, 72, 255), width=1)
    draw.rounded_rectangle([80, 50, 86, 95], radius=3, fill=color_accent)
    draw.text((102, 62), act_text.upper(), font=font_act, fill=color_accent)
    draw.text((210, 63), f"|  {text}", font=font_badge, fill=MUTED)

# --- Scene Generators ---

def gen_scene03_bank_loan():
    """Scene 03: The Bank Loan Rejection Desk."""
    img = create_base_canvas((18, 14, 22), (8, 6, 12))
    img = add_radial_glow(img, 960, 500, 700, RED, 70)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE LENDING GATE", "ACT 1", RED)
    
    # Architectural counter silhouette
    draw.rectangle([0, 760, 1920, 1080], fill=(12, 10, 18, 255), outline=(40, 20, 30, 255), width=2)
    draw.line([0, 760, 1920, 760], fill=RED, width=3)
    
    # Surveillance / barred window graphics
    for x in range(300, 1700, 240):
        draw.line([x, 200, x, 760], fill=(239, 68, 68, 25), width=2)
        
    # Dramatic Stamp
    stamp_w, stamp_h = 720, 160
    sx, sy = 600, 420
    draw.rounded_rectangle([sx - 10, sy - 10, sx + stamp_w + 10, sy + stamp_h + 10], radius=16, outline=RED, width=6)
    draw.rounded_rectangle([sx, sy, sx + stamp_w, sy + stamp_h], radius=12, fill=(40, 10, 15, 230), outline=RED, width=3)
    font_stamp = ImageFont.truetype(FONT_IMPACT, 76)
    draw.text((sx + 50, sy + 30), "LOAN APPLICATION: DENIED", font=font_stamp, fill=RED)
    
    # Subtitle
    font_sub = ImageFont.truetype(FONT_MONO, 24)
    draw.text((640, 620), "RATIO > 2.0x ANNUAL WAGE  -->  IMPOUND ASSETS", font=font_sub, fill=MUTED)
    
    img.save(os.path.join(ASSETS_DIR, "scene03_bank_loan.png"), "PNG")
    print("Generated: scene03_bank_loan.png")

def gen_scene04_podcast_studio():
    """Scene 04: The Host Introduction (Owl Avatar at Podcast Desk)."""
    img = create_base_canvas((14, 20, 35), (8, 12, 20))
    img = add_radial_glow(img, 450, 540, 600, CYAN, 80)
    img = add_radial_glow(img, 1400, 400, 500, GOLD, 60)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THINKLATE INTEL DESK", "ACT 1", GOLD)
    
    # Desk silhouette
    draw.rectangle([0, 780, 1920, 1080], fill=(12, 18, 30, 255), outline=(30, 48, 80, 255), width=2)
    draw.line([0, 780, 1920, 780], fill=CYAN, width=3)
    
    # Sound foam acoustic grid backdrop
    for x in range(900, 1850, 120):
        for y in range(180, 720, 120):
            draw.rounded_rectangle([x, y, x + 100, y + 100], radius=10, fill=(15, 24, 40, 200), outline=(25, 40, 68, 255), width=1)
            
    # Composite Master Avatar on Left (Host position)
    avatar_path = os.path.join(BRAND_DIR, "00_MASTER_avatar.png")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA")
        av = av.resize((580, 580), Image.Resampling.LANCZOS)
        img.paste(av, (160, 260), av)
        
    img.save(os.path.join(ASSETS_DIR, "scene04_podcast_studio.png"), "PNG")
    print("Generated: scene04_podcast_studio.png")

def gen_scene05_debt_mountain():
    """Scene 05: The Global Debt Mountain Exponential Graph."""
    img = create_base_canvas((16, 22, 38), (8, 10, 18))
    img = add_radial_glow(img, 1200, 480, 700, RED, 90)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "SOVEREIGN LIQUIDITY SPIRAL", "ACT 2", RED)
    
    # Coordinate system
    gx0, gy0, gx1, gy1 = 160, 820, 960, 220
    draw.line([gx0, gy0, gx1, gy0], fill=(100, 116, 139, 200), width=2)
    draw.line([gx0, gy0, gx0, gy1], fill=(100, 116, 139, 200), width=2)
    
    # Exponential Debt Curve points
    curve_points = []
    for i in range(100):
        t = i / 99.0
        x = gx0 + t * (gx1 - gx0)
        y = gy0 - (t ** 2.8) * (gy0 - gy1)
        curve_points.append((x, y))
        
    # Fill area under curve
    poly = [(gx0, gy0)] + curve_points + [(gx1, gy0)]
    poly_img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(poly_img)
    p_draw.polygon(poly, fill=(239, 68, 68, 40))
    img = Image.alpha_composite(img, poly_img)
    draw = ImageDraw.Draw(img)
    
    # Glowing stroke
    for i in range(len(curve_points) - 1):
        draw.line([curve_points[i], curve_points[i+1]], fill=RED, width=4)
        
    # Marker at the peak
    px, py = curve_points[-1]
    draw.ellipse([px - 12, py - 12, px + 12, py + 12], fill=RED, outline=WHITE, width=3)
    
    font_peak = ImageFont.truetype(FONT_IMPACT, 48)
    draw.text((px - 140, py - 60), "$365 TRILLION", font=font_peak, fill=RED)
    
    img.save(os.path.join(ASSETS_DIR, "scene05_debt_mountain.png"), "PNG")
    print("Generated: scene05_debt_mountain.png")

def gen_scene06_villain_dilution():
    """Scene 06: Dark Navy Canvas with Dissolving Currency."""
    img = create_base_canvas((18, 20, 32), (8, 10, 16))
    img = add_radial_glow(img, 960, 540, 650, RED, 70)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE INVISIBLE THEFT", "ACT 2", RED)
    
    # Concentric target lines showing wealth erosion
    for r in range(150, 700, 110):
        draw.ellipse([960 - r, 540 - r, 960 + r, 540 + r], outline=(239, 68, 68, 30), width=1)
        
    img.save(os.path.join(ASSETS_DIR, "scene06_villain_dilution.png"), "PNG")
    print("Generated: scene06_villain_dilution.png")

def gen_scene08_roman_legion():
    """Scene 08: Roman Legions & Silver Bullion."""
    img = create_base_canvas((16, 24, 38), (8, 12, 20))
    img = add_radial_glow(img, 500, 480, 600, CYAN, 80)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "ANCIENT COINAGE MONOPOLY", "ACT 3", CYAN)
    
    # Classical columns silhouette on left
    for col_x in [160, 300, 440]:
        draw.rectangle([col_x, 260, col_x + 50, 860], fill=(20, 32, 54, 255), outline=(35, 55, 90, 255), width=2)
        draw.rectangle([col_x - 15, 230, col_x + 65, 260], fill=(30, 48, 80, 255))
        draw.rectangle([col_x - 15, 860, col_x + 65, 890], fill=(30, 48, 80, 255))
        
    # Huge Silver Denarius Coin Motif
    cx, cy, cr = 680, 520, 160
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(30, 45, 70, 220), outline=CYAN, width=4)
    draw.ellipse([cx - cr + 15, cy - cr + 15, cx + cr - 15, cy + cr - 15], outline=(148, 163, 184, 120), width=2)
    font_coin = ImageFont.truetype(FONT_BOLD, 36)
    draw.text((cx - 100, cy - 25), "DENARIUS", font=font_coin, fill=WHITE)
    draw.text((cx - 85, cy + 25), "90% PURE Ag", font=ImageFont.truetype(FONT_MONO, 20), fill=CYAN)
    
    img.save(os.path.join(ASSETS_DIR, "scene08_roman_legion.png"), "PNG")
    print("Generated: scene08_roman_legion.png")

def gen_scene09_coin_foundry():
    """Scene 09: Imperial Mint Foundry (Silver melted with zinc & copper)."""
    img = create_base_canvas((24, 16, 12), (10, 6, 6))
    img = add_radial_glow(img, 960, 580, 750, GOLD, 100)
    img = add_radial_glow(img, 960, 580, 400, RED, 110)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE DEBASEMENT CRUCIBLE", "ACT 3", GOLD)
    
    # Molten furnace silhouette
    draw.ellipse([660, 450, 1260, 850], fill=(45, 18, 12, 240), outline=GOLD, width=3)
    draw.ellipse([740, 510, 1180, 790], fill=(245, 158, 11, 160))
    draw.ellipse([800, 550, 1120, 750], fill=(255, 230, 100, 220))
    
    # Chemical dilution tags
    font_chem = ImageFont.truetype(FONT_IMPACT, 44)
    draw.text((450, 360), "+ COPPER", font=font_chem, fill=RED)
    draw.text((1200, 360), "+ ZINC", font=font_chem, fill=GOLD)
    draw.text((820, 300), "- SILVER", font=font_chem, fill=MUTED)
    
    img.save(os.path.join(ASSETS_DIR, "scene09_coin_foundry.png"), "PNG")
    print("Generated: scene09_coin_foundry.png")

def gen_scene10_paris_1720():
    """Scene 10: Paris 1720 & John Law's Paper Money."""
    img = create_base_canvas((18, 20, 30), (8, 10, 16))
    img = add_radial_glow(img, 500, 450, 600, GOLD, 75)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "PARIS 1720: THE FIAT INCEPTION", "ACT 3", GOLD)
    
    # Baroque archways
    for x in [200, 550]:
        draw.arc([x, 220, x + 300, 600], start=180, end=0, fill=GOLD, width=2)
        draw.line([x, 410, x, 850], fill=(30, 44, 72, 255), width=2)
        draw.line([x + 300, 410, x + 300, 850], fill=(30, 44, 72, 255), width=2)
        
    # Vintage Banque Royale Note Silhouette
    bx0, by0, bx1, by1 = 300, 380, 750, 640
    draw.rectangle([bx0, by0, bx1, by1], fill=(22, 30, 48, 240), outline=GOLD, width=2)
    font_law = ImageFont.truetype(FONT_BOLD, 26)
    draw.text((bx0 + 40, by0 + 40), "BANQUE ROYALE (1720)", font=font_law, fill=WHITE)
    draw.text((bx0 + 40, by0 + 90), "John Law Mississippi Note", font=ImageFont.truetype(FONT_REG, 20), fill=MUTED)
    draw.text((bx0 + 40, by0 + 140), "FIAT BACKING: NIL", font=ImageFont.truetype(FONT_MONO, 22), fill=RED)
    
    img.save(os.path.join(ASSETS_DIR, "scene10_paris_1720.png"), "PNG")
    print("Generated: scene10_paris_1720.png")

def gen_scene11_cantillon_study():
    """Scene 11: Cantillon's Private Hard Asset Accumulation."""
    img = create_base_canvas((16, 22, 34), (8, 10, 16))
    img = add_radial_glow(img, 600, 520, 650, CYAN, 80)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE CANTILLON ARBITRAGE", "ACT 3", CYAN)
    
    # Stacks of gold & physical deed ledger
    for i in range(5):
        y = 700 - i * 36
        draw.rounded_rectangle([360, y, 620, y + 28], radius=6, fill=(245, 158, 11, 230), outline=(255, 230, 120, 255), width=1)
    draw.text((410, 720), "TANGIBLE GOLD", font=ImageFont.truetype(FONT_BOLD, 24), fill=WHITE)
    
    img.save(os.path.join(ASSETS_DIR, "scene11_cantillon_study.png"), "PNG")
    print("Generated: scene11_cantillon_study.png")

def gen_scene12_historical_con():
    """Scene 12: Triptych Comparison: Roman Coin -> 1720 Banknote -> 2026 Display."""
    img = create_base_canvas((18, 18, 28), (8, 8, 14))
    img = add_radial_glow(img, 960, 540, 700, GOLD, 70)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE CYCLICAL FORMULA", "ACT 3", GOLD)
    
    # 3 Pillar Panels
    panels = [
        (180, "270 AD", "MELTED DENARIUS", "Tin & Zinc Alloy", CYAN),
        (720, "1720 AD", "BANQUE ROYALE", "Paper Note Dilution", GOLD),
        (1260, "2026 AD", "DIGITAL LEDGERS", "Trillions via Keystroke", RED)
    ]
    for px, era, title, desc, col in panels:
        draw.rounded_rectangle([px, 260, px + 480, 820], radius=16, fill=(14, 20, 34, 220), outline=col, width=2)
        draw.text((px + 40, 310), era, font=ImageFont.truetype(FONT_IMPACT, 42), fill=col)
        draw.text((px + 40, 375), title, font=ImageFont.truetype(FONT_BOLD, 28), fill=WHITE)
        draw.text((px + 40, 425), desc, font=ImageFont.truetype(FONT_REG, 20), fill=MUTED)
        draw.line([px + 40, 480, px + 440, 480], fill=(30, 44, 72, 255), width=1)
        
    img.save(os.path.join(ASSETS_DIR, "scene12_historical_con.png"), "PNG")
    print("Generated: scene12_historical_con.png")

def gen_scene13_digital_mint():
    """Scene 13: Modern Digital Mint Server Room."""
    img = create_base_canvas((12, 22, 36), (6, 12, 20))
    img = add_radial_glow(img, 960, 500, 800, CYAN, 100)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE SILICON MINT", "ACT 4", CYAN)
    
    # Server rack corridors perspective
    for i in range(7):
        rx = 200 + i * 110
        draw.rectangle([rx, 240, rx + 80, 840], fill=(12, 24, 40, 240), outline=(20, 48, 80, 255), width=2)
        # Server LED activity blinks
        for ly in range(260, 820, 40):
            draw.ellipse([rx + 16, ly, rx + 24, ly + 8], fill=CYAN)
            draw.ellipse([rx + 36, ly, rx + 44, ly + 8], fill=GOLD if (ly % 80 == 0) else (15, 60, 80, 255))
            
    img.save(os.path.join(ASSETS_DIR, "scene13_digital_mint.png"), "PNG")
    print("Generated: scene13_digital_mint.png")

def gen_scene14_private_equity():
    """Scene 14: Private Equity Land Grab."""
    img = create_base_canvas((16, 20, 30), (8, 10, 16))
    img = add_radial_glow(img, 500, 450, 650, RED, 80)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "INSTITUTIONAL BUYOUTS", "ACT 4", RED)
    
    # Wall Street tower shadow over suburban houses
    draw.rectangle([180, 180, 520, 860], fill=(16, 24, 38, 255), outline=(35, 50, 75, 255), width=2)
    for wy in range(220, 820, 50):
        for wx in range(210, 490, 45):
            draw.rectangle([wx, wy, wx + 25, wy + 25], fill=(245, 158, 11, 140))
            
    # Suburban house silhouettes below
    for hx in range(600, 1050, 90):
        draw.polygon([(hx, 800), (hx + 35, 750), (hx + 70, 800)], fill=(20, 32, 50, 255))
        draw.rectangle([hx, 800, hx + 70, 860], fill=(15, 24, 38, 255))
        
    img.save(os.path.join(ASSETS_DIR, "scene14_private_equity.png"), "PNG")
    print("Generated: scene14_private_equity.png")

def gen_scene15_startup_pipeline():
    """Scene 15: Speculative Tech Pipeline & Factory Floor."""
    img = create_base_canvas((16, 24, 36), (8, 12, 18))
    img = add_radial_glow(img, 500, 500, 600, GOLD, 75)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE CAPITAL SINKHOLE", "ACT 4", GOLD)
    
    # Factory conveyor / manufacturing gear silhouette
    draw.ellipse([300, 400, 680, 780], outline=GOLD, width=4)
    for a in range(0, 360, 45):
        rad = math.radians(a)
        x1 = 490 + 190 * math.cos(rad)
        y1 = 590 + 190 * math.sin(rad)
        draw.rectangle([x1 - 12, y1 - 12, x1 + 12, y1 + 12], fill=GOLD)
    draw.text((390, 570), "PHYSICAL ASSET", font=ImageFont.truetype(FONT_BOLD, 24), fill=WHITE)
    
    img.save(os.path.join(ASSETS_DIR, "scene15_startup_pipeline.png"), "PNG")
    print("Generated: scene15_startup_pipeline.png")

def gen_scene16_capital_flow():
    """Scene 16: Macro Capital Pipeline Diagram."""
    img = create_base_canvas((14, 20, 32), (8, 10, 16))
    img = add_radial_glow(img, 960, 540, 750, CYAN, 70)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE TRANSMISSION MECHANISM", "ACT 4", CYAN)
    
    # 4 Flow Nodes
    nodes = [
        (140, "CENTRAL BANK", "Digit Creation", CYAN),
        (580, "MEGA-FUNDS", "Zero Holding Fee", GOLD),
        (1020, "PHYSICAL ASSETS", "Real Estate / Stocks", RED),
        (1460, "RETAIL PRICES", "Everyday Inflation", WHITE)
    ]
    for nx, title, desc, col in nodes:
        draw.rounded_rectangle([nx, 440, nx + 320, 620], radius=12, fill=(16, 26, 44, 230), outline=col, width=2)
        draw.text((nx + 25, 480), title, font=ImageFont.truetype(FONT_BOLD, 24), fill=col)
        draw.text((nx + 25, 530), desc, font=ImageFont.truetype(FONT_REG, 18), fill=MUTED)
        if nx < 1460:
            # Connecting Arrow
            draw.line([nx + 325, 530, nx + 415, 530], fill=CYAN, width=3)
            draw.polygon([(nx + 415, 520), (nx + 435, 530), (nx + 415, 540)], fill=CYAN)
            
    img.save(os.path.join(ASSETS_DIR, "scene16_capital_flow.png"), "PNG")
    print("Generated: scene16_capital_flow.png")

def gen_scene17_generational_contrast():
    """Scene 17: Generational Divergence (1970 vs 2026)."""
    img = create_base_canvas((16, 22, 34), (8, 10, 16))
    img = add_radial_glow(img, 500, 500, 600, CYAN, 75)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "PURCHASING POWER EROSION", "ACT 5", CYAN)
    
    # Hourglass motif showing time erosion
    hx, hy = 480, 540
    draw.polygon([(hx - 120, hy - 160), (hx + 120, hy - 160), (hx, hy), (hx - 120, hy - 160)], outline=CYAN, width=3)
    draw.polygon([(hx, hy), (hx + 120, hy + 160), (hx - 120, hy + 160), (hx, hy)], outline=CYAN, width=3)
    
    img.save(os.path.join(ASSETS_DIR, "scene17_generational_contrast.png"), "PNG")
    print("Generated: scene17_generational_contrast.png")

def gen_scene18_melting_vault():
    """Scene 18: Cash Dilution in Checking Accounts (Melting Vault)."""
    img = create_base_canvas((18, 16, 26), (8, 8, 14))
    img = add_radial_glow(img, 960, 540, 700, RED, 80)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "THE MELTING ICE CUBE", "ACT 5", RED)
    
    # Massive Steel Vault Door Circle
    cx, cy, cr = 960, 560, 260
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(16, 22, 36, 240), outline=RED, width=4)
    draw.ellipse([cx - cr + 40, cy - cr + 40, cx + cr - 40, cy + cr - 40], outline=(40, 50, 70, 255), width=2)
    for a in range(0, 360, 30):
        rad = math.radians(a)
        bx = cx + (cr - 20) * math.cos(rad)
        by = cy + (cr - 20) * math.sin(rad)
        draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=RED)
        
    font_vault = ImageFont.truetype(FONT_IMPACT, 42)
    draw.text((cx - 160, cy - 25), "CASH BALANCES: -64%", font=font_vault, fill=RED)
    
    img.save(os.path.join(ASSETS_DIR, "scene18_melting_vault.png"), "PNG")
    print("Generated: scene18_melting_vault.png")

def gen_scene19_build_boat():
    """Scene 19: Build A Boat (Closing Climax with Owl Avatar)."""
    img = create_base_canvas((14, 22, 38), (8, 12, 22))
    img = add_radial_glow(img, 1400, 480, 700, GOLD, 90)
    img = add_radial_glow(img, 450, 540, 600, CYAN, 80)
    draw = ImageDraw.Draw(img)
    add_header_badge(draw, "FINAL RESOLUTION", "ACT 5", GOLD)
    
    # Sturdy boat silhouette on water line
    draw.rectangle([0, 820, 1920, 1080], fill=(10, 18, 30, 255))
    draw.line([0, 820, 1920, 820], fill=CYAN, width=3)
    
    # Boat hull polygon
    boat_poly = [(1100, 820), (1650, 820), (1750, 740), (1050, 740)]
    draw.polygon(boat_poly, fill=(24, 36, 58, 255), outline=GOLD)
    # Mast & Lantern
    draw.line([1380, 740, 1380, 460], fill=GOLD, width=4)
    draw.ellipse([1365, 480, 1395, 510], fill=GOLD)
    
    # Composite Master Avatar on Left looking forward
    avatar_path = os.path.join(BRAND_DIR, "00_MASTER_avatar.png")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA")
        av = av.resize((560, 560), Image.Resampling.LANCZOS)
        img.paste(av, (160, 300), av)
        
    img.save(os.path.join(ASSETS_DIR, "scene19_build_boat.png"), "PNG")
    print("Generated: scene19_build_boat.png")

if __name__ == '__main__':
    print("=== GENERATING PROCEDURAL SCENE PLATES ===")
    gen_scene03_bank_loan()
    gen_scene04_podcast_studio()
    gen_scene05_debt_mountain()
    gen_scene06_villain_dilution()
    gen_scene08_roman_legion()
    gen_scene09_coin_foundry()
    gen_scene10_paris_1720()
    gen_scene11_cantillon_study()
    gen_scene12_historical_con()
    gen_scene13_digital_mint()
    gen_scene14_private_equity()
    gen_scene15_startup_pipeline()
    gen_scene16_capital_flow()
    gen_scene17_generational_contrast()
    gen_scene18_melting_vault()
    gen_scene19_build_boat()
    print("All 16 procedural scene plates generated!")
