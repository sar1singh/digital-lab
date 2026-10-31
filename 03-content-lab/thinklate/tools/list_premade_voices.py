import os, urllib.request, json

api_key = ''
with open('digital-lab/03-content-lab/thinklate/.env') as f:
    for line in f:
        if line.startswith('ELEVENLABS_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

req = urllib.request.Request(
    'https://api.elevenlabs.io/v1/voices',
    headers={'xi-api-key': api_key}
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    voices = data.get('voices', [])
    print(f"Total available premade API voices: {len(voices)}")
    for v in sorted(voices, key=lambda x: x['name']):
        labels = v.get('labels', {})
        print(f"- {v['name']} (ID: {v['voice_id']}) | {labels.get('accent')} | {labels.get('gender')} | {labels.get('use_case')}")
