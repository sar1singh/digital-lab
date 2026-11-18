"""
ThinkLate Dual-Anchor Voiceover Synthesizer
Primary Engine: Google Gemini 3.8 Flash TTS (Interactions API, natural prosody, Voice Design & Replication)
Studio Alt Engine: ElevenLabs (eleven_v3 / eleven_multilingual_v2)
Fallback Engine: Microsoft Edge-TTS Neural (ONLY when explicitly selected via --engine edge)

Characters:
- owl    -> Eddy Thinklate (Founder & Lead Host, Gemini voice: Charon / Orus / custom voice_...)
- falcon -> Vera Vance (Forensic Investigator, Gemini voice: Kore / Aoede / custom voice_...)
"""

import argparse
import asyncio
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _find_repo_root(start_dir: str) -> str:
    cur = os.path.abspath(start_dir)
    for _ in range(6):
        if os.path.isdir(os.path.join(cur, ".agents")) or os.path.isfile(os.path.join(cur, "PROFILE.md")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))


REPO_ROOT = _find_repo_root(SCRIPT_DIR)
AUDIO_REF_DIR = os.path.join(
    REPO_ROOT, "digital-lab", "03-content-lab", "shared", "motion_engine", "public", "audio"
)

GEMINI_TTS_MODEL = "gemini-3.8-flash-tts"
ELEVENLABS_DEFAULT_MODEL = "eleven_v3"
ELEVENLABS_FALLBACK_MODEL = "eleven_multilingual_v2"

# Preserve natural dynamic range (LRA=11) while softly attenuating heavy inter-clause breath gasps
# via downward expansion before loudnorm, and trimming only dead leading/trailing padding.
NATURAL_MASTER_FILTER = (
    "silenceremove=start_periods=1:start_duration=0.02:start_threshold=-52dB,"
    "areverse,silenceremove=start_periods=1:start_duration=0.02:start_threshold=-52dB,areverse,"
    "agate=threshold=-36dB:ratio=2.2:range=-14dB:attack=8:release=120,"
    "loudnorm=I=-16:TP=-1.5:LRA=11"
)

VOICE_PROFILES = {
    "owl": {
        "name": "Eddy Thinklate (Founder & Lead Host)",
        "gemini_voice": "voice_x5l6j0ub25m1",  # Eddy Custom Voice Design (Default)
        "gemini_backup_voice": "Charon",       # Secondary Male Backup
        "gemini_style": (
            "Smooth, fluent, witty late-night storyteller talking to a smart friend — "
            "crisp conversational flow, minimal breathing, zero audible gasps or heavy inhales "
            "between clauses, slight dry amusement, clear contrast when voicing a skeptical "
            "question versus your sharp rebuttal"
        ),
        "gemini_design_prompt": (
            "A grounded, slightly cynical 35-year-old software engineer and late-night "
            "documentary storyteller with a warm baritone, natural conversational timing, "
            "subtle dry humor, and clear articulation — sounds like a sharp friend over coffee, "
            "never like a news anchor or corporate narrator."
        ),
        "elevenlabs_voice": "TX3LPaxmHKxFdv7VOQHJ",  # Liam (Shorts-only optional ElevenLabs voice)
        "gemini_eq_filter": NATURAL_MASTER_FILTER,
        "edge_voice": "en-US-AndrewMultilingualNeural",
        "rate": "+4%",
        "pitch": "+0Hz",
        "volume": "+0%",
        "edge_eq_filter": NATURAL_MASTER_FILTER,
        "ref_audio": os.path.join(AUDIO_REF_DIR, "owl_executive_hook.wav"),
    },
    "falcon": {
        "name": "Vera Vance (Forensic Investigator)",
        "gemini_voice": "Kore",
        "gemini_backup_voice": "Kore",
        "gemini_style": (
            "Crisp, curious, perceptive journalist walking a friend through shocking "
            "corporate receipts — natural conversational rhythm, warm presence, "
            "subtle eyebrow-raise inflection on contradictions"
        ),
        "gemini_design_prompt": (
            "A sharp, perceptive 32-year-old investigative tech journalist with a clear, "
            "warm mid-range voice, crisp articulation, natural conversational cadence, "
            "and subtle wry skepticism when exposing corporate contradictions."
        ),
        "elevenlabs_voice": "TX3LPaxmHKxFdv7VOQHJ",  # Liam (if ElevenLabs override used)
        "gemini_eq_filter": NATURAL_MASTER_FILTER,
        "edge_voice": "en-US-AvaMultilingualNeural",
        "rate": "+3%",
        "pitch": "+0Hz",
        "volume": "+0%",
        "edge_eq_filter": NATURAL_MASTER_FILTER,
        "ref_audio": os.path.join(AUDIO_REF_DIR, "falcon_investigation.wav"),
    },
}


def _load_credentials() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for candidate in [
        os.path.join(REPO_ROOT, ".agents", "credentials", ".env"),
        os.path.join(REPO_ROOT, "digital-lab", "03-content-lab", "thinklate", ".env"),
        os.path.join(REPO_ROOT, ".env"),
    ]:
        if os.path.isfile(candidate):
            load_dotenv(candidate, override=False)


def _run_ffmpeg_master(src_path: str, eq_filter: str, output_path: str) -> None:
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        src_path,
        "-af",
        eq_filter,
        "-ar",
        "48000",
        "-ac",
        "2",
        output_path,
    ]
    creationflags = 0x08000000 if os.name == "nt" else 0
    res = subprocess.run(cmd, creationflags=creationflags, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg mastering failed: {res.stderr[-400:]}")


def _clean_script_text_for_tts(text: str) -> str:
    """Strip teleprompter beat cues (//, ///) without injecting extra commas or breath gasps."""
    cleaned = text.replace("<short pause>", " ").replace("<breath>", " ")
    cleaned = cleaned.replace("///", " ").replace("//", " ")
    cleaned = " ".join(cleaned.split())
    return cleaned.strip()


def _synthesize_gemini(
    text: str,
    profile: dict,
    output_path: str,
    voice_override: str | None = None,
    style_override: str | None = None,
    model_override: str | None = None,
) -> None:
    _load_credentials()
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not configured in environment or .agents/credentials/.env")

    from google import genai

    model = model_override or GEMINI_TTS_MODEL
    voice_name = voice_override or profile["gemini_voice"]
    style = style_override or profile["gemini_style"]
    spoken_text = _clean_script_text_for_tts(text)

    client = genai.Client(api_key=api_key, http_options={"api_version": "v1beta"})
    voices_to_try = [voice_name]
    backup = profile.get("gemini_backup_voice")
    if not voice_override and backup and backup != voice_name:
        voices_to_try.append(backup)

    interaction = None
    last_exc = None
    for candidate_voice in voices_to_try:
        try:
            interaction = client.interactions.create(
                model=model,
                input=[
                    {
                        "type": "user_input",
                        "content": [
                            {
                                "type": "text",
                                "text": spoken_text,
                                "annotations": [
                                    {
                                        "type": "speech_metadata",
                                        "style": style,
                                    }
                                ],
                            }
                        ],
                    }
                ],
                response_format={"type": "audio"},
                generation_config={
                    "speech_config": [
                        {"voice": candidate_voice},
                    ]
                },
            )
            break
        except Exception as exc:
            last_exc = exc
            if candidate_voice != voices_to_try[-1]:
                print(
                    f"[WARN] Gemini voice '{candidate_voice}' failed ({exc}); retrying backup '{voices_to_try[-1]}'...",
                    file=sys.stderr,
                )
    if interaction is None:
        raise RuntimeError(f"Gemini 3.8 TTS failed: {last_exc}")

    out_audio = getattr(interaction, "output_audio", None)
    if not out_audio or not getattr(out_audio, "data", None):
        raise RuntimeError("Gemini 3.8 TTS returned no output_audio payload.")

    raw_data = out_audio.data
    audio_bytes = base64.b64decode(raw_data) if isinstance(raw_data, str) else bytes(raw_data)

    temp_wav = output_path + ".gemini.tmp.wav"
    try:
        if audio_bytes[:4] == b"RIFF":
            with open(temp_wav, "wb") as f:
                f.write(audio_bytes)
        else:
            import wave

            with wave.open(temp_wav, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                wf.writeframes(audio_bytes)

        _run_ffmpeg_master(temp_wav, profile["gemini_eq_filter"], output_path)
    finally:
        if os.path.exists(temp_wav):
            os.remove(temp_wav)


def create_designed_gemini_voice(
    display_name: str,
    gender: str,
    prompt: str,
    language_code: str = "en-US",
    preview_out: str | None = None,
) -> str:
    """Create a persistent custom Gemini 3.8 TTS voice persona using Voice Design."""
    _load_credentials()
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not configured.")

    from google import genai

    client = genai.Client(api_key=api_key, http_options={"api_version": "v1beta"})
    created = client.voices.create(
        store=True,
        voice={
            "model": GEMINI_TTS_MODEL,
            "type": "prompted",
            "display_name": display_name,
            "gender": gender,
            "language_code": language_code,
            "prompted": {"input": prompt},
        },
    )
    if preview_out and getattr(created, "sample_audio", None) and getattr(created.sample_audio, "data", None):
        raw_prev = created.sample_audio.data
        prev_bytes = base64.b64decode(raw_prev) if isinstance(raw_prev, str) else bytes(raw_prev)
        os.makedirs(os.path.dirname(os.path.abspath(preview_out)), exist_ok=True)
        with open(preview_out, "wb") as f:
            f.write(prev_bytes)
    return created.id


def _synthesize_elevenlabs(
    text: str,
    profile: dict,
    output_path: str,
    voice_override: str | None = None,
    model_override: str | None = None,
) -> None:
    _load_credentials()
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("ELEVENLABS_API_KEY not configured in environment or .agents/credentials/.env")

    voice_id = voice_override or profile["elevenlabs_voice"]
    spoken_text = _clean_script_text_for_tts(text)
    models_to_try = [model_override] if model_override else [ELEVENLABS_DEFAULT_MODEL, ELEVENLABS_FALLBACK_MODEL]

    last_err = None
    audio_bytes = None
    for model_id in models_to_try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        payload = {
            "text": spoken_text,
            "model_id": model_id,
            "voice_settings": {
                "stability": 0.42,
                "similarity_boost": 0.78,
                "style": 0.35,
                "use_speaker_boost": True,
            },
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "xi-api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                audio_bytes = resp.read()
            break
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="ignore")
            last_err = f"HTTP {exc.code} ({model_id}): {body[:300]}"
        except Exception as exc:
            last_err = f"{model_id}: {exc}"

    if not audio_bytes:
        raise RuntimeError(f"ElevenLabs TTS failed: {last_err}")

    temp_mp3 = output_path + ".eleven.tmp.mp3"
    try:
        with open(temp_mp3, "wb") as f:
            f.write(audio_bytes)
        _run_ffmpeg_master(temp_mp3, profile["gemini_eq_filter"], output_path)
    finally:
        if os.path.exists(temp_mp3):
            os.remove(temp_mp3)


async def _synthesize_edge(text: str, profile: dict, output_path: str) -> None:
    import edge_tts

    spoken_text = _clean_script_text_for_tts(text)
    temp_mp3 = output_path + ".edge.tmp.mp3"
    try:
        communicate = edge_tts.Communicate(
            spoken_text,
            profile["edge_voice"],
            rate=profile["rate"],
            pitch=profile["pitch"],
            volume=profile["volume"],
        )
        await communicate.save(temp_mp3)
        _run_ffmpeg_master(temp_mp3, profile["edge_eq_filter"], output_path)
    finally:
        if os.path.exists(temp_mp3):
            os.remove(temp_mp3)


async def synthesize_speech(
    text: str,
    speaker: str,
    output_path: str,
    engine: str = "gemini",
    voice_override: str | None = None,
    style_override: str | None = None,
    model_override: str | None = None,
    allow_fallback: bool = False,
) -> str:
    speaker = speaker.lower()
    if speaker not in VOICE_PROFILES:
        raise ValueError(f"Unknown speaker '{speaker}'. Must be 'owl' or 'falcon'.")

    profile = VOICE_PROFILES[speaker]
    if engine == "gemini":
        try:
            _synthesize_gemini(
                text,
                profile,
                output_path,
                voice_override=voice_override,
                style_override=style_override,
                model_override=model_override,
            )
            print(
                f"[OK] Synthesized {profile['name']} via Gemini 3.8 TTS "
                f"({voice_override or profile['gemini_voice']}) -> {output_path}"
            )
            return "gemini"
        except Exception as exc:
            if not allow_fallback:
                raise
            print(f"[WARN] Gemini TTS failed ({exc}); falling back to Edge-TTS...", file=sys.stderr)

    elif engine == "elevenlabs":
        _synthesize_elevenlabs(
            text,
            profile,
            output_path,
            voice_override=voice_override,
            model_override=model_override,
        )
        print(
            f"[OK] Synthesized {profile['name']} via ElevenLabs "
            f"({voice_override or profile['elevenlabs_voice']}) -> {output_path}"
        )
        return "elevenlabs"

    await _synthesize_edge(text, profile, output_path)
    print(f"[OK] Synthesized {profile['name']} via Edge-TTS -> {output_path}")
    return "edge"


def main():
    parser = argparse.ArgumentParser(description="ThinkLate Dual-Anchor Voiceover Synthesizer")
    parser.add_argument(
        "--speaker", "-s", choices=["owl", "falcon"], default="owl", help="Speaker: 'owl' or 'falcon'"
    )
    parser.add_argument("--text", "-t", required=True, help="Dialogue text to synthesize")
    parser.add_argument("--out", "-o", required=True, help="Output WAV file path")
    parser.add_argument(
        "--engine",
        "-e",
        choices=["gemini", "elevenlabs", "edge"],
        default="gemini",
        help="TTS engine (default: gemini 3.8 flash tts)",
    )
    parser.add_argument("--voice", default=None, help="Voice name, voice_... ID, or ElevenLabs voice_id")
    parser.add_argument("--style", default=None, help="Gemini delivery style annotation override")
    parser.add_argument("--model", default=None, help="Model override (e.g., eleven_v3, gemini-3.8-flash-tts)")
    parser.add_argument(
        "--allow-edge-fallback",
        action="store_true",
        help="Explicitly permit falling back to Edge-TTS if primary API fails (disabled by default)",
    )

    args = parser.parse_args()
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    asyncio.run(
        synthesize_speech(
            args.text,
            args.speaker,
            args.out,
            engine=args.engine,
            voice_override=args.voice,
            style_override=args.style,
            model_override=args.model,
            allow_fallback=args.allow_edge_fallback,
        )
    )


if __name__ == "__main__":
    main()
