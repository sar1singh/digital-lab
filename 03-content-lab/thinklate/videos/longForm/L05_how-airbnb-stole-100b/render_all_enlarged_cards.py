import os
import subprocess
import time

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate"
ENGINE_DIR = os.path.join(BASE_DIR, "tools", "motion_engine")
CARDS_DIR = os.path.join(BASE_DIR, "videos", "05_how-airbnb-stole-100b", "assets", "motion_cards")
os.makedirs(CARDS_DIR, exist_ok=True)
CREATE_NO_WINDOW = 0x08000000

TARGETS = [
    ("EvidenceCard", "card_01_evidence_eviction.mov"),
    ("TypographySlam", "card_02_typography_slam_hook.mov"),
    ("ComparisonSplit", "card_03_comparison_hotel_vs_airbed.mov"),
    ("MetricCounter", "card_04_metric_cereal_capital.mov"),
    ("ForensicHeadline", "card_05_headline_angel_rejection.mov"),
    ("SocialCitation", "card_06_citation_paulg.mov"),
    ("DocumentRedaction", "card_07_redaction_vc_pass.mov"),
    ("GlitchDecoder", "card_08_glitch_cartel.mov"),
    ("AnimatedBarChart", "card_09_barchart_multiples.mov"),
    ("AnimatedLineChart", "card_10_linechart_ipo_spike.mov"),
    ("TornPaperReceipt", "card_11_receipt_junk_fees.mov"),
    ("HighlighterWipe", "card_12_highlighter_rules.mov")
]

print(f"Batch re-rendering {len(TARGETS)} enlarged ProRes 4444 transparent cards...", flush=True)

for idx, (comp_id, out_name) in enumerate(TARGETS, 1):
    out_path = os.path.join(CARDS_DIR, out_name)
    print(f"[{idx}/{len(TARGETS)}] Rendering {comp_id} -> {out_name}...", flush=True)
    t0 = time.time()
    
    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts", comp_id,
        out_path,
        "--codec=prores",
        "--prores-profile=4444",
        "--pixel-format=yuva444p10le",
        "--image-format=png",
        "--gl=angle",
        "--quiet"
    ]
    
    with open(os.devnull, 'w') as null_f:
        res = subprocess.run(cmd, cwd=ENGINE_DIR, creationflags=CREATE_NO_WINDOW, stdout=null_f, stderr=null_f)
        
    dur = time.time() - t0
    if os.path.exists(out_path):
        size_mb = os.path.getsize(out_path) / (1024 * 1024)
        print(f"  SUCCESS in {dur:.1f}s | Size: {size_mb:.2f} MB", flush=True)
    else:
        print(f"  FAILED: {comp_id}", flush=True)

print("\nALL 12 ENLARGED PRORES 4444 CARDS RENDERED!", flush=True)
