import asyncio
import os
import edge_tts

text = (
    "You walk out of a showroom with a brand new sixty-thousand-dollar luxury car. "
    "The leather is pristine, the paint is flawless, and the winter morning outside is below freezing. "
    "You sit down, you tap the touchscreen to turn on the heated seats. "
    "And the car says: eighteen dollars a month. Or three hundred dollars up front. "
    "The physical heating coils are already bolted inside the seat. "
    "You paid for the copper, you paid for the leather. "
    "But a cloud server three thousand miles away decided you don't own the warmth."
)

voices = [
    ("en-IN-PrabhatNeural", "sample_01_prabhat_indian_authentic.mp3", "+2%"),
    ("en-US-BrianNeural", "sample_02_brian_us_conversational_punchy.mp3", "+3%"),
    ("en-US-ChristopherNeural", "sample_03_christopher_us_documentary_deep.mp3", "+2%"),
    ("en-US-GuyNeural", "sample_04_guy_us_smart_explainer.mp3", "+3%"),
    ("en-GB-RyanNeural", "sample_05_ryan_british_dry_satire.mp3", "+2%"),
]

output_dir = r"C:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\assets\audio\voice_samples"
os.makedirs(output_dir, exist_ok=True)

async def main():
    for voice_id, filename, rate in voices:
        filepath = os.path.join(output_dir, filename)
        print(f"Generating {filename} with {voice_id}...")
        communicate = edge_tts.Communicate(text, voice_id, rate=rate)
        await communicate.save(filepath)
        print(f"  Saved -> {filepath}")

if __name__ == "__main__":
    asyncio.run(main())

