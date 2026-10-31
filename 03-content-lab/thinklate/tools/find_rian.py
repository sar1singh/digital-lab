import urllib.request
import json

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"

# 1. Search shared voices for 'Rian'
url = "https://api.elevenlabs.io/v1/shared-voices?search=Rian"
req = urllib.request.Request(url, headers={"xi-api-key": API_KEY})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        voices = data.get("voices", [])
        print(f"Found {len(voices)} voices matching 'Rian':")
        for v in voices:
            name = v.get("name")
            vid = v.get("voice_id")
            accent = v.get("accent")
            desc = v.get("descriptive")
            use_case = v.get("use_case")
            pub_id = v.get("public_owner_id")
            print(f"Name: {name} | ID: {vid} | Accent: {accent} | Desc: {desc} | UseCase: {use_case}")
except Exception as e:
    print("Error:", e)

# 2. Also search for 'Hindi' in shared voices
url_hi = "https://api.elevenlabs.io/v1/shared-voices?search=Hindi&page_size=10"
req_hi = urllib.request.Request(url_hi, headers={"xi-api-key": API_KEY})
try:
    with urllib.request.urlopen(req_hi) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        voices = data.get("voices", [])
        print(f"\nFound {len(voices)} voices matching 'Hindi':")
        for v in voices:
            print(f"Name: {v.get('name')} | ID: {v.get('voice_id')} | Accent: {v.get('accent')} | Desc: {v.get('descriptive')}")
except Exception as e:
    print("Error Hindi search:", e)

