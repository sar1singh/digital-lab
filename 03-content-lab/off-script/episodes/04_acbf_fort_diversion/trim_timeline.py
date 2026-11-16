"""
Off Script Episode 04 — Synced Audio & Video Trimming Pipeline
Aligns Audacity Voiceover (t0 = +4.150s) with OBS MKV Video Time (0.000s - 7912.834s).
Trims dead silence gaps > 20s down to balanced 20s Game Audio Breathing Gaps,
removes pre-speech intro setup (0-34.41s) and trailing stop-menu outro (7904.51-7912.834s),
and runs 100% headlessly with CREATE_NO_WINDOW (0x08000000).
"""

import os
import sys
import json
import subprocess
from pathlib import Path

import numpy as np

CREATE_NO_WINDOW = 0x08000000
SW_HIDE = 0

EP_DIR = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\off-script\episodes\04_acbf_fort_diversion")
VIDEO_FILE = Path(r"C:\Users\sar1s\Videos\obs\2026-11-15 01-16-18.mkv")
AUDIO_FILE = Path(r"C:\Users\sar1s\Documents\MyWork\audacity\ACBF-Gameplay-15-Nov-2026.mp3")
METRICS_FILE = EP_DIR / "analysis" / "speech_audit_metrics.json"

OUT_AUDIO = EP_DIR / "audio" / "ep04_voiceover_trimmed.mp3"
OUT_CSV = EP_DIR / "analysis" / "ep04_timeline_cuts.csv"
OUT_EDL = EP_DIR / "analysis" / "ep04_timeline_cuts.edl"
OUT_FILTER = EP_DIR / "analysis" / "audio_filter_complex.txt"
OUT_SCRIPT = EP_DIR / "analysis" / "render_trimmed_video.ps1"
OUT_CHAPTERS = EP_DIR / "analysis" / "chapters_trimmed.md"
OUT_VERIFICATION = EP_DIR / "analysis" / "render_verification.json"
SEG_DIR = EP_DIR / "analysis" / "render_segments"
MASTER_OUT = Path(r"C:\Users\sar1s\Videos\obs\edited\OffScript_Gameplay_04_2026-11-15_Trimmed.mp4")

T0_OFFSET = 4.150


def hidden_startupinfo():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = SW_HIDE
    return si


def format_tc(sec: float, fps: int = 60) -> str:
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    frames = int(round((sec - int(sec)) * fps))
    if frames >= fps:
        frames = fps - 1
    return f"{hrs:02d}:{mins:02d}:{secs:02d}:{frames:02d}"


def format_hms(sec: float) -> str:
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"


def build_timeline_from_metrics():
    with open(METRICS_FILE, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    total_video_dur = metrics["video_duration_sec"]
    intro_end = max(0.0, round(metrics["intro_silence"]["end"] - 2.0, 3))
    # End right after "See you in the next one" (finishes at 7853.60s + 0.90s clean tail)
    outro_start = 7854.500

    cuts = [{"label": "Intro Setup", "start": 0.0, "end": intro_end, "duration": intro_end}]
    for i, s in enumerate(metrics["pause_statistics"]["excess_silences_to_trim"], 1):
        c_start = round(s["start"] + 10.0, 3)
        c_end = round(s["end"] - 10.0, 3)
        cuts.append({
            "label": f"Silence Gap {i:02d}",
            "start": c_start,
            "end": c_end,
            "duration": round(c_end - c_start, 3),
        })
    cuts.append({
        "label": "Outro Menu/Quit",
        "start": outro_start,
        "end": total_video_dur,
        "duration": round(total_video_dur - outro_start, 3),
    })

    keeps = []
    cur = intro_end
    for c in cuts[1:]:
        if c["start"] > cur:
            keeps.append({
                "v_start": round(cur, 3),
                "v_end": round(c["start"], 3),
                "a_start": round(cur + T0_OFFSET, 3),
                "a_end": round(c["start"] + T0_OFFSET, 3),
                "duration": round(c["start"] - cur, 3),
            })
        cur = c["end"]

    return total_video_dur, cuts, keeps


def render_trimmed_audio(keeps):
    OUT_AUDIO.parent.mkdir(parents=True, exist_ok=True)
    total_dur = round(sum(k["duration"] for k in keeps), 3)
    fade_start = round(max(0.0, total_dur - 0.6), 3)
    filter_parts = [
        f"[0:a]atrim=start={k['a_start']:.3f}:end={k['a_end']:.3f},asetpts=PTS-STARTPTS[a{i}]"
        for i, k in enumerate(keeps)
    ]
    concat_inputs = "".join(f"[a{i}]" for i in range(len(keeps)))
    filter_script = (
        ";\n".join(filter_parts)
        + f";\n{concat_inputs}concat=n={len(keeps)}:v=0:a=1,afade=t=out:st={fade_start:.3f}:d=0.6[outa]\n"
    )

    with open(OUT_FILTER, "w", encoding="utf-8") as f:
        f.write(filter_script)

    cmd = [
        "ffmpeg", "-y", "-v", "warning",
        "-i", str(AUDIO_FILE),
        "-filter_complex_script", str(OUT_FILTER),
        "-map", "[outa]",
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        str(OUT_AUDIO),
    ]
    subprocess.run(
        cmd,
        check=True,
        creationflags=CREATE_NO_WINDOW,
        startupinfo=hidden_startupinfo(),
    )
    print(f"[SUCCESS] Synced trimmed audio exported: {OUT_AUDIO}")


def probe_media(media_path: Path) -> dict:
    """Run ffprobe cleanly without console popups and return parsed JSON."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_format", "-show_streams",
        "-of", "json",
        str(media_path),
    ]
    res = subprocess.run(
        cmd,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        creationflags=CREATE_NO_WINDOW,
        startupinfo=hidden_startupinfo(),
    )
    return json.loads(res.stdout)


def summarize_probe(media_path: Path, expected_dur: float) -> dict:
    info = probe_media(media_path)
    fmt = info.get("format", {})
    dur = float(fmt.get("duration", 0.0))
    size_bytes = media_path.stat().st_size
    streams_summary = []
    for s in info.get("streams", []):
        streams_summary.append({
            "index": s.get("index"),
            "codec_type": s.get("codec_type"),
            "codec_name": s.get("codec_name"),
            "width": s.get("width"),
            "height": s.get("height"),
            "r_frame_rate": s.get("r_frame_rate"),
            "avg_frame_rate": s.get("avg_frame_rate"),
            "sample_rate": s.get("sample_rate"),
            "channels": s.get("channels"),
            "bit_rate": s.get("bit_rate"),
        })
    deviation = round(abs(dur - expected_dur), 3)
    return {
        "path": str(media_path),
        "exists": True,
        "size_bytes": size_bytes,
        "size_mb": round(size_bytes / (1024 ** 2), 2),
        "size_gb": round(size_bytes / (1024 ** 3), 3),
        "duration_sec": round(dur, 3),
        "duration_hms": format_hms(dur),
        "expected_duration_sec": round(expected_dur, 3),
        "deviation_sec": deviation,
        "within_2s_tolerance": deviation <= 2.0,
        "bit_rate": fmt.get("bit_rate"),
        "streams": streams_summary,
    }


def render_master_video(keeps):
    SEG_DIR.mkdir(parents=True, exist_ok=True)
    MASTER_OUT.parent.mkdir(parents=True, exist_ok=True)
    segment_files = []

    for i, k in enumerate(keeps, 1):
        seg_file = SEG_DIR / f"seg_{i:02d}.ts"
        segment_files.append(seg_file)
        if seg_file.exists() and seg_file.stat().st_size > 1024 * 1024:
            try:
                seg_info = probe_media(seg_file)
                seg_dur = float(seg_info["format"]["duration"])
                if abs(seg_dur - k["duration"]) <= 2.0:
                    print(f"Resuming: skipping valid Seg {i:02d}/{len(keeps)} ({seg_dur:.2f}s)...", flush=True)
                    continue
            except Exception:
                pass

        cmd_seg = [
            "ffmpeg", "-y", "-v", "error",
            "-hwaccel", "cuda",
            "-ss", f"{k['v_start']:.3f}",
            "-t", f"{k['duration']:.3f}",
            "-i", str(VIDEO_FILE),
            "-ss", f"{k['a_start']:.3f}",
            "-t", f"{k['duration']:.3f}",
            "-i", str(AUDIO_FILE),
            "-filter_complex", "[0:a:2]volume=-22dB[game];[1:a:0]volume=0dB[vo];[game][vo]amix=inputs=2:duration=first:normalize=0[outa]",
            "-map", "0:v:0",
            "-map", "[outa]",
            "-c:v", "h264_nvenc",
            "-cq", "21",
            "-preset", "p4",
            "-r", "60",
            "-c:a", "aac",
            "-b:a", "192k",
            "-f", "mpegts",
            str(seg_file),
        ]
        print(f"Rendering Seg {i:02d}/{len(keeps)} ({format_hms(k['v_start'])} -> {format_hms(k['v_end'])}, {k['duration']:.2f}s)...", flush=True)
        subprocess.run(
            cmd_seg,
            check=True,
            creationflags=CREATE_NO_WINDOW,
            startupinfo=hidden_startupinfo(),
        )

    concat_list = SEG_DIR / "concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for sf in segment_files:
            f.write(f"file '{sf.resolve().as_posix()}'\n")

    cmd_final = [
        "ffmpeg", "-y", "-v", "warning",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        "-movflags", "+faststart",
        str(MASTER_OUT),
    ]
    print(f"Concatenating {len(segment_files)} synced segments into {MASTER_OUT}...", flush=True)
    subprocess.run(
        cmd_final,
        check=True,
        creationflags=CREATE_NO_WINDOW,
        startupinfo=hidden_startupinfo(),
    )

    if MASTER_OUT.exists() and MASTER_OUT.stat().st_size > 0:
        for sf in segment_files:
            if sf.exists():
                sf.unlink()
        print(f"[CLEANUP] Deleted temporary seg_XX.ts files from {SEG_DIR}", flush=True)
    print(f"[SUCCESS] Master Video Rendered: {MASTER_OUT}", flush=True)


def deecho_comb_iir(pcm: np.ndarray, delay: int = 6637, alpha: float = 0.38) -> np.ndarray:
    """Apply exact IIR inverse-comb de-echo filter H(z) = 1 / (1 + alpha * z^-delay)."""
    if pcm.shape[0] <= delay:
        return pcm
    out = np.empty_like(pcm)
    first = min(delay, pcm.shape[0])
    out[:first] = pcm[:first]
    for pos in range(delay, pcm.shape[0], delay):
        end = min(pos + delay, pcm.shape[0])
        span = end - pos
        out[pos:end] = pcm[pos:end] - alpha * out[pos - delay : pos - delay + span]
    return np.clip(out, -0.99, 0.99)


def fast_remux_master_video(keeps, trimmed_dur: float):
    if not MASTER_OUT.exists():
        raise FileNotFoundError(f"Existing video not found for fast remux: {MASTER_OUT}")

    SEG_DIR.mkdir(parents=True, exist_ok=True)
    deecho_flac = SEG_DIR / "ep04_game_deecho.flac"
    master_tmp = MASTER_OUT.with_name(MASTER_OUT.stem + "_remux_tmp.mp4")

    print(f"Extracting & de-echoing game audio (0:a:2, delay=6637, alpha=0.38) across {len(keeps)} segments...", flush=True)
    cmd_flac = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "f32le", "-ar", "48000", "-ac", "2",
        "-i", "pipe:0",
        "-c:a", "flac",
        str(deecho_flac),
    ]
    enc_proc = subprocess.Popen(
        cmd_flac,
        stdin=subprocess.PIPE,
        creationflags=CREATE_NO_WINDOW,
        startupinfo=hidden_startupinfo(),
    )
    try:
        for i, k in enumerate(keeps, 1):
            print(f"De-echoing Seg {i:02d}/{len(keeps)} ({format_hms(k['v_start'])} -> {format_hms(k['v_end'])})...", flush=True)
            cmd_ext = [
                "ffmpeg", "-v", "error",
                "-vn",
                "-ss", f"{k['v_start']:.3f}",
                "-t", f"{k['duration']:.3f}",
                "-i", str(VIDEO_FILE),
                "-map", "0:a:2",
                "-ac", "2", "-ar", "48000",
                "-f", "f32le",
                "pipe:1",
            ]
            res = subprocess.run(
                cmd_ext,
                capture_output=True,
                check=True,
                creationflags=CREATE_NO_WINDOW,
                startupinfo=hidden_startupinfo(),
            )
            raw = np.frombuffer(res.stdout, dtype=np.float32)
            frames = len(raw) // 2
            pcm = raw[: frames * 2].reshape(frames, 2)
            target_frames = int(round(k["duration"] * 48000))
            if frames > target_frames:
                pcm = pcm[:target_frames]
            elif frames < target_frames:
                pcm = np.vstack([pcm, np.zeros((target_frames - frames, 2), dtype=np.float32)])
            cleaned = deecho_comb_iir(pcm, delay=6637, alpha=0.38)
            enc_proc.stdin.write(cleaned.astype(np.float32).tobytes())
        enc_proc.stdin.close()
        rc = enc_proc.wait()
        if rc != 0:
            raise RuntimeError(f"FLAC encoder failed with exit code {rc}")
    except Exception:
        enc_proc.kill()
        enc_proc.wait()
        raise

    fade_start = round(max(0.0, trimmed_dur - 0.6), 3)
    filter_mix = (
        "[2:a:0]equalizer=f=2200:t=q:w=1.2:g=-4,volume=-26dB[game];"
        "[1:a:0]volume=0dB[vo];"
        f"[game][vo]amix=inputs=2:duration=shortest:normalize=0,afade=t=out:st={fade_start:.3f}:d=0.6[outa]"
    )
    cmd_remux = [
        "ffmpeg", "-y", "-v", "warning",
        "-i", str(MASTER_OUT),
        "-i", str(OUT_AUDIO),
        "-i", str(deecho_flac),
        "-filter_complex", filter_mix,
        "-map", "0:v:0",
        "-map", "[outa]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", f"{trimmed_dur:.3f}",
        "-movflags", "+faststart",
        str(master_tmp),
    ]
    print(f"Stream-copying video (-t {trimmed_dur:.3f}s) & muxing cleaned audio into {master_tmp}...", flush=True)
    subprocess.run(
        cmd_remux,
        check=True,
        creationflags=CREATE_NO_WINDOW,
        startupinfo=hidden_startupinfo(),
    )

    if not master_tmp.exists() or master_tmp.stat().st_size < 100 * 1024 * 1024:
        raise RuntimeError(f"Remuxed file missing or too small: {master_tmp}")

    master_tmp.replace(MASTER_OUT)
    if deecho_flac.exists():
        deecho_flac.unlink()
    print(f"[SUCCESS] Fast-remuxed cleaned Master Video: {MASTER_OUT}", flush=True)


def verify_outputs(mode: str, expected_dur: float):
    report = {
        "expected_duration_sec": round(expected_dur, 3),
        "expected_duration_hms": format_hms(expected_dur),
        "audio": summarize_probe(OUT_AUDIO, expected_dur) if OUT_AUDIO.exists() else {"path": str(OUT_AUDIO), "exists": False},
    }
    if mode in ("--render-video", "--fast-remux"):
        report["video"] = summarize_probe(MASTER_OUT, expected_dur) if MASTER_OUT.exists() else {"path": str(MASTER_OUT), "exists": False}

    OUT_VERIFICATION.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_VERIFICATION, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=== RENDER VERIFICATION SUMMARY ===", flush=True)
    for key in ("audio", "video"):
        if key in report and report[key].get("exists"):
            item = report[key]
            print(
                f"{key.upper()}: {item['path']} | {item['duration_hms']} ({item['duration_sec']}s) "
                f"| dev={item['deviation_sec']}s | {item['size_mb']} MB ({item['size_gb']} GB)",
                flush=True,
            )
    if not report["audio"].get("within_2s_tolerance"):
        raise RuntimeError(f"Audio duration deviation exceeded 2s: {report['audio']}")
    if mode in ("--render-video", "--fast-remux") and not report["video"].get("within_2s_tolerance"):
        raise RuntimeError(f"Video duration deviation exceeded 2s: {report['video']}")


def main():
    if not METRICS_FILE.exists():
        print(f"Error: {METRICS_FILE} not found!")
        sys.exit(1)

    total_dur, cuts, keeps = build_timeline_from_metrics()
    trimmed_dur = round(sum(k["duration"] for k in keeps), 3)
    print(f"Original Video: {format_hms(total_dur)} ({total_dur:.3f}s)", flush=True)
    print(f"Trimmed Output: {format_hms(trimmed_dur)} ({trimmed_dur:.3f}s)", flush=True)
    print(f"Dead Air Cut:   {format_hms(total_dur - trimmed_dur)} ({total_dur - trimmed_dur:.3f}s)", flush=True)

    mode = sys.argv[1] if len(sys.argv) > 1 else "--audio-only"
    render_trimmed_audio(keeps)
    if mode == "--render-video":
        render_master_video(keeps)
    elif mode == "--fast-remux":
        fast_remux_master_video(keeps, trimmed_dur)
    verify_outputs(mode, trimmed_dur)


if __name__ == "__main__":
    main()
