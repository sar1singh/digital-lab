"""
Off Script Episode 04 — Autonomous Transcription, Synced Timeline & Silence Audit Engine
Uses faster-whisper on CUDA with FP16 (via DaVinci Resolve CUDA 12 DLLs) for fast transcription.
Aligns Audacity voiceover timestamps to OBS Video Time using verified t0 offset (+4.150s).
"""

import os
import sys
import json
import time
from pathlib import Path

# Inject DaVinci Resolve's CUDA 12 directory so cublas64_12.dll loads cleanly on RTX GPU
DAVINCI_DIR = r"C:\Program Files\Blackmagic Design\DaVinci Resolve"
if os.path.exists(DAVINCI_DIR):
    os.add_dll_directory(DAVINCI_DIR)
    os.environ["PATH"] = DAVINCI_DIR + ";" + os.environ.get("PATH", "")

from faster_whisper import WhisperModel

EP_DIR = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\off-script\episodes\04_acbf_fort_diversion")
AUDIO_PATH = Path(r"C:\Users\sar1s\Documents\MyWork\audacity\ACBF-Gameplay-15-Nov-2026.mp3")
VIDEO_PATH = Path(r"C:\Users\sar1s\Videos\obs\2026-11-15 01-16-18.mkv")

OUTPUT_DIR = EP_DIR / "analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(EP_DIR / "audio").mkdir(parents=True, exist_ok=True)

OUT_JSON = OUTPUT_DIR / "transcript_segments.json"
OUT_MD = OUTPUT_DIR / "transcript_readable.md"
OUT_SRT = OUTPUT_DIR / "transcript_subtitles.srt"
OUT_METRICS = OUTPUT_DIR / "speech_audit_metrics.json"

T0_OFFSET = 4.150
VIDEO_DURATION = 7912.834


def format_time(sec: float) -> str:
    sec = max(0.0, sec)
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"


def format_srt_time(sec: float) -> str:
    sec = max(0.0, sec)
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    millis = int(round((sec - int(sec)) * 1000))
    if millis >= 1000:
        millis = 999
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"


def main():
    if not AUDIO_PATH.exists():
        print(f"Error: {AUDIO_PATH} not found!")
        sys.exit(1)

    t0 = time.time()
    print("Initializing faster-whisper (model='base', device='cuda', compute_type='float16')...", flush=True)
    model = WhisperModel("base", device="cuda", compute_type="float16", local_files_only=True)
    print(f"Model loaded in {time.time() - t0:.2f}s.", flush=True)

    print(f"Transcribing & translating {AUDIO_PATH} (sync offset t0 = +{T0_OFFSET:.3f}s)...", flush=True)
    segments_generator, info = model.transcribe(
        str(AUDIO_PATH),
        task="translate",
        beam_size=3,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=800),
    )

    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})", flush=True)
    print(f"Audacity audio duration: {info.duration:.3f}s ({format_time(info.duration)})", flush=True)

    segments = []
    pauses = []
    prev_v_end = None
    last_reported = 0
    seg_idx = 1

    md_lines = [
        "# Off Script Episode 04 — Voiceover Transcript & Synced Segment Audit",
        f"**Video Source:** `2026-11-15 01-16-18.mkv` (`{format_time(VIDEO_DURATION)}` / `{VIDEO_DURATION:.3f}s`)  ",
        f"**Audio Source:** `ACBF-Gameplay-15-Nov-2026.mp3` (`{format_time(info.duration)}` / `{info.duration:.3f}s`)  ",
        f"**Sync Offset ($t_0$):** `+{T0_OFFSET:.3f}s` ($t_{{\\text{{video}}}} = t_{{\\text{{aud}}}} - {T0_OFFSET:.3f}\\text{{s}}$)  ",
        f"**Detected Language:** `{info.language}` ({info.language_probability * 100:.1f}%)  \n",
        "| # | Video Timecode | Audacity Timecode | Duration | Spoken Content (Translated) |",
        "| :-: | :--- | :--- | :-: | :--- |"
    ]
    srt_lines = []

    for seg in segments_generator:
        aud_start = round(seg.start, 2)
        aud_end = round(seg.end, 2)

        # Skip segments wholly outside the OBS video span
        if aud_end <= T0_OFFSET or aud_start >= T0_OFFSET + VIDEO_DURATION:
            continue

        v_start = round(max(0.0, aud_start - T0_OFFSET), 2)
        v_end = round(min(VIDEO_DURATION, aud_end - T0_OFFSET), 2)
        dur = round(v_end - v_start, 2)
        if dur <= 0:
            continue

        text = seg.text.strip().replace("|", "\\|")

        # Record mid-run silence gaps in OBS Video Time
        if prev_v_end is not None:
            gap = round(v_start - prev_v_end, 2)
            if gap >= 3.0:
                pauses.append({
                    "start": round(prev_v_end, 2),
                    "end": v_start,
                    "audacity_start": round(prev_v_end + T0_OFFSET, 2),
                    "audacity_end": round(v_start + T0_OFFSET, 2),
                    "duration": gap,
                    "timecode": f"{format_time(prev_v_end)} - {format_time(v_start)}",
                    "audacity_timecode": f"{format_time(prev_v_end + T0_OFFSET)} - {format_time(v_start + T0_OFFSET)}"
                })

        prev_v_end = v_end

        segments.append({
            "id": seg_idx,
            "video_start": v_start,
            "video_end": v_end,
            "audacity_start": aud_start,
            "audacity_end": aud_end,
            "duration": dur,
            "video_timecode": f"{format_time(v_start)} - {format_time(v_end)}",
            "audacity_timecode": f"{format_time(aud_start)} - {format_time(aud_end)}",
            "text": seg.text.strip()
        })

        md_lines.append(
            f"| {seg_idx} | `{format_time(v_start)} - {format_time(v_end)}` | "
            f"`{format_time(aud_start)} - {format_time(aud_end)}` | {dur}s | {text} |"
        )

        srt_lines.append(f"{seg_idx}")
        srt_lines.append(f"{format_srt_time(v_start)} --> {format_srt_time(v_end)}")
        srt_lines.append(f"{seg.text.strip()}\n")

        if int(v_end // 600) > last_reported:
            last_reported = int(v_end // 600)
            elapsed = time.time() - t0
            print(f"Processed up to {format_time(v_end)} ({v_end / VIDEO_DURATION * 100:.1f}%) in {elapsed:.1f}s...", flush=True)

        seg_idx += 1

    first_v_start = segments[0]["video_start"] if segments else 0.0
    last_v_end = segments[-1]["video_end"] if segments else VIDEO_DURATION

    intro_silence = {
        "start": 0.0,
        "end": first_v_start,
        "audacity_start": T0_OFFSET,
        "audacity_end": round(first_v_start + T0_OFFSET, 2),
        "duration": round(first_v_start, 2),
        "timecode": f"00:00 - {format_time(first_v_start)}",
    }
    outro_silence = {
        "start": last_v_end,
        "end": VIDEO_DURATION,
        "audacity_start": round(last_v_end + T0_OFFSET, 2),
        "audacity_end": round(VIDEO_DURATION + T0_OFFSET, 2),
        "duration": round(VIDEO_DURATION - last_v_end, 2),
        "timecode": f"{format_time(last_v_end)} - {format_time(VIDEO_DURATION)}",
    }

    total_speech_time = round(sum(s["duration"] for s in segments), 2)
    total_silence_time = round(VIDEO_DURATION - total_speech_time, 2)

    hesitations = [p for p in pauses if 3.0 <= p["duration"] < 6.0]
    breathers = [p for p in pauses if 6.0 <= p["duration"] < 15.0]
    game_audio_windows = [p for p in pauses if 15.0 <= p["duration"] <= 20.0]
    excess_silences_to_trim = [p for p in pauses if p["duration"] > 20.0]

    metrics = {
        "video_file": str(VIDEO_PATH),
        "audio_file": str(AUDIO_PATH),
        "t0_offset_sec": T0_OFFSET,
        "video_duration_sec": VIDEO_DURATION,
        "audacity_duration_sec": round(info.duration, 3),
        "formatted_video_duration": format_time(VIDEO_DURATION),
        "detected_language": info.language,
        "language_confidence": round(info.language_probability, 4),
        "total_segments": len(segments),
        "total_speech_duration_sec": total_speech_time,
        "speech_ratio": round(total_speech_time / VIDEO_DURATION, 4),
        "total_silence_duration_sec": total_silence_time,
        "intro_silence": intro_silence,
        "outro_silence": outro_silence,
        "pause_statistics": {
            "total_pauses_over_3s": len(pauses),
            "hesitations_3_to_6s_count": len(hesitations),
            "breathers_6_to_15s_count": len(breathers),
            "game_audio_windows_15_to_20s_count": len(game_audio_windows),
            "excess_silences_over_20s_count": len(excess_silences_to_trim),
            "excess_silences_total_sec": round(sum(p["duration"] for p in excess_silences_to_trim), 2),
            "excess_silences_to_trim": excess_silences_to_trim,
            "game_audio_windows": game_audio_windows,
            "breathers": breathers,
        },
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(segments, f, ensure_ascii=False, indent=2)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    with open(OUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    with open(OUT_METRICS, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    total_time = time.time() - t0
    print(f"\n[SUCCESS] Transcribed {len(segments)} segments in {total_time:.1f}s ({VIDEO_DURATION / total_time:.1f}x speed)!", flush=True)
    print(f"Speech duration: {total_speech_time:.1f}s ({metrics['speech_ratio'] * 100:.1f}%) | Excess silences (>20s): {len(excess_silences_to_trim)}", flush=True)
    print(f"Saved: {OUT_JSON}", flush=True)
    print(f"Saved: {OUT_MD}", flush=True)
    print(f"Saved: {OUT_SRT}", flush=True)
    print(f"Saved: {OUT_METRICS}", flush=True)


if __name__ == "__main__":
    main()
