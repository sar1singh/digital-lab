import json

try:
    with open(r'c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\youtube_live_metadata.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except Exception:
    with open(r'c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\youtube_live_metadata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

print('--- CORE DETAILS ---')
print('Title:', data.get('title'))
print('Title Length:', len(data.get('title', '')))
print('Channel:', data.get('channel'))
print('Channel URL:', data.get('channel_url'))
print('Duration (s):', data.get('duration'))
print('Upload Date:', data.get('upload_date'))
print('Availability:', data.get('availability'))

print('\n--- FORMATS / TRANSCODE ---')
formats = data.get('formats', [])
heights = sorted(list(set(f.get('height') for f in formats if f.get('height'))))
print('Available Heights:', heights)
vcodecs = list(set(f.get('vcodec') for f in formats if f.get('vcodec') and f.get('vcodec') != 'none'))
print('Video Codecs:', vcodecs[:5])

print('\n--- CHAPTERS ---')
chapters = data.get('chapters')
if chapters:
    print(f'Total Chapters: {len(chapters)}')
    for ch in chapters:
        print(f"  {ch.get('start_time')}s - {ch.get('title')}")
else:
    print('Chapters: None reported in native chapters list')

print('\n--- SUBTITLES ---')
subtitles = data.get('subtitles')
auto_subs = data.get('automatic_captions')
print('Manual Subtitles:', list(subtitles.keys()) if subtitles else 'None')
print('Auto Captions Available:', bool(auto_subs))

print('\n--- THUMBNAILS ---')
thumbnail = data.get('thumbnail')
print('Primary Thumbnail:', thumbnail)

print('\n--- TAGS ---')
tags = data.get('tags')
print('Tags count:', len(tags) if tags else 0)
if tags:
    print('Tags:', tags[:10])

print('\n--- DESCRIPTION ---')
desc = data.get('description', '')
print('Description length:', len(desc))
print('Description preview (first 400 chars):')
print(desc[:400])
