import os, urllib.request, json

api_key = ''
with open('digital-lab/03-content-lab/thinklate/.env') as f:
    for line in f:
        if line.startswith('ELEVENLABS_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

voice_id = 's3TPKV1kjDlVtZbl4Ksh'
sample_text = "In 2022, BMW made an announcement that sounded like an April Fools joke. If you wanted the heated seats in your fifty-thousand-dollar car to warm your back, you had to pay eighteen dollars every single month."

url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
payload = {
    "text": sample_text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0.0,
        "use_speaker_boost": True
    }
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'xi-api-key': api_key,
        'Content-Type': 'application/json'
    }
)

out_file = 'digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/audio_takes/voice_shootout/elevenlabs_adam_engaging_sample.mp3'

try:
    with urllib.request.urlopen(req) as resp:
        audio = resp.read()
        with open(out_file, 'wb') as f:
            f.write(audio)
        print(f"SUCCESS! Saved {len(audio)} bytes to {out_file}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode()
    print(f"HTTPError {e.code}: {e.reason}")
    print(f"Response: {err_body}")
except Exception as e:
    print(f"Error: {e}")
