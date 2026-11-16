import os
import subprocess
import time

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate"
ENGINE_DIR = os.path.join(BASE_DIR, "tools", "motion_engine")
CARDS_DIR = os.path.join(BASE_DIR, "videos", "05_how-airbnb-stole-100b", "assets", "motion_cards")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

os.makedirs(CARDS_DIR, exist_ok=True)
CREATE_NO_WINDOW = 0x08000000

# Composition targets: (Composition ID, Output Filename, Description)
TARGETS = [
    ("EvidenceCard", "card_01_evidence_eviction.mp4", "Act 1: Eviction Notice Glass Card"),
    ("TypographySlam", "card_02_typography_slam_hook.mp4", "Act 1: Kinetic Typography Slam"),
    ("ComparisonSplit", "card_03_comparison_hotel_vs_airbed.mp4", "Act 2: Hotel Cartel vs Airbed Arbitrage"),
    ("MetricCounter", "card_04_metric_cereal_capital.mp4", "Act 3: Cereal Box Bootstrap Counter ($30k)"),
    ("ForensicHeadline", "card_05_headline_angel_rejection.mp4", "Act 4: WSJ Angel Rejection Headline"),
    ("SocialCitation", "card_06_citation_paulg.mp4", "Act 4: Paul Graham Verified Citation"),
    ("DocumentRedaction", "card_07_redaction_vc_pass.mp4", "Act 5: Classified Redacted VC Exhibit"),
    ("GlitchDecoder", "card_08_glitch_cartel.mp4", "Act 5: Glitch Decrypted Matrix Reveal"),
    ("AnimatedBarChart", "card_09_barchart_multiples.mp4", "Act 6: Animated Valuation Multiples Bar Chart"),
    ("AnimatedLineChart", "card_10_linechart_ipo_spike.mp4", "Act 6: $100B IPO Spike Trajectory Curve"),
    ("TornPaperReceipt", "card_11_receipt_junk_fees.mp4", "Act 7: Torn Paper Receipt (141% Fee Markup)"),
    ("HighlighterWipe", "card_12_highlighter_rules.mp4", "Act 8: Neon Highlighter Statement Wipe")
]

print(f"Starting batch render of {len(TARGETS)} Remotion broadcast motion cards...")

for idx, (comp_id, out_name, desc) in enumerate(TARGETS, 1):
    out_path = os.path.join(CARDS_DIR, out_name)
    print(f"[{idx}/{len(TARGETS)}] Rendering {comp_id} -> {out_name} ({desc})...")
    t0 = time.time()
    
    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts", comp_id,
        out_path,
        "--gl=angle"
    ]
    
    res = subprocess.run(cmd, cwd=ENGINE_DIR, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  FAILED to render {comp_id}!")
        print(res.stderr[-500:])
        continue
        
    duration = time.time() - t0
    fsize_kb = os.path.getsize(out_path) / 1024
    print(f"  SUCCESS! Rendered in {duration:.1f}s | Size: {fsize_kb:.1f} KB")
    
    # Extract preview JPG at 2.0s for artifact review
    thumb_name = out_name.replace(".mp4", ".jpg")
    thumb_path = os.path.join(ARTIFACT_DIR, thumb_name)
    subprocess.run([
        "ffmpeg", "-y", "-ss", "2.0", "-i", out_path,
        "-vframes", "1", "-q:v", "2", thumb_path
    ], creationflags=CREATE_NO_WINDOW, capture_output=True)

print("\nALL MOTION CARDS RENDERED SUCCESSFULLY!")

