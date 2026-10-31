import whisper

files = [
    r'C:/Users/sar1s/.gemini/antigravity/brain/fa6cc279-b4cc-4a52-9629-aff42dfd0eb7/.user_uploaded/uploaded_media_0_1793376381096.mp3',
    r'C:/Users/sar1s/.gemini/antigravity/brain/fa6cc279-b4cc-4a52-9629-aff42dfd0eb7/.user_uploaded/uploaded_media_1_1793376381096.mp3',
    r'C:/Users/sar1s/.gemini/antigravity/brain/fa6cc279-b4cc-4a52-9629-aff42dfd0eb7/.user_uploaded/uploaded_media_2_1793376381096.mp3'
]

print("Loading Whisper model (tiny.en or base.en)...")
model = whisper.load_model("base.en")

for i, f in enumerate(files):
    print(f"\n--- Transcribing File {i} ---")
    result = model.transcribe(f, fp16=False)
    text = result['text'].strip()
    segments = result['segments']
    print(f"Total segments: {len(segments)}")
    if segments:
        print("Start:", segments[0]['text'])
        print("End:", segments[-1]['text'])
    print("Full text preview (first 120 chars):", text[:120])
    print("Full text preview (last 120 chars):", text[-120:])

