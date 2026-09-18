import os, subprocess, glob

FFMPEG = r'C:\Users\sar1s\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe'
FFPROBE = r'C:\Users\sar1s\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffprobe.exe'

BASE_DIR = 'videos/01_is-ai-a-bubble-ask-the-railways'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
AUDIO_DIR = os.path.join(BASE_DIR, 'audio_takes')
TEMP_DIR = os.path.join(BASE_DIR, 'temp_segments')
os.makedirs(TEMP_DIR, exist_ok=True)

scenes = [
    (1, os.path.join(ASSETS_DIR, 'A1_datacenter_exterior.png')),
    (2, os.path.join(ASSETS_DIR, 'S04_title.png')),
    (3, os.path.join(ASSETS_DIR, 'A2_tech_workspace.png')),
    (4, os.path.join(ASSETS_DIR, 'S04_evidence_ssrn_mania.png')),
    (5, os.path.join(ASSETS_DIR, 'evidence_gdp_odlyzko.png')),
    (6, os.path.join(ASSETS_DIR, 'S06_evidence_ssrn_measures.png')),
    (7, os.path.join(ASSETS_DIR, 'S07_evidence_historical_share.png')),
    (8, os.path.join(ASSETS_DIR, 'S08_evidence_disaster_utility.png')),
    (9, os.path.join(ASSETS_DIR, 'S09_lt_pattern.png')),
    (10, os.path.join(ASSETS_DIR, 'S10_evidence_1830s_paradox.png')),
    (11, os.path.join(ASSETS_DIR, 'S11_evidence_goldman_report.png')),
    (12, os.path.join(ASSETS_DIR, 'S12_evidence_sequoia_chart.png')),
    (13, os.path.join(ASSETS_DIR, 'S13_endcard.png')),
]

segment_files = []

for num, img_path in scenes:
    audio_path = os.path.join(AUDIO_DIR, f'take_{num:02d}.mp3')
    out_segment = os.path.join(TEMP_DIR, f'seg_{num:02d}.mp4')
    
    # Get audio duration
    p = subprocess.run([FFPROBE, '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_path], capture_output=True, text=True)
    dur = float(p.stdout.strip()) + 0.5 # 0.5s pad
    
    print(f'Rendering Segment {num:02d} (Duration: {dur:.2f}s)...')
    
    # Subtle Ken Burns push in: zoompan filter
    # For speed and stability on stills, scale to 1920x1080 and pad
    cmd = [
        FFMPEG, '-y',
        '-loop', '1', '-i', img_path,
        '-i', audio_path,
        '-c:v', 'libx264', '-tune', 'stillimage', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k',
        '-t', str(dur),
        '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p',
        '-shortest',
        out_segment
    ]
    subprocess.run(cmd, check=True)
    segment_files.append(out_segment)

# Concat all segments
concat_txt = os.path.join(TEMP_DIR, 'concat.txt')
with open(concat_txt, 'w', encoding='utf-8') as f:
    for seg in segment_files:
        # ffmpeg concat demuxer needs forward slashes
        f.write(f"file '{os.path.abspath(seg).replace(chr(92), '/')}'\n")

final_mp4 = os.path.join(BASE_DIR, 'draft_video_v1.mp4')
print('Concatenating full video...')
subprocess.run([
    FFMPEG, '-y',
    '-f', 'concat', '-safe', '0',
    '-i', concat_txt,
    '-c', 'copy',
    final_mp4
], check=True)

print(f'SUCCESS! Master draft video rendered at: {final_mp4}')
