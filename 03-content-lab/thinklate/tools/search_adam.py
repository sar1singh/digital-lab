import urllib.request
import json

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
url = "https://api.elevenlabs.io/v1/shared-voices?search=Adam"
req = urllib.request.Request(url, headers={"xi-api-key": API_KEY})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        voices = data.get("voices", [])
        print(f"Found {len(voices)} voices matching 'Adam':")
        for v in voices:
            name = v.get("name")
            vid = v.get("voice_id")
            accent = v.get("accent")
            desc = v.get("descriptive")
            use_case = v.get("use_case")
            print(f"Name: {name} | ID: {vid} | Accent: {accent} | Desc: {desc} | UseCase: {use_case}")
except Exception as e:
    print("Error:", e)
