import urllib.request
import json

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
VOICE_ID = "nPczCjzI2devNBz1zQrb" # Brian

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

data = {
    "text": "In July 2022, BMW started charging rent on heated seats.",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        audio = resp.read()
        print("ElevenLabs TTS Success! Received bytes:", len(audio))
        with open("test_elevenlabs_brian.mp3", "wb") as f:
            f.write(audio)
        print("Saved test_elevenlabs_brian.mp3 successfully!")
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
    print(e.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)

