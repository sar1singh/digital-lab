import os
import json
import urllib.request
import subprocess

API_KEY = "sk_d2896cffe9f84aeab33a4cbb39cfce129ff78dd996ffc0ec"
VOICE_ID = "iP95p4xoKVk53GoZ742B"  # Chris

OUT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\audio_takes\voice_shootout"
RAW_FILE = os.path.join(OUT_DIR, "elevenlabs_chris_extended_raw.mp3")
MASTERED_FILE = os.path.join(OUT_DIR, "elevenlabs_chris_extended_mastered.mp3")

with open(r'digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_paste_part1.txt', 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

hook_hp = '\n\n'.join(paras[:40])
hook_hp = hook_hp.replace(',.', ',').replace('.,', ',')

print(f"Synthesizing Chris Extended Take: {len(hook_hp)} characters, {len(hook_hp.split())} words...")

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}
payload = {
    "text": hook_hp,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.48,
        "similarity_boost": 0.75,
        "style": 0.05,
        "use_speaker_boost": True
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        audio_data = resp.read()
        with open(RAW_FILE, "wb") as f:
            f.write(audio_data)
        print(f"TTS Success! Saved {len(audio_data)} bytes to {RAW_FILE}")
except Exception as e:
    print(f"TTS Error: {e}")
    exit(1)

# Studio Sharp Mastering Chain
dsp_chain = (
    "highpass=f=90,"
    "equalizer=f=220:t=q:w=1.2:g=-3.5,"
    "equalizer=f=340:t=q:w=1.4:g=-2.0,"
    "equalizer=f=3500:t=q:w=1.5:g=3.5,"
    "equalizer=f=5200:t=q:w=1.8:g=2.0,"
    "treble=g=2.5:f=11000,"
    "speechnorm=e=4:r=0.0001:l=1,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=120:makeup=2.5,"
    "loudnorm=I=-16.0:LRA=7.0:TP=-1.5"
)

cmd = [
    "ffmpeg", "-y", "-i", RAW_FILE,
    "-af", dsp_chain,
    "-c:a", "libmp3lame", "-b:a", "320k",
    MASTERED_FILE
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"Mastering Success! Saved to {MASTERED_FILE} ({os.path.getsize(MASTERED_FILE)} bytes)")
else:
    print(f"Mastering Error: {res.stderr}")

