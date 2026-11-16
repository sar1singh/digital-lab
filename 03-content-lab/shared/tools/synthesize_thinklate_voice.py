"""
ThinkLate Dual-Anchor Voiceover Synthesizer
Primary Engine: Google Gemini 2.5 Flash Preview TTS (v1alpha, natural human prosody)
Fallback Engine: Microsoft Edge-TTS Neural (offline/quota fallback)

Characters:
- owl    -> Eddy Thinklate (Founder & Lead Host, Gemini voice: Charon)
- falcon -> Vera Vance (Forensic Investigator, Gemini voice: Kore)
"""

import argparse
import asyncio
import os
import subprocess
import sys
import wave

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

GEMINI_TTS_MODEL = "gemini-2.5-flash-preview-tts"
GEMINI_API_VERSION = "v1alpha"

VOICE_PROFILES = {
    "owl": {
        "name": "Eddy Thinklate (Founder & Lead Host)",
        "gemini_voice": "Charon",
        "gemini_style": (
            "Speak like a sharp, witty, grounded late-night documentary host explaining a sneaky "
            "real-world pattern to a smart friend — warm executive authority, natural human breathing, "
            "crisp emphasis, zero robotic cadence"
        ),
        "gemini_eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB:"
            "stop_periods=-1:stop_duration=0.35:stop_threshold=-45dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,areverse,"
            "equalizer=f=180:t=q:w=1.2:g=1.5,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
        "edge_voice": "en-US-ChristopherNeural",
        "rate": "+12%",
        "pitch": "-4Hz",
        "volume": "+0%",
        "edge_eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-42dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB,areverse,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.5,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
        "ref_audio": os.path.join(AUDIO_REF_DIR, "owl_executive_hook.wav"),
    },
    "falcon": {
        "name": "Vera Vance (Forensic Investigator)",
        "gemini_voice": "Kore",
        "gemini_style": (
            "Speak like a razor-sharp investigative journalist uncovering a hidden corporate paper trail "
            "— crisp, curious, conversational, articulate, natural human rhythm, zero robotic cadence"
        ),
        "gemini_eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB:"
            "stop_periods=-1:stop_duration=0.35:stop_threshold=-45dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,areverse,"
            "highpass=f=85,equalizer=f=2800:t=q:w=1.4:g=1.2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
        "edge_voice": "en-US-AvaNeural",
        "rate": "+15%",
        "pitch": "+0Hz",
        "volume": "+0%",
        "edge_eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.065:stop_threshold=-42dB,"
            "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB,areverse,"
            "highpass=f=100,lowpass=f=9500,equalizer=f=2800:t=q:w=1.4:g=2.0,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
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


def _synthesize_gemini(
    text: str,
    profile: dict,
    output_path: str,
    voice_override: str | None = None,
    style_override: str | None = None,
) -> None:
    _load_credentials()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not configured in environment or .agents/credentials/.env")

    from google import genai
    from google.genai import types

    voice_name = voice_override or profile["gemini_voice"]
    style = style_override or profile["gemini_style"]
    prompt = f"{style}:\n\n{text.strip()}"

    client = genai.Client(api_key=api_key, http_options={"api_version": GEMINI_API_VERSION})
    resp = client.models.generate_content(
        model=GEMINI_TTS_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice_name)
                )
            ),
        ),
    )

    audio_bytes = None
    mime_type = ""
    for cand in getattr(resp, "candidates", []) or []:
        content = getattr(cand, "content", None)
        for part in getattr(content, "parts", []) or []:
            inline = getattr(part, "inline_data", None)
            if inline and inline.data:
                audio_bytes = inline.data
                mime_type = inline.mime_type or ""
                break
        if audio_bytes:
            break

    if not audio_bytes:
        raise RuntimeError("Gemini TTS returned no audio payload.")

    temp_wav = output_path + ".gemini.tmp.wav"
    try:
        if mime_type == "audio/wav" or audio_bytes[:4] == b"RIFF":
            with open(temp_wav, "wb") as f:
                f.write(audio_bytes)
        else:
            with wave.open(temp_wav, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                wf.writeframes(audio_bytes)

        _run_ffmpeg_master(temp_wav, profile["gemini_eq_filter"], output_path)
    finally:
        if os.path.exists(temp_wav):
            os.remove(temp_wav)


async def _synthesize_edge(text: str, profile: dict, output_path: str) -> None:
    import edge_tts

    temp_mp3 = output_path + ".edge.tmp.mp3"
    try:
        communicate = edge_tts.Communicate(
            text,
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
    allow_fallback: bool = True,
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
            )
            print(
                f"[OK] Synthesized {profile['name']} via Gemini TTS "
                f"({voice_override or profile['gemini_voice']}) -> {output_path}"
            )
            return "gemini"
        except Exception as exc:
            if not allow_fallback:
                raise
            print(
                f"[WARN] Gemini TTS failed ({exc}); falling back to Edge-TTS...",
                file=sys.stderr,
            )

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
        "--engine", "-e", choices=["gemini", "edge"], default="gemini", help="TTS engine (default: gemini)"
    )
    parser.add_argument("--voice", default=None, help="Optional Gemini prebuilt voice override (e.g. Charon, Kore)")
    parser.add_argument("--style", default=None, help="Optional Gemini delivery style instruction override")
    parser.add_argument(
        "--no-fallback", action="store_true", help="Fail instead of falling back to Edge-TTS on Gemini error"
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
            allow_fallback=not args.no_fallback,
        )
    )


if __name__ == "__main__":
    main()
