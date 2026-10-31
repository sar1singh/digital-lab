#!/usr/bin/env python3
"""
ThinkLate - Broadcast Sharpness & Proximity Mud Killer Chain
A/B Test Generator:
Compares:
1. Sample A: Raw Brian (Unprocessed - boomy proximity effect)
2. Sample B: Brian + Studio Sharpness EQ (Mud Cut at 220Hz, +4dB Presence at 3.2kHz, +3dB Air at 11kHz)
3. Sample C: Brian + Ultra Crisp / Lean (Steep 120Hz HPF, -6dB Mud Cut, +5dB Presence - zero proximity effect)
4. Sample D: Guy Neural + Studio Sharpness EQ (Naturally brighter, leaner modern explainer tone)
"""

import os
import subprocess
import asyncio
import edge_tts

SAMPLE_TEXT = (
    "You walk out of a showroom with a brand new sixty-thousand-dollar luxury car. "
    "The leather is pristine, the paint is flawless, and the winter morning outside is below freezing. "
    "You sit down, you tap the touchscreen to turn on the heated seats. "
    "And the car says: eighteen dollars a month. Or three hundred dollars up front. "
    "The physical heating coils are already bolted inside the seat. "
    "You paid for the copper, you paid for the leather. "
    "But a cloud server three thousand miles away decided you don't own the warmth."
)

OUT_DIR = r"C:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets\audio\eq_tests"
os.makedirs(OUT_DIR, exist_ok=True)

# EQ Filter Chains
# 1. Studio Sharpness (Standard Proximity Tamer)
EQ_STUDIO_SHARP = (
    "highpass=f=95,"
    "equalizer=f=220:t=q:w=1.3:g=-4.5,"     # Kill proximity chest boom
    "equalizer=f=340:t=q:w=1.6:g=-3.0,"     # Remove boxy cardboard mud
    "equalizer=f=3300:t=q:w=1.4:g=3.8,"     # Sharp presence & consonant clarity
    "equalizer=f=5200:t=q:w=2.0:g=2.2,"     # Articulation
    "equalizer=f=11000:t=h:g=3.0,"          # High air / modern YouTube sheen
    "speechnorm=p=0.9:e=3.0:c=2.0:r=0.001:f=0.002,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=110,"
    "loudnorm=I=-16.0:TP=-1.5:LRA=8"
)

# 2. Ultra Crisp & Lean (Aggressive anti-boom, cutting broadcast lead)
EQ_ULTRA_CRISP = (
    "highpass=f=120,"
    "equalizer=f=200:t=q:w=1.2:g=-6.5,"     # Deep cut on boomy low-end
    "equalizer=f=360:t=q:w=1.5:g=-4.0,"     # Clear lower mid congestion
    "equalizer=f=1000:t=q:w=1.8:g=-2.0,"    # Dip nasal boxiness
    "equalizer=f=3500:t=q:w=1.5:g=4.8,"     # Razor-sharp consonant punch
    "equalizer=f=6000:t=q:w=2.0:g=-1.5,"    # De-ess harsh sibilance
    "equalizer=f=11500:t=h:g=3.5,"          # Crystalline high air
    "speechnorm=p=0.92:e=3.2:c=2.2:r=0.001:f=0.002,"
    "acompressor=threshold=-17dB:ratio=3.0:attack=12:release=95,"
    "loudnorm=I=-16.0:TP=-1.5:LRA=7"
)

def apply_ffmpeg_eq(input_wav, output_mp3, filter_chain):
    cmd = [
        "ffmpeg", "-y",
        "-i", input_wav,
        "-af", filter_chain,
        "-b:a", "192k",
        output_mp3
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print(f"Mastered: {os.path.basename(output_mp3)}")

async def main():
    # 1. Generate Raw Brian
    raw_brian = os.path.join(OUT_DIR, "raw_brian.wav")
    comm_brian = edge_tts.Communicate(SAMPLE_TEXT, "en-US-BrianNeural", rate="+3%")
    await comm_brian.save(raw_brian)
    print("Raw Brian generated.")

    # 2. Generate Raw Guy
    raw_guy = os.path.join(OUT_DIR, "raw_guy.wav")
    comm_guy = edge_tts.Communicate(SAMPLE_TEXT, "en-US-GuyNeural", rate="+3%")
    await comm_guy.save(raw_guy)
    print("Raw Guy generated.")

    # Process Variants
    # Variant 1: Brian Studio Sharp
    v1_out = os.path.join(OUT_DIR, "test_01_brian_studio_sharp.mp3")
    apply_ffmpeg_eq(raw_brian, v1_out, EQ_STUDIO_SHARP)

    # Variant 2: Brian Ultra Crisp (Lean, zero bass boom, sharp presence)
    v2_out = os.path.join(OUT_DIR, "test_02_brian_ultra_crisp_lean.mp3")
    apply_ffmpeg_eq(raw_brian, v2_out, EQ_ULTRA_CRISP)

    # Variant 3: Guy Studio Sharp (Naturally brighter, leaner modern explainer tone)
    v3_out = os.path.join(OUT_DIR, "test_03_guy_studio_sharp.mp3")
    apply_ffmpeg_eq(raw_guy, v3_out, EQ_STUDIO_SHARP)

    # Variant 4: Guy Ultra Crisp
    v4_out = os.path.join(OUT_DIR, "test_04_guy_ultra_crisp.mp3")
    apply_ffmpeg_eq(raw_guy, v4_out, EQ_ULTRA_CRISP)

    # Clean up intermediate raw wavs
    if os.path.exists(raw_brian): os.remove(raw_brian)
    if os.path.exists(raw_guy): os.remove(raw_guy)
    print("\nALL 4 SHARPNESS VARIANTS READY FOR AUDIT!")

if __name__ == "__main__":
    asyncio.run(main())

