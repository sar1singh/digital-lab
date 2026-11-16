import os
import subprocess

AUDIO_DIR = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/longForm/L06_the-memory-lie/assets/audio")
TAKE_01 = os.path.join(AUDIO_DIR, "takes", "take_01_owl.wav")
BGM_SRC = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/shortForm/S01_ai-energy-shock/assets/audio/ambient_music_dark_fog.mp3")
CINEMA_SFX = os.path.abspath("digital-lab/03-content-lab/shared/assets/sfx/cinema_vault/sub_impact_deep_cinematic.mp3")
SHORT_MIX = os.path.join(AUDIO_DIR, "short01_mix.wav")

cmd = [
    "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", TAKE_01
]
dur = float(subprocess.check_output(cmd).decode().strip())
print(f"Take 1 duration: {dur:.2f}s")

# Mix dialogue, ducked BGM, and gavel at 3.5s
mix_cmd = [
    "ffmpeg", "-y",
    "-i", TAKE_01,
    "-stream_loop", "-1", "-i", BGM_SRC,
    "-i", CINEMA_SFX,
    "-filter_complex", (
        "[0:a]volume=1.0[vocal];"
        f"[1:a]atrim=0:{dur},volume=-24dB,equalizer=f=1500:t=q:w=1.5:g=-6,afade=t=out:st={dur-1.5}:d=1.5[bgm];"
        "[2:a]adelay=3500|3500,volume=-12dB,lowpass=f=8000[sfx];"
        "[vocal][bgm][sfx]amix=inputs=3:duration=first:dropout_transition=1:normalize=0[mixed];"
        "[mixed]loudnorm=I=-16.5:TP=-1.0:LRA=7[out]"
    ),
    "-map", "[out]",
    "-ar", "48000", "-ac", "2",
    SHORT_MIX
]
subprocess.run(mix_cmd, creationflags=0x08000000, check=True)
print(f"[+] Short 1 audio mix created: {SHORT_MIX}")
