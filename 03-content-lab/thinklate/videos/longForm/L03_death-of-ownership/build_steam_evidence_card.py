"""
ThinkLate Video 03 — Evidence 02 Builder
Compiles the user's uploaded Steam screenshot into a broadcast-grade 1080p Evidence Card:
Shows Black Myth: Wukong (₹3,599.00) + Glowing Cyan Highlight Box on verbatim license disclaimer.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
RAW_IMG = r"C:\Users\sar1s\.gemini\antigravity-ide\brain\4f05742b-22eb-4117-94f9-956be0c27f13\.user_uploaded\media_1792044651753.png"

# Canvas dimensions
W, H = 1920, 1080
canvas = Image.new("RGBA", (W, H), (7, 11, 20, 255))
draw = ImageDraw.Draw(canvas)

# Subtle background gradient / vignette
for y in range(H):
    alpha = int(255 * (1 - 0.25 * (y / H)))
    # subtle radial or linear tint

# Load raw steam capture
raw = Image.open(RAW_IMG).convert("RGBA")

# 1. Main Steam Cart Crop (Include Your Shopping Cart header)
# Raw is 1024 x 618
cart_crop = raw.crop((15, 42, 835, 425))

# Resize to high resolution (scale 1.55x)
cart_w = int(cart_crop.width * 1.55)
cart_h = int(cart_crop.height * 1.55)
cart_scaled = cart_crop.resize((cart_w, cart_h), Image.Resampling.LANCZOS)

# Center placement on canvas
pos_x = (W - cart_w) // 2
pos_y = 195

# Frosted backing card
card_rect = [pos_x - 30, pos_y - 25, pos_x + cart_w + 30, pos_y + cart_h + 35]
draw.rounded_rectangle(card_rect, radius=20, fill=(15, 23, 42, 245), outline=(30, 41, 59, 255), width=2)

# Paste scaled cart crop
canvas.paste(cart_scaled, (pos_x, pos_y), cart_scaled)

# 2. Highlight Box around the Disclaimer
# Relative to crop (x0=15, y0=42):
rel_x1 = int((565 - 15) * 1.55) + pos_x
rel_y1 = int((318 - 42) * 1.55) + pos_y
rel_x2 = int((812 - 15) * 1.55) + pos_x
rel_y2 = int((380 - 42) * 1.55) + pos_y

# Draw glowing cyan highlight box
box_pad = 8
cyan_box = [rel_x1 - box_pad, rel_y1 - box_pad, rel_x2 + box_pad, rel_y2 + box_pad]

# Cyan glow layer
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)
glow_draw.rounded_rectangle(cyan_box, radius=10, fill=(6, 182, 212, 35), outline=(6, 182, 212, 220), width=4)
canvas = Image.alpha_composite(canvas, glow_layer)
draw = ImageDraw.Draw(canvas)

# 3. Callout Badge / Arrow pointing to disclaimer
# Add a prominent tag above or below the box
badge_x1 = cyan_box[0]
badge_y1 = cyan_box[3] + 16
badge_x2 = cyan_box[1] + 340
badge_y2 = badge_y1 + 42

draw.rounded_rectangle([badge_x1, badge_y1, badge_x1 + 380, badge_y1 + 44], radius=8,
                       fill=(8, 51, 68, 245), outline=(6, 182, 212, 255), width=2)

# Try loading font or fallback
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 18)
    font_header = ImageFont.truetype("arialbd.ttf", 36)
    font_sub = ImageFont.truetype("arial.ttf", 18)
    font_pill = ImageFont.truetype("arialbd.ttf", 15)
except:
    font_bold = ImageFont.load_default()
    font_header = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_pill = ImageFont.load_default()

draw.text((badge_x1 + 14, badge_y1 + 12), "▲ OCT 2024 VALVE STOREFRONT UPDATE", fill=(56, 189, 248), font=font_pill)

# 4. Super-Titles & Header on Canvas
draw.text((100, 60), "PRIMARY EVIDENCE 02 • VALVE STEAM CLIENT", fill=(245, 158, 11), font=font_pill)
draw.text((100, 95), "Even Steam Admits: You Are Buying a License, Not a Game", fill=(248, 250, 252), font=font_header)

# Footnote
draw.text((100, H - 70), "Verbatim Clause: 'A purchase of a digital product grants a license for the product on Steam.'", fill=(148, 163, 184), font=font_sub)
draw.text((W - 380, H - 70), "SOURCE: Valve Corporation (2024)", fill=(100, 116, 139), font=font_sub)

# Save master outputs
out_full = os.path.join(ASSETS_DIR, "EVID_02_STEAM_CART_composite_card.png")
out_warning = os.path.join(ASSETS_DIR, "EVID_02_STEAM_CART_WARNING.png")

canvas.save(out_full, "PNG")
# Save standard asset
canvas.save(out_warning, "PNG")

print(f"[SUCCESS] Built: {out_full} (1920x1080)")
print(f"[SUCCESS] Built: {out_warning} (1920x1080)")
