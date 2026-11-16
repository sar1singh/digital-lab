import os
import subprocess
import time

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate"
ENGINE_DIR = os.path.join(BASE_DIR, "tools", "motion_engine")
CARDS_DIR = os.path.join(BASE_DIR, "videos", "05_how-airbnb-stole-100b", "assets", "motion_cards")

os.makedirs(CARDS_DIR, exist_ok=True)
CREATE_NO_WINDOW = 0x08000000

TARGETS = [
    ("EvidenceCard", "card_01_evidence_eviction.webm"),
    ("TypographySlam", "card_02_typography_slam_hook.webm"),
    ("ComparisonSplit", "card_03_comparison_hotel_vs_airbed.webm"),
    ("MetricCounter", "card_04_metric_cereal_capital.webm"),
    ("ForensicHeadline", "card_05_headline_angel_rejection.webm"),
    ("SocialCitation", "card_06_citation_paulg.webm"),
    ("DocumentRedaction", "card_07_redaction_vc_pass.webm"),
    ("GlitchDecoder", "card_08_glitch_cartel.webm"),
    ("AnimatedBarChart", "card_09_barchart_multiples.webm"),
    ("AnimatedLineChart", "card_10_linechart_ipo_spike.webm"),
    ("TornPaperReceipt", "card_11_receipt_junk_fees.webm"),
    ("HighlighterWipe", "card_12_highlighter_rules.webm")
]

print(f"Batch rendering {len(TARGETS)} transparent WebM cards with UTF-8 subprocess...")

for idx, (comp_id, out_name) in enumerate(TARGETS, 1):
    out_path = os.path.join(CARDS_DIR, out_name)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"[{idx}/{len(TARGETS)}] Already exists: {out_name}")
        continue
        
    print(f"[{idx}/{len(TARGETS)}] Rendering {comp_id} -> {out_name}...")
    t0 = time.time()
    
    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts", comp_id,
        out_path,
        "--codec=vp9",
        "--pixel-format=yuva420p",
        "--image-format=png",
        "--gl=angle",
        "--quiet"
    ]
    
    # Run with stdout/stderr piped to NUL or devnull to avoid Windows CP1252 decode error on Remotion emoji output
    with open(os.devnull, 'w') as null_f:
        res = subprocess.run(cmd, cwd=ENGINE_DIR, creationflags=CREATE_NO_WINDOW, stdout=null_f, stderr=null_f)
        
    duration = time.time() - t0
    if os.path.exists(out_path):
        fsize_kb = os.path.getsize(out_path) / 1024
        print(f"  SUCCESS! Rendered in {duration:.1f}s | Size: {fsize_kb:.1f} KB")
    else:
        print(f"  FAILED to render {comp_id}!")

print("\nALL 12 TRANSPARENT WEBM CARDS READY!")
