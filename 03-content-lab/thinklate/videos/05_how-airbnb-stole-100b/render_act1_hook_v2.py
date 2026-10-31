import os
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
os.chdir(BASE_DIR)

scene1 = "assets/generative_broll/scene_01_eviction_door.jpg"
scene2 = "assets/generative_broll/scene_02_real_founders_archive.jpg"
scene3 = "assets/generative_broll/scene_03_hotel_no_vacancy.jpg"
stock_city = "assets/documentary_broll/scene1_01_city_apartments.mp4"
gameplay = "assets/action_gameplay_clips/action_01_sea_sailing.mp4"
AUDIO_SRC = "audio_takes/dual_full_mix_preview_plus15.wav"
OUTPUT_MP4 = "ThinkLate_Video05_Act1_Hook_Revamp_60s.mp4"

font_impact = "assets/fonts/impact.ttf"
font_arial = "assets/fonts/arialbd.ttf"

# FFmpeg filter complex:
# Master audio is George (+15% speed) + Andrew (+14.5% speed) with -16.5 dB BGM.
# All still plates are 100% rock-solid static (ZERO SHAKE).
# All kinetic typography is dead-center stacked.

filter_complex = (
    # Scene 1: Weathered Door (0 to 7.0s) - Dynamic Warning Typography
    f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1,"
    f"drawtext=fontfile={font_impact}:text='\\$1,100 RENT DUE':"
    f"fontsize=88:fontcolor=white:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.75:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-100:enable='between(t, 0.4, 7.0)',"
    f"drawtext=fontfile={font_impact}:text='3 DAYS UNTIL EVICTION':"
    f"fontsize=82:fontcolor=0xFF3B30:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=0x1C0000@0.85:boxborderw=16:"
    f"x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t, 2.0, 7.0)',"
    f"drawtext=fontfile={font_impact}:text='\\$0 BANK BALANCE':"
    f"fontsize=88:fontcolor=0xFFCC00:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.75:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+100:enable='between(t, 4.5, 7.0)'[v0];"

    # Scene 2: Real Founders Archive (7.0 to 21.0s) - Archival Story Card
    f"[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1,"
    f"drawtext=fontfile={font_impact}:text='UNEMPLOYED & SCRAMBLING':"
    f"fontsize=84:fontcolor=0xFF453A:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.80:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-55:enable='between(t, 6.5, 14.0)',"
    f"drawtext=fontfile={font_arial}:text='EMPTY LIVING ROOM • \\$0 INCOME':"
    f"fontsize=50:fontcolor=white:shadowcolor=black@0.90:shadowx=4:shadowy=4:box=1:boxcolor=0x151515@0.85:boxborderw=16:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+55:enable='between(t, 8.5, 14.0)'[v1];"

    # Scene 3: Hotel Lobby (21.0 to 30.0s) - 9.0s 100% STATIC (ZERO SHAKE) + High-Contrast Alert
    f"[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1,"
    f"drawtext=fontfile={font_impact}:text='DESIGN CONFERENCE FLOODS IN':"
    f"fontsize=78:fontcolor=0xFFD60A:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.80:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-60:enable='between(t, 0.5, 9.0)',"
    f"drawtext=fontfile={font_impact}:text='HOTELS 100% SOLD OUT':"
    f"fontsize=90:fontcolor=white:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=0xCC1100@0.90:boxborderw=22:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+50:enable='between(t, 3.8, 9.0)'[v2];"

    # Scene 4: 4K Drone City Sweep (30.0 to 43.0s) - 13.0s + Dynamic Contrast Stack
    f"[3:v]trim=0:13.0,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1,"
    f"drawtext=fontfile={font_impact}:text='THE EMERGENCY HUSTLE':"
    f"fontsize=82:fontcolor=white:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.80:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-95:enable='between(t, 0.5, 13.0)',"
    f"drawtext=fontfile={font_arial}:text='3 CHEAP BLUE AIR MATTRESSES':"
    f"fontsize=52:fontcolor=0x64D2FF:shadowcolor=black@0.90:shadowx=4:shadowy=4:box=1:boxcolor=0x001B3A@0.85:boxborderw=16:"
    f"x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t, 3.0, 13.0)',"
    f"drawtext=fontfile={font_impact}:text='\\$80 / NIGHT + POP-TARTS':"
    f"fontsize=86:fontcolor=0x30D158:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=0x052A0F@0.85:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+95:enable='between(t, 6.5, 13.0)'[v3];"

    # Scene 5: Living Gameplay Canvas Spine (43.0 to 55.0s) - 12.0s + Dynamic Climax Slam (NO BROKEN EMOJI)
    f"[4:v]trim=0:12.0,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=6:1,fps=30,setsar=1,"
    f"drawtext=fontfile={font_impact}:text='\\$80 FLOOR HUSTLE':"
    f"fontsize=84:fontcolor=white:shadowcolor=black@0.95:shadowx=5:shadowy=5:box=1:boxcolor=black@0.80:boxborderw=18:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-65:enable='between(t, 0.5, 12.0)',"
    f"drawtext=fontfile={font_impact}:text='TURNS INTO \\$100 BILLION EMPIRE':"
    f"fontsize=84:fontcolor=0x30D158:shadowcolor=black@0.95:shadowx=6:shadowy=6:box=1:boxcolor=0x052A0F@0.90:boxborderw=22:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+55:enable='between(t, 2.8, 12.0)'[v4];"

    # Concatenate all 5 video segments (7 + 14 + 9 + 13 + 12 = 55.0s)
    f"[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v_out]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "7.0", "-i", scene1,
    "-loop", "1", "-t", "14.0", "-i", scene2,
    "-loop", "1", "-t", "9.0", "-i", scene3,
    "-i", stock_city,
    "-i", gameplay,
    "-ss", "0", "-t", "55.0", "-i", AUDIO_SRC,
    "-filter_complex", filter_complex,
    "-map", "[v_out]",
    "-map", "5:a",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-t", "55.0",
    OUTPUT_MP4
]

print("Executing FFmpeg rendering with George (+15%) & Center Stacked Typography...")
CREATE_NO_WINDOW = 0x08000000
proc = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)

if proc.returncode == 0:
    print(f"Render SUCCESS! Saved to: {OUTPUT_MP4}")
    print(f"File size: {os.path.getsize(OUTPUT_MP4) / 1024 / 1024:.2f} MB")
else:
    print("Render FAILED!")
    print(proc.stderr[-1000:])
