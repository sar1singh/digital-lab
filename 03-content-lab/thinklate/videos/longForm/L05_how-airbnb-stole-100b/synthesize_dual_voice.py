import os
import sys
import re
import json
import requests
import subprocess
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.append(r"c:\Users\sar1s\Documents\MyWork\Git\tools")
from check_api_keys import load_env

load_env()
key = os.environ.get("ELEVENLABS_API_KEY")
if not key:
    print("Error: ELEVENLABS_API_KEY not found!")
    sys.exit(1)

VIDEO_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")
SFX_DIR   = os.path.join(VIDEO_DIR, "assets", "sfx")

# Act 1 Text for George (Warm, Captivating Storyteller)
# Cleaned of artifacts
GEORGE_TEXT = """Your rent is eleven hundred dollars. You have three days before your landlord kicks you out, and your bank account is empty. What do you do?

In October 2007, that wasn't a hypothetical question for Brian Chesky and his roommate, Joe Gebbia. They were two broke design school graduates sharing an apartment, completely unemployed, and scrambling for any quick cash just to survive the weekend!

Then, pure luck handed them an opening. A massive international design conference was flooding into town, and every single hotel room in the city was completely sold out. Tourists had nowhere to sleep. So Brian and Joe looked at their empty floor, ran to Target, bought three cheap blue air mattresses, and charged desperate designers eighty bucks a night to sleep on their rug, throwing in a box of Pop-Tarts in the morning!

Eighteen years later, that embarrassing emergency hustle on the floor became a hundred-billion-dollar empire! And if you are an entrepreneur or solo builder trying to start something with zero cash today, this journey holds the ultimate blueprint. Because by the end of this video, you are going to see the three uncensored tactical survival moves Brian used to hijack an entire industry, and the fatal scaling trap you must avoid so your business doesn't destroy itself once it wins!

That first weekend actually worked. The three designers handed over two hundred and forty dollars in cash, and the rent was paid. Brian and Joe looked at the deflated air mattresses on the floor and realized... wait. If complete strangers are willing to sleep in our living room, what if people could do this in every city on earth?

There was only one problem. Neither of them knew how to write software code. They were industrial designers who drew sketches, not programmers. So they called up their former roommate, Nate Blecharczyk, a gifted software engineer, and convinced him to build a primitive website called Airbed and Breakfast. The idea was simple: turn everyday homes into mini bed-and-breakfasts.

Once the website was live in early 2008, they thought the hardest part was over. They needed cash to keep the servers running, so they took their brand-new website to top Silicon Valley venture capitalists. The meetings were an absolute disaster! Investors literally laughed in their faces. Renowned venture capitalists walked out of coffee shops, or stared at them like they were completely insane. Why on earth would anyone invest in an app for strangers to sleep on air mattresses on dirty floors? Every single investor said no!"""

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("Synthesizing Act 1 with ElevenLabs George...")
print(f"Characters to synthesize: {len(GEORGE_TEXT):,} chars ({len(GEORGE_TEXT.split())} words)")

voice_id = "JBFqnCBsd6RMkjVDRZzb" # George
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {
    "xi-api-key": key,
    "Content-Type": "application/json"
}
payload = {
    "text": GEORGE_TEXT,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.52,
        "similarity_boost": 0.80,
        "style": 0.15,
        "use_speaker_boost": True
    }
}

r = requests.post(url, headers=headers, json=payload, verify=False, timeout=60)
if r.status_code != 200:
    print(f"ElevenLabs synthesis failed: HTTP {r.status_code}: {r.text}")
    sys.exit(1)

george_raw_mp3 = os.path.join(AUDIO_DIR, "act1_george_raw.mp3")
with open(george_raw_mp3, "wb") as f:
    f.write(r.content)
print(f"[OK] Saved Act 1 George: {george_raw_mp3} ({os.path.getsize(george_raw_mp3):,} bytes)")

# Convert George to 48kHz 24-bit WAV
george_wav = os.path.join(AUDIO_DIR, "act1_george_48k.wav")
subprocess.run(
    ["ffmpeg", "-y", "-i", george_raw_mp3, "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", george_wav],
    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)

# Probe George duration
proc = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", george_wav],
    capture_output=True, text=True, check=True
)
george_dur = float(proc.stdout.strip())
print(f"Act 1 George Duration: {george_dur:.2f}s (~{int(george_dur//60)}m {int(george_dur%60)}s)")

# Now extract Andrew Act 2-8 from fallback_andrew/voice_mastered.wav
# In Whisper timestamps: "They had a live website" starts right around 153.25s
andrew_src = os.path.join(AUDIO_DIR, "fallback_andrew", "voice_mastered.wav")
andrew_act2_wav = os.path.join(AUDIO_DIR, "act2_andrew_48k.wav")

# Find exact start of "They had a live website"
whisper_json = os.path.join(VIDEO_DIR, "transcription_timestamps.json")
with open(whisper_json, "r", encoding="utf-8") as f:
    segs = json.load(f)

andrew_start = 153.20
for s in segs:
    if "live website" in s["text"].lower() and "zero funding" in s["text"].lower():
        andrew_start = s["start"]
        print(f"Whisper matched Andrew takeover: {s['start']:.2f}s: '{s['text']}'")
        break

# Cut Andrew from takeover point to the end
subprocess.run(
    ["ffmpeg", "-y", "-ss", f"{andrew_start:.3f}", "-i", andrew_src, "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", andrew_act2_wav],
    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)

proc_a = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", andrew_act2_wav],
    capture_output=True, text=True, check=True
)
andrew_dur = float(proc_a.stdout.strip())
print(f"Act 2-8 Andrew Duration: {andrew_dur:.2f}s (~{int(andrew_dur//60)}m {int(andrew_dur%60)}s)")

# Splice George + Sub-bass transition hit + Andrew
# Build concat list
concat_list = os.path.join(AUDIO_DIR, "dual_voice_concat.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file 'act1_george_48k.wav'\n")
    f.write(f"file 'act2_andrew_48k.wav'\n")

dual_master_wav = os.path.join(AUDIO_DIR, "dual_voice_mastered.wav")
subprocess.run(
    ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c:a", "pcm_s24le", dual_master_wav],
    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)

total_dual_dur = george_dur + andrew_dur
print(f"SUCCESS: Spliced Dual-Voice Master Audio: {dual_master_wav} ({total_dual_dur:.2f}s | ~{int(total_dual_dur//60)}m {int(total_dual_dur%60)}s)")
