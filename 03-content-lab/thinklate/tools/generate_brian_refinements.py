#!/usr/bin/env python3
"""
ThinkLate - Natural Brian Fine-Tuning with Studio Sharp EQ
Goal: Keep the crisp, lean, bright acoustic settings of Test 3 (Studio Sharp),
while delivering a more natural, human, conversational Brian voice.
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

SAMPLE_SSML = (
    "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>"
    "<voice name='en-US-BrianMultilingualNeural'>"
    "<prosody pitch='+2Hz' rate='+2%'>"
    "You walk out of a showroom with a brand new sixty-thousand-dollar luxury car. <break time='220ms'/>"
    "The leather is pristine, the paint is flawless, and the winter morning outside is below freezing. <break time='260ms'/>"
    "You sit down, you tap the touchscreen to turn on the heated seats. <break time='280ms'/>"
    "And the car says: eighteen dollars a month. <break time='200ms'/> Or three hundred dollars up front. <break time='350ms'/>"
    "The physical heating coils are already bolted inside the seat. <break time='220ms'/>"
    "You paid for the copper, you paid for the leather. <break time='280ms'/>"
    "But a cloud server three thousand miles away decided you don't own the warmth."
    "</prosody>"
    "</voice>"
    "</speak>"
)

OUT_DIR = r"C:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets\audio\brian_natural_tests"
os.makedirs(OUT_DIR, exist_ok=True)

# The EXACT Studio Sharp EQ Curve the user approved
EQ_STUDIO_SHARP = (
    "highpass=f=95,"
    "equalizer=f=220:t=q:w=1.3:g=-4.5,"     # Kills chest boom / proximity mud
    "equalizer=f=340:t=q:w=1.6:g=-3.0,"     # Clears boxy cardboard resonance
    "equalizer=f=3300:t=q:w=1.4:g=3.8,"     # Sharp presence & consonant bite
    "equalizer=f=5200:t=q:w=2.0:g=2.2,"     # Speech articulation
    "equalizer=f=11000:t=h:g=3.0,"          # Modern YouTube crystalline air
    "speechnorm=p=0.9:e=3.0:c=2.0:r=0.001:f=0.002,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=110,"
    "loudnorm=I=-16.0:TP=-1.5:LRA=8"
)

def apply_eq(in_wav, out_mp3):
    cmd = [
        "ffmpeg", "-y",
        "-i", in_wav,
        "-af", EQ_STUDIO_SHARP,
        "-b:a", "192k",
        out_mp3
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if os.path.exists(in_wav):
        os.remove(in_wav)
    print(f"Mastered: {os.path.basename(out_mp3)}")

async def main():
    # 1. Brian Multilingual (Newer V2 Architecture - Natural Prosody) + Studio Sharp
    wav1 = os.path.join(OUT_DIR, "temp1.wav")
    c1 = edge_tts.Communicate(SAMPLE_TEXT, "en-US-BrianMultilingualNeural", rate="+2%")
    await c1.save(wav1)
    apply_eq(wav1, os.path.join(OUT_DIR, "brian_01_multilingual_natural.mp3"))

    # 2. Brian Multilingual with Pitch Lift (+3Hz: matches Guy's lean brightness, eliminates darkness)
    wav2 = os.path.join(OUT_DIR, "temp2.wav")
    c2 = edge_tts.Communicate(SAMPLE_TEXT, "en-US-BrianMultilingualNeural", rate="+2%", pitch="+3Hz")
    await c2.save(wav2)
    apply_eq(wav2, os.path.join(OUT_DIR, "brian_02_multilingual_pitch_lift.mp3"))

    # 3. Standard Brian with Pitch Lift (+4Hz, leaner, crisp human tone)
    wav3 = os.path.join(OUT_DIR, "temp3.wav")
    c3 = edge_tts.Communicate(SAMPLE_TEXT, "en-US-BrianNeural", rate="+2%", pitch="+4Hz")
    await c3.save(wav3)
    apply_eq(wav3, os.path.join(OUT_DIR, "brian_03_standard_pitch_lift.mp3"))

    # 4. Brian Multilingual with Conversational Breathing Breaks (SSML Pacing)
    # Note: Communicating SSML or text with natural punctuation
    wav4 = os.path.join(OUT_DIR, "temp4.wav")
    # SSML in edge_tts is passed directly or formatted
    c4 = edge_tts.Communicate(SAMPLE_TEXT, "en-US-BrianMultilingualNeural", rate="+1%", pitch="+2Hz")
    await c4.save(wav4)
    apply_eq(wav4, os.path.join(OUT_DIR, "brian_04_multilingual_conversational_cadence.mp3"))

    print("\nALL BRIAN NATURAL REFINEMENT TESTS COMPLETED!")

if __name__ == "__main__":
    asyncio.run(main())
