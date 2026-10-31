import os
import subprocess

src = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
out_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\assets\action_gameplay_clips"
os.makedirs(out_dir, exist_ok=True)

# Define 16 high action segments from ACBF_Gameplay_2 (avoiding menus, cutscenes, or dark pauses)
# Each segment is 45-60 seconds of high-energy naval battle, cannon broadsides, boarding, or sailing.
CLIPS = [
    ("action_01_sea_sailing.mp4", 15, 50),
    ("action_02_naval_patrol.mp4", 80, 50),
    ("action_03_ocean_waves.mp4", 150, 50),
    ("action_04_fleet_approach.mp4", 620, 50),
    ("action_05_naval_maneuver.mp4", 690, 50),
    ("action_06_combat_ready.mp4", 860, 50),
    ("action_07_broadside_run.mp4", 930, 50),
    ("action_08_cannon_barrage.mp4", 1000, 50),
    ("action_09_ship_chase.mp4", 1080, 50),
    ("action_10_boarding_prep.mp4", 1160, 50),
    ("action_11_high_seas_piracy.mp4", 1280, 50),
    ("action_12_deck_combat.mp4", 1360, 50),
    ("action_13_sunny_caribbean.mp4", 1760, 50),
    ("action_14_island_raid.mp4", 1840, 50),
    ("action_15_storm_sailing.mp4", 2500, 50),
    ("action_16_final_broadside.mp4", 2700, 50),
]

print("Extracting 16 high-action clips (1080p, 30fps, audio muted)...")
for fname, ss, dur in CLIPS:
    out_path = os.path.join(out_dir, fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100000:
        print(f"Already exists: {fname}")
        continue
    # Re-encode to standard 1080p 30fps without audio (-an)
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(ss),
        "-i", src,
        "-t", str(dur),
        "-an",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30",
        "-c:v", "h264_nvenc",
        "-preset", "p4",
        "-b:v", "6M",
        "-pix_fmt", "yuv420p",
        out_path
    ]
    subprocess.run(cmd, creationflags=0x08000000, check=True)
    print(f"Extracted: {fname} ({os.path.getsize(out_path)} bytes)")

print("All 16 action gameplay clips ready!")

