import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

SRC = r"C:\Users\sar1s\.gemini\antigravity\brain\fa6cc279-b4cc-4a52-9629-aff42dfd0eb7\.user_uploaded\media_1793382647937_7f3ee7bf.jpg"
OUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets"

def get_font(size, bold=True):
    paths = [
        r"C:\Windows\Fonts\impact.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def process_base_crop():
    """
    Crops the original 1024x571 image to focus tightly on the
    steering wheel, POS terminal, and credit card hand,
    upscaling to broadcast 1280x720.
    """
    img = Image.open(SRC).convert("RGBA")
    w, h = img.size
    
    # Crop to 16:9 centered on the steering wheel & card interaction
    # Focus bounding box: x from 120 to 920 (w=800), y from 50 to 500 (h=450)
    crop_x1 = int(w * 0.12)
    crop_x2 = int(w * 0.90)
    crop_w = crop_x2 - crop_x1
    crop_h = int(crop_w * 9 / 16)
    crop_y1 = int(h * 0.08)
    crop_y2 = crop_y1 + crop_h
    
    cropped = img.crop((crop_x1, crop_y1, crop_x2, crop_y2))
    resized = cropped.resize((1280, 720), Image.Resampling.LANCZOS)
    
    # Chiaroscuro & Cinematic Contrast Grade
    # 1. Boost contrast to give deep obsidian blacks
    resized = ImageEnhance.Contrast(resized).enhance(1.30)
    # 2. Adjust brightness slightly down to eliminate washed out gray shadows
    resized = ImageEnhance.Brightness(resized).enhance(0.92)
    # 3. Boost saturation for the cyan glow and amber streetlights
    resized = ImageEnhance.Color(resized).enhance(1.15)
    
    # 4. Add dramatic dark perimeter vignette (keeping center glowing)
    vignette = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    
    # Darken bottom right (YouTube timestamp safe zone)
    v_draw.rectangle([980, 560, 1280, 720], fill=(0, 0, 0, 200))
    # Soft perimeter vignette
    for i in range(80):
        alpha = int(90 * (1 - (i / 80)))
        v_draw.rectangle([i, i, 1280 - i, 720 - i], outline=(5, 8, 15, alpha), width=1)
        
    return Image.alpha_composite(resized, vignette)

def build_variant_1_pure_visual(base):
    """
    Variant 1: Pure Visual Cinema (Zero Text Outside the World)
    - Diegetically enhances the POS terminal screen with '$18 / MO' and 'TAP TO STEER'.
    - Completely textless on the outer canvas.
    - Pure modern Magnates Media / Moon standard.
    """
    img = base.copy()
    draw = ImageDraw.Draw(img)
    
    # In the 1280x720 crop, the POS terminal screen is located roughly:
    # x: ~480 to ~640, y: ~260 to ~530
    # Let's add a glowing digital banner right across the lower half of the terminal screen
    # Terminal screen box overlay:
    tx1, ty1, tx2, ty2 = 505, 415, 615, 465
    
    # Soft cyan digital glow box on screen
    draw.rounded_rectangle([tx1, ty1, tx2, ty2], radius=6, fill=(0, 30, 45, 220), outline=(56, 189, 248, 255), width=2)
    
    f_price = get_font(26, bold=True)
    draw.text((tx1 + 10, ty1 + 10), "$18.00 / MO", font=f_price, fill=(255, 255, 255, 255))
    
    # Bottom prompt on terminal
    f_micro = get_font(13, bold=True)
    draw.text((tx1 + 14, ty1 + 36), "TAP TO STEER", font=f_micro, fill=(56, 189, 248, 255))
    
    out_path = os.path.join(OUT_DIR, "thumbnail_v1_pure_visual_tap.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Saved Variant 1: {out_path}")

def build_variant_2_red_alert(base):
    """
    Variant 2: The Red Hazard Pop
    - Terminal screen shows a glowing crimson warning: 'LOCKED • $18/MO'
    - High-contrast visual tension between cyan dashboard and red lock.
    """
    img = base.copy()
    draw = ImageDraw.Draw(img)
    
    tx1, ty1, tx2, ty2 = 505, 415, 615, 465
    draw.rounded_rectangle([tx1, ty1, tx2, ty2], radius=6, fill=(40, 10, 15, 230), outline=(239, 68, 68, 255), width=2)
    
    f_price = get_font(24, bold=True)
    draw.text((tx1 + 12, ty1 + 8), "$18 / MO", font=f_price, fill=(255, 255, 255, 255))
    
    f_micro = get_font(12, bold=True)
    draw.text((tx1 + 12, ty1 + 36), "UNLOCK TO DRIVE", font=f_micro, fill=(239, 68, 68, 255))
    
    # Subtle warning pill in upper left
    draw.rounded_rectangle([60, 50, 360, 95], radius=8, fill=(10, 15, 25, 210), outline=(239, 68, 68, 220), width=2)
    f_pill = get_font(20, bold=True)
    draw.text((80, 62), "SUBSCRIPTION REQUIRED", font=f_pill, fill=(239, 68, 68, 255))
    
    out_path = os.path.join(OUT_DIR, "thumbnail_v2_red_alert_tap.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Saved Variant 2: {out_path}")

def build_variant_3_bold_slam(base):
    """
    Variant 3: The 3-Word Minimalist Hook: 'PAY TO DRIVE'
    - Massive, bold, crisp 90pt font in the upper left negative space.
    - Thick black shadow for instant 500ms mobile recognition.
    """
    img = base.copy()
    draw = ImageDraw.Draw(img)
    
    # Diegetic screen label
    tx1, ty1, tx2, ty2 = 505, 415, 615, 465
    draw.rounded_rectangle([tx1, ty1, tx2, ty2], radius=6, fill=(0, 25, 40, 220), outline=(56, 189, 248, 255), width=2)
    f_price = get_font(24, bold=True)
    draw.text((tx1 + 10, ty1 + 10), "$18 / MO", font=f_price, fill=(255, 255, 255, 255))
    f_micro = get_font(12, bold=True)
    draw.text((tx1 + 14, ty1 + 36), "TAP TO STEER", font=f_micro, fill=(56, 189, 248, 255))
    
    # Massive 3-Word Hook in upper left (where the dark windshield provides negative space)
    f_slam = get_font(84, bold=True)
    line1 = "PAY TO"
    line2 = "DRIVE."
    
    # Multi-directional heavy shadow
    for dx, dy in [(-4, -4), (-4, 4), (4, -4), (4, 4), (0, 6), (6, 0), (6, 6)]:
        draw.text((60 + dx, 50 + dy), line1, font=f_slam, fill=(0, 0, 0, 255))
        draw.text((60 + dx, 140 + dy), line2, font=f_slam, fill=(0, 0, 0, 255))
        
    draw.text((60, 50), line1, font=f_slam, fill=(244, 241, 234, 255))
    draw.text((60, 140), line2, font=f_slam, fill=(245, 158, 11, 255))  # Warning Amber
    
    out_path = os.path.join(OUT_DIR, "thumbnail_v3_pay_to_drive_slam.png")
    img.convert("RGB").save(out_path, quality=95)
    print(f"Saved Variant 3: {out_path}")

def main():
    base = process_base_crop()
    build_variant_1_pure_visual(base)
    build_variant_2_red_alert(base)
    build_variant_3_bold_slam(base)
    print("All 3 high-converting thumbnail variants created successfully!")

if __name__ == "__main__":
    main()

