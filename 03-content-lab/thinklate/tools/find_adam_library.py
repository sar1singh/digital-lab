import os, urllib.request, json, urllib.parse

api_key = ''
with open('digital-lab/03-content-lab/thinklate/.env') as f:
    for line in f:
        if line.startswith('ELEVENLABS_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

queries = ['Adam', 'Engaging, Friendly', 'Bright', 'Friendly', 'Engaging']
found = set()

for query in queries:
    url = f'https://api.elevenlabs.io/v1/shared-voices?search={urllib.parse.quote(query)}&page_size=50'
    req = urllib.request.Request(url, headers={'xi-api-key': api_key})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            for v in data.get('voices', []):
                vid = v.get('voice_id')
                name = v.get('name', '')
                desc = v.get('description', '')
                if 'adam' in name.lower() or 'adam' in desc.lower():
                    if vid not in found:
                        found.add(vid)
                        print(f"Match: Name='{name}', ID='{vid}', desc='{desc[:80]}...'")
    except Exception as e:
        print(f"Error querying {query}: {e}")
