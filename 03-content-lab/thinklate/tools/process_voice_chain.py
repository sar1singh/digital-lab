"""
ThinkLate Voice Chain Processor & Speech Leveler
Solves uneven vocal volume (whispers vs shouting/peaks) and applies YouTube broadcast mastering:
1. High-Pass Filter (80Hz sub-rumble removal)
2. Dynamic Speech Normalizer (speechnorm: raises too-low speech, reins in too-loud speech)
3. Presence EQ (4.2kHz gentle lift for vocal crispness)
4. Studio Compressor (2.5:1 ratio, -18dB threshold for consistent vocal body)
5. ITU-R BS.1770 / EBU R128 Loudness Normalization (-15.0 LUFS target)
6. True Peak Limiter (-1.5 dBFS ceiling to prevent any digital distortion)

Usage:
    python process_voice_chain.py <input_audio.wav> [output_mastered.wav]
"""

import sys
import os
import subprocess

def process_audio(input_file, output_file=None):
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return False

    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_mastered{ext}"

    filter_chain = (
        "highpass=f=80,"
        "speechnorm=p=0.9:e=3.5:c=2.5:r=0.001:f=0.002,"
        "equalizer=f=300:t=q:w=1.5:g=-2.5,"      # Clear chest mud & congestion
        "equalizer=f=950:t=q:w=1.8:g=-3.0,"      # Remove nasal resonance / boxy nose tone
        "equalizer=f=4000:t=q:w=1.5:g=2.0,"     # Crisp speech presence & vocal articulation
        "equalizer=f=6200:t=q:w=2.5:g=-2.0,"     # Tame dry-mouth saliva clicks & sibilance
        "acompressor=threshold=-18dB:ratio=2.5:attack=25:release=140,"
        "loudnorm=I=-15.0:TP=-1.5:LRA=9,"
        "alimiter=level=false:limit=0.841"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", input_file,
        "-af", filter_chain,
        "-ar", "44100",
        "-c:a", "pcm_s16le",
        "-fflags", "+bitexact",
        "-rf64", "never",
        output_file
    ]

    print(f"\n=======================================================")
    print(f" [ThinkLate Studio] Processing: {os.path.basename(input_file)}")
    print(f" [ThinkLate Studio] Leveling uneven speech & mastering to -15 LUFS...")
    print(f" [ThinkLate Studio] Output: {output_file}")
    print(f"=======================================================")
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:\n", res.stderr)
        return False

    print("\n[ThinkLate Studio] Mastering successfully completed!")
    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python process_voice_chain.py <input_audio.wav> [output_mastered.wav]")
        sys.exit(1)

    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    res = process_audio(inp, out)
    if res:
        qc_script = os.path.join(os.path.dirname(__file__), "qc_audio.py")
        if os.path.exists(qc_script):
            print("\n[QC Auditor] Running acoustic compliance audit...")
            # Script final word count is 1667 words
            subprocess.run([sys.executable, qc_script, res, "--words", "1667"])
