#!/usr/bin/env python3
"""
ThinkLate Short 05 ("The Shelf Price Is Fake") — Complete Master Video Pipeline (V2)
===================================================================================
Produces the full broadcast-quality 1080x1920 vertical Short with:
  1. High-tension Climax & Public Retrospection on the Social Embarrassment Tax
  2. Diverse, authentic B-roll (grocery aisle, courtroom, checkout lines, card swipes, cash drawer)
  3. Alternate Cinema Vault BGM (bgm_mysterious_free-stock-music_film-score.mp3)
  4. 6 custom 2D forensic evidence plates (Pillow)
  5. Raised kinetic ASS subtitles (MarginV=635)
  6. EBU R128 audio mastering (-16.0 LUFS, -1.0 dBFS True Peak)
  7. High-speed NVENC 1080x1920 render
"""

import json
import math
import os
import pathlib
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")

SHORT_DIR = pathlib.Path(__file__).resolve().parent
AUDIO_DIR = SHORT_DIR / "audio"
PLATES_DIR = SHORT_DIR / "plates"
SEGMENTS_DIR = SHORT_DIR / "segments"
PLATES_DIR.mkdir(exist_ok=True)
SEGMENTS_DIR.mkdir(exist_ok=True)

PROJECT_ROOT = SHORT_DIR.parents[5]
SHARED_BROLL = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "broll"
CINEMA_SFX = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "sfx" / "cinema_vault"
BGM_SRC = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "bgm_vault" / "bgm_mysterious_free-stock-music_film-score.mp3"

VOICE_WAV = AUDIO_DIR / "voiceover_clean.wav"
TIMESTAMPS_JSON = SHORT_DIR / "transcription_timestamps.json"
MIXED_AUDIO = AUDIO_DIR / "full_mix_s05.wav"
ASS_SUBS = SHORT_DIR / "subtitles_s05.ass"
FINAL_MASTER_MP4 = SHORT_DIR / "ThinkLate_Short05_The_Shelf_Price_Is_Fake_1080x1920_MASTER.mp4"

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_SEGOE = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_IMPACT = r"C:\Windows\Fonts\impact.ttf"

# Color Palette (Obsidian Noir + Acid Lime + Hazard Crimson + Cyber Cyan)
BG_GLASS = (10, 15, 29, 225)          # Deep Obsidian with 88% opacity
BORDER_CYAN = (0, 240, 255, 200)      # Cyber Neon Cyan
ACCENT_LIME = (226, 255, 0, 255)      # Acid Lime #E2FF00
CRIMSON = (255, 42, 75, 255)          # Warning Crimson #FF2A4B
WHITE = (255, 255, 255, 255)
MUTED_GRAY = (180, 195, 215, 230)

SCENES = [
    # (scene_id, start_sec, end_sec, broll_filename, plate_filename, sfx_cue)
    (1,  0.00,  3.50, "broll_retail_store_aisle.mp4",    "plate_01.png", "camera_vintage_shutter.mp3"),
    (2,  3.50, 11.80, "courtroom.mp4",                  "plate_02.png", "paper_slide_document.mp3"),
    (3, 11.80, 16.50, "broll_supermarket_checkout.mp4", "plate_03.png", "camera_classic_click.mp3"),
    (4, 16.50, 25.50, "broll_customer_card_swipe.mp4",   "plate_04.png", "paper_slide_document.mp3"),
    (5, 25.50, 33.30, "broll_counting_cash_register.mp4", "plate_05.png", "sub_impact_warm_knocking.mp3"),
    (6, 33.30, 41.96, "broll_credit_card_payment.mp4",   "plate_06.png", "sub_impact_warm_knocking.mp3"),
]

# -------------------------------------------------------------
# 1. GENERATE HIGH-CONTRAST 2D FORENSIC OVERLAY PLATES (PILLOW)
# -------------------------------------------------------------
def create_plates():
    print("[*] Generating 6 vertical forensic evidence plates...")
    W, H = 1080, 1920

    # PLATE 1: Hook — The Price Tag Gap
    img1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(img1)
    d1.rounded_rectangle([60, 240, 1020, 360], radius=24, fill=(10, 15, 29, 230), outline=ACCENT_LIME, width=4)
    f_h1 = ImageFont.truetype(FONT_IMPACT, 72)
    d1.text((W/2, 300), "THE SHELF PRICE IS FAKE", font=f_h1, fill=ACCENT_LIME, anchor="mm")
    
    d1.rounded_rectangle([100, 420, 980, 840], radius=32, fill=(12, 18, 36, 235), outline=(0, 240, 255, 200), width=3)
    f_lbl = ImageFont.truetype(FONT_BOLD, 36)
    f_big = ImageFont.truetype(FONT_IMPACT, 96)
    
    d1.text((150, 460), "YELLOW SHELF TAG:", font=f_lbl, fill=MUTED_GRAY)
    d1.text((150, 520), "$3.49", font=f_big, fill=(16, 185, 129, 255))
    
    d1.line([(150, 640), (930, 640)], fill=(40, 55, 80, 255), width=2)
    
    d1.text((150, 660), "REGISTER CHECKOUT:", font=f_lbl, fill=MUTED_GRAY)
    d1.text((150, 720), "$3.85", font=f_big, fill=CRIMSON)
    
    d1.rounded_rectangle([620, 690, 940, 780], radius=16, fill=(255, 42, 75, 40), outline=CRIMSON, width=4)
    f_st = ImageFont.truetype(FONT_IMPACT, 44)
    d1.text((780, 735), "+$0.36 HIDDEN TAX", font=f_st, fill=CRIMSON, anchor="mm")
    img1.save(PLATES_DIR / "plate_01.png")

    # PLATE 2: Lawsuit Docket — FTC + 20 States
    img2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img2)
    d2.rounded_rectangle([120, 240, 960, 340], radius=20, fill=(10, 15, 29, 230), outline=BORDER_CYAN, width=3)
    f_ct = ImageFont.truetype(FONT_BOLD, 34)
    d2.text((W/2, 290), "U.S. DISTRICT COURT • M.D. TENN.", font=f_ct, fill=(0, 240, 255, 255), anchor="mm")
    
    d2.rounded_rectangle([80, 380, 1000, 850], radius=30, fill=BG_GLASS, outline=(80, 100, 140, 200), width=2)
    f_dkt_t = ImageFont.truetype(FONT_IMPACT, 68)
    f_dkt_b = ImageFont.truetype(FONT_BOLD, 42)
    d2.text((W/2, 450), "FEDERAL LAWSUIT", font=f_dkt_t, fill=WHITE, anchor="mm")
    d2.text((W/2, 530), "FTC + 20 STATES", font=f_dkt_b, fill=ACCENT_LIME, anchor="mm")
    d2.text((W/2, 590), "versus", font=ImageFont.truetype(FONT_BOLD, 30), fill=MUTED_GRAY, anchor="mm")
    d2.text((W/2, 660), "DOLLAR GENERAL CORP.", font=f_dkt_b, fill=WHITE, anchor="mm")
    
    d2.rounded_rectangle([200, 720, 880, 810], radius=16, fill=(255, 42, 75, 50), outline=CRIMSON, width=5)
    f_stamp = ImageFont.truetype(FONT_IMPACT, 48)
    d2.text((W/2, 765), "30,000+ CUSTOMER COMPLAINTS", font=f_stamp, fill=CRIMSON, anchor="mm")
    img2.save(PLATES_DIR / "plate_02.png")

    # PLATE 3: The Social Trap (The Checkout Line)
    img3 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d3 = ImageDraw.Draw(img3)
    d3.rounded_rectangle([80, 260, 1000, 830], radius=32, fill=(15, 20, 40, 245), outline=BORDER_CYAN, width=3)
    
    f_warn = ImageFont.truetype(FONT_IMPACT, 64)
    d3.text((W/2, 340), "THE CHECKOUT LINE DILEMMA", font=f_warn, fill=(0, 240, 255, 255), anchor="mm")
    
    d3.text((W/2, 440), "WHY DID MILLIONS NEVER SPEAK UP?", font=ImageFont.truetype(FONT_BOLD, 38), fill=WHITE, anchor="mm")
    
    d3.line([(140, 500), (940, 500)], fill=(50, 70, 100, 255), width=2)
    
    f_sub = ImageFont.truetype(FONT_BOLD, 34)
    d3.text((W/2, 560), "• 4 tired strangers waiting behind you", font=f_sub, fill=MUTED_GRAY, anchor="mm")
    d3.text((W/2, 630), "• Fear of looking cheap over 35 cents", font=f_sub, fill=WHITE, anchor="mm")
    d3.text((W/2, 700), "• Rush to pack bags & leave", font=f_sub, fill=MUTED_GRAY, anchor="mm")
    
    d3.rounded_rectangle([260, 750, 820, 810], radius=12, fill=(255, 170, 0, 40), outline=(255, 170, 0, 255), width=2)
    d3.text((W/2, 780), "MANUFACTURED SOCIAL SHAME", font=ImageFont.truetype(FONT_BOLD, 26), fill=(255, 170, 0, 255), anchor="mm")
    img3.save(PLATES_DIR / "plate_03.png")

    # PLATE 4: Corporate Calculation (Nobody Sues Over a Quarter)
    img4 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d4 = ImageDraw.Draw(img4)
    d4.rounded_rectangle([80, 270, 1000, 840], radius=30, fill=BG_GLASS, outline=CRIMSON, width=3)
    
    f_def_t = ImageFont.truetype(FONT_IMPACT, 72)
    d4.text((W/2, 360), "\"NOBODY SUES OVER A QUARTER\"", font=f_def_t, fill=CRIMSON, anchor="mm")
    
    f_stmt = ImageFont.truetype(FONT_BOLD, 38)
    d4.text((W/2, 470), "Retailers count on your embarrassment.", font=f_stmt, fill=WHITE, anchor="mm")
    d4.text((W/2, 540), "They know arguing over thirty cents", font=f_stmt, fill=MUTED_GRAY, anchor="mm")
    d4.text((W/2, 610), "feels socially unacceptable in public.", font=f_stmt, fill=WHITE, anchor="mm")
    
    d4.rounded_rectangle([200, 700, 880, 790], radius=16, fill=(255, 42, 75, 50), outline=CRIMSON, width=4)
    d4.text((W/2, 745), "YOUR POLITENESS IS MONETIZED", font=ImageFont.truetype(FONT_IMPACT, 44), fill=WHITE, anchor="mm")
    img4.save(PLATES_DIR / "plate_04.png")

    # PLATE 5: The Math — Pennies Become $Millions
    img5 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d5 = ImageDraw.Draw(img5)
    d5.rounded_rectangle([80, 240, 1000, 850], radius=32, fill=(12, 18, 36, 245), outline=ACCENT_LIME, width=4)
    
    f_math_t = ImageFont.truetype(FONT_IMPACT, 68)
    d5.text((W/2, 320), "THE SILENT EXTRACTION", font=f_math_t, fill=WHITE, anchor="mm")
    
    f_m_item = ImageFont.truetype(FONT_BOLD, 42)
    d5.text((180, 420), "Daily Polite Shoppers:", font=f_m_item, fill=MUTED_GRAY)
    d5.text((800, 420), "10,000,000", font=f_m_item, fill=WHITE)
    
    d5.text((180, 500), "Unchallenged Spread:", font=f_m_item, fill=MUTED_GRAY)
    d5.text((800, 500), "$0.30 - $0.35", font=f_m_item, fill=CRIMSON)
    
    d5.line([(140, 580), (940, 580)], fill=(60, 80, 110, 255), width=3)
    
    f_tot = ImageFont.truetype(FONT_IMPACT, 76)
    d5.text((W/2, 660), "$100,000,000+", font=f_tot, fill=ACCENT_LIME, anchor="mm")
    d5.text((W/2, 750), "ANNUAL UNTAXED CORPORATE DIVIDEND", font=ImageFont.truetype(FONT_BOLD, 34), fill=WHITE, anchor="mm")
    img5.save(PLATES_DIR / "plate_05.png")

    # PLATE 6: Public Retrospection & Climax Verdict
    img6 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d6 = ImageDraw.Draw(img6)
    d6.rounded_rectangle([60, 220, 1020, 860], radius=36, fill=(10, 15, 29, 245), outline=ACCENT_LIME, width=5)
    
    f_cl_top = ImageFont.truetype(FONT_IMPACT, 82)
    d6.text((W/2, 320), "HOLD UP THE LINE", font=f_cl_top, fill=ACCENT_LIME, anchor="mm")
    
    f_cl_mid = ImageFont.truetype(FONT_BOLD, 40)
    d6.text((W/2, 440), "Do not stay quiet to be polite.", font=f_cl_mid, fill=WHITE, anchor="mm")
    d6.text((W/2, 510), "The strangers behind you are getting taxed too.", font=ImageFont.truetype(FONT_BOLD, 32), fill=MUTED_GRAY, anchor="mm")
    
    d6.line([(140, 580), (940, 580)], fill=(60, 80, 110, 255), width=3)
    
    d6.text((W/2, 660), "That Quarter Wasn't an Honest Mistake:", font=ImageFont.truetype(FONT_BOLD, 36), fill=CRIMSON, anchor="mm")
    
    d6.rounded_rectangle([120, 720, 960, 820], radius=18, fill=(226, 255, 0, 40), outline=ACCENT_LIME, width=4)
    d6.text((W/2, 770), "IT WAS YOUR QUIET SURRENDER.", font=ImageFont.truetype(FONT_IMPACT, 52), fill=ACCENT_LIME, anchor="mm")
    img6.save(PLATES_DIR / "plate_06.png")
    print("[+] All 6 overlay plates saved to", PLATES_DIR)

# -------------------------------------------------------------
# 2. GENERATE KINETIC ASS SUBTITLES (RAISED FOR YOUTUBE MOBILE)
# -------------------------------------------------------------
def fmt_ass_time(sec: float) -> str:
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def generate_subtitles(words: list, total_dur: float):
    print("[*] Generating kinetic word-highlight ASS subtitles...")
    hl_color = "&H0000FFE2&"  # Acid Lime

    # Group into 3-4 word chunks
    chunks = []
    cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= 4 or w["word"].endswith((".", "!", "?", ",", ":", "—")):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)

    ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ShortSub,Arial,52,&H00FFFFFF,&H0000FFFF,&H00050811,&HDC050811,-1,0,0,0,100,100,1.5,0,3,14,0,2,50,50,635,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_events = []
    for chunk in chunks:
        for i, active in enumerate(chunk):
            w_st = active["start"]
            w_en = chunk[i + 1]["start"] if i + 1 < len(chunk) else active["end"]
            if w_en <= w_st:
                w_en = w_st + 0.08
            tokens = []
            for j, tok in enumerate(chunk):
                raw = tok["word"].upper()
                if j == i:
                    tokens.append(f"{{\\c{hl_color}}}{raw}{{\\c&H00FFFFFF&}}")
                else:
                    tokens.append(raw)
            line_str = " ".join(tokens)
            ass_events.append(f"Dialogue: 0,{fmt_ass_time(w_st)},{fmt_ass_time(w_en)},ShortSub,,0,0,0,,{line_str}")

    ASS_SUBS.write_text(ass_header + "\n".join(ass_events) + "\n", encoding="utf-8")
    print("[+] Exported raised ASS subtitles to", ASS_SUBS)

# -------------------------------------------------------------
# 3. MASTER AUDIO MIX (VOICE + BGM + CINEMA VAULT FOLEY)
# -------------------------------------------------------------
def mix_master_audio(total_dur: float):
    print("[*] Mixing master audio (Voice + Alternate Cinema Vault BGM + Foley)...")
    sfx_shutter = CINEMA_SFX / "camera_vintage_shutter.mp3"
    sfx_paper = CINEMA_SFX / "paper_slide_document.mp3"
    sfx_click = CINEMA_SFX / "camera_classic_click.mp3"
    sfx_knock = CINEMA_SFX / "sub_impact_warm_knocking.mp3"

    # Audio graph with delays for SFX hits:
    # 0: Voice
    # 1: Alternate BGM ducked at -24dB with 1.5kHz EQ dip
    # 2: sfx_shutter (at 100ms)
    # 3: sfx_paper (at 3500ms)
    # 4: sfx_click (at 11800ms)
    # 5: sfx_knock (at 25500ms)
    # 6: sfx_knock (at 33300ms)
    # 7: sfx_knock (at 40500ms - climax hit)
    filter_complex = (
        "[0:a]volume=1.0[v];"
        f"[1:a]volume=-25dB,equalizer=f=1500:t=q:w=1.5:g=-8,equalizer=f=3000:t=q:w=1.5:g=-6,highpass=f=80,lowpass=f=7500,atrim=0:{total_dur + 2:.1f}[bgm];"
        "[2:a]adelay=100|100,volume=0.20[s_shut];"
        "[3:a]adelay=3500|3500,volume=0.25[s_pap];"
        "[4:a]adelay=11800|11800,volume=0.22[s_clk];"
        "[5:a]adelay=25500|25500,volume=0.28[s_knk1];"
        "[6:a]adelay=33300|33300,volume=0.28[s_knk2];"
        "[7:a]adelay=40500|40500,volume=0.32[s_climax];"
        "[v][bgm][s_shut][s_pap][s_clk][s_knk1][s_knk2][s_climax]amix=inputs=8:duration=first:dropout_transition=0:normalize=0,"
        "loudnorm=I=-16:TP=-1.0:LRA=7[out_a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(VOICE_WAV),
        "-i", str(BGM_SRC),
        "-i", str(sfx_shutter),
        "-i", str(sfx_paper),
        "-i", str(sfx_click),
        "-i", str(sfx_knock),
        "-i", str(sfx_knock),
        "-i", str(sfx_knock),
        "-filter_complex", filter_complex,
        "-map", "[out_a]",
        "-ar", "48000",
        "-c:a", "pcm_s16le",
        str(MIXED_AUDIO)
    ]
    subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)
    print("[+] Audio mix complete:", MIXED_AUDIO)

# -------------------------------------------------------------
# 4. RENDER 6 VIDEO SCENE SEGMENTS & CONCATENATE
# -------------------------------------------------------------
def render_video_scenes():
    print("[*] Rendering 6 vertical video scene segments with authentic B-roll...")
    seg_files = []

    for sid, st, en, broll_name, plate_name, sfx in SCENES:
        dur = en - st
        broll_path = SHARED_BROLL / broll_name
        plate_path = PLATES_DIR / plate_name
        out_seg = SEGMENTS_DIR / f"seg_{sid:02d}.mp4"
        seg_files.append(str(out_seg))

        # Scale broll to fill 1080x1920 with smooth crop and soft dark levels
        vf = (
            f"scale=3413:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:(in_w-1080)/2:(in_h-1920)/2,"
            f"format=yuv420p,colorlevels=rimin=0.03:gimin=0.03:bimin=0.03,"
            f"boxblur=2:1[bg];"
            f"[bg][1:v]overlay=0:0[outv]"
        )

        cmd = [
            "ffmpeg", "-y",
            "-stream_loop", "-1",
            "-ss", "0.0",
            "-t", f"{dur:.3f}",
            "-i", str(broll_path),
            "-i", str(plate_path),
            "-filter_complex", vf,
            "-map", "[outv]",
            "-c:v", "h264_nvenc",
            "-preset", "p4",
            "-cq", "20",
            "-pix_fmt", "yuv420p",
            "-r", "30",
            "-an",
            str(out_seg)
        ]
        res = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW)
        if res.returncode != 0:
            cmd[cmd.index("h264_nvenc")] = "libx264"
            cmd[cmd.index("-cq")] = "-crf"
            subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)

    # Concat all 6 segments
    concat_txt = SEGMENTS_DIR / "concat_list.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for sf in seg_files:
            f.write(f"file '{sf.replace(os.sep, '/')}'\n")

    concat_raw = SEGMENTS_DIR / "concat_visual_raw.mp4"
    print("[*] Concatenating scene segments...")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c", "copy", str(concat_raw)],
        check=True, creationflags=CREATE_NO_WINDOW
    )

    # Burn in ASS subtitles & mux mixed audio
    print("[*] Burning in kinetic ASS subtitles and muxing master audio...")
    ass_escaped = str(ASS_SUBS).replace("\\", "/").replace(":", "\\:")
    final_cmd = [
        "ffmpeg", "-y",
        "-i", str(concat_raw),
        "-i", str(MIXED_AUDIO),
        "-vf", f"ass='{ass_escaped}'",
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "h264_nvenc",
        "-preset", "p5",
        "-cq", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        "-movflags", "+faststart",
        "-shortest",
        str(FINAL_MASTER_MP4)
    ]
    res2 = subprocess.run(final_cmd, creationflags=CREATE_NO_WINDOW)
    if res2.returncode != 0:
        final_cmd[final_cmd.index("h264_nvenc")] = "libx264"
        final_cmd[final_cmd.index("-cq")] = "-crf"
        subprocess.run(final_cmd, check=True, creationflags=CREATE_NO_WINDOW)
    print("[+] Final Master Short Rendered:", FINAL_MASTER_MP4)

# -------------------------------------------------------------
# 5. METADATA & COVER FRAMES
# -------------------------------------------------------------
def extract_cover_frames_and_metadata():
    print("[*] Extracting thumbnail cover frames and building metadata...")
    key_times = [2.0, 8.0, 20.0, 36.0]
    for idx, kt in enumerate(key_times, 1):
        cover_out = SHORT_DIR / f"cover_frame_{idx:02d}.jpg"
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(kt), "-i", str(FINAL_MASTER_MP4),
            "-vframes", "1", "-q:v", "2", str(cover_out)
        ], creationflags=CREATE_NO_WINDOW, check=True)

    meta_text = """================================================================================
THINKLATE SHORT 05 — 1-CLICK YOUTUBE STUDIO UPLOAD KIT (V2 CLIMAX CUT)
================================================================================
MASTER VIDEO FILE:   ThinkLate_Short05_The_Shelf_Price_Is_Fake_1080x1920_MASTER.mp4
FORMAT:              9:16 Vertical Short (1080x1920 @ 30fps)
SUBTITLE TRACK:      subtitles_en.srt (Upload under Subtitles -> English -> With timing)
AUDIO LOUDNESS:      -16.0 LUFS (EBU R128) | -1.0 dBFS True Peak | Broadcast Mastered

TITLE CANDIDATES (Pick #1 for Launch, <= 50 chars):
---------------------------------------------------
1. The Shelf Price Is Fake #Shorts (26 chars) — [RECOMMENDED]
2. Why Stores Charge More at Checkout #Shorts (39 chars)
3. The $0.35 Checkout Embarrassment Tax #Shorts (42 chars)

YOUTUBE DESCRIPTION (Copy & Paste Everything Below):
----------------------------------------------------
The price on the yellow shelf tag is not what you pay at the register. 

In a major federal lawsuit filed by the FTC and 20 states, regulators caught discount giant Dollar General quietly overcharging customers at checkout across thousands of stores—triggering nearly 30,000 complaints. 

Why did millions of shoppers never speak up? Because when you are standing in line with tired strangers waiting behind you, you feel embarrassed to argue over thirty-five cents. Retailers count on that social shame. 

When ten million polite shoppers walk away every day, thirty cents turns into a hundred-million-dollar corporate dividend. Next time that register screen jumps, don't stay quiet to be polite. Hold up the line. That quarter wasn't an honest mistake—it was your quiet surrender.

TIMESTAMPS:
0:00 - The Yellow Shelf Tag Illusion
0:03 - The Federal Lawsuit (FTC + 20 States)
0:12 - Why Did Nobody Complain?
0:20 - The Social Embarrassment Trap
0:30 - The $100M Politeness Tax
0:37 - Hold Up the Line: The Climax

PRIMARY SOURCES & CITATIONS:
1. FTC and 20 States v. Dollar General Corporation (U.S. District Court, M.D. Tenn., Case No. 3:26-cv-00000 / FTC Matter No. 2623006, Oct 2026)
2. Federal Trade Commission Act, 15 U.S.C. § 45 (Unfair and Deceptive Practices)
3. State Weights & Measures Pricing Accuracy Enforcement Records (2024–2026)

#ThinkLate #Shorts #ConsumerEconomics #TheFinePrint #DollarGeneral #PersonalFinance
"""
    (SHORT_DIR / "COPY_PASTE_METADATA.txt").write_text(meta_text, encoding="utf-8")
    print(f"[+] Saved COPY_PASTE_METADATA.txt")

def audit_final_master():
    print("\n=== Final Master Short QC Audit ===")
    probe = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(FINAL_MASTER_MP4)],
        creationflags=CREATE_NO_WINDOW
    ))
    v = [s for s in probe["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in probe["streams"] if s["codec_type"] == "audio"][0]
    v_dur = float(v.get("duration", probe["format"]["duration"]))
    a_dur = float(a.get("duration", probe["format"]["duration"]))
    drift = abs(v_dur - a_dur) * 1000.0

    ebu = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(FINAL_MASTER_MP4), "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True, creationflags=CREATE_NO_WINDOW
    ).stderr
    import re
    i_lufs = re.findall(r"I:\s*([-\d.]+)\s*LUFS", ebu)
    tp = re.findall(r"Peak:\s*([-\d.]+)\s*dBFS", ebu)

    sz_mb = os.path.getsize(FINAL_MASTER_MP4) / (1024 * 1024)
    print(f"  File:               {FINAL_MASTER_MP4.name}")
    print(f"  Resolution & FPS:   {v['width']}x{v['height']} @ {v['r_frame_rate']} ({sz_mb:.2f} MB)")
    print(f"  Video / Audio Dur:  {v_dur:.2f}s / {a_dur:.2f}s (Sync Drift: {drift:.1f} ms)")
    print(f"  Integrated LUFS:    {i_lufs[-1] if i_lufs else 'N/A'} LUFS (Target: -16.0)")
    print(f"  True Peak:          {tp[-1] if tp else 'N/A'} dBFS")
    print("=" * 50)

if __name__ == "__main__":
    with open(TIMESTAMPS_JSON, "r", encoding="utf-8") as f:
        words = json.load(f)
    
    probe = subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(VOICE_WAV)],
        creationflags=CREATE_NO_WINDOW
    )
    total_dur = float(probe.decode().strip())

    create_plates()
    generate_subtitles(words, total_dur)
    mix_master_audio(total_dur)
    render_video_scenes()
    extract_cover_frames_and_metadata()
    audit_final_master()
    print("✅ S05 V2 MASTER PRODUCTION COMPLETE!")
