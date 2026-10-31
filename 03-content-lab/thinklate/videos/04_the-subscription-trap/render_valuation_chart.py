"""
ThinkLate (@wethinklate) — Video 04 Animated Chart Generator
Renders Broadcast-Grade 1080p30 MP4: Wall Street Valuation Multiplier
Hardware (1.5x illustrative / $1.5B) vs Subscription ARR (6.7x median / $6.7B), on an illustrative $1B revenue base.
Source: SaaS Capital Index, June 2025 (median public SaaS ARR multiple 6.7x).
Output: assets/CHART_VALUATION_MULTIPLIER_animated.mp4
"""

import os
import subprocess
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
OUT_MP4 = os.path.join(ASSETS_DIR, "CHART_VALUATION_MULTIPLIER_animated.mp4")

# Specifications
WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION_SEC = 8
TOTAL_FRAMES = FPS * DURATION_SEC  # 240 frames

# Brand Tokens
BG_COLOR    = (8, 12, 20, 255)       # #080C14
CARD_BG     = (15, 22, 38, 255)      # #0F1626
BORDER_COL  = (30, 44, 72, 255)      # #1E2C48
GOLD        = (245, 158, 11, 255)    # #F59E0B
CYAN        = (6, 182, 212, 255)     # #06B6D4
RED         = (239, 68, 68, 255)     # #EF4444
WHITE       = (241, 245, 249, 255)   # #F1F5F9
MUTED       = (100, 116, 139, 255)   # #64748B
DIM         = (148, 163, 184, 255)   # #94A3B8

# Fonts
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_BOLD = os.path.join(FONTS_DIR, 'segoeuib.ttf')
FONT_REG  = os.path.join(FONTS_DIR, 'segoeui.ttf')
FONT_MONO = os.path.join(FONTS_DIR, 'consola.ttf')

try:
    font_title = ImageFont.truetype(FONT_BOLD, 46)
    font_sub   = ImageFont.truetype(FONT_MONO, 22)
    font_val   = ImageFont.truetype(FONT_BOLD, 54)
    font_label = ImageFont.truetype(FONT_BOLD, 26)
    font_small = ImageFont.truetype(FONT_REG, 20)
    font_tag   = ImageFont.truetype(FONT_MONO, 18)
except Exception:
    font_title = font_sub = font_val = font_label = font_small = font_tag = ImageFont.load_default()

def ease_out_cubic(x):
    return 1 - math.pow(1 - x, 3)

def generate_frame(frame_idx):
    progress = frame_idx / float(TOTAL_FRAMES)
    
    # Base Canvas
    img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Ambient Background Glow
    # Soft cyan glow behind right bar
    glow_box = [1100, 200, 1750, 950]
    draw.rounded_rectangle(glow_box, radius=40, fill=(6, 182, 212, 10))

    # Main Center Container Card
    c_x0, c_y0 = 160, 100
    c_x1, c_y1 = 1760, 980
    draw.rounded_rectangle([c_x0, c_y0, c_x1, c_y1], radius=24, fill=CARD_BG, outline=BORDER_COL, width=2)

    # Title & Header
    draw.text((c_x0 + 60, c_y0 + 50), "THE WALL STREET VALUATION MULTIPLIER", font=font_title, fill=WHITE)
    draw.text((c_x0 + 60, c_y0 + 115), "WHY CEOS KILL PHYSICAL OWNERSHIP // REVENUE VALUATION MULTIPLES", font=font_sub, fill=GOLD)

    # Baseline & Chart Coordinates
    base_y = c_y1 - 180
    bar_width = 340
    
    # Left Bar: Hardware (1.5x)
    # Target height: 90px (represents 1.5x)
    left_x = c_x0 + 260
    left_target_h = 100
    
    # Right Bar: Subscription SaaS (6.7x median)
    # Target height: 447px (100px per 1.5x -> 6.7x)
    right_x = c_x0 + 880
    right_target_h = 447

    # Animation timing:
    # 0.0 - 0.25 (frames 0-60): Left bar grows
    # 0.25 - 0.70 (frames 60-168): Right bar explodes upward
    # 0.70 - 1.00 (frames 168-240): Hold and pulse
    
    # Calculate Left Bar Progress
    left_p = min(1.0, max(0.0, frame_idx / 45.0))
    left_cur_h = left_target_h * ease_out_cubic(left_p)
    left_val_num = 1.5 * ease_out_cubic(left_p)
    left_ev_num = 1.5 * ease_out_cubic(left_p)

    # Calculate Right Bar Progress
    right_p = min(1.0, max(0.0, (frame_idx - 45) / 95.0))
    right_cur_h = right_target_h * ease_out_cubic(right_p)
    right_val_num = 6.7 * ease_out_cubic(right_p)
    right_ev_num = 1.5 + (5.2 * ease_out_cubic(right_p))

    # Grid / Zero Line
    draw.line([c_x0 + 100, base_y, c_x1 - 100, base_y], fill=(45, 60, 95, 255), width=2)

    # --- DRAW LEFT BAR (HARDWARE 1.5x) ---
    if left_cur_h > 2:
        l_box = [left_x, base_y - left_cur_h, left_x + bar_width, base_y]
        draw.rounded_rectangle(l_box, radius=12, fill=(40, 55, 85, 255), outline=(70, 95, 140, 255), width=2)
        # Value callout above bar
        draw.text((left_x + 20, base_y - left_cur_h - 75), f"{left_val_num:.1f}x", font=font_val, fill=WHITE)
        draw.text((left_x + 160, base_y - left_cur_h - 60), "REVENUE MULTIPLE", font=font_tag, fill=DIM)

    # Labels below Left Bar
    draw.text((left_x + 10, base_y + 20), "ONE-TIME PURCHASE", font=font_label, fill=WHITE)
    draw.text((left_x + 10, base_y + 58), "Hardware / Manufacturing", font=font_small, fill=MUTED)
    draw.text((left_x + 10, base_y + 90), f"Valuation: ${left_ev_num:.1f} Billion", font=font_sub, fill=DIM)

    # --- DRAW RIGHT BAR (SUBSCRIPTION 6.7x) ---
    if right_cur_h > 2:
        r_box = [right_x, base_y - right_cur_h, right_x + bar_width, base_y]
        draw.rounded_rectangle(r_box, radius=12, fill=(6, 182, 212, 190), outline=CYAN, width=3)
        # Value callout above bar
        val_color = GOLD if right_p >= 0.95 else WHITE
        draw.text((right_x + 20, base_y - right_cur_h - 75), f"{right_val_num:.1f}x", font=font_val, fill=val_color)
        draw.text((right_x + 185, base_y - right_cur_h - 60), "ARR MULTIPLE", font=font_tag, fill=GOLD)

    # Labels below Right Bar
    draw.text((right_x + 10, base_y + 20), "SUBSCRIPTION MODEL", font=font_label, fill=CYAN)
    draw.text((right_x + 10, base_y + 58), "Recurring Credit Card Billing", font=font_small, fill=DIM)
    draw.text((right_x + 10, base_y + 90), f"Valuation: ${right_ev_num:.1f} Billion", font=font_sub, fill=GOLD)

    # Center Comparison Arrow & Callout (when right bar grows)
    if right_p > 0.4:
        arrow_opacity = min(255, int(255 * ((right_p - 0.4) / 0.4)))
        # +347% Growth Tag (6.7 / 1.5 - 1)
        tag_x = (left_x + bar_width + right_x) // 2 - 80
        tag_y = base_y - 280
        draw.rounded_rectangle([tag_x, tag_y, tag_x + 160, tag_y + 55], radius=10, fill=(239, 68, 68, 220), outline=RED, width=1)
        draw.text((tag_x + 22, tag_y + 12), "+347%", font=font_label, fill=WHITE)
        draw.text((tag_x - 15, tag_y + 68), "VALUATION JUMP", font=font_tag, fill=GOLD)

    # Source footnote (always visible)
    draw.text((c_x0 + 60, c_y1 - 55), "Illustrative $1B revenue. 1.5x hardware = illustrative. 6.7x = median public SaaS ARR multiple, SaaS Capital Index, Jun 2025.", font=font_tag, fill=MUTED)

    return img

def render_video():
    print(f"[INFO] Rendering {TOTAL_FRAMES} frames ({WIDTH}x{HEIGHT} @ {FPS}fps) to MP4...")

    ffmpeg_cmd = [
        'ffmpeg', '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{WIDTH}x{HEIGHT}',
        '-pix_fmt', 'rgba',
        '-r', str(FPS),
        '-i', '-',
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '18',
        '-pix_fmt', 'yuv420p',
        OUT_MP4
    ]

    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    for i in range(TOTAL_FRAMES):
        frame = generate_frame(i)
        proc.stdin.write(frame.tobytes())
        if i % 30 == 0:
            print(f"  [Progress] Rendered frame {i}/{TOTAL_FRAMES} ({(i/TOTAL_FRAMES)*100:.1f}%)")

    proc.stdin.close()
    proc.wait()
    print(f"[SUCCESS] Exported Broadcast MP4: {OUT_MP4}")

if __name__ == "__main__":
    render_video()
