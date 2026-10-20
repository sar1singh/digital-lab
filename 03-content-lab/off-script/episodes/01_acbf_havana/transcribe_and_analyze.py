"""
Off Script Episode 01 — Autonomous Transcription, Timeline & Speech Quality Engine
Uses faster-whisper on CUDA with FP16 for fast, accurate speech-to-text extraction.
Extracts:
1. Full segment-by-segment transcript with timestamps.
2. Long pause / silence analysis (detecting hesitation, water sips, Game Audio windows).
3. Speaking speed & pacing metrics.
4. Topic & visual evidence markers.
"""

import os
import sys
import json
import time
from pathlib import Path

AUDIO_PATH = Path(r"03-content-lab/off-script/episodes/01_acbf_havana/audio/take1.mp3")
OUTPUT_DIR = Path(r"03-content-lab/off-script/episodes/01_acbf_havana/analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_JSON = OUTPUT_DIR / "transcript_segments.json"
OUT_MD = OUTPUT_DIR / "transcript_readable.md"
OUT_SRT = OUTPUT_DIR / "transcript_subtitles.srt"
OUT_METRICS = OUTPUT_DIR / "speech_audit_metrics.json"

def format_time(sec):
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def format_srt_time(sec):
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    millis = int((sec - int(sec)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def main():
    import torch
    from faster_whisper import WhisperModel

    if not AUDIO_PATH.exists():
        print(f"Error: {AUDIO_PATH} not found!")
        sys.exit(1)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if device == "cuda" else "int8"
    print(f"Initializing faster-whisper (model='base', device='{device}', compute_type='{compute_type}')...")

    t0 = time.time()
    # 'base' model is extremely fast on RTX 3050 and fits easily within 4GB VRAM
    model = WhisperModel("base", device=device, compute_type=compute_type)
    print(f"Model loaded in {time.time()-t0:.2f}s.")

    print(f"Transcribing {AUDIO_PATH} (01:05:54 duration)...")
    # Using beam_size=3 for balanced speed and accuracy, VAD filter enabled for clean segment boundaries
    segments_generator, info = model.transcribe(
        str(AUDIO_PATH),
        beam_size=3,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=800)
    )

    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
    print(f"Audio duration: {info.duration:.2f}s ({format_time(info.duration)})")

    segments = []
    pauses = []
    prev_end = 0.0

    md_lines = [
        "# Off Script Episode 01 — Voiceover Transcript & Segment Audit",
        f"**File:** `take1.mp3`  ",
        f"**Duration:** `{format_time(info.duration)}` ({info.duration:.2f}s)  ",
        f"**Detected Language:** `{info.language}` ({info.language_probability*100:.1f}%)  \n",
        "| # | Timecode | Duration | Spoken Content |",
        "| :-: | :--- | :-: | :--- |"
    ]
    srt_lines = []

    last_reported = 0
    seg_idx = 1

    for seg in segments_generator:
        start = round(seg.start, 2)
        end = round(seg.end, 2)
        dur = round(end - start, 2)
        text = seg.text.strip()

        # Check silence gap from previous segment
        gap = round(start - prev_end, 2)
        if prev_end > 0 and gap >= 3.0:
            pauses.append({
                "start": round(prev_end, 2),
                "end": start,
                "duration": gap,
                "timecode": f"{format_time(prev_end)} - {format_time(start)}"
            })

        prev_end = end

        segments.append({
            "id": seg_idx,
            "start": start,
            "end": end,
            "duration": dur,
            "timecode": f"{format_time(start)} - {format_time(end)}",
            "text": text
        })

        md_lines.append(f"| {seg_idx} | `{format_time(start)} - {format_time(end)}` | {dur}s | {text} |")

        srt_lines.append(f"{seg_idx}")
        srt_lines.append(f"{format_srt_time(start)} --> {format_srt_time(end)}")
        srt_lines.append(f"{text}\n")

        # Progress reporting every 300s (5 mins) of processed audio
        if int(end // 300) > last_reported:
            last_reported = int(end // 300)
            elapsed = time.time() - t0
            print(f"Processed up to {format_time(end)} ({end/info.duration*100:.1f}%) in {elapsed:.1f}s...")

        seg_idx += 1

    total_speech_time = sum(s["duration"] for s in segments)
    total_pause_time = round(info.duration - total_speech_time, 2)

    # Classify pauses:
    # 3-5s: micro-pauses / hesitation / thinking
    # 5-15s: deliberate pauses / water sips
    # >15s: major silence / potential Game Audio Takeover
    hesitations = [p for p in pauses if 3.0 <= p["duration"] < 6.0]
    breathers = [p for p in pauses if 6.0 <= p["duration"] < 15.0]
    game_audio_windows = [p for p in pauses if p["duration"] >= 15.0]

    metrics = {
        "audio_file": str(AUDIO_PATH),
        "total_duration_sec": round(info.duration, 2),
        "formatted_duration": format_time(info.duration),
        "detected_language": info.language,
        "language_confidence": round(info.language_probability, 4),
        "total_segments": len(segments),
        "total_speech_duration_sec": round(total_speech_time, 2),
        "speech_ratio": round(total_speech_time / info.duration, 4),
        "total_silence_duration_sec": total_pause_time,
        "pause_statistics": {
            "total_pauses_over_3s": len(pauses),
            "hesitations_3_to_6s_count": len(hesitations),
            "breathers_6_to_15s_count": len(breathers),
            "major_silence_over_15s_count": len(game_audio_windows),
            "major_silences": game_audio_windows,
            "hesitations_sample": hesitations[:15]
        }
    }

    # Save output files
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(segments, f, ensure_ascii=False, indent=2)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    with open(OUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    with open(OUT_METRICS, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    total_time = time.time() - t0
    print(f"\n[SUCCESS] Transcribed {len(segments)} segments in {total_time:.1f}s ({info.duration/total_time:.1f}x real-time speed)!")
    print(f"Saved: {OUT_JSON}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {OUT_SRT}")
    print(f"Saved: {OUT_METRICS}")

if __name__ == "__main__":
    main()
