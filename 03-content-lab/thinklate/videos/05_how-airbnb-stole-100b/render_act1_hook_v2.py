import os
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
os.chdir(BASE_DIR)

# Relative asset paths
scene1 = "assets/generative_broll/scene_01_eviction_door.jpg"
scene2 = "assets/generative_broll/scene_02_broke_designers_floor.jpg"
scene3 = "assets/generative_broll/scene_03_hotel_no_vacancy.jpg"
stock_city = "assets/documentary_broll/scene1_01_city_apartments.mp4"
gameplay = "assets/action_gameplay_clips/action_01_sea_sailing.mp4"
AUDIO_SRC = "audio_takes/dual_full_mix_preview.wav"
OUTPUT_MP4 = "ThinkLate_Video05_Act1_Hook_Revamp_60s.mp4"

font_impact = "assets/fonts/impact.ttf"
font_arial = "assets/fonts/arialbd.ttf"

# FFmpeg filter complex:
# [v0] Scene 1 (0 to 8s): 240 frames @ 30fps
# [v1] Scene 2 (8 to 24s): 480 frames @ 30fps
# [v2] Scene 3 (24 to 34.5s): 315 frames @ 30fps
# [v3] Stock keys (34.5 to 49s): 14.5s
# [v4] Gameplay Canvas (49 to 60s): 11s

filter_complex = (
    # Scene 1: Eviction door with slow Ken Burns push + 3-stage typography
    f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
    f"zoompan=z='min(zoom+0.0015,1.15)':d=240:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
    f"drawtext=fontfile={font_impact}:text='\\$1,100 RENT DUE':fontcolor=white:fontsize=76:x=(w-text_w)/2:y=h-220:box=1:boxcolor=black@0.75:boxborderw=20:enable='between(t,0.5,2.3)',"
    f"drawtext=fontfile={font_impact}:text='3 DAYS UNTIL EVICTION':fontcolor=0xFF3B30:fontsize=72:x=(w-text_w)/2:y=h-220:box=1:boxcolor=black@0.75:boxborderw=20:enable='between(t,2.3,5.2)',"
    f"drawtext=fontfile={font_impact}:text='\\$0 BANK BALANCE':fontcolor=0xFFCC00:fontsize=76:x=(w-text_w)/2:y=h-220:box=1:boxcolor=black@0.75:boxborderw=20:enable='between(t,5.2,8.0)'[v0];"

    # Scene 2: Loft floor slow pan + typography
    f"[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
    f"zoompan=z='min(zoom+0.0008,1.10)':d=480:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
    f"drawtext=fontfile={font_impact}:text='SAN FRANCISCO - OCT 2007':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,0,7.5)',"
    f"drawtext=fontfile={font_arial}:text='BRIAN CHESKY & JOE GEBBIA':fontcolor=0x30D158:fontsize=48:x=(w-text_w)/2:y=h-150:box=1:boxcolor=black@0.7:boxborderw=14:enable='between(t,0,7.5)',"
    f"drawtext=fontfile={font_impact}:text='UNEMPLOYED & BROKE':fontcolor=0xFF453A:fontsize=68:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,7.5,16.0)',"
    f"drawtext=fontfile={font_arial}:text='EMPTY LIVING ROOM - \\$0 INCOME':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=h-150:box=1:boxcolor=black@0.7:boxborderw=14:enable='between(t,7.5,16.0)'[v1];"

    # Scene 3: Hotel lobby + brass NO VACANCY
    f"[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
    f"zoompan=z='min(zoom+0.0012,1.12)':d=315:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
    f"drawtext=fontfile={font_impact}:text='DESIGN CONFERENCE FLOODS IN':fontcolor=0xFFCC00:fontsize=64:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,0,5.2)',"
    f"drawtext=fontfile={font_impact}:text='HOTELS 100% SOLD OUT':fontcolor=0xFF3B30:fontsize=72:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=20:enable='between(t,5.2,10.5)',"
    f"drawtext=fontfile={font_arial}:text='ZERO VACANCY IN ENTIRE CITY':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=h-150:box=1:boxcolor=black@0.7:boxborderw=14:enable='between(t,5.2,10.5)'[v2];"

    # Scene 4: Real stock B-roll (apartment keys) - 14.5s
    f"[3:v]trim=0:14.5,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,"
    f"drawtext=fontfile={font_impact}:text='THE EMERGENCY HUSTLE':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,0,8.0)',"
    f"drawtext=fontfile={font_arial}:text='3 CHEAP BLUE AIR MATTRESSES':fontcolor=0x0A84FF:fontsize=50:x=(w-text_w)/2:y=h-150:box=1:boxcolor=black@0.7:boxborderw=14:enable='between(t,0,8.0)',"
    f"drawtext=fontfile={font_impact}:text='\\$80 / NIGHT + POP-TARTS':fontcolor=0x30D158:fontsize=68:x=(w-text_w)/2:y=h-240:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,8.0,14.5)'[v3];"

    # Scene 5: Living Gameplay Canvas Spine (Track 1 with subtle blur) - 11.0s
    f"[4:v]trim=0:11.0,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=6:1,fps=30,"
    f"drawtext=fontfile={font_impact}:text='\\$80 FLOOR HUSTLE':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=h-300:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,0,7.0)',"
    f"drawtext=fontfile={font_impact}:text='-> \\$100 BILLION EMPIRE':fontcolor=0x30D158:fontsize=76:x=(w-text_w)/2:y=h-200:box=1:boxcolor=black@0.75:boxborderw=20:enable='between(t,0,7.0)',"
    f"drawtext=fontfile={font_impact}:text='THE 3 SURVIVAL MOVES':fontcolor=0xFFCC00:fontsize=68:x=(w-text_w)/2:y=h-220:box=1:boxcolor=black@0.75:boxborderw=18:enable='between(t,7.0,11.0)'[v4];"

    # Concatenate all 5 video segments
    f"[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v_out]"
)

# Notice: NO '-loop 1' on image inputs [0:v], [1:v], [2:v]!
cmd = [
    "ffmpeg", "-y",
    "-i", scene1,
    "-i", scene2,
    "-i", scene3,
    "-i", stock_city,
    "-i", gameplay,
    "-ss", "0", "-t", "60.0", "-i", AUDIO_SRC,
    "-filter_complex", filter_complex,
    "-map", "[v_out]",
    "-map", "5:a",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-t", "60.0",
    OUTPUT_MP4
]

print("Executing FFmpeg rendering for Act 1 Hook (60s proof-of-concept)...")
CREATE_NO_WINDOW = 0x08000000
proc = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)

if proc.returncode == 0:
    print(f"Render SUCCESS! Saved to: {OUTPUT_MP4}")
    print(f"File size: {os.path.getsize(OUTPUT_MP4) / 1024 / 1024:.2f} MB")
else:
    print("Render FAILED!")
    print(proc.stderr[-1000:])
