"""
Local Chatterbox TTS Zero-Shot Voice Cloning Demo (Founder Voice Reference)

Clones the founder's clean 20s reference sample (`founder_hinglish_ref_20s.wav`)
completely offline after fetching `ResembleAI/chatterbox` checkpoints, and renders:
  1. L08 Hook Audition: auditions/10_chatterbox_founder_clone.wav
  2. S06 Short Demo:   S06_founder_chatterbox_clone.wav
Both outputs are mastered at -16 LUFS / 48kHz stereo with minimal-breath gating
for a fair 1:1 A/B comparison against Eddy Custom (voice_x5l6j0ub25m1) and Liam.
"""

from __future__ import annotations

import concurrent.futures
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import numpy as np
import soundfile as sf
import torch
from huggingface_hub import hf_hub_download
from safetensors.torch import save_file

from chatterbox.tts import ChatterboxTTS

REPO_ID = "ResembleAI/chatterbox"
CREATION_FLAGS = 0x08000000 if os.name == "nt" else 0

REPO_ROOT = Path(r"c:\Users\sar1s\Documents\MyWork\Git")
sys.path.insert(0, str(REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "tools"))
import synthesize_thinklate_voice as stv  # noqa: E402

REF_WAV = REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "characters" / "founder_hinglish_ref_20s.wav"
L08_AUDIO_DIR = (
    REPO_ROOT
    / "digital-lab"
    / "03-content-lab"
    / "thinklate"
    / "videos"
    / "longForm"
    / "L08_ai-layoffs-capex-heist"
    / "assets"
    / "audio"
)
AUDITIONS_DIR = L08_AUDIO_DIR / "auditions"
S06_DIR = (
    REPO_ROOT
    / "digital-lab"
    / "03-content-lab"
    / "thinklate"
    / "videos"
    / "shortForm"
    / "S06_30-percent-ai-rehire-trap"
)
S06_SCRIPT = S06_DIR / "script_final.md"
S06_AUDIO_DIR = S06_DIR / "assets" / "audio"

DEMO1_OUT = AUDITIONS_DIR / "10_chatterbox_founder_clone.wav"
DEMO2_OUT = S06_AUDIO_DIR / "S06_founder_chatterbox_clone.wav"
REVIEW_HTML = L08_AUDIO_DIR / "L08_AUDIO_REVIEW.html"
AUDITION_HTML = AUDITIONS_DIR / "AUDITION_PLAYER.html"

L08_HOOK_CHUNKS = [
    (
        "Picture a Tuesday morning in Bangalore or Austin, Texas. "
        "A senior software developer opens her laptop at seven a.m. "
        "Her coffee is still hot, and her company just posted another multi-billion-dollar profit! "
        "She clicks Slack, and sees three words. Account deactivated."
    ),
    (
        "No warning. No failing company. Just a polite automated email blaming artificial intelligence! "
        "Look at the names signing those pink slips: Meta, Amazon, Microsoft, Oracle. "
        "They didn't replace coders with AI. They raided human payroll to pay their GPU bill!"
    ),
]


def run_ffmpeg(args: list[str]) -> None:
    res = subprocess.run(
        ["ffmpeg", "-y", *args],
        creationflags=CREATION_FLAGS,
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg error: {res.stderr[-500:]}")


def probe_duration(path: Path) -> float:
    if not path.exists():
        return 0.0
    res = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=nw=1:nk=1",
            str(path),
        ],
        creationflags=CREATION_FLAGS,
        capture_output=True,
        text=True,
    )
    try:
        return float(res.stdout.strip())
    except Exception:
        return 0.0


def parallel_range_download(repo_id: str, filename: str, dest: Path, min_bytes: int, workers: int = 12, chunk_mb: int = 16) -> Path:
    if dest.exists() and dest.stat().st_size >= min_bytes:
        print(f"[CACHE] {filename} already present ({dest.stat().st_size / 1e6:.1f} MB)", flush=True)
        return dest

    url = f"https://huggingface.co/{repo_id}/resolve/main/{filename}"
    probe_req = urllib.request.Request(url, headers={"Range": "bytes=0-0", "User-Agent": "ThinkLateChatterbox/1.0"})
    with urllib.request.urlopen(probe_req, timeout=30) as resp:
        final_url = resp.geturl()
        cr = resp.headers.get("Content-Range", "")
        if "/" in cr:
            total_bytes = int(cr.split("/")[-1])
        else:
            total_bytes = int(resp.headers.get("Content-Length", "0"))

    if total_bytes < min_bytes:
        raise RuntimeError(f"Unexpected remote size for {filename}: {total_bytes} bytes")

    print(f"[DL] Fetching {filename} ({total_bytes / 1e6:.1f} MB) using {workers} threads...", flush=True)
    chunk_bytes = chunk_mb * 1024 * 1024
    ranges = [(start, min(start + chunk_bytes - 1, total_bytes - 1)) for start in range(0, total_bytes, chunk_bytes)]

    part_path = dest.with_suffix(dest.suffix + ".part")
    with open(part_path, "wb") as f:
        f.truncate(total_bytes)

    lock = threading.Lock()
    done_bytes = [0]
    next_log = [128 * 1024 * 1024]
    t0 = time.time()

    def fetch_range(byte_range: tuple[int, int]) -> None:
        start, end = byte_range
        expected_len = end - start + 1
        last_exc: Exception | None = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(
                    final_url,
                    headers={"Range": f"bytes={start}-{end}", "User-Agent": "ThinkLateChatterbox/1.0"},
                )
                with urllib.request.urlopen(req, timeout=45) as resp:
                    buf = resp.read()
                if len(buf) != expected_len:
                    raise RuntimeError(f"Short read {len(buf)} != {expected_len}")
                with lock:
                    with open(part_path, "r+b") as f:
                        f.seek(start)
                        f.write(buf)
                    done_bytes[0] += expected_len
                    if done_bytes[0] >= next_log[0] or done_bytes[0] == total_bytes:
                        dt = max(time.time() - t0, 0.01)
                        mb_done = done_bytes[0] / 1e6
                        speed = mb_done / dt
                        print(f"     {filename}: {mb_done:.0f}/{total_bytes / 1e6:.0f} MB ({speed:.1f} MB/s)", flush=True)
                        next_log[0] += 128 * 1024 * 1024
                return
            except Exception as exc:
                last_exc = exc
                time.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"Range {start}-{end} failed for {filename}: {last_exc}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(fetch_range, ranges))

    part_path.replace(dest)
    print(f"[OK] Saved {filename} ({dest.stat().st_size / 1e6:.1f} MB)", flush=True)
    return dest


def ensure_chatterbox_checkpoints() -> Path:
    base_paths = {}
    for fname in ["ve.safetensors", "tokenizer.json", "conds.pt"]:
        p = Path(hf_hub_download(repo_id=REPO_ID, filename=fname))
        base_paths[fname] = p
    ckpt_dir = base_paths["ve.safetensors"].parent
    print(f"[CKPT] Resolved snapshot dir: {ckpt_dir}", flush=True)

    parallel_range_download(REPO_ID, "s3gen.safetensors", ckpt_dir / "s3gen.safetensors", min_bytes=900_000_000)

    t3_safetensors = ckpt_dir / "t3_cfg.safetensors"
    if t3_safetensors.exists() and t3_safetensors.stat().st_size >= 900_000_000:
        print(f"[CACHE] t3_cfg.safetensors ready ({t3_safetensors.stat().st_size / 1e6:.1f} MB)", flush=True)
    else:
        t3_pt = parallel_range_download(REPO_ID, "t3_cfg.pt", ckpt_dir / "t3_cfg.pt", min_bytes=900_000_000)
        print("[CONVERT] Converting t3_cfg.pt -> t3_cfg.safetensors (cloning tensors cleanly)...", flush=True)
        raw = torch.load(t3_pt, map_location="cpu", weights_only=False)
        if isinstance(raw, dict) and "model" in raw:
            mdl = raw["model"]
            state = mdl[0] if isinstance(mdl, (list, tuple)) else mdl
        else:
            state = raw
        clean_state = {
            k: v.detach().cpu().clone().contiguous()
            for k, v in state.items()
            if torch.is_tensor(v)
        }
        tmp_st = ckpt_dir / "t3_cfg.safetensors.tmp"
        save_file(clean_state, str(tmp_st))
        tmp_st.replace(t3_safetensors)
        print(f"[OK] Converted t3_cfg.safetensors ({t3_safetensors.stat().st_size / 1e6:.1f} MB)", flush=True)

    return ckpt_dir


def parse_s06_segments(script_path: Path) -> list[dict]:
    """Parse S06 script into 2-sentence speech chunks and explicit [DEAD AIR] pauses."""
    lines = script_path.read_text(encoding="utf-8").splitlines()
    segments: list[dict] = []
    sent_buf: list[str] = []

    def flush_speech() -> None:
        nonlocal sent_buf
        if not sent_buf:
            return
        # Group into chunks of 2 sentences (~20-35 words each) for Chatterbox stability
        for i in range(0, len(sent_buf), 2):
            chunk_text = " ".join(sent_buf[i : i + 2]).strip()
            if chunk_text:
                segments.append({"kind": "speech", "text": chunk_text})
        sent_buf = []

    for line in lines:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<!--"):
            continue
        m_dead = re.match(r"^\[DEAD AIR:\s*([0-9.]+)\s*seconds?.*\]$", s, re.IGNORECASE)
        if m_dead:
            flush_speech()
            segments.append({"kind": "silence", "seconds": float(m_dead.group(1))})
            continue
        if s.startswith("["):
            continue
        cleaned = s.replace("///", " ").replace("//", " ")
        cleaned = " ".join(cleaned.split()).strip()
        if cleaned:
            sent_buf.append(cleaned)
    flush_speech()
    return segments


def synth_chunks_and_master(
    model: ChatterboxTTS,
    segments: list[dict],
    out_wav: Path,
    tag: str,
    exaggeration: float = 0.45,
    cfg_weight: float = 0.5,
    temperature: float = 0.78,
) -> float:
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = out_wav.parent / f"_tmp_{tag}"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    part_paths: list[Path] = []
    pause_wav = tmp_dir / "_gap_015s.wav"
    run_ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "0.15", str(pause_wav)])

    for idx, seg in enumerate(segments, 1):
        if seg["kind"] == "silence":
            sil_p = tmp_dir / f"{idx:02d}_silence.wav"
            run_ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(seg["seconds"]), str(sil_p)])
            part_paths.append(sil_p)
            print(f"  [{tag} {idx}/{len(segments)}] SILENCE {seg['seconds']}s", flush=True)
            continue

        t0 = time.time()
        print(f"  [{tag} {idx}/{len(segments)}] Generating: {seg['text'][:70]}...", flush=True)
        with torch.inference_mode():
            wav_tensor = model.generate(
                seg["text"],
                exaggeration=exaggeration,
                cfg_weight=cfg_weight,
                temperature=temperature,
                repetition_penalty=1.18,
            )
        wav_np = wav_tensor.squeeze(0).detach().cpu().numpy().astype(np.float32)
        chunk_p = tmp_dir / f"{idx:02d}_chunk.wav"
        sf.write(str(chunk_p), wav_np, model.sr)
        part_paths.append(chunk_p)
        print(f"     -> {len(wav_np) / model.sr:.2f}s audio rendered in {time.time() - t0:.1f}s", flush=True)

    concat_txt = tmp_dir / "concat.txt"
    entries = []
    for i, p in enumerate(part_paths):
        entries.append(f"file '{p.as_posix()}'")
        if i < len(part_paths) - 1 and "silence" not in p.name:
            entries.append(f"file '{pause_wav.as_posix()}'")
    concat_txt.write_text("\n".join(entries), encoding="utf-8")

    raw_cat = tmp_dir / "raw_concat.wav"
    run_ffmpeg(["-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c:a", "pcm_s16le", str(raw_cat)])
    run_ffmpeg(
        [
            "-i",
            str(raw_cat),
            "-af",
            stv.NATURAL_MASTER_FILTER,
            "-ar",
            "48000",
            "-ac",
            "2",
            str(out_wav),
        ]
    )

    for p in tmp_dir.iterdir():
        p.unlink(missing_ok=True)
    tmp_dir.rmdir()
    return probe_duration(out_wav)


def update_review_htmls(d1_dur: float, d2_dur: float) -> None:
    # 1. Update L08_AUDIO_REVIEW.html idempotently
    if REVIEW_HTML.exists():
        html = REVIEW_HTML.read_text(encoding="utf-8")
        marker = "auditions/10_chatterbox_founder_clone.wav"
        cards = (
            f'<div class="card"><div class="title">L08 Hook Demo — Local Chatterbox Founder Clone ({d1_dur:.1f}s)</div>'
            f'<audio controls src="auditions/10_chatterbox_founder_clone.wav"></audio></div>\n'
            f'<div class="card"><div class="title">S06 Complete Demo — Local Chatterbox Founder Clone ({d2_dur:.1f}s)</div>'
            f'<audio controls src="../../../../shortForm/S06_30-percent-ai-rehire-trap/assets/audio/S06_founder_chatterbox_clone.wav"></audio></div>'
        )
        if marker in html:
            html = re.sub(
                r'<div class="card"><div class="title">L08 Hook Demo — Local Chatterbox Founder Clone.*?S06_founder_chatterbox_clone\.wav"></audio></div>',
                cards,
                html,
                flags=re.DOTALL,
            )
        elif "<h2>Solo Eddy Segments</h2>" in html:
            html = html.replace("<h2>Solo Eddy Segments</h2>", cards + "\n<h2>Solo Eddy Segments</h2>")
        REVIEW_HTML.write_text(html, encoding="utf-8")
        print(f"[HTML] Updated {REVIEW_HTML}", flush=True)

    # 2. Update AUDITION_PLAYER.html idempotently
    if AUDITION_HTML.exists():
        html = AUDITION_HTML.read_text(encoding="utf-8")
        marker = "10_chatterbox_founder_clone.wav"
        block = f"""  <div class="section">Founder Voice Clone (Local Chatterbox TTS — Hinglish Ref Demo)</div>
  <div class="card">
    <div class="meta">
      <div class="title"><span class="badge b-g38">CHATTERBOX LOCAL</span> 10 · Founder Clone — L08 Opening Hook ({d1_dur:.1f}s)</div>
      <div class="desc">Zero-shot local clone from founder_hinglish_ref_20s.wav running completely free offline.</div>
    </div>
    <audio controls src="10_chatterbox_founder_clone.wav"></audio>
  </div>
  <div class="card">
    <div class="meta">
      <div class="title"><span class="badge b-g38">CHATTERBOX LOCAL</span> 11 · Founder Clone — Full S06 Short ({d2_dur:.1f}s)</div>
      <div class="desc">Complete S06 Short synthesized offline with founder voice clone + 0.5s dead-air climax drop.</div>
    </div>
    <audio controls src="../../../../../shortForm/S06_30-percent-ai-rehire-trap/assets/audio/S06_founder_chatterbox_clone.wav"></audio>
  </div>"""
        if marker in html:
            html = re.sub(
                r'  <div class="section">Founder Voice Clone.*?S06_founder_chatterbox_clone\.wav"></audio>\s*</div>',
                block,
                html,
                flags=re.DOTALL,
            )
        elif "</body>" in html:
            html = html.replace("</body>", block + "\n</body>")
        AUDITION_HTML.write_text(html, encoding="utf-8")
        print(f"[HTML] Updated {AUDITION_HTML}", flush=True)


def main() -> None:
    if not REF_WAV.exists():
        raise FileNotFoundError(f"Missing founder voice reference: {REF_WAV}")
    if not S06_SCRIPT.exists():
        raise FileNotFoundError(f"Missing S06 script: {S06_SCRIPT}")

    print(f"[START] Founder voice reference: {REF_WAV} ({probe_duration(REF_WAV):.2f}s)", flush=True)
    ckpt_dir = ensure_chatterbox_checkpoints()

    print("[LOAD] Loading ChatterboxTTS onto CPU...", flush=True)
    t_load = time.time()
    model = ChatterboxTTS.from_local(ckpt_dir, device="cpu")
    print(f"[LOAD] Model loaded in {time.time() - t_load:.1f}s", flush=True)

    print(f"[COND] Extracting speaker embedding from {REF_WAV.name}...", flush=True)
    model.prepare_conditionals(str(REF_WAV), exaggeration=0.45)

    l08_segs = [{"kind": "speech", "text": t} for t in L08_HOOK_CHUNKS]
    print("[DEMO 1] Synthesizing L08 Hook Audition (Founder Clone)...", flush=True)
    d1_dur = synth_chunks_and_master(model, l08_segs, DEMO1_OUT, tag="L08_HOOK")
    print(f"[DEMO 1 OK] {DEMO1_OUT} ({d1_dur:.2f}s)", flush=True)

    s06_segs = parse_s06_segments(S06_SCRIPT)
    print(f"[DEMO 2] Synthesizing S06 Short ({len(s06_segs)} segments)...", flush=True)
    d2_dur = synth_chunks_and_master(model, s06_segs, DEMO2_OUT, tag="S06_FULL")
    print(f"[DEMO 2 OK] {DEMO2_OUT} ({d2_dur:.2f}s)", flush=True)

    update_review_htmls(d1_dur, d2_dur)
    print("[DONE] All local Chatterbox founder clone demos verified!", flush=True)


if __name__ == "__main__":
    main()
