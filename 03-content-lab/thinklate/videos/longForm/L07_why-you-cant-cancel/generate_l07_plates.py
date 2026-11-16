#!/usr/bin/env python3
"""
ThinkLate Episode L07 ("Why You Can't Cancel Anything") — 2D Widescreen Forensic Plates
Generates 5 high-contrast 1920x1080 RGBA transparent overlay plates via Pillow:
  Plate 1: The Amazon Iliad Flow (1-click sign-up vs 6-click maze)
  Plate 2: Wall Street Churn Math (3% monthly = 31% annual loss)
  Plate 3: The Law That Died & ROSCA Enforcement (FTC v. Toast)
  Plate 4: Global Dual-Anchor (US Auto-renew vs India RBI 2FA)
  Plate 5: Behavioral Friction Architecture (Sign-up vs Cancel)
"""

import pathlib
from PIL import Image, ImageDraw, ImageFont

L07_DIR = pathlib.Path(__file__).resolve().parent
PLATES_DIR = L07_DIR / "assets" / "plates"
PLATES_DIR.mkdir(parents=True, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_SEGOE = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_IMPACT = r"C:\Windows\Fonts\impact.ttf"

BG_GLASS = (10, 15, 29, 235)          # Deep Obsidian with 92% opacity
BORDER_CYAN = (0, 240, 255, 220)      # Cyber Neon Cyan
ACCENT_LIME = (226, 255, 0, 255)      # Acid Lime #E2FF00
CRIMSON = (255, 42, 75, 255)          # Warning Crimson #FF2A4B
WHITE = (255, 255, 255, 255)
MUTED_GRAY = (180, 195, 215, 230)
GREEN = (16, 185, 129, 255)

def create_plates():
    W, H = 1920, 1080

    # -------------------------------------------------------------
    # PLATE 1: The Amazon Iliad Flow
    # -------------------------------------------------------------
    img1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(img1)
    
    # Top Category Pill
    d1.rounded_rectangle([160, 90, 800, 155], radius=16, fill=(10, 15, 29, 230), outline=BORDER_CYAN, width=2)
    f_pill = ImageFont.truetype(FONT_BOLD, 26)
    d1.text((480, 122), "FTC v. AMAZON.COM • CASE NO. 2:23-CV-00932", font=f_pill, fill=(0, 240, 255, 255), anchor="mm")

    # Main Card
    d1.rounded_rectangle([160, 180, 1760, 880], radius=28, fill=BG_GLASS, outline=BORDER_CYAN, width=3)
    
    f_title = ImageFont.truetype(FONT_IMPACT, 68)
    d1.text((220, 260), "PROJECT ILIAD: THE CANCELLATION MAZE", font=f_title, fill=WHITE)
    
    # Split comparison boxes
    # Left: Sign Up
    d1.rounded_rectangle([220, 340, 920, 720], radius=20, fill=(16, 185, 129, 25), outline=GREEN, width=3)
    f_box_t = ImageFont.truetype(FONT_IMPACT, 48)
    d1.text((260, 390), "SIGNING UP (1 CLICK)", font=f_box_t, fill=GREEN)
    f_b_item = ImageFont.truetype(FONT_BOLD, 32)
    d1.text((260, 480), "• Total Screens:  1 Page", font=f_b_item, fill=WHITE)
    d1.text((260, 540), "• Interaction:    1 Tap", font=f_b_item, fill=WHITE)
    d1.text((260, 600), "• Elapsed Time:   4 Seconds", font=f_b_item, fill=WHITE)
    d1.text((260, 660), "• Friction Level: ZERO", font=f_b_item, fill=GREEN)

    # Right: Cancel
    d1.rounded_rectangle([980, 340, 1700, 720], radius=20, fill=(255, 42, 75, 25), outline=CRIMSON, width=3)
    d1.text((1020, 390), "CANCELLING (ILIAD FLOW)", font=f_box_t, fill=CRIMSON)
    d1.text((1020, 480), "• Total Screens:  4 Sequential Pages", font=f_b_item, fill=WHITE)
    d1.text((1020, 540), "• Interaction:    6 Separate Clicks", font=f_b_item, fill=WHITE)
    d1.text((1020, 600), "• Roadblocks:     15 Alternative Offers", font=f_b_item, fill=WHITE)
    d1.text((1020, 660), "• Friction Level: EXTREME WEAR-OUT", font=f_b_item, fill=CRIMSON)

    # Bottom Rubber Stamp
    d1.rounded_rectangle([1180, 750, 1680, 830], radius=14, fill=(255, 42, 75, 40), outline=CRIMSON, width=4)
    f_stamp = ImageFont.truetype(FONT_IMPACT, 42)
    d1.text((1430, 790), "SETTLED: $2.5 BILLION", font=f_stamp, fill=CRIMSON, anchor="mm")
    img1.save(PLATES_DIR / "plate_01.png")

    # -------------------------------------------------------------
    # PLATE 2: Wall Street Churn Math
    # -------------------------------------------------------------
    img2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img2)
    
    d2.rounded_rectangle([160, 90, 720, 155], radius=16, fill=(10, 15, 29, 230), outline=(245, 158, 11, 255), width=2)
    d2.text((440, 122), "SAAS CORPORATE FINANCE BENCHMARK", font=f_pill, fill=(245, 158, 11, 255), anchor="mm")

    d2.rounded_rectangle([160, 180, 1760, 880], radius=28, fill=BG_GLASS, outline=(245, 158, 11, 220), width=3)
    d2.text((220, 260), "THE MONTHLY CHURN LEAK", font=f_title, fill=WHITE)

    # Metrics container
    d2.rounded_rectangle([220, 340, 1700, 720], radius=20, fill=(20, 28, 48, 220), outline=(60, 80, 120, 255), width=2)
    f_big_m = ImageFont.truetype(FONT_IMPACT, 84)
    d2.text((280, 410), "3% / Month", font=f_big_m, fill=(245, 158, 11, 255))
    d2.text((280, 520), "Monthly Churn (Sounds Tiny)", font=ImageFont.truetype(FONT_BOLD, 36), fill=MUTED_GRAY)
    
    # Arrow
    d2.text((900, 410), "➔", font=f_big_m, fill=WHITE)

    d2.text((1060, 410), "= 30.6% Lost", font=f_big_m, fill=CRIMSON)
    d2.text((1060, 520), "Annual Customer Evaporation!", font=ImageFont.truetype(FONT_BOLD, 36), fill=CRIMSON)

    d2.line([(280, 600), (1640, 600)], fill=(60, 80, 120, 255), width=2)
    d2.text((280, 640), "Executive Priority: Plugging the hole with friction is 10x cheaper than marketing.", font=ImageFont.truetype(FONT_BOLD, 32), fill=ACCENT_LIME)

    # Stamp
    d2.rounded_rectangle([1180, 750, 1680, 830], radius=14, fill=(245, 158, 11, 40), outline=(245, 158, 11, 255), width=4)
    d2.text((1430, 790), "VALUATION PROTECTION", font=f_stamp, fill=(245, 158, 11, 255), anchor="mm")
    img2.save(PLATES_DIR / "plate_02.png")

    # -------------------------------------------------------------
    # PLATE 3: The Law That Died & ROSCA Enforcement
    # -------------------------------------------------------------
    img3 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d3 = ImageDraw.Draw(img3)
    
    d3.rounded_rectangle([160, 90, 760, 155], radius=16, fill=(10, 15, 29, 230), outline=CRIMSON, width=2)
    d3.text((460, 122), "REGULATORY & JUDICIAL TIMELINE", font=f_pill, fill=CRIMSON, anchor="mm")

    d3.rounded_rectangle([160, 180, 1760, 880], radius=28, fill=BG_GLASS, outline=CRIMSON, width=3)
    d3.text((220, 260), "CLICK-TO-CANCEL RULE: VACATED", font=f_title, fill=WHITE)

    d3.rounded_rectangle([220, 340, 920, 720], radius=20, fill=(255, 42, 75, 25), outline=CRIMSON, width=2)
    d3.text((260, 390), "FEDERAL RULE KILLED", font=f_box_t, fill=CRIMSON)
    d3.text((260, 480), "• FTC 16 CFR Rule finalized in 2024", font=f_b_item, fill=WHITE)
    d3.text((260, 540), "• Sued by corporate lobbying groups", font=f_b_item, fill=WHITE)
    d3.text((260, 600), "• Eighth Circuit appeals court throws it out", font=f_b_item, fill=MUTED_GRAY)
    d3.text((260, 660), "• Status: STRUCK DOWN NATIONWIDE", font=f_b_item, fill=CRIMSON)

    d3.rounded_rectangle([980, 340, 1700, 720], radius=20, fill=(0, 240, 255, 25), outline=BORDER_CYAN, width=2)
    d3.text((1020, 390), "THE ROSCA PIVOT (ACTIVE)", font=f_box_t, fill=(0, 240, 255, 255))
    d3.text((1020, 480), "• Restore Online Shoppers' Confidence Act", font=f_b_item, fill=WHITE)
    d3.text((1020, 540), "• FTC + 20 States sue Toast, Inc. (Oct 2026)", font=f_b_item, fill=ACCENT_LIME)
    d3.text((1020, 600), "• Target: Multi-step exits & $150/mo exit fees", font=f_b_item, fill=WHITE)
    d3.text((1020, 660), "• State Laws: CA, NY, IL Automatic Renewal", font=f_b_item, fill=(0, 240, 255, 255))

    d3.rounded_rectangle([1180, 750, 1680, 830], radius=14, fill=(0, 240, 255, 40), outline=BORDER_CYAN, width=4)
    d3.text((1430, 790), "ACTIVE FEDERAL LITIGATION", font=f_stamp, fill=(0, 240, 255, 255), anchor="mm")
    img3.save(PLATES_DIR / "plate_03.png")

    # -------------------------------------------------------------
    # PLATE 4: Global Dual-Anchor (US vs India)
    # -------------------------------------------------------------
    img4 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d4 = ImageDraw.Draw(img4)
    
    d4.rounded_rectangle([160, 90, 760, 155], radius=16, fill=(10, 15, 29, 230), outline=ACCENT_LIME, width=2)
    d4.text((460, 122), "GLOBAL POLICY ARCHITECTURE COMPARISON", font=f_pill, fill=ACCENT_LIME, anchor="mm")

    d4.rounded_rectangle([160, 180, 1760, 880], radius=28, fill=BG_GLASS, outline=ACCENT_LIME, width=3)
    d4.text((220, 260), "HOW TO KILL INERTIA: USA vs INDIA", font=f_title, fill=WHITE)

    # US side
    d4.rounded_rectangle([220, 340, 920, 720], radius=20, fill=(20, 28, 48, 220), outline=(80, 100, 140, 255), width=2)
    d4.text((260, 390), "UNITED STATES DEFAULT", font=f_box_t, fill=(255, 100, 100, 255))
    d4.text((260, 480), "• Silent auto-renewals every 30 days", font=f_b_item, fill=WHITE)
    d4.text((260, 540), "• Zero pre-charge verification", font=f_b_item, fill=WHITE)
    d4.text((260, 600), "• Burden: Consumer must remember to chase", font=f_b_item, fill=MUTED_GRAY)
    d4.text((260, 660), "• Philosophy: PROFIT OFF INATTENTION", font=f_b_item, fill=CRIMSON)

    # India side
    d4.rounded_rectangle([980, 340, 1700, 720], radius=20, fill=(16, 185, 129, 25), outline=GREEN, width=2)
    d4.text((1020, 390), "INDIA (RBI E-MANDATE)", font=f_box_t, fill=GREEN)
    d4.text((1020, 480), "• Mandatory SMS alert 24h before debit", font=f_b_item, fill=WHITE)
    d4.text((1020, 540), "• Mandatory 2FA for charges > ₹15,000", font=f_b_item, fill=WHITE)
    d4.text((1020, 600), "• Burden: Merchant must ask permission", font=f_b_item, fill=ACCENT_LIME)
    d4.text((1020, 660), "• Philosophy: ACTIVE SOVEREIGNTY", font=f_b_item, fill=GREEN)

    d4.rounded_rectangle([1180, 750, 1680, 830], radius=14, fill=(16, 185, 129, 40), outline=GREEN, width=4)
    d4.text((1430, 790), "PERMISSION OVER INERTIA", font=f_stamp, fill=GREEN, anchor="mm")
    img4.save(PLATES_DIR / "plate_04.png")

    # -------------------------------------------------------------
    # PLATE 5: Public Retrospection & Climax Verdict
    # -------------------------------------------------------------
    img5 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d5 = ImageDraw.Draw(img5)
    
    d5.rounded_rectangle([160, 90, 760, 155], radius=16, fill=(10, 15, 29, 230), outline=ACCENT_LIME, width=2)
    d5.text((460, 122), "PUBLIC RETROSPECTION & VERDICT", font=f_pill, fill=ACCENT_LIME, anchor="mm")

    d5.rounded_rectangle([160, 180, 1760, 880], radius=28, fill=BG_GLASS, outline=ACCENT_LIME, width=4)
    d5.text((220, 260), "EVICT THE ALGORITHM FROM YOUR WALLET", font=f_title, fill=WHITE)

    d5.rounded_rectangle([220, 340, 1700, 720], radius=20, fill=(15, 24, 45, 240), outline=(60, 90, 140, 255), width=2)
    f_quote = ImageFont.truetype(FONT_BOLD, 38)
    d5.text((280, 395), "The Public Retrospection:", font=f_quote, fill=ACCENT_LIME)
    d5.text((280, 465), "• Your exhaustion was budgeted into their quarterly earnings.", font=ImageFont.truetype(FONT_BOLD, 32), fill=WHITE)
    d5.text((280, 525), "• They didn't sell convenience—they bought permanent, unmonitored access to your money.", font=ImageFont.truetype(FONT_BOLD, 32), fill=MUTED_GRAY)
    d5.text((280, 585), "• Action: Never give your primary debit card. Use single-use virtual limits.", font=ImageFont.truetype(FONT_BOLD, 32), fill=WHITE)

    f_loop = ImageFont.truetype(FONT_IMPACT, 52)
    d5.text((W/2, 675), "BREAK THE PIPELINE. MAKE THEM EARN EVERY DOLLAR.", font=f_loop, fill=ACCENT_LIME, anchor="mm")

    # Bottom Callout Stamp
    d5.rounded_rectangle([1180, 750, 1680, 830], radius=14, fill=(226, 255, 0, 40), outline=ACCENT_LIME, width=4)
    d5.text((1430, 790), "RECLAIM YOUR AUTONOMY", font=f_stamp, fill=ACCENT_LIME, anchor="mm")
    img5.save(PLATES_DIR / "plate_05.png")
    print(f"[+] All 5 forensic plates generated successfully in {PLATES_DIR}")

if __name__ == "__main__":
    create_plates()
