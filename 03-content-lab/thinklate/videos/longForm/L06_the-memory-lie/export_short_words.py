import json
import os

TS_PATH = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/longForm/L06_the-memory-lie/transcription_timestamps.json")
OUT_TS = os.path.abspath("digital-lab/03-content-lab/shared/motion_engine/src/compositions/shorts/memory_lie_words.ts")

with open(TS_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

words = []
for s in data["segments"]:
    if s["end"] <= 38.0:
        for w in s.get("words", []):
            words.append({
                "word": w["word"].strip(),
                "start": round(w["start"], 2),
                "end": round(w["end"], 2)
            })

ts_content = """export interface WordToken {
  word: string;
  start: number;
  end: number;
}

export const MEMORY_LIE_WORDS: WordToken[] = """ + json.dumps(words, indent=2) + ";\n"

with open(OUT_TS, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"[+] Exported {len(words)} word tokens to: {OUT_TS}")
