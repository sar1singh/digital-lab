"""
Generate High-CTR YouTube Thumbnail Variations for YouTube Studio 'Test & Compare'
Creates 3 distinct psychological angle thumbnails at 1280x720 (16:9).
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\assets"
BRAND_DIR  = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\brand"
FONTS_DIR  = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

FONT_BOLD   = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG    = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO   = os.path.join(FONTS_DIR, 'consola.ttf')
FONT_IMPACT = os.path.join(FONTS_DIR, 'impact.ttf')

BG_DARK = (8, 12, 20, 255)
GOLD    = (245, 158, 11, 255)
CYAN    = (6, 182, 212, 255)
RED     = (239, 68, 68, 255)
WHITE   = (241, 245, 249, 255)
MUTED   = (148, 163, 184, 255)

def get_avatar(size=(520, 520)):
    avatar_path = os.path.join(BRAND_DIR, "00_MASTER_avatar.png")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA")
        return av.resize(size, Image.Resampling.LANCZOS)
    return None

def generate_thumb_b_housing_paradox():
    """Concept B: The $15M Housing Paradox (Curiosity / Contrast)."""
    thumb = Image.new('RGBA', (1280, 720), BG_DARK)
    draw = ImageDraw.Draw(thumb)

    # Ambient split glow (Cyan vs Gold)
    for r in range(450, 0, -25):
        alpha = int(22 * (1 - r / 450))
        draw.ellipse([300 - r, 360 - r, 300 + r, 360 + r], fill=(6, 182, 212, alpha))
        draw.ellipse([980 - r, 360 - r, 980 + r, 360 + r], fill=(245, 158, 11, alpha))

    # Grid texture
    for x in range(0, 1280, 64):
        draw.line([(x, 0), (x, 720)], fill=(255, 255, 255, 10), width=1)

    # Avatar on left
    av = get_avatar((540, 540))
    if av:
        thumb.paste(av, (30, 150), av)

    # Bold Typography Right Side
    font_badge = ImageFont.truetype(FONT_MONO, 22)
    font_main  = ImageFont.truetype(FONT_IMPACT, 96)
    font_sub   = ImageFont.truetype(FONT_IMPACT, 72)
    font_kicker= ImageFont.truetype(FONT_BOLD, 26)

    # Badge
    draw.rounded_rectangle([580, 100, 890, 145], radius=6, fill=CYAN)
    draw.text((605, 110), "REAL ESTATE IS BROKEN", font=font_badge, fill=(8, 12, 20, 255))

    # Main Headline
    draw.text((584, 174), "$15,000,000", font=font_main, fill=(0, 0, 0, 220))
    draw.text((580, 170), "$15,000,000", font=font_main, fill=WHITE)

    draw.text((584, 284), "CASTLE OR CONDO?", font=font_sub, fill=(0, 0, 0, 220))
    draw.text((580, 280), "CASTLE OR CONDO?", font=font_sub, fill=GOLD)

    # Sub-kicker
    draw.rounded_rectangle([580, 390, 1140, 460], radius=8, fill=(15, 24, 40, 220), outline=GOLD, width=1)
    draw.text((605, 410), "THE HIDDEN DILUTION EFFECT", font=font_kicker, fill=WHITE)

    out_path = os.path.join(ASSETS_DIR, "thumbnail_variant_b_housing_paradox.png")
    thumb.save(out_path, "PNG")
    print(f"Generated: {out_path}")

def generate_thumb_c_cantillon_con():
    """Concept C: The Cantillon Con / First To Touch The Cash (Psychological Hook)."""
    thumb = Image.new('RGBA', (1280, 720), BG_DARK)
    draw = ImageDraw.Draw(thumb)

    # Red/Gold warning radiance
    for r in range(480, 0, -25):
        alpha = int(25 * (1 - r / 480))
        draw.ellipse([800 - r, 360 - r, 800 + r, 360 + r], fill=(239, 68, 68, alpha))

    # Avatar on left
    av = get_avatar((540, 540))
    if av:
        thumb.paste(av, (30, 150), av)

    font_badge = ImageFont.truetype(FONT_MONO, 22)
    font_main  = ImageFont.truetype(FONT_IMPACT, 88)
    font_sub   = ImageFont.truetype(FONT_IMPACT, 72)
    font_kicker= ImageFont.truetype(FONT_BOLD, 26)

    # Badge
    draw.rounded_rectangle([580, 100, 870, 145], radius=6, fill=RED)
    draw.text((605, 110), "THE RIGGED PIPELINE", font=font_badge, fill=WHITE)

    # Main Headline
    draw.text((584, 174), "WHO GETS IT", font=font_main, fill=(0, 0, 0, 220))
    draw.text((580, 170), "WHO GETS IT", font=font_main, fill=WHITE)

    draw.text((584, 274), "FIRST?", font=font_main, fill=(0, 0, 0, 220))
    draw.text((580, 270), "FIRST?", font=font_main, fill=RED)

    # Sub-headline
    draw.text((584, 384), "WHY SAVINGS MELT DOWN", font=font_sub, fill=(0, 0, 0, 220))
    draw.text((580, 380), "WHY SAVINGS MELT DOWN", font=font_sub, fill=GOLD)

    out_path = os.path.join(ASSETS_DIR, "thumbnail_variant_c_cantillon_con.png")
    thumb.save(out_path, "PNG")
    print(f"Generated: {out_path}")

if __name__ == '__main__':
    print("=== GENERATING YOUTUBE A/B THUMBNAIL VARIATIONS ===")
    generate_thumb_b_housing_paradox()
    generate_thumb_c_cantillon_con()
    print("Done!")
