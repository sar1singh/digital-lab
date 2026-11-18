"""Transcribe S06_eddy_custom_voice_master.wav with word-level timestamps using cached faster-whisper."""
import json
from pathlib import Path
from faster_whisper import WhisperModel

AUDIO = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\shortForm\S06_30-percent-ai-rehire-trap\assets\audio\S06_eddy_custom_voice_master.wav")
OUT = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\shortForm\S06_30-percent-ai-rehire-trap\hf_pilot_demo\s06_timestamps.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(str(AUDIO), word_timestamps=True)
data = {"duration": info.duration, "segments": []}
for seg in segments:
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for w in (seg.words or [])]
    data["segments"].append({"s": round(seg.start, 3), "e": round(seg.end, 3), "text": seg.text.strip(), "words": words})
    print(f"[{seg.start:5.2f} -> {seg.end:5.2f}] {seg.text.strip()}")

OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("SAVED:", OUT)
