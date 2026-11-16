import os
import sys
import re
import json
import asyncio
import subprocess
import edge_tts
import whisper

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "script.md")
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
TAKES_DIR = os.path.join(AUDIO_DIR, "takes")
os.makedirs(TAKES_DIR, exist_ok=True)

MASTER_DIALOGUE_WAV = os.path.join(AUDIO_DIR, "full_dialogue_master.wav")
TIMESTAMPS_JSON = os.path.join(BASE_DIR, "transcription_timestamps.json")

VOICE_CONFIGS = {
    "owl": {
        "voice": "en-US-ChristopherNeural",
        "rate": "+12%",
        "pitch": "-4Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-42dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB,areverse,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.5,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        )
    },
    "falcon": {
        "voice": "en-US-AvaNeural",
        "rate": "+15%",
        "pitch": "+0Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-42dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB,areverse,"
            "highpass=f=100,lowpass=f=9500,equalizer=f=2800:t=q:w=1.4:g=2.0,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        )
    }
}

def parse_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    lines = text.split("\n")
    blocks = []
    current_speaker = None
    current_lines = []

    for line in lines:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        
        speaker_match = re.match(r'^\[(OWL|FALCON)\]\s*:', line_clean, re.IGNORECASE)
        if speaker_match:
            if current_speaker and current_lines:
                blocks.append((current_speaker.lower(), " ".join(current_lines)))
                current_lines = []
            current_speaker = speaker_match.group(1).lower()
            remaining = line_clean[speaker_match.end():].strip()
            if remaining:
                current_lines.append(remaining)
        else:
            if current_speaker:
                current_lines.append(line_clean)

    if current_speaker and current_lines:
        blocks.append((current_speaker.lower(), " ".join(current_lines)))

    cleaned_blocks = []
    for idx, (speaker, content) in enumerate(blocks, 1):
        # Remove [SFX: ...] stage directions
        content_clean = re.sub(r'\[SFX:.*?\]', '', content)
        # Remove breath markers // and ///
        content_clean = content_clean.replace("///", " ").replace("//", " ")
        content_clean = re.sub(r'\s+', ' ', content_clean).strip()
        if content_clean:
            cleaned_blocks.append({
                "take_id": idx,
                "speaker": speaker,
                "text": content_clean
            })

    return cleaned_blocks

async def synthesize_all_takes(blocks):
    take_files = []
    print(f"[*] Total dialogue takes to synthesize: {len(blocks)}")
    
    for b in blocks:
        take_id = b["take_id"]
        speaker = b["speaker"]
        text = b["text"]
        cfg = VOICE_CONFIGS[speaker]

        temp_mp3 = os.path.join(TAKES_DIR, f"take_{take_id:02d}_{speaker}.temp.mp3")
        final_wav = os.path.join(TAKES_DIR, f"take_{take_id:02d}_{speaker}.wav")

        print(f"  -> Synthesizing Take {take_id:02d} [{speaker.upper()}]: {text[:60]}...")
        
        comm = edge_tts.Communicate(
            text=text,
            voice=cfg["voice"],
            rate=cfg["rate"],
            pitch=cfg["pitch"]
        )
        await comm.save(temp_mp3)

        cmd = [
            "ffmpeg", "-y", "-i", temp_mp3,
            "-af", cfg["eq_filter"],
            "-ar", "48000", "-ac", "2",
            final_wav
        ]
        res = subprocess.run(cmd, creationflags=0x08000000, capture_output=True)
        if os.path.exists(temp_mp3):
            os.remove(temp_mp3)

        if res.returncode == 0:
            take_files.append(final_wav)
        else:
            print(f"[-] Error processing take {take_id:02d}: {res.stderr.decode('utf-8', errors='ignore')}")

    return take_files

def concatenate_takes(take_files, output_wav):
    print(f"[*] Concatenating {len(take_files)} takes into master dialogue track...")
    concat_list_path = os.path.join(AUDIO_DIR, "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for t in take_files:
            f.write(f"file '{t.replace(os.sep, '/')}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        output_wav
    ]
    res = subprocess.run(cmd, creationflags=0x08000000, capture_output=True)
    if os.path.exists(concat_list_path):
        os.remove(concat_list_path)

    if res.returncode == 0:
        print(f"[+] Concatenation complete: {output_wav}")
        return True
    else:
        print(f"[-] Concatenation failed: {res.stderr.decode('utf-8', errors='ignore')}")
        return False

def generate_whisper_alignment(wav_path, output_json):
    print(f"[*] Running local Whisper model on master dialogue track...")
    print(f"    File: {wav_path}")
    model = whisper.load_model("base")
    result = model.transcribe(wav_path, word_timestamps=True, language="en")

    structured_data = {
        "text": result["text"],
        "segments": []
    }

    for seg in result["segments"]:
        segment_entry = {
            "id": seg["id"],
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip(),
            "words": []
        }
        if "words" in seg:
            for w in seg["words"]:
                segment_entry["words"].append({
                    "word": w["word"].strip(),
                    "start": w["start"],
                    "end": w["end"],
                    "probability": w.get("probability", 1.0)
                })
        structured_data["segments"].append(segment_entry)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(structured_data, f, indent=2, ensure_ascii=False)

    total_duration = result["segments"][-1]["end"] if result["segments"] else 0.0
    print(f"[+] Whisper alignment complete!")
    print(f"    Total Speech Duration: {total_duration:.2f}s (~{int(total_duration//60)}m {int(total_duration%60)}s)")
    print(f"    Timestamps saved to: {output_json}")
    return structured_data

async def main():
    print("=" * 70)
    print("🎙️ THINKLATE L06 DUAL-ANCHOR AUDIO PRODUCTION PIPELINE")
    print("=" * 70)

    blocks = parse_script(SCRIPT_PATH)
    print(f"[+] Successfully parsed {len(blocks)} dialogue turns from script.md")

    take_files = await synthesize_all_takes(blocks)
    if not take_files:
        print("[-] No audio takes were produced. Aborting.")
        return

    success = concatenate_takes(take_files, MASTER_DIALOGUE_WAV)
    if success:
        generate_whisper_alignment(MASTER_DIALOGUE_WAV, TIMESTAMPS_JSON)
        print("=" * 70)
        print("✅ AUDIO PIPELINE FINISHED SUCCESSFULLY")
        print(f"   Master WAV: {MASTER_DIALOGUE_WAV}")
        print(f"   Timestamps: {TIMESTAMPS_JSON}")
        print("=" * 70)

if __name__ == "__main__":
    asyncio.run(main())

