import os, urllib.request, json

api_key = os.environ.get('ELEVENLABS_API_KEY')
if not api_key:
    for env_path in [r'digital-lab/03-content-lab/thinklate/.env', r'agent-os/.env.local']:
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith('ELEVENLABS_API_KEY='):
                        api_key = line.strip().split('=', 1)[1]
                        break

print('API Key found:', bool(api_key))

# 1. Check user's voices / premade voices
req = urllib.request.Request(
    'https://api.elevenlabs.io/v1/voices',
    headers={'xi-api-key': api_key}
)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f'Total voices in v1/voices: {len(data.get("voices", []))}')
        for v in data.get('voices', []):
            if 'adam' in v['name'].lower():
                print(f"Found in v1/voices: Name='{v['name']}', ID='{v['voice_id']}', category='{v.get('category')}', labels={v.get('labels')}")
except Exception as e:
    print('Error v1/voices:', e)

# 2. Search shared voice library for 'Adam - Engaging, Friendly and Bright' or 'Adam'
req_lib = urllib.request.Request(
    'https://api.elevenlabs.io/v1/shared-voices?search=Adam',
    headers={'xi-api-key': api_key}
)
try:
    with urllib.request.urlopen(req_lib) as response:
        data_lib = json.loads(response.read().decode())
        voices = data_lib.get('voices', [])
        print(f"\nFound {len(voices)} matching 'Adam' in Shared Library:")
        for v in voices[:10]:
            print(f"- Name: '{v.get('name')}', public_owner_id: {v.get('public_owner_id')}, voice_id: '{v.get('voice_id')}', category: {v.get('category')}, desc: {v.get('description')}")
except Exception as e:
    print('Error shared-voices:', e)
