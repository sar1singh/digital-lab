import os
import sys
import time
import shutil
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(".")
MOTION_ENGINE = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "motion_engine")
L06_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "thinklate", "videos", "longForm", "L06_the-memory-lie")
SHORTS_OUT_DIR = os.path.join(L06_DIR, "shorts")
S02_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "thinklate", "videos", "shortForm", "S02_the-eyewitness-lie")

os.makedirs(SHORTS_OUT_DIR, exist_ok=True)
os.makedirs(S02_DIR, exist_ok=True)

RAW_MP4 = os.path.join(SHORTS_OUT_DIR, "MemoryLieShort_raw.mp4")
AUDIO_MIX = os.path.join(L06_DIR, "assets", "audio", "short01_mix.wav")
FINAL_MASTER_MP4 = os.path.join(SHORTS_OUT_DIR, "ThinkLate_Short01_The_Eyewitness_Lie_1080x1920_MASTER.mp4")

print("=" * 70)
print("🎬 RENDERING THINKLATE L06 VERTICAL SHORT (1,122 FRAMES @ 30 FPS)")
print("=" * 70)

remotion_cmd = [
    "npx.cmd", "remotion", "render",
    "src/index.ts", "MemoryLieShort",
    RAW_MP4,
    "--gl=angle",
    "--concurrency=4"
]

t0 = time.time()
proc = subprocess.Popen(
    remotion_cmd,
    cwd=MOTION_ENGINE,
    creationflags=0x08000000,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    errors="replace",
    bufsize=1
)

for line in iter(proc.stdout.readline, ""):
    line_clean = line.strip()
    if any(k in line_clean for k in ["Bundling", "Rendered", "Error", "error", "Done"]):
        print(line_clean, flush=True)

proc.stdout.close()
proc.wait()
elapsed = time.time() - t0
print(f"\n[+] Remotion video render finished in {elapsed:.1f}s (code: {proc.returncode})")

if proc.returncode != 0 or not os.path.exists(RAW_MP4):
    print("[-] Remotion render failed!")
    sys.exit(1)

print(f"[*] Muxing video with broadcast master audio ({AUDIO_MIX})...")
mux_cmd = [
    "ffmpeg", "-y",
    "-i", RAW_MP4,
    "-i", AUDIO_MIX,
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-t", "37.41",
    FINAL_MASTER_MP4
]
mux_res = subprocess.run(mux_cmd, creationflags=0x08000000, capture_output=True, text=True)
if mux_res.returncode != 0:
    print("[-] FFmpeg Mux Error:", mux_res.stderr)
    sys.exit(1)

# Copy to S02 shortForm directory
s02_target = os.path.join(S02_DIR, "ThinkLate_Short02_The_Eyewitness_Lie_1080x1920_MASTER.mp4")
shutil.copy2(FINAL_MASTER_MP4, s02_target)

# Copy to artifact directory so user can open/preview directly!
artifact_dir = r"C:\Users\sar1s\.gemini\antigravity\brain\d8895c41-3403-4f18-9410-6e0368cec188"
artifact_copy = os.path.join(artifact_dir, "ThinkLate_Short01_The_Eyewitness_Lie_1080x1920_MASTER.mp4")
shutil.copy2(FINAL_MASTER_MP4, artifact_copy)

size_mb = os.path.getsize(FINAL_MASTER_MP4) / (1024 * 1024)
print("=" * 70)
print(f"✅ SHORT MASTER RENDER COMPLETE: {size_mb:.2f} MB")
print(f"   Master File: {FINAL_MASTER_MP4}")
print(f"   ShortForm Registry: {s02_target}")
print(f"   Artifact Copy: {artifact_copy}")
print("=" * 70)
