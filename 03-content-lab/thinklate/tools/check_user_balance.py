import urllib.request, json

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
url = "https://api.elevenlabs.io/v1/user"
headers = {"xi-api-key": API_KEY}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        sub = data.get("subscription", {})
        print("Tier:", sub.get("tier"))
        print("Character count:", sub.get("character_count"))
        print("Character limit:", sub.get("character_limit"))
        print("Remaining characters:", sub.get("character_limit") - sub.get("character_count"))
except Exception as e:
    print("Error:", e)

