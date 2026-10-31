import urllib.request
import json
import os
import subprocess

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
VOICE_ID = "IvLWq57RKibBrqZGpQrC" # Rian - Energetic Hindi Conversational

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

# The opening hook from Video 04
text = (
    "In July 2022, BMW started charging rent on heated seats. "
    "Not at a dealership, but through the car's own screen. "
    "South Korea, the UK, Germany. About eighteen dollars a month, or one hundred and eighty a year. "
    "Here is the strange part: the heating coils were already inside the seat. "
    "Copper, relays, switches, every physical gram of it. "
    "But a software flag said: not unless your credit card bills every thirty days."
)

data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.55,       # Smooth, natural conversational stability
        "similarity_boost": 0.78, # Crisp, clear articulation
        "style": 0.15,            # Subtle conversational inflection
        "use_speaker_boost": True
    }
}

req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)

out_dir = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/audio_takes/voice_shootout"
raw_mp3 = os.path.join(out_dir, "elevenlabs_rian_raw.mp3")
mastered_mp3 = os.path.join(out_dir, "elevenlabs_rian_mastered.mp3")

try:
    print(f"Generating ElevenLabs Rian voice ({VOICE_ID})...")
    with urllib.request.urlopen(req) as resp:
        audio = resp.read()
        with open(raw_mp3, "wb") as f:
            f.write(audio)
        print(f"Saved raw audio: {raw_mp3} ({len(audio)} bytes)")

    # Apply ThinkLate Conversational Broadcast Filter:
    # Tuned specifically for Indian / Hindi-accented English natural voice:
    # Highpass 85Hz, mild 250Hz warmth trim (-2.5dB), 950Hz boxy trim (-2.0dB),
    # 3.8kHz crisp presence (+2.5dB), 10.5kHz air shelf (+2.0dB), speechnorm, smooth compressor, -17.5 LUFS
    cmd_master = [
        "ffmpeg", "-y", "-i", raw_mp3,
        "-af", (
            "highpass=f=85,"
            "equalizer=f=250:t=q:w=1.2:g=-2.5,"
            "equalizer=f=950:t=q:w=1.4:g=-2.0,"
            "equalizer=f=3800:t=q:w=1.5:g=2.8,"
            "treble=g=2.0:f=10500,"
            "speechnorm=e=3.5:r=0.0001:l=1,"
            "acompressor=threshold=-18dB:ratio=2.4:attack=15:release=110:makeup=2.0,"
            "loudnorm=I=-17.5:LRA=7.0:TP=-1.5"
        ),
        "-c:a", "libmp3lame", "-b:a", "320k",
        mastered_mp3
    ]
    subprocess.run(cmd_master, check=True)
    print(f"Mastered conversational ThinkLate Rian audio: {mastered_mp3} ({os.path.getsize(mastered_mp3)} bytes)")

except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
    print(e.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)

