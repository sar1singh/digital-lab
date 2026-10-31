import urllib.request
import json
import os

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"

# 1. Check user subscription
req_sub = urllib.request.Request("https://api.elevenlabs.io/v1/user/subscription", headers={"xi-api-key": API_KEY})
try:
    with urllib.request.urlopen(req_sub) as resp:
        sub_data = json.loads(resp.read().decode("utf-8"))
        print("=== ELEVENLABS SUBSCRIPTION ===")
        print(f"Tier: {sub_data.get('tier')}")
        print(f"Character count: {sub_data.get('character_count')} / {sub_data.get('character_limit')}")
        print(f"Can use instant voice cloning: {sub_data.get('can_use_instant_voice_cloning')}")
except Exception as e:
    print("Subscription Error:", e)

# 2. List voices
req_v = urllib.request.Request("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": API_KEY})
try:
    with urllib.request.urlopen(req_v) as resp:
        v_data = json.loads(resp.read().decode("utf-8"))
        voices = v_data.get("voices", [])
        print(f"\n=== AVAILABLE VOICES ({len(voices)} total) ===")
        for v in voices:
            cat = v.get("category", "premade")
            labels = v.get("labels", {})
            desc = f"{labels.get('accent', '')} {labels.get('description', '')} {labels.get('gender', '')}".strip()
            print(f"{v['voice_id']} | {v['name']} ({cat}) | {desc}")
except Exception as e:
    print("Voices Error:", e)

