import os
import subprocess

VIDEO_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")

VOICE_FILE = os.path.join(AUDIO_DIR, "dual_voice_mastered.wav")
AMBIENT_BED_WAV = os.path.join(AUDIO_DIR, "ambient_bed_track.wav")
FULL_MIX_MP3 = os.path.join(AUDIO_DIR, "dual_full_mix_preview.mp3")
FULL_MIX_WAV = os.path.join(AUDIO_DIR, "dual_full_mix_preview.wav")

flags = 0x08000000

print("Mixing Dual-Voice Voiceover (George + Andrew @ 90%) + Ambient BGM bed (-16.5 dB)...")
cmd_mix = [
    "ffmpeg", "-y",
    "-i", VOICE_FILE,
    "-i", AMBIENT_BED_WAV,
    "-filter_complex", "[0:a]volume=0.90[v];[1:a]volume=0.15[bgm];[v][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0",
    "-b:a", "192k",
    FULL_MIX_MP3
]
subprocess.run(cmd_mix, check=True, creationflags=flags)

cmd_mix_wav = [
    "ffmpeg", "-y",
    "-i", VOICE_FILE,
    "-i", AMBIENT_BED_WAV,
    "-filter_complex", "[0:a]volume=0.90[v];[1:a]volume=0.15[bgm];[v][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0",
    "-ar", "48000", "-c:a", "pcm_s24le",
    FULL_MIX_WAV
]
subprocess.run(cmd_mix_wav, check=True, creationflags=flags)
print(f"SUCCESS: Dual-Voice Broadcast Master Mixed!")
print(f"  MP3: {FULL_MIX_MP3} ({os.path.getsize(FULL_MIX_MP3):,} bytes)")
print(f"  WAV: {FULL_MIX_WAV} ({os.path.getsize(FULL_MIX_WAV):,} bytes)")

