import os, urllib.request, json

api_key = ''
with open('digital-lab/03-content-lab/thinklate/.env') as f:
    for line in f:
        if line.startswith('ELEVENLABS_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

req = urllib.request.Request(
    'https://api.elevenlabs.io/v1/user/subscription',
    headers={'xi-api-key': api_key}
)

try:
    with urllib.request.urlopen(req) as resp:
        sub = json.loads(resp.read().decode())
        print(f"Tier: {sub.get('tier')}")
        print(f"Character count: {sub.get('character_count')} / {sub.get('character_limit')}")
        print(f"Can extend character limit: {sub.get('can_extend_character_limit')}")
        print(f"Allowed to use instant voice cloning: {sub.get('can_use_instant_voice_cloning')}")
except Exception as e:
    print('Error:', e)
