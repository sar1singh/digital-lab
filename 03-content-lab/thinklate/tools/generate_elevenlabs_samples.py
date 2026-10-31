import urllib.request
import json
import os

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
text = "In July 2022, BMW started charging rent on heated seats. Not at a dealership, but through the car's own screen."

voices = [
    ("elevenlabs_adam", "pNInz6obpgDQGcFmaJgB"),
    ("elevenlabs_george", "JBFqnCBsd6RMkjVDRZzb"),
]

out_dir = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/audio_takes/voice_shootout"

for label, vid in voices:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{vid}"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": API_KEY}
    data = {"text": text, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    with urllib.request.urlopen(req) as resp:
        out_p = os.path.join(out_dir, f"{label}_sample.mp3")
        with open(out_p, "wb") as f:
            f.write(resp.read())
        print(f"Saved: {out_p} ({os.path.getsize(out_p)} bytes)")

