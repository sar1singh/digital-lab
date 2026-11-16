import subprocess
import os

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")

# 1. Inputs
george_raw = os.path.join(AUDIO_DIR, "act1_george_speed_114.mp3") # George Hook +15%
andrew_src = os.path.join(AUDIO_DIR, "fallback_andrew", "voice_mastered.wav") # Original Andrew Master
bgm_src = os.path.join(BASE_DIR, "assets", "audio", "ambient_music_dark_fog.mp3")

# 2. Intermediate files
george_48k = os.path.join(AUDIO_DIR, "act1_george_115_48k.wav")
andrew_act2_raw = os.path.join(AUDIO_DIR, "act2_andrew_raw.wav")
andrew_act2_115_48k = os.path.join(AUDIO_DIR, "act2_andrew_115_48k.wav")

# 3. Final outputs
master_voice = os.path.join(AUDIO_DIR, "dual_voice_mastered_plus15.wav")
master_mix_wav = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
master_mix_mp3 = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.mp3")

CREATE_NO_WINDOW = 0x08000000

print("Step 1: Converting George Hook (+15%) to 48kHz 24-bit stereo...")
subprocess.run([
    "ffmpeg", "-y", "-i", george_raw,
    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le",
    george_48k
], creationflags=CREATE_NO_WINDOW, check=True)

print("Step 2: Slicing Andrew Acts 2-8 from master (starting at 154.04s) and accelerating +14.5% via atempo...")
subprocess.run([
    "ffmpeg", "-y", "-ss", "154.04", "-i", andrew_src,
    "-filter:a", "atempo=1.145",
    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le",
    andrew_act2_115_48k
], creationflags=CREATE_NO_WINDOW, check=True)

print("Step 3: Splicing George Hook + Andrew Deep Dive into master voice track...")
concat_list = os.path.join(AUDIO_DIR, "concat_dual_115.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{os.path.basename(george_48k)}'\n")
    f.write(f"file '{os.path.basename(andrew_act2_115_48k)}'\n")

subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
    "-c:a", "pcm_s24le",
    master_voice
], creationflags=CREATE_NO_WINDOW, check=True)

print("Step 4: Mixing with voice pushed forward (+5 dB) and BGM tucked in background (-26 dB) with vocal EQ pocket...")
# Voice at 1.8 (+5.1 dB boost for broadcast dialogue clarity)
# BGM at 0.045 with -6 dB dip at 1.5 kHz so it NEVER clashes with vocal fundamentals
# normalize=0 guarantees FFmpeg amix DOES NOT halve voiceover volume!
cmd_mix = [
    "ffmpeg", "-y",
    "-i", master_voice,
    "-stream_loop", "-1", "-i", bgm_src,
    "-filter_complex",
    "[0:a]volume=1.8[v];[1:a]volume=0.045,equalizer=f=1500:t=q:w=1.5:g=-6[bgm];[v][bgm]amix=inputs=2:duration=first:normalize=0[a_out]",
    "-map", "[a_out]",
    "-c:a", "pcm_s24le",
    master_mix_wav
]
subprocess.run(cmd_mix, creationflags=CREATE_NO_WINDOW, check=True)

# Also generate high-quality MP3 (128k) strictly under 20MB for direct in-IDE playback
subprocess.run([
    "ffmpeg", "-y", "-i", master_mix_wav,
    "-b:a", "128k",
    master_mix_mp3
], creationflags=CREATE_NO_WINDOW, check=True)

def get_dur(p):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', p]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())

dur = get_dur(master_mix_wav)
mins = int(dur // 60)
secs = int(dur % 60)
print(f"Master accelerated audio generated successfully!")
print(f"Total Duration: {mins}m {secs}s ({dur:.2f}s)")
print(f"Saved: {master_mix_mp3} ({os.path.getsize(master_mix_mp3) / 1024 / 1024:.2f} MB)")
