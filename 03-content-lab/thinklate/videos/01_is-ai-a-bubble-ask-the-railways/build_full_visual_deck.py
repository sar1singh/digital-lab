import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = 'videos/01_is-ai-a-bubble-ask-the-railways/assets'

INK = (27, 42, 74)        # #1B2A4A
INK_PANEL = (36, 54, 92)  # #24365C
PAPER = (244, 241, 234)   # #F4F1EA
AMBER = (217, 154, 43)    # #D99A2B
SLATE = (152, 162, 179)   # #98A2B3
HIGHLIGHT = (255, 230, 0, 110)

try:
    font_badge = ImageFont.truetype('C:/Windows/Fonts/CascadiaMono.ttf', 20)
    font_title = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 30)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)
    font_pill = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 18)
    font_hero = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 44)
    font_card = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24)
except Exception:
    font_badge = font_title = font_sub = font_pill = font_hero = font_card = ImageFont.load_default()

def draw_lower_third(canvas, badge, title, subtitle, claim_tag=""):
    bx0, by0, bx1, by1 = 100, 860, 1820, 1015
    panel = Image.new('RGBA', (bx1 - bx0, by1 - by0), (27, 42, 74, 240))
    pdraw = ImageDraw.Draw(panel)
    pdraw.rectangle([(0, 0), (bx1 - bx0 - 1, by1 - by0 - 1)], outline=(152, 162, 179, 120), width=1)
    pdraw.rectangle([(0, 0), (8, by1 - by0 - 1)], fill=AMBER)
    canvas.alpha_composite(panel, (bx0, by0))
    
    draw = ImageDraw.Draw(canvas)
    draw.text((bx0 + 36, by0 + 20), badge.upper(), fill=AMBER, font=font_badge)
    draw.text((bx0 + 36, by0 + 52), title, fill=PAPER, font=font_title)
    draw.text((bx0 + 36, by0 + 98), subtitle, fill=SLATE, font=font_sub)
    
    if claim_tag:
        tw = int(font_pill.getlength(claim_tag)) if hasattr(font_pill, 'getlength') else 200
        px0 = bx1 - tw - 60
        py0 = by0 + 20
        px1 = bx1 - 25
        py1 = by0 + 54
        draw.rounded_rectangle([(px0, py0), (px1, py1)], radius=6, fill=INK_PANEL, outline=AMBER, width=1)
        draw.text((px0 + 15, py0 + 6), claim_tag, fill=PAPER, font=font_pill)

# =========================================================================
# 1. Composite Scene 11: Goldman Sachs Report
# =========================================================================
def build_s11():
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    
    header_path = os.path.join(ASSETS_DIR, 'raw_goldman_header_1789721746106.png')
    takeaway_path = os.path.join(ASSETS_DIR, 'goldman_takeaways_screenshot_1789721617198.png')
    
    if os.path.exists(header_path):
        hdr = Image.open(header_path).convert('RGBA')
        # Crop to the core title area
        w, h = hdr.size
        hdr_crop = hdr.crop((120, 40, w - 120, min(h, 450)))
        # Resize to fit width 1600
        nw = 1600
        nh = int(hdr_crop.height * (nw / hdr_crop.width))
        hdr_resized = hdr_crop.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas.paste(hdr_resized, (160, 80))
        
        # Draw border
        cdraw = ImageDraw.Draw(canvas)
        cdraw.rectangle([(158, 78), (160 + nw + 2, 80 + nh + 2)], outline=(152, 162, 179, 160), width=2)
    
    if os.path.exists(takeaway_path):
        tkw = Image.open(takeaway_path).convert('RGBA')
        w, h = tkw.size
        tkw_crop = tkw.crop((120, 50, w - 120, min(h, 480)))
        nw = 1600
        nh = int(tkw_crop.height * (nw / tkw_crop.width))
        if nh > 320:
            nh = 320
            tkw_crop = tkw_crop.crop((0, 0, tkw_crop.width, int(320 * (tkw_crop.width / nw))))
        tkw_resized = tkw_crop.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas.paste(tkw_resized, (160, 510))
        
        cdraw = ImageDraw.Draw(canvas)
        cdraw.rectangle([(158, 508), (160 + nw + 2, 510 + nh + 2)], outline=(152, 162, 179, 160), width=2)

    # Disclaimer Badge (Pinned top right per script)
    cdraw = ImageDraw.Draw(canvas)
    cdraw.rounded_rectangle([(1320, 20), (1800, 60)], radius=4, fill=(155, 58, 47, 220), outline=PAPER, width=1)
    cdraw.text((1340, 28), "ANALYSIS & INFERENCE — NOT DOCUMENTED FACT", fill=PAPER, font=font_pill)

    draw_lower_third(
        canvas,
        "Wall Street Research · Top of Mind Report",
        'Goldman Sachs Global Investment Research — Jim Covello',
        '"Gen AI: Too Much Spend, Too Little Benefit?" (June 2024)',
        "CAPEX RISK: Who Carries the Bill When Spend Stops?"
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S11_evidence_goldman_report.png'))
    print("Rendered S11_evidence_goldman_report.png")

# =========================================================================
# 2. Composite Scene 12: Sequoia Capital 600B Question
# =========================================================================
def build_s12():
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    
    chart_path = os.path.join(ASSETS_DIR, 'sequoia_chart_600b_1789722131588.png')
    header_path = os.path.join(ASSETS_DIR, 'sequoia_header_1789722077931.png')
    
    if os.path.exists(header_path):
        hdr = Image.open(header_path).convert('RGBA')
        w, h = hdr.size
        hdr_crop = hdr.crop((200, 80, w - 200, min(h, 420)))
        nw = 1600
        nh = int(hdr_crop.height * (nw / hdr_crop.width))
        hdr_resized = hdr_crop.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas.paste(hdr_resized, (160, 60))
        cdraw = ImageDraw.Draw(canvas)
        cdraw.rectangle([(158, 58), (160 + nw + 2, 60 + nh + 2)], outline=(152, 162, 179, 160), width=2)
    
    if os.path.exists(chart_path):
        cht = Image.open(chart_path).convert('RGBA')
        w, h = cht.size
        # Crop table nicely
        cht_crop = cht.crop((180, 20, w - 180, min(h, 600)))
        nw = 1600
        nh = int(cht_crop.height * (nw / cht_crop.width))
        if nh > 420:
            nh = 420
        cht_resized = cht_crop.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas.paste(cht_resized, (160, 410))
        cdraw = ImageDraw.Draw(canvas)
        cdraw.rectangle([(158, 408), (160 + nw + 2, 410 + nh + 2)], outline=(152, 162, 179, 160), width=2)

    draw_lower_third(
        canvas,
        "Venture Analysis · Modern Infrastructure Gap",
        'Sequoia Capital Analysis — David Cahn',
        '"AI\'s $600B Question" — Infrastructure Capex vs Software Revenue',
        "THE QUESTION: Shareholder vs Headcount"
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S12_evidence_sequoia_chart.png'))
    print("Rendered S12_evidence_sequoia_chart.png")

# =========================================================================
# 3. Composite Scene 7: Victorian Railway Speculators (Darwin, Mill, Brontës)
# =========================================================================
def build_s07():
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Title header
    draw.text((120, 60), "1845 RAILWAY MANIA — SHARE SUBSCRIPTION ARCHIVE", fill=AMBER, font=font_badge)
    draw.text((120, 100), "The Intellectuals Caught in the Bubble", fill=PAPER, font=font_hero)
    draw.text((120, 160), "Odlyzko (2010): \"Smart log. Available data. Phir bhi: a collective hallucination.\"", fill=SLATE, font=font_sub)
    
    # 3 Speculator Cards
    investors = [
        ("CHARLES DARWIN", "Naturalist & Author", "£20,000+ portfolio", "Heavily invested in railway debentures & shares. Lost heavily in the 1845-47 crash.", (36, 54, 92)),
        ("JOHN STUART MILL", "Leading Economist", "System of Logic", "Foremost authority on political economy; subscribed to railway lines that went bust.", (42, 64, 110)),
        ("THE BRONTË SISTERS", "Charlotte, Emily, Anne", "York & North Midland", "Invested aunt's £500 legacy into George Hudson's rail empire. Shares lost 70%+.", (36, 54, 92))
    ]
    
    for i, (name, role, holding, desc, col) in enumerate(investors):
        x0 = 120 + i * 570
        y0 = 240
        x1 = x0 + 540
        y1 = 800
        
        # Card panel
        draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=10, fill=col, outline=(152, 162, 179, 120), width=2)
        # Amber top border
        draw.rectangle([(x0, y0), (x1, y0 + 6)], fill=AMBER)
        
        draw.text((x0 + 30, y0 + 35), name, fill=PAPER, font=font_card)
        draw.text((x0 + 30, y0 + 75), role.upper(), fill=AMBER, font=font_pill)
        
        # Divider
        draw.line([(x0 + 30, y0 + 115), (x1 - 30, y0 + 115)], fill=(152, 162, 179, 80), width=1)
        
        draw.text((x0 + 30, y0 + 140), "HOLDING RECORD:", fill=SLATE, font=font_pill)
        draw.text((x0 + 30, y0 + 175), holding, fill=PAPER, font=font_card)
        
        # Description
        lines = [desc[:35], desc[35:70], desc[70:]]
        for li, line in enumerate(lines):
            draw.text((x0 + 30, y0 + 260 + li * 34), line.strip(), fill=PAPER, font=font_sub)
            
        # Stamp badge
        draw.rounded_rectangle([(x0 + 30, y1 - 80), (x1 - 30, y1 - 30)], radius=6, fill=(155, 58, 47, 180), outline=(244, 241, 234, 100), width=1)
        draw.text((x0 + 55, y1 - 68), "SPECULATIVE CASUALTY · 1845", fill=PAPER, font=font_pill)

    draw_lower_third(
        canvas,
        "Primary Historical Archive · Share Registers (1845)",
        "British Parliamentary Papers & Bank of England Archives",
        "Victorian Speculators Registry: Charles Darwin, John Stuart Mill, Brontë Family",
        'HISTORICAL FACT: "A Collective Hallucination"'
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S07_evidence_historical_share.png'))
    print("Rendered S07_evidence_historical_share.png")

# =========================================================================
# 4. Cinematic B-Roll Background Stills (A1, A2, A3)
# =========================================================================
def build_cinematic_stills():
    # A1: Data Center Exterior at Twilight
    a1 = Image.new('RGB', (1920, 1080), (18, 28, 50))
    adraw = ImageDraw.Draw(a1)
    # Architectural perspective lines + glow
    for y in range(300, 900, 30):
        adraw.line([(0, y), (1920, int(y * 0.95))], fill=(24, 38, 68), width=2)
    # Server rack glowing grids
    for x in range(300, 1600, 140):
        adraw.rectangle([(x, 380), (x + 90, 720)], fill=(28, 44, 78), outline=(36, 60, 105), width=2)
        adraw.rectangle([(x + 10, 400), (x + 80, 415)], fill=AMBER)
        adraw.rectangle([(x + 10, 440), (x + 80, 450)], fill=(70, 130, 180))
    # Ambient twilight gradient overlay
    adraw.text((120, 920), "A1 // HYPERSCALE AI DATA CENTER FACILITY", fill=SLATE, font=font_badge)
    adraw.text((120, 955), "Capital Outlay · Infrastructure Buildout Phase", fill=PAPER, font=font_sub)
    a1.save(os.path.join(ASSETS_DIR, 'A1_datacenter_exterior.png'))
    print("Rendered A1_datacenter_exterior.png")

    # A2: Modern Corporate Office Desk
    a2 = Image.new('RGB', (1920, 1080), (22, 32, 54))
    adraw2 = ImageDraw.Draw(a2)
    # Minimalist corporate desk with laptop screen glow
    adraw2.rectangle([(400, 260), (1520, 820)], fill=(28, 42, 70), outline=(45, 68, 110), width=2)
    adraw2.rectangle([(480, 320), (1440, 760)], fill=(18, 26, 44))
    adraw2.text((540, 420), "ENTERPRISE AI CAPEX ALLOCATION", fill=AMBER, font=font_title)
    adraw2.text((540, 480), "Software Licenses: +340%  |  Headcount Impact: Under Review", fill=PAPER, font=font_sub)
    adraw2.text((540, 530), "Depreciation Schedule: 3-5 Years Accelerated", fill=SLATE, font=font_sub)
    adraw2.text((120, 920), "A2 // ENTERPRISE WORKSPACE & SALARIED EMPLOYMENT", fill=SLATE, font=font_badge)
    a2.save(os.path.join(ASSETS_DIR, 'A2_tech_workspace.png'))
    print("Rendered A2_tech_workspace.png")

build_s11()
build_s12()
build_s07()
build_cinematic_stills()
print("All visual evidence slides and cinematic stills compiled successfully!")
