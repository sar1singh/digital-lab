import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(r"c:\Users\sar1s\Documents\MyWork\Git")
sys.path.insert(0, str(REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "tools"))
import synthesize_thinklate_voice as stv

stv._load_credentials()
GEMINI_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
EL_KEY = os.environ.get("ELEVENLABS_API_KEY")

L08_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "thinklate" / "videos" / "longForm" / "L08_ai-layoffs-capex-heist"
S06_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "thinklate" / "videos" / "shortForm" / "S06_30-percent-ai-rehire-trap"
L08_AUDIO_DIR = L08_DIR / "assets" / "audio"
L08_BEATS_DIR = L08_AUDIO_DIR / "beats"
L08_TAKES_DIR = L08_AUDIO_DIR / "takes"
S06_AUDIO_DIR = S06_DIR / "assets" / "audio"
L08_BEATS_DIR.mkdir(parents=True, exist_ok=True)
S06_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

CREATION_FLAGS = 0x08000000 if os.name == "nt" else 0

SELF_DEBATE_STYLE = (
    "Smooth, fluent, slightly cynical late-night storyteller debating with yourself in front of a smart friend — "
    "clearly shift inflection when voicing skeptical questions or corporate excuses vs your sharp, wry rebuttal, "
    "clean continuous conversational flow with minimal breathing and zero audible gasps between clauses"
)

DEBREATH_EXISTING_FILTER = (
    "agate=threshold=-34dB:ratio=2.5:range=-16dB:attack=6:release=110,"
    "loudnorm=I=-16:TP=-1.5:LRA=11"
)


def run_ffmpeg(args: list[str]) -> None:
    res = subprocess.run(["ffmpeg", "-y", *args], creationflags=CREATION_FLAGS, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg error: {res.stderr[-400:]}")


def probe_duration(path: Path) -> float:
    if not path.exists():
        return 0.0
    res = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        creationflags=CREATION_FLAGS, capture_output=True, text=True,
    )
    try:
        return float(res.stdout.strip())
    except Exception:
        return 0.0


def debreath_existing_wav(wav_path: Path) -> None:
    if not wav_path.exists() or probe_duration(wav_path) <= 0.2:
        return
    tmp = wav_path.with_suffix(".debreath.tmp.wav")
    run_ffmpeg(["-i", str(wav_path), "-af", DEBREATH_EXISTING_FILTER, "-ar", "48000", "-ac", "2", str(tmp)])
    tmp.replace(wav_path)


def gemini_tts_rest(text: str, voice_id: str, style: str, out_wav: Path, backup_voice: str | None = "Charon") -> tuple[str, str]:
    models = ["gemini-3.8-flash-tts", "gemini-3.8-flash-lite-tts"]
    voices = [voice_id] + ([backup_voice] if backup_voice and backup_voice != voice_id else [])
    last_err = None
    for mdl in models:
        for v in voices:
            payload = {
                "model": mdl,
                "input": [{
                    "type": "user_input",
                    "content": [{
                        "type": "text",
                        "text": text,
                        "annotations": [{"type": "speech_metadata", "style": style}],
                    }],
                }],
                "response_format": {"type": "audio"},
                "generation_config": {"speech_config": [{"voice": v}]},
            }
            req = urllib.request.Request(
                "https://generativelanguage.googleapis.com/v1beta/interactions",
                data=json.dumps(payload).encode("utf-8"),
                headers={"x-goog-api-key": GEMINI_KEY, "Content-Type": "application/json", "Api-Revision": "2026-05-20"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                audio_b64 = None
                for step in data.get("steps", []):
                    if step.get("type") == "model_output":
                        for part in step.get("content", []):
                            if part.get("type") == "audio" and part.get("data"):
                                audio_b64 = part["data"]
                if not audio_b64:
                    raise RuntimeError("No audio payload in Gemini response")
                tmp = out_wav.with_suffix(".tmp.wav")
                tmp.write_bytes(base64.b64decode(audio_b64))
                run_ffmpeg(["-i", str(tmp), "-af", stv.NATURAL_MASTER_FILTER, "-ar", "48000", "-ac", "2", str(out_wav)])
                tmp.unlink(missing_ok=True)
                return mdl, v
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="ignore")
                last_err = f"{mdl}/{v}: HTTP {exc.code} {body[:160]}"
                if exc.code == 429:
                    break  # Skip backup voice on same quota-limited model; try next model
            except Exception as exc:
                last_err = f"{mdl}/{v}: {exc}"
    raise RuntimeError(f"Gemini TTS failed: {last_err}")


def parse_beats(script_path: Path) -> list[dict]:
    """Parse script into Q-beat speech blocks and [DEAD AIR] pauses."""
    lines = script_path.read_text(encoding="utf-8").splitlines()
    segments: list[dict] = []
    cur_label = "beat_01"
    buf: list[str] = []

    def flush():
        if buf:
            raw = " ".join(buf)
            cleaned = raw.replace("<short pause>", " ").replace("<breath>", " ")
            cleaned = cleaned.replace("///", " ").replace("//", " ")
            cleaned = " ".join(cleaned.split()).strip()
            if cleaned:
                segments.append({"kind": "speech", "label": cur_label, "text": cleaned})
            buf.clear()

    beat_num = 0
    for line in lines:
        s = line.strip()
        if s.startswith("### "):
            flush()
            beat_num += 1
            cur_label = f"beat_{beat_num:02d}"
            continue
        if not s or s.startswith("#") or s.startswith("<!--"):
            continue
        m_dead = re.match(r"^\[DEAD AIR:\s*([0-9.]+)\s*seconds?.*\]$", s, re.IGNORECASE)
        if m_dead:
            flush()
            segments.append({"kind": "silence", "seconds": float(m_dead.group(1)), "label": f"silence_{beat_num:02d}"})
            cur_label = f"beat_{beat_num:02d}b"
            continue
        if s.startswith("["):
            continue
        buf.append(s)
    flush()
    return segments


def concat_segments(segment_paths: list[Path], out_wav: Path, inter_pause_s: float = 1.20) -> None:
    """Concatenate Q-beat speech segments with natural 1.2s act/chapter breathing pauses and micro-fades."""
    pause_wav = out_wav.parent / "_inter_pause.wav"
    run_ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(inter_pause_s), str(pause_wav)])
    tmp_faded_dir = out_wav.parent / "_faded_tmp"
    tmp_faded_dir.mkdir(parents=True, exist_ok=True)
    concat_txt = out_wav.parent / "_concat_list.txt"
    entries = []
    for i, p in enumerate(segment_paths):
        if "silence_" in p.name:
            entries.append(f"file '{p.as_posix()}'")
            continue
        dur = probe_duration(p)
        fp = tmp_faded_dir / p.name
        if dur > 0.15:
            fade_out_start = max(0.0, dur - 0.025)
            run_ffmpeg(["-i", str(p), "-af", f"afade=t=in:st=0:d=0.020,afade=t=out:st={fade_out_start:.3f}:d=0.025", "-ar", "48000", "-ac", "2", str(fp)])
            entries.append(f"file '{fp.as_posix()}'")
        else:
            entries.append(f"file '{p.as_posix()}'")
        if i < len(segment_paths) - 1:
            next_is_silence = "silence_" in segment_paths[i + 1].name
            if not next_is_silence:
                entries.append(f"file '{pause_wav.as_posix()}'")
    concat_txt.write_text("\n".join(entries), encoding="utf-8")
    raw_cat = out_wav.with_suffix(".concat.tmp.wav")
    run_ffmpeg(["-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c:a", "pcm_s16le", str(raw_cat)])
    run_ffmpeg(["-i", str(raw_cat), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "2", str(out_wav)])
    raw_cat.unlink(missing_ok=True)
    pause_wav.unlink(missing_ok=True)
    concat_txt.unlink(missing_ok=True)
    for fp in tmp_faded_dir.glob("*.wav"):
        fp.unlink(missing_ok=True)
    tmp_faded_dir.rmdir()


def main():
    # --- 1. QC Audits on Both Rewritten Solo Scripts ---
    for rel in [
        "digital-lab/03-content-lab/thinklate/videos/longForm/L08_ai-layoffs-capex-heist/script_final.md",
        "digital-lab/03-content-lab/thinklate/videos/shortForm/S06_30-percent-ai-rehire-trap/script_final.md",
    ]:
        full = str(REPO_ROOT / rel)
        r1 = subprocess.run([sys.executable, str(REPO_ROOT / "digital-lab/03-content-lab/thinklate/tools/audit_story_script.py"), full], capture_output=True, text=True, encoding="utf-8", errors="replace", creationflags=CREATION_FLAGS)
        r2 = subprocess.run([sys.executable, str(REPO_ROOT / "digital-lab/03-content-lab/thinklate/tools/fact_check_qc.py"), full], capture_output=True, text=True, encoding="utf-8", errors="replace", creationflags=CREATION_FLAGS)
        print(f"=== QC {rel} (codes: {r1.returncode}, {r2.returncode}) ===")
        print(r1.stdout)
        print(r2.stdout)

    # --- 2. S06 Single-Voice Eddy Synthesis (Short script <60s) ---
    s06_segs = parse_beats(S06_DIR / "script_final.md")
    s06_text = " ".join(t["text"] for t in s06_segs if t["kind"] == "speech")
    s06_plain = s06_text

    s06_eddy = S06_AUDIO_DIR / "S06_eddy_custom_voice_master.wav"
    s06_v2_marker = s06_eddy.with_suffix(".v2clean")
    if s06_v2_marker.exists() and s06_eddy.exists() and probe_duration(s06_eddy) > 10.0:
        print(f"S06_EDDY_CACHED_V2:", s06_eddy, f"{probe_duration(s06_eddy):.2f}s")
    else:
        s06_eddy_tmp = s06_eddy.with_suffix(".new.wav")
        try:
            mdl_used, v_used = gemini_tts_rest(s06_text, "voice_x5l6j0ub25m1", SELF_DEBATE_STYLE, s06_eddy_tmp)
            s06_eddy_tmp.replace(s06_eddy)
            s06_v2_marker.write_text("ok", encoding="utf-8")
            print(f"S06_EDDY_OK ({mdl_used}/{v_used}):", s06_eddy, f"{probe_duration(s06_eddy):.2f}s")
        except Exception as exc:
            s06_eddy_tmp.unlink(missing_ok=True)
            debreath_existing_wav(s06_eddy)
            print("S06_EDDY_DEBREATHED_CACHED:", exc, f"existing={probe_duration(s06_eddy):.2f}s")

    s06_liam = S06_AUDIO_DIR / "S06_liam_elevenlabs_master.wav"
    if EL_KEY and (not s06_liam.exists() or probe_duration(s06_liam) <= 2.0):
        try:
            stv._synthesize_elevenlabs(s06_plain, stv.VOICE_PROFILES["owl"], str(s06_liam), voice_override="TX3LPaxmHKxFdv7VOQHJ")
            print("S06_LIAM_OK:", s06_liam, f"{probe_duration(s06_liam):.2f}s")
        except Exception as exc:
            print("S06_LIAM_ERR:", exc)
    else:
        print("S06_LIAM_CACHED:", s06_liam, f"{probe_duration(s06_liam):.2f}s")

    # De-breath any cached Eddy takes from prior runs
    if L08_TAKES_DIR.exists():
        for take_p in sorted(L08_TAKES_DIR.glob("*_eddy.wav")):
            debreath_existing_wav(take_p)

    # --- 3. L08 5-Beat Solo Eddy Synthesis (Only 5-6 Requests Total!) ---
    l08_segs = parse_beats(L08_DIR / "script_final.md")
    print("L08_BEAT_SEGMENTS:", len(l08_segs))
    completed_paths: list[Path] = []
    quota_halted = False

    for idx, seg in enumerate(l08_segs, 1):
        if seg["kind"] == "silence":
            sil_p = L08_BEATS_DIR / f"{idx:02d}_{seg['label']}.wav"
            run_ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(seg["seconds"]), str(sil_p)])
            completed_paths.append(sil_p)
            print(f"  [{idx}/{len(l08_segs)}] SILENCE {seg['seconds']}s")
            continue

        beat_p = L08_BEATS_DIR / f"{idx:02d}_{seg['label']}_eddy.wav"
        v2_marker = beat_p.with_suffix(".v2clean")
        if v2_marker.exists() and beat_p.exists() and probe_duration(beat_p) > 2.0:
            completed_paths.append(beat_p)
            print(f"  [{idx}/{len(l08_segs)}] CACHED_V2 {beat_p.name} ({probe_duration(beat_p):.2f}s)")
            continue

        if not quota_halted:
            beat_tmp = beat_p.with_suffix(".new.wav")
            try:
                mdl_u, v_u = gemini_tts_rest(seg["text"], "voice_x5l6j0ub25m1", SELF_DEBATE_STYLE, beat_tmp)
                beat_tmp.replace(beat_p)
                v2_marker.write_text("ok", encoding="utf-8")
                completed_paths.append(beat_p)
                print(f"  [{idx}/{len(l08_segs)}] OK_V2 ({mdl_u}/{v_u}) {beat_p.name} ({probe_duration(beat_p):.2f}s)")
                time.sleep(7.0)
                continue
            except Exception as exc:
                beat_tmp.unlink(missing_ok=True)
                print(f"  [{idx}/{len(l08_segs)}] QUOTA_FALLBACK_DEBREATH: {exc}")
                quota_halted = True

        if beat_p.exists() and probe_duration(beat_p) > 2.0:
            debreath_existing_wav(beat_p)
            completed_paths.append(beat_p)
            print(f"  [{idx}/{len(l08_segs)}] DEBREATHED_CACHED {beat_p.name} ({probe_duration(beat_p):.2f}s)")

    l08_master = L08_AUDIO_DIR / "L08_voiceover_master.wav"
    if len(completed_paths) == len(l08_segs):
        concat_segments(completed_paths, l08_master)
        master_label = f"L08 Complete Solo Eddy Master ({probe_duration(l08_master):.1f}s)"
        beat_cards = completed_paths
    else:
        # Fallback cleanly to cached solo Eddy takes (take_01, take_03, take_05 — zero Vera/Kore!)
        solo_eddy_takes = sorted([p for p in L08_TAKES_DIR.glob("*_eddy.wav") if probe_duration(p) > 0.5])
        if completed_paths:
            concat_segments(completed_paths, l08_master)
            master_label = f"L08 Partial Solo Eddy Master ({len(completed_paths)}/{len(l08_segs)} beats, {probe_duration(l08_master):.1f}s)"
            beat_cards = completed_paths
        elif solo_eddy_takes:
            concat_segments(solo_eddy_takes, l08_master)
            master_label = f"L08 Solo Eddy Preview ({len(solo_eddy_takes)} cached Eddy takes, {probe_duration(l08_master):.1f}s — Zero Vera/Kore)"
            beat_cards = solo_eddy_takes
        else:
            master_label = "L08 Audio Pending Quota Reset"
            beat_cards = []
    print("L08_MASTER_STATUS:", master_label)

    # --- 4. Refresh L08_AUDIO_REVIEW.html (100% Single-Host Eddy Only — Zero Vera/Kore) ---
    cards_html = "\n".join(
        f'<div class="card"><div class="title">{p.name} ({probe_duration(p):.1f}s)</div>'
        f'<audio controls src="{"beats" if p.parent == L08_BEATS_DIR else "takes"}/{p.name}"></audio></div>'
        for p in beat_cards
    )
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>ThinkLate L08 &amp; S06 — Solo Eddy Voiceover Review</title>
<style>body{{background:#080C14;color:#F1F5F9;font-family:system-ui,sans-serif;padding:28px;max-width:920px;margin:0 auto}}
h1{{color:#E2FF00;font-size:24px}}h2{{color:#06B6D4;font-size:15px;text-transform:uppercase;margin:24px 0 10px}}
.card{{background:#0F1626;border:1px solid #1E2C48;border-radius:12px;padding:14px 18px;margin-bottom:10px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px}}
.title{{font-weight:700;font-size:15px}}audio{{width:340px;max-width:100%}}</style></head><body>
<h1>ThinkLate L08 &amp; S06 — Single-Host Self-Debate Review (Eddy Only)</h1>
<h2>Locked Master Tracks (Eddy Custom voice_x5l6j0ub25m1 — Solo Self-Debate)</h2>
<div class="card"><div class="title">{master_label}</div><audio controls src="L08_voiceover_master.wav"></audio></div>
<div class="card"><div class="title">S06 Master — Eddy Custom (voice_x5l6j0ub25m1, {probe_duration(s06_eddy):.1f}s)</div><audio controls src="../../../../shortForm/S06_30-percent-ai-rehire-trap/assets/audio/S06_eddy_custom_voice_master.wav"></audio></div>
<div class="card"><div class="title">S06 Optional — ElevenLabs Liam ({probe_duration(s06_liam):.1f}s)</div><audio controls src="../../../../shortForm/S06_30-percent-ai-rehire-trap/assets/audio/S06_liam_elevenlabs_master.wav"></audio></div>
<h2>Solo Eddy Segments</h2>
{cards_html}
</body></html>"""
    (L08_AUDIO_DIR / "L08_AUDIO_REVIEW.html").write_text(html, encoding="utf-8")
    print("REVIEW_HTML_UPDATED:", L08_AUDIO_DIR / "L08_AUDIO_REVIEW.html")


if __name__ == "__main__":
    main()
