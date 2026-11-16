"""
Generate broadcast-grade evidence quote card for ThinkLate Video 04:
Enrique Lores (HP CEO) CNBC interview quote card with yellow highlight.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "evidence_hp_ceo_quote.jpg")

FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_BOLD = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG  = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO = os.path.join(FONTS_DIR, 'consola.ttf')

W, H = 1920, 1080
img = Image.new('RGB', (W, H), (8, 12, 20)) # #080C14 Dark Slate Noir
draw = ImageDraw.Draw(img)

# Subtle ambient grid & vignette
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(15, 22, 38), width=1)
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(15, 22, 38), width=1)

# Card Box: Center 1500 x 720
card_w, card_h = 1520, 720
x0 = (W - card_w) // 2
y0 = (H - card_h) // 2
x1 = x0 + card_w
y1 = y0 + card_h

# Draw Outer Glowing Border
draw.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], radius=24, outline=(30, 58, 110), width=2)
# Card body
draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(12, 18, 32))

# Top CNBC Header Bar
draw.rounded_rectangle([x0, y0, x1, y0 + 90], radius=22, fill=(18, 28, 48))
# Straight bottom on header
draw.rectangle([x0, y0 + 60, x1, y0 + 90], fill=(18, 28, 48))
draw.line([(x0, y0 + 90), (x1, y0 + 90)], fill=(40, 70, 120), width=2)

font_tag = ImageFont.truetype(FONT_BOLD, 22)
font_source = ImageFont.truetype(FONT_MONO, 18)

# CNBC pill tag
draw.rounded_rectangle([x0 + 40, y0 + 24, x0 + 260, y0 + 66], radius=8, fill=(220, 38, 38))
draw.text((x0 + 55, y0 + 32), "CNBC EXCLUSIVE", font=font_tag, fill=(255, 255, 255))
draw.text((x0 + 290, y0 + 34), "RECORDED BROADCAST • TRANSCRIPT RECORD", font=font_source, fill=(148, 163, 184))

# Speaker Attribution Section
font_speaker = ImageFont.truetype(FONT_BOLD, 36)
font_title = ImageFont.truetype(FONT_REG, 22)

draw.text((x0 + 60, y0 + 130), "ENRIQUE LORES", font=font_speaker, fill=(241, 245, 249))
draw.text((x0 + 60, y0 + 180), "President & Chief Executive Officer, HP Inc.", font=font_title, fill=(245, 158, 11)) # Amber Gold

# Accent dividing line
draw.line([(x0 + 60, y0 + 230), (x1 - 60, y0 + 230)], fill=(30, 44, 72), width=2)

# Quote Marks
font_quote_mark = ImageFont.truetype(FONT_BOLD, 120)
draw.text((x0 + 50, y0 + 210), "\"", font=font_quote_mark, fill=(60, 90, 140))

# Quote Text Lines
font_quote = ImageFont.truetype(FONT_BOLD, 38)
font_quote_italic = ImageFont.truetype(FONT_REG, 38)

lines = [
    ("Every time a customer buys a printer,", False),
    ("it's an investment for us.", True),   # Highlight
    ("We're investing in that customer, and if that customer", False),
    ("doesn't print enough or doesn't use our supplies,", False),
    ("it's a bad investment.\"", True)     # Highlight
]

curr_y = y0 + 280
for text, is_highlight in lines:
    if is_highlight:
        # Yellow highlight backing
        bbox = draw.textbbox((x0 + 110, curr_y), text, font=font_quote)
        # Highlight rectangle
        draw.rectangle([bbox[0] - 8, bbox[1] - 4, bbox[2] + 12, bbox[3] + 6], fill=(245, 158, 11, 220))
        draw.text((x0 + 110, curr_y), text, font=font_quote, fill=(8, 12, 20)) # Dark text on yellow
    else:
        draw.text((x0 + 110, curr_y), text, font=font_quote, fill=(241, 245, 249))
    curr_y += 66

# Bottom Footer / Regulatory Citation
font_footer = ImageFont.truetype(FONT_MONO, 16)
draw.line([(x0 + 60, y1 - 70), (x1 - 60, y1 - 70)], fill=(30, 44, 72), width=1)
draw.text((x0 + 60, y1 - 48), "SOURCE: HP INC. EARNINGS & BARCLAYS GLOBAL TECHNOLOGY CONFERENCE | SEC 10-K CROSS-CHECKED", font=font_footer, fill=(100, 116, 139))

img.save(OUTPUT_FILE, quality=95)
print(f"Quote card generated: {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)")

