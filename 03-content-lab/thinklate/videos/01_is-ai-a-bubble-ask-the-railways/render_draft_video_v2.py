import os, subprocess

FFMPEG = r'C:\Users\sar1s\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe'
FFPROBE = r'C:\Users\sar1s\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffprobe.exe'

BASE_DIR = 'videos/01_is-ai-a-bubble-ask-the-railways'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
AUDIO_DIR = os.path.join(BASE_DIR, 'audio_takes')
TEMP_DIR = os.path.join(BASE_DIR, 'temp_segments_v2')
os.makedirs(TEMP_DIR, exist_ok=True)

DRONE_AUDIO = os.path.join(AUDIO_DIR, 'ambient_drone.wav')
WHOOSH_SFX = os.path.join(AUDIO_DIR, 'transition_whoosh.wav')

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
    
    p = subprocess.run([FFPROBE, '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_path], capture_output=True, text=True)
    dur = float(p.stdout.strip()) + 0.4
    frames = int(dur * 25)
    
    print(f'Rendering Animated Segment {num:02d} ({dur:.2f}s, {frames} frames)...')
    
    # Smooth continuous Ken Burns slow push: zoom from 1.0 to 1.05 over the duration
    # zoompan filter with 25fps at 1920x1080
    zoom_step = 0.05 / max(frames, 1)
    vf_filter = (
        f"scale=2112:1188,format=yuv420p,"
        f"zoompan=z='min(zoom+{zoom_step:.6f},1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=25"
    )
    
    cmd = [
        FFMPEG, '-y',
        '-loop', '1', '-i', img_path,
        '-i', audio_path,
        '-c:v', 'libx264', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k',
        '-t', str(dur),
        '-vf', vf_filter,
        '-shortest',
        out_segment
    ]
    subprocess.run(cmd, check=True)
    segment_files.append(out_segment)

# Concat video
concat_txt = os.path.join(TEMP_DIR, 'concat.txt')
with open(concat_txt, 'w', encoding='utf-8') as f:
    for seg in segment_files:
        f.write(f"file '{os.path.abspath(seg).replace(chr(92), '/')}'\n")

raw_concat_mp4 = os.path.join(TEMP_DIR, 'raw_concat.mp4')
print('Concatenating video segments...')
subprocess.run([
    FFMPEG, '-y',
    '-f', 'concat', '-safe', '0',
    '-i', concat_txt,
    '-c', 'copy',
    raw_concat_mp4
], check=True)

# Now mix audio: Voiceover + Ambient Drone at -22dB
final_mp4 = os.path.join(BASE_DIR, 'draft_video_v2_cinematic.mp4')
print('Mixing atmospheric background music and mastering final video...')

# Filter complex:
# [0:a] is voiceover, [1:a] is ambient drone ducked to 0.08 volume (-22dB)
audio_filter = "[0:a]volume=1.0[v0];[1:a]volume=0.08[bg0];[v0][bg0]amix=inputs=2:duration=first:dropout_transition=2[aout]"

cmd_mix = [
    FFMPEG, '-y',
    '-i', raw_concat_mp4,
    '-i', DRONE_AUDIO,
    '-c:v', 'copy',
    '-filter_complex', audio_filter,
    '-map', '0:v',
    '-map', '[aout]',
    '-c:a', 'aac', '-b:a', '192k',
    '-shortest',
    final_mp4
]
subprocess.run(cmd_mix, check=True)
print(f'SUCCESS! Cinematic draft video with ambient soundscape rendered at: {final_mp4}')
