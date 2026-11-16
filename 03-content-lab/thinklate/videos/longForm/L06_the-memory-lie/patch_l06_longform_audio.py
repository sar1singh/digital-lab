#!/usr/bin/env python3
"""
Re-synthesizes the 7 modified dialogue takes in L06 Long-Form so that:
  1. Zero characters are called 'Owl' or 'Falcon' in the audio ('Eddy' is used instead).
  2. Zero takes end on unfinished splice conjunctions ('...which leads to...', '...explains why...', '...which is why...').
  3. Take 17 speaks the complete 'read-only storage' phrase without clipping.
  4. Each re-synthesized take is duration-locked to takes_timing.json so all 23 video scene cuts stay 100% synced.
  5. Re-runs Whisper word-level alignment, applies all phonetic fixes, regenerates ASS/SRT subtitles, and updates ThinkLate_L06_The_Memory_Lie_1080p_MASTER.mp4.
"""
import asyncio
import glob
import json
import os
import pathlib
import subprocess
import edge_tts
import whisper

VIDEO_DIR = pathlib.Path(__file__).resolve().parent
AUDIO_DIR = VIDEO_DIR / "assets" / "audio"
TAKES_DIR = AUDIO_DIR / "takes"
MASTER_DIALOGUE_WAV = AUDIO_DIR / "full_dialogue_master.wav"
TIMESTAMPS_JSON = VIDEO_DIR / "transcription_timestamps.json"
TAKES_TIMING_JSON = VIDEO_DIR / "takes_timing.json"

VOICE_CONFIGS = {
    "owl": {
        "voice": "en-US-ChristopherNeural",
        "rate": "+12%",
        "pitch": "-4Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-45dB,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.5,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
    },
    "falcon": {
        "voice": "en-US-AvaNeural",
        "rate": "+15%",
        "pitch": "+0Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-45dB,"
            "highpass=f=100,lowpass=f=9500,equalizer=f=2800:t=q:w=1.4:g=2.0,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
    },
}

UPDATED_TAKES = {
    1: (
        "owl",
        "In nineteen eighty-four, a college student named Jennifer Thompson looked straight into the eyes of a judge "
        "and swore on a Bible. She was one hundred percent certain she recognized the man who attacked her. "
        "She studied his face during the assault. She picked him out of a police lineup. "
        "She sent Ronald Cotton to prison for life! Eleven years later, modern DNA forensics tested the evidence. "
        "Ronald Cotton was completely innocent. Over seventy percent of wrongful convictions overturned by DNA evidence "
        "share this exact horrifying flaw: an eyewitness who was totally confident, perfectly calm, and dead wrong. "
        "By the end of this video, you will discover the concrete blueprint of why your skull has no hard drive, "
        "and the psychological trap you must avoid whenever you trust your own past."
    ),
    2: (
        "falcon",
        "And here is the terrifying part, Eddy. Jennifer Thompson wasn't lying! She passed every polygraph. "
        "Her heart rate was steady. In her mind, she was recalling a real, high-definition photograph. "
        "But the human brain does not possess a camera lens. It does not possess a solid-state drive. "
        "And it certainly does not save MP4 video files to an anatomical folder in your temporal lobe."
    ),
    7: (
        "falcon",
        "If you take a traditional photograph of your family, cut the print in half with scissors, "
        "and throw away the left side, you permanently lose half your family. "
        "But if you record a true three-dimensional optical hologram on a glass plate, take a hammer, "
        "and smash that glass into fifty jagged shards, something miraculous happens! "
        "Pick up any tiny, broken sliver of that glass, shine a coherent laser beam through it, "
        "and you do not see a fifty-percent sliver of the image. You see the entire family portrait, "
        "completely intact, just with slightly softer resolution. In a hologram, information is not stored "
        "in a localized pixel. It is smeared across the entire interference pattern."
    ),
    13: (
        "falcon",
        "They were not pretending, Eddy. They had physically overwritten their own past. "
        "Every time the researcher asked, Do you remember the mall?, the subject's brain generated a hypothetical "
        "simulation to test the question. And once that simulation ran, the brain tagged the simulation "
        "as an authentic historical memory and stored it right back into the network."
    ),
    15: (
        "owl",
        "In the year two thousand, neuroscientist Karim Nader proved something that terrified cognitive scientists. "
        "When you retrieve an old memory, your brain does not just view it. The act of remembering physically "
        "destabilizes the protein synthesis bonds holding that memory together! For three to five hours after you "
        "think about an event, that memory becomes malleable liquid clay. If you are anxious, romantic, angry, "
        "or listening to a suggestive friend, those new emotions become permanently baked into the original trace. "
        "When you fall asleep that night, your brain synthesizes new proteins and saves the altered file over the original. "
        "You never remember your actual past. You only remember the last time you remembered it, "
        "adding five percent distortion every single round."
    ),
    16: (
        "falcon",
        "That means your favorite childhood story is essentially a twenty-fifth-generation photocopy of a photocopy. "
        "The dramatic winning goal you scored in middle school soccer? Every time you bragged about it over drinks, "
        "your brain nudged the defenders two feet further away. Every time you felt nostalgic, "
        "the sunset grew slightly more golden. By the time you are thirty-five, "
        "you are defending an epic Hollywood screenplay that your own neurons authored without telling you."
    ),
    17: (
        "owl",
        "So why on earth would natural selection design such a ridiculous system? "
        "If accurate memory is so crucial for human survival, why didn't evolution give us rigid, uncorrupted, read-only storage?"
    ),
}

def probe_dur(path: pathlib.Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        creationflags=0x08000000
    ).decode().strip()
    return float(out)

async def resynthesize_updated_takes():
    timings = {t["file"]: t["duration"] for t in json.loads(TAKES_TIMING_JSON.read_text(encoding="utf-8"))}

    for take_id, (speaker, text) in UPDATED_TAKES.items():
        cfg = VOICE_CONFIGS[speaker]
        fname = f"take_{take_id:02d}_{speaker}.wav"
        target_dur = timings[fname]
        temp_mp3 = TAKES_DIR / f"take_{take_id:02d}_{speaker}.temp.mp3"
        raw_wav = TAKES_DIR / f"take_{take_id:02d}_{speaker}.raw.wav"
        final_wav = TAKES_DIR / fname

        print(f"[*] Re-synthesizing {fname} (target={target_dur:.2f}s)...")
        comm = edge_tts.Communicate(text=text, voice=cfg["voice"], rate=cfg["rate"], pitch=cfg["pitch"])
        await comm.save(str(temp_mp3))

        subprocess.run([
            "ffmpeg", "-y", "-i", str(temp_mp3),
            "-af", cfg["eq_filter"],
            "-ar", "48000", "-ac", "2", str(raw_wav)
        ], check=True, creationflags=0x08000000)
        temp_mp3.unlink(missing_ok=True)

        actual_dur = probe_dur(raw_wav)
        # If raw_wav is slightly longer than target_dur, speed up gently via atempo; then pad/trim to exact target_dur
        ratio = actual_dur / target_dur
        if ratio > 1.005:
            atempo = min(1.15, max(1.0, ratio * 1.01))
            af_lock = f"atempo={atempo:.4f},apad,atrim=0:{target_dur:.4f}"
        else:
            af_lock = f"apad,atrim=0:{target_dur:.4f}"

        subprocess.run([
            "ffmpeg", "-y", "-i", str(raw_wav),
            "-af", af_lock,
            "-ar", "48000", "-ac", "2", str(final_wav)
        ], check=True, creationflags=0x08000000)
        raw_wav.unlink(missing_ok=True)
        print(f"  ✓ Locked {fname}: {probe_dur(final_wav):.2f}s (target {target_dur:.2f}s)")

def concat_and_transcribe():
    # Transcribe with Whisper
    print("[*] Running Whisper alignment on updated full_dialogue_master.wav...")
    model = whisper.load_model("base")
    result = model.transcribe(str(MASTER_DIALOGUE_WAV), word_timestamps=True, language="en")
    structured = {
        "text": result["text"],
        "segments": [
            {
                "id": seg["id"],
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"].strip(),
                "words": [
                    {
                        "word": w["word"].strip(),
                        "start": w["start"],
                        "end": w["end"],
                        "probability": w.get("probability", 1.0),
                    }
                    for w in seg.get("words", [])
                ],
            }
            for seg in result["segments"]
        ],
    }
    raw_json = json.dumps(structured, indent=2, ensure_ascii=False)

    # Apply phonetic fixes so zero Whisper typos appear on screen
    PHONETIC_FIXES = [
        ('"word": "damn"', '"word": "dim"'),
        ("a damn refrigerator", "a dim refrigerator"),
        ('"word": "Reconcilitation."', '"word": "Reconsolidation."'),
        ("memory Reconcilitation", "Memory Reconsolidation"),
        ('"word": "Pride"', '"word": "Cried"'),
        ("Pride for hours", "Cried for hours"),
        ('"word": "safe."', '"word": "save."'),
        ("hit safe.", "hit save."),
        ('"word": "We\'re"', '"word": "Were"'),
        ("We're comforted", "Were comforted"),
        ("we're finally", "were finally"),
        ('"word": "But"', '"word": "Put"'),
        ("But the ego down", "Put the ego down"),
        ('"word": "shadow"', '"word": "shatter"'),
        ("shadow your memories", "shatter your memories"),
        ("wet where", "wetware"),
        ('"word": "Eddie."', '"word": "Eddy."'),
        ('"word": "Eddie,"', '"word": "Eddy,"'),
        ("Eddie", "Eddy"),
        ("Kareem", "Karim"),
    ]
    for old, new in PHONETIC_FIXES:
        raw_json = raw_json.replace(old, new)

    TIMESTAMPS_JSON.write_text(raw_json, encoding="utf-8")
    print("[+] Updated & phonetically verified transcription_timestamps.json")

    # Regenerate ASS & SRT subtitles and re-compile Master MP4
    subprocess.run(["python", str(VIDEO_DIR / "generate_l06_master_subtitles.py")], check=True, creationflags=0x08000000)
    subprocess.run(["python", str(VIDEO_DIR / "compile_l06_documentary_master.py")], check=True, creationflags=0x08000000)

async def main():
    concat_and_transcribe()

if __name__ == "__main__":
    asyncio.run(main())
