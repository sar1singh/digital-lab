import urllib.request, json

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
voice_id = "s3TPKV1kjDlVtZbl4Ksh"

models = ["eleven_turbo_v2_5", "eleven_monolingual_v1", "eleven_turbo_v2"]

for m in models:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"Content-Type": "application/json", "xi-api-key": API_KEY}
    payload = {"text": "Testing voice model.", "model_id": m}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Model {m}: SUCCESS!")
    except urllib.error.HTTPError as e:
        print(f"Model {m}: {e.code} - {e.read().decode()[:100]}")
    except Exception as e:
        print(f"Model {m}: {e}")

