"""
ThinkLate Voice & Ambient Audio Mixer
1. Re-balances master voiceover to a gentle, comfortable documentary level (-18.5 LUFS, True Peak -2.5 dBFS).
2. Prepares ambient background bed looped/trimmed to match video duration with smooth fade-in and fade-out.
3. Ducks and frequency-shapes background music so it sits quietly behind the voice (-23 dB).
4. Outputs:
   - voice_mastered_balanced.wav (soft, clear vocal stem)
   - ambient_bed_track.wav (isolated background music stem)
   - full_mix_voice_and_ambient.wav (complete preview mix)
"""

import sys
import os
import subprocess

def mix_audio(voice_file, ambient_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Get exact voice duration
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        voice_file
    ]
    res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, text=True)
    dur = float(res.stdout.strip())
    print(f"[ThinkLate Mixer] Voice Duration: {dur:.2f} seconds ({dur/60:.2f} min)")

    # 2. Re-balance voice to comfortable documentary loudness (-18.5 LUFS, -2.5 dBFS Peak)
    balanced_voice = os.path.join(output_dir, "voice_mastered_balanced.wav")
    print("\n[ThinkLate Mixer] Step 1: Calibrating voiceover to comfortable volume (-18.5 LUFS)...")
    voice_filter = (
        "highpass=f=80,"
        "speechnorm=p=0.88:e=3.0:c=2.0:r=0.001:f=0.002,"
        "equalizer=f=4200:t=q:w=1.5:g=2.0,"
        "acompressor=threshold=-20dB:ratio=2.2:attack=25:release=140,"
        "loudnorm=I=-18.5:TP=-2.5:LRA=9,"
        "alimiter=level=false:limit=0.749"  # -2.5 dBFS ceiling (10^(-2.5/20) = 0.749)
    )
    cmd_v = [
        "ffmpeg", "-y", "-i", voice_file,
        "-af", voice_filter,
        "-ar", "44100", "-c:a", "pcm_s16le",
        "-fflags", "+bitexact", "-rf64", "never",
        balanced_voice
    ]
    subprocess.run(cmd_v, check=True)
    print(" -> Balanced voice ready: voice_mastered_balanced.wav")

    # 3. Process Ambient Bed (Loop, trim to duration, apply gentle EQ & duck to -24 dB)
    ambient_bed = os.path.join(output_dir, "ambient_bed_track.wav")
    print(f"\n[ThinkLate Mixer] Step 2: Preparing ambient music bed ({os.path.basename(ambient_file)})...")
    # Lowpass at 3800Hz, Highpass at 60Hz, volume -23dB, fadein 3s, fadeout 5s
    fadeout_start = max(0, dur - 5.0)
    amb_filter = (
        f"aloop=loop=-1:size=2e+09,"
        f"atrim=0:{dur},"
        f"highpass=f=60,lowpass=f=4000,"
        f"volume=-23dB,"
        f"afade=t=in:ss=0:d=3.0,afade=t=out:st={fadeout_start:.2f}:d=5.0"
    )
    cmd_a = [
        "ffmpeg", "-y", "-i", ambient_file,
        "-af", amb_filter,
        "-ar", "44100", "-c:a", "pcm_s16le",
        "-fflags", "+bitexact", "-rf64", "never",
        ambient_bed
    ]
    subprocess.run(cmd_a, check=True)
    print(" -> Ambient bed ready: ambient_bed_track.wav")

    # 4. Generate Combined Full Mix
    full_mix = os.path.join(output_dir, "full_mix_voice_and_ambient.wav")
    print("\n[ThinkLate Mixer] Step 3: Mixing voiceover + ambient bed together...")
    cmd_m = [
        "ffmpeg", "-y",
        "-i", balanced_voice,
        "-i", ambient_bed,
        "-filter_complex", "amix=inputs=2:duration=first:dropout_transition=3,alimiter=level=false:limit=0.749",
        "-ar", "44100", "-c:a", "pcm_s16le",
        "-fflags", "+bitexact", "-rf64", "never",
        full_mix
    ]
    subprocess.run(cmd_m, check=True)
    print(f" -> Full mix successfully created: {os.path.basename(full_mix)}")
    print("\n[ThinkLate Mixer] Complete audio suite exported to audio_takes folder!")

if __name__ == '__main__':
    takes_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox\audio_takes"
    raw_voice = os.path.join(takes_dir, "raw_voice.wav")
    
    # Priority: Dark Fog or Ambiment
    amb_file = os.path.join(takes_dir, "ambient_music_dark_fog.mp3")
    if not os.path.exists(amb_file):
        amb_file = os.path.join(takes_dir, "ambient_music_ambiment.mp3")

    mix_audio(raw_voice, amb_file, takes_dir)
