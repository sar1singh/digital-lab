import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def get_font(size, bold=True):
    font_paths = [
        r"C:\Windows\Fonts\impact.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def create_high_ctr_concept_a():
    """Concept A: CANCEL SUBSCRIPTION? - Pure focus, zero clutter, massive typography."""
    base_img_path = os.path.join(ASSETS_DIR, "anchor_01_frosted_dashboard.jpg")
    img = Image.open(base_img_path).convert("RGBA")
    img = img.resize((1280, 720), Image.Resampling.LANCZOS)
    
    # Cinematic contrast and moody grade
    img = ImageEnhance.Brightness(img).enhance(0.55)
    img = ImageEnhance.Contrast(img).enhance(1.40)
    
    # Left dark vignette for text dominance
    dark_overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    d_draw = ImageDraw.Draw(dark_overlay)
    # Heavy dark gradient block across left and center
    for x in range(950):
        alpha = int(240 * (1 - (x / 950) ** 1.8))
        d_draw.line([(x, 0), (x, 720)], fill=(8, 12, 22, alpha))
    # Bottom right dark shadow for timestamp safety
    d_draw.rectangle([960, 540, 1280, 720], fill=(0, 0, 0, 220))
    img = Image.alpha_composite(img, dark_overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Red Warning Pill Tag
    draw.rounded_rectangle([70, 90, 420, 150], radius=10, fill=(239, 68, 68, 255))
    f_tag = get_font(32, bold=True)
    draw.text((95, 102), "HARDWARE LOCKED", font=f_tag, fill=(255, 255, 255, 255))
    
    # Massive Slam Text: CANCEL SUBSCRIPTION?
    f_huge = get_font(92, bold=True)
    text_line1 = "CANCEL"
    text_line2 = "SUBSCRIPTION?"
    
    # Thick black drop shadow for extreme contrast
    for dx, dy in [(-4, -4), (-4, 4), (4, -4), (4, 4), (0, 6), (6, 0), (6, 6), (0, 8)]:
        draw.text((70 + dx, 180 + dy), text_line1, font=f_huge, fill=(0, 0, 0, 255))
        draw.text((70 + dx, 280 + dy), text_line2, font=f_huge, fill=(0, 0, 0, 255))
        
    draw.text((70, 180), text_line1, font=f_huge, fill=(255, 255, 255, 255))
    draw.text((70, 280), text_line2, font=f_huge, fill=(239, 68, 68, 255))
    
    # High-impact Sub-Hook
    f_sub = get_font(42, bold=True)
    for dx, dy in [(-2, 2), (2, 2), (0, 3)]:
        draw.text((72 + dx, 410 + dy), "PAY $18/MO TO DRIVE", font=f_sub, fill=(0, 0, 0, 255))
    draw.text((72, 410), "PAY $18/MO TO DRIVE", font=f_sub, fill=(245, 158, 11, 255))
    
    # ThinkLate Badge (Top Right, away from timestamp)
    f_badge = get_font(24, bold=True)
    draw.rounded_rectangle([1100, 30, 1240, 70], radius=8, fill=(0, 0, 0, 200), outline=(217, 154, 43, 220), width=2)
    draw.text((1115, 38), "THINKLATE", font=f_badge, fill=(217, 154, 43, 255))
    
    out_path = os.path.join(ASSETS_DIR, "thumbnail_concept_a_cancel_sub.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Rendered High-CTR Thumbnail A: {out_path}")

def create_high_ctr_concept_b():
    """Concept B: NOT YOUR CAR. - High cognitive dissonance."""
    base_img_path = os.path.join(ASSETS_DIR, "anchor_07_seat_warm_glow.jpg")
    if not os.path.exists(base_img_path):
        base_img_path = os.path.join(ASSETS_DIR, "anchor_01_frosted_dashboard.jpg")
    img = Image.open(base_img_path).convert("RGBA")
    img = img.resize((1280, 720), Image.Resampling.LANCZOS)
    
    img = ImageEnhance.Brightness(img).enhance(0.50)
    img = ImageEnhance.Contrast(img).enhance(1.45)
    
    dark_overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    d_draw = ImageDraw.Draw(dark_overlay)
    for x in range(950):
        alpha = int(245 * (1 - (x / 950) ** 1.8))
        d_draw.line([(x, 0), (x, 720)], fill=(5, 10, 18, alpha))
    d_draw.rectangle([960, 540, 1280, 720], fill=(0, 0, 0, 220))
    img = Image.alpha_composite(img, dark_overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Amber Warning Box
    draw.rounded_rectangle([70, 90, 480, 150], radius=10, fill=(245, 158, 11, 255))
    f_tag = get_font(32, bold=True)
    draw.text((95, 102), "REMOTE SHUTDOWN", font=f_tag, fill=(0, 0, 0, 255))
    
    # HUGE Slam Text: NOT YOUR CAR.
    f_huge = get_font(105, bold=True)
    text_line1 = "NOT"
    text_line2 = "YOUR CAR."
    
    for dx, dy in [(-5, -5), (-5, 5), (5, -5), (5, 5), (0, 7), (7, 0), (7, 7)]:
        draw.text((70 + dx, 175 + dy), text_line1, font=f_huge, fill=(0, 0, 0, 255))
        draw.text((70 + dx, 280 + dy), text_line2, font=f_huge, fill=(0, 0, 0, 255))
        
    draw.text((70, 175), text_line1, font=f_huge, fill=(245, 158, 11, 255))
    draw.text((70, 280), text_line2, font=f_huge, fill=(255, 255, 255, 255))
    
    # Sub-Hook
    f_sub = get_font(42, bold=True)
    for dx, dy in [(-2, 2), (2, 2), (0, 3)]:
        draw.text((72 + dx, 415 + dy), "YOU BOUGHT A LEASE", font=f_sub, fill=(0, 0, 0, 255))
    draw.text((72, 415), "YOU BOUGHT A LEASE", font=f_sub, fill=(239, 68, 68, 255))
    
    # ThinkLate Badge
    f_badge = get_font(24, bold=True)
    draw.rounded_rectangle([1100, 30, 1240, 70], radius=8, fill=(0, 0, 0, 200), outline=(217, 154, 43, 220), width=2)
    draw.text((1115, 38), "THINKLATE", font=f_badge, fill=(217, 154, 43, 255))
    
    out_path = os.path.join(ASSETS_DIR, "thumbnail_concept_b_not_your_car.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Rendered High-CTR Thumbnail B: {out_path}")

def create_high_ctr_concept_c():
    """Concept C: PAY TO UNLOCK - The systemic mechanism."""
    base_img_path = os.path.join(ASSETS_DIR, "anchor_06_phone_lock_delivery.jpg")
    if not os.path.exists(base_img_path):
        base_img_path = os.path.join(ASSETS_DIR, "anchor_01_frosted_dashboard.jpg")
    img = Image.open(base_img_path).convert("RGBA")
    img = img.resize((1280, 720), Image.Resampling.LANCZOS)
    
    img = ImageEnhance.Brightness(img).enhance(0.48)
    img = ImageEnhance.Contrast(img).enhance(1.50)
    
    dark_overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    d_draw = ImageDraw.Draw(dark_overlay)
    for x in range(950):
        alpha = int(245 * (1 - (x / 950) ** 1.8))
        d_draw.line([(x, 0), (x, 720)], fill=(4, 12, 24, alpha))
    d_draw.rectangle([960, 540, 1280, 720], fill=(0, 0, 0, 220))
    img = Image.alpha_composite(img, dark_overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Cyan Tag
    draw.rounded_rectangle([70, 90, 480, 150], radius=10, fill=(56, 189, 248, 255))
    f_tag = get_font(32, bold=True)
    draw.text((95, 102), "ACCESS REVOKED", font=f_tag, fill=(0, 0, 0, 255))
    
    # HUGE Slam Text: PAY TO UNLOCK
    f_huge = get_font(105, bold=True)
    text_line1 = "PAY TO"
    text_line2 = "UNLOCK"
    
    for dx, dy in [(-5, -5), (-5, 5), (5, -5), (5, 5), (0, 7), (7, 0), (7, 7)]:
        draw.text((70 + dx, 175 + dy), text_line1, font=f_huge, fill=(0, 0, 0, 255))
        draw.text((70 + dx, 280 + dy), text_line2, font=f_huge, fill=(0, 0, 0, 255))
        
    draw.text((70, 175), text_line1, font=f_huge, fill=(56, 189, 248, 255))
    draw.text((70, 280), text_line2, font=f_huge, fill=(255, 255, 255, 255))
    
    # Sub-Hook
    f_sub = get_font(42, bold=True)
    for dx, dy in [(-2, 2), (2, 2), (0, 3)]:
        draw.text((72 + dx, 415 + dy), "ONE UPDATE TO LEASE", font=f_sub, fill=(0, 0, 0, 255))
    draw.text((72, 415), "ONE UPDATE TO LEASE", font=f_sub, fill=(217, 154, 43, 255))
    
    # ThinkLate Badge
    f_badge = get_font(24, bold=True)
    draw.rounded_rectangle([1100, 30, 1240, 70], radius=8, fill=(0, 0, 0, 200), outline=(56, 189, 248, 220), width=2)
    draw.text((1115, 38), "THINKLATE", font=f_badge, fill=(56, 189, 248, 255))
    
    out_path = os.path.join(ASSETS_DIR, "thumbnail_concept_c_pay_to_unlock.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Rendered High-CTR Thumbnail C: {out_path}")

def main():
    create_high_ctr_concept_a()
    create_high_ctr_concept_b()
    create_high_ctr_concept_c()

if __name__ == "__main__":
    main()
