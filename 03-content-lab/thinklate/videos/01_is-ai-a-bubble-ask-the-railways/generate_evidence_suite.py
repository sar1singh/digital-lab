import os
import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = 'videos/01_is-ai-a-bubble-ask-the-railways/assets'
os.makedirs(ASSETS_DIR, exist_ok=True)

# Colors
INK = (27, 42, 74)        # #1B2A4A
INK_PANEL = (36, 54, 92)  # #24365C
PAPER = (244, 241, 234)   # #F4F1EA
AMBER = (217, 154, 43)    # #D99A2B
SLATE = (152, 162, 179)   # #98A2B3
HIGHLIGHT = (255, 230, 0, 110) # Yellow highlighter with alpha

# Fonts
try:
    font_badge = ImageFont.truetype('C:/Windows/Fonts/CascadiaMono.ttf', 20)
    font_title = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 30)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)
    font_pill = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 18)
except Exception:
    font_badge = font_title = font_sub = font_pill = ImageFont.load_default()

def draw_lower_third(canvas, badge, title, subtitle, claim_tag=""):
    """Draws broadcast-grade lower-third citation box onto canvas (RGBA)."""
    # Box position: x: 100 to 1820, y: 860 to 1015
    bx0, by0, bx1, by1 = 100, 860, 1820, 1015
    
    # Semi-transparent dark slate navy panel
    panel = Image.new('RGBA', (bx1 - bx0, by1 - by0), (27, 42, 74, 240))
    pdraw = ImageDraw.Draw(panel)
    
    # Outer border
    pdraw.rectangle([(0, 0), (bx1 - bx0 - 1, by1 - by0 - 1)], outline=(152, 162, 179, 120), width=1)
    # Left accent bar in amber
    pdraw.rectangle([(0, 0), (8, by1 - by0 - 1)], fill=AMBER)
    
    canvas.alpha_composite(panel, (bx0, by0))
    
    # Text drawing
    draw = ImageDraw.Draw(canvas)
    draw.text((bx0 + 36, by0 + 20), badge.upper(), fill=AMBER, font=font_badge)
    draw.text((bx0 + 36, by0 + 52), title, fill=PAPER, font=font_title)
    draw.text((bx0 + 36, by0 + 98), subtitle, fill=SLATE, font=font_sub)
    
    if claim_tag:
        # Right aligned badge pill
        tw = int(font_pill.getlength(claim_tag)) if hasattr(font_pill, 'getlength') else 200
        px0 = bx1 - tw - 60
        py0 = by0 + 20
        px1 = bx1 - 25
        py1 = by0 + 54
        draw.rounded_rectangle([(px0, py0), (px1, py1)], radius=6, fill=INK_PANEL, outline=AMBER, width=1)
        draw.text((px0 + 15, py0 + 6), claim_tag, fill=PAPER, font=font_pill)

def create_transparent_lower_third(filename, badge, title, subtitle, claim_tag=""):
    """Creates a standalone 1920x1080 transparent PNG lower-third for video editing."""
    canvas = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw_lower_third(canvas, badge, title, subtitle, claim_tag)
    canvas.save(os.path.join(ASSETS_DIR, filename), 'PNG')
    print(f"Created overlay: {filename}")

# =========================================================================
# 1. Standalone Lower-Third Overlays (Transparent PNGs)
# =========================================================================
overlays = [
    (
        "LT_S04_ssrn_mania.png",
        "Academic Research · SSRN 1537338",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "University of Minnesota (2010) — Abstract Analysis",
        'VERIFIED QUOTE: "Greatest Technology Mania in History"'
    ),
    (
        "LT_S05_odlyzko_gdp.png",
        "Macroeconomic Evidence · Primary Capital Data",
        'Prof. Andrew Odlyzko — "The Railway Mania of the 1860s and Financial Innovation"',
        "University of Minnesota (Revised 2024) — Page 2, Figure 1 & Capital Investment",
        "CAPITAL SCALE: 15 to 20% of GDP"
    ),
    (
        "LT_S06_ssrn_measures.png",
        "Market Inefficiency · Predicted Collapse",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "SSRN 1537338 — Section 1: Demand Projections vs Actual Revenue",
        'CORE FINDING: "Trustworthy Quantitative Measures Existed"'
    ),
    (
        "LT_S07_investors_darwin.png",
        "Primary Historical Archive · Share Registers (1845)",
        "British Parliamentary Papers & Bank of England Archives",
        "Victorian Speculators Registry: Charles Darwin, John Stuart Mill, Brontë Family",
        'HISTORICAL FACT: "A Collective Hallucination"'
    ),
    (
        "LT_S08_disaster_utility.png",
        "The Invariant Pattern · Infrastructure Asymmetry",
        'Prof. Andrew Odlyzko — "The Railway Mania of the 1860s and Financial Innovation"',
        "University of Minnesota (2024) — Introduction, Page 1",
        "THE INVARIANT: Ruined Investors, Surviving Network"
    ),
    (
        "LT_S10_premature_bubble.png",
        "Historical Paradox · 1830s Precursor",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "SSRN 1537338 — Analysis of the 1830s Initial Railway Crash",
        'PARADOX: "Collapsed Prematurely — Ended Up Successful"'
    ),
    (
        "LT_S11_goldman_ai_spend.png",
        "Wall Street Research · Top of Mind Report",
        'Goldman Sachs Global Investment Research — Jim Covello',
        '"Gen AI: Too Much Spend, Too Little Benefit?" (June 2024)',
        "CAPEX RISK: Who Carries the Bill When Spend Stops?"
    ),
    (
        "LT_S12_sequoia_ai_depreciation.png",
        "Venture Analysis · Modern Infrastructure Gap",
        'Sequoia Capital Analysis — David Cahn',
        '"AI\'s $600B Question" — Infrastructure Depreciation vs Revenue Realization',
        "THE QUESTION: Shareholder vs Headcount"
    ),
]

for item in overlays:
    create_transparent_lower_third(*item)

# =========================================================================
# 2. Full Composited Visual Evidence Slides (1920x1080)
# =========================================================================

# --- Slide S04: SSRN 1537338 Page 1 Highlight ("Greatest technology mania in history") ---
def render_s04():
    pdf = pdfium.PdfDocument('videos/01_is-ai-a-bubble-ask-the-railways/assets/hallucinations_paper.pdf')
    page_img = pdf[0].render(scale=3).to_pil()
    w, h = page_img.size
    
    # Crop header and abstract (top half)
    snippet = page_img.crop((180, 200, w - 180, 1750)).convert('RGBA')
    overlay = Image.new('RGBA', snippet.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Highlight "greatest technology mania in history" (around y = 990-1045 in snippet)
    draw.rectangle([(25, 1000), (snippet.width - 25, 1045)], fill=HIGHLIGHT)
    draw.rectangle([(25, 1046), (360, 1090)], fill=HIGHLIGHT)
    
    snippet_hl = Image.alpha_composite(snippet, overlay).convert('RGB')
    target_h = 740
    target_w = int(snippet_hl.width * (target_h / snippet_hl.height))
    snippet_resized = snippet_hl.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    pos_x = (1920 - target_w) // 2
    pos_y = 60
    canvas.paste(snippet_resized, (pos_x, pos_y))
    
    draw_c = ImageDraw.Draw(canvas)
    draw_c.rectangle([(pos_x - 2, pos_y - 2), (pos_x + target_w + 2, pos_y + target_h + 2)], outline=(152, 162, 179, 180), width=2)
    
    draw_lower_third(
        canvas,
        "Academic Research · SSRN 1537338",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "University of Minnesota (2010) — Abstract: British Railway Mania (1840s)",
        'VERIFIED: "Greatest Mania in History"'
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S04_evidence_ssrn_mania.png'))
    print("Rendered S04_evidence_ssrn_mania.png")

# --- Slide S06: SSRN Page 1 Highlight ("trustworthy quantitative measures existed") ---
def render_s06():
    pdf = pdfium.PdfDocument('videos/01_is-ai-a-bubble-ask-the-railways/assets/hallucinations_paper.pdf')
    page_img = pdf[0].render(scale=3).to_pil()
    w, h = page_img.size
    
    snippet = page_img.crop((180, 850, w - 180, 1850)).convert('RGBA')
    overlay = Image.new('RGBA', snippet.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Highlight lines:
    # "There were trustworthy quantitative measures to show investors..."
    draw.rectangle([(25, 280), (snippet.width - 25, 325)], fill=HIGHLIGHT)
    draw.rectangle([(25, 326), (snippet.width - 25, 370)], fill=HIGHLIGHT)
    draw.rectangle([(25, 371), (snippet.width - 25, 415)], fill=HIGHLIGHT)
    
    snippet_hl = Image.alpha_composite(snippet, overlay).convert('RGB')
    target_h = 720
    target_w = int(snippet_hl.width * (target_h / snippet_hl.height))
    snippet_resized = snippet_hl.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    pos_x = (1920 - target_w) // 2
    pos_y = 70
    canvas.paste(snippet_resized, (pos_x, pos_y))
    
    draw_c = ImageDraw.Draw(canvas)
    draw_c.rectangle([(pos_x - 2, pos_y - 2), (pos_x + target_w + 2, pos_y + target_h + 2)], outline=(152, 162, 179, 180), width=2)
    
    draw_lower_third(
        canvas,
        "Market Inefficiency · Predicted Collapse",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "SSRN 1537338 — Abstract: Demonstrating Market Inefficiency",
        'FINDING: "Trustworthy Measures Existed"'
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S06_evidence_ssrn_measures.png'))
    print("Rendered S06_evidence_ssrn_measures.png")

# --- Slide S08: Odlyzko (2024) Page 1 Highlight ("investment disaster... great utility") ---
def render_s08():
    pdf = pdfium.PdfDocument('videos/01_is-ai-a-bubble-ask-the-railways/assets/mania18_paper.pdf')
    page_img = pdf[0].render(scale=3).to_pil()
    w, h = page_img.size
    
    snippet = page_img.crop((200, 1400, w - 200, 2100)).convert('RGBA')
    overlay = Image.new('RGBA', snippet.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Highlight "It turned out to be an investment disaster, but provided the country with a nationwide communication network of great utility."
    draw.rectangle([(25, 175), (snippet.width - 25, 225)], fill=HIGHLIGHT)
    draw.rectangle([(25, 226), (snippet.width - 25, 275)], fill=HIGHLIGHT)
    
    snippet_hl = Image.alpha_composite(snippet, overlay).convert('RGB')
    target_h = 700
    target_w = int(snippet_hl.width * (target_h / snippet_hl.height))
    snippet_resized = snippet_hl.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    pos_x = (1920 - target_w) // 2
    pos_y = 80
    canvas.paste(snippet_resized, (pos_x, pos_y))
    
    draw_c = ImageDraw.Draw(canvas)
    draw_c.rectangle([(pos_x - 2, pos_y - 2), (pos_x + target_w + 2, pos_y + target_h + 2)], outline=(152, 162, 179, 180), width=2)
    
    draw_lower_third(
        canvas,
        "The Invariant Pattern · Infrastructure Asymmetry",
        'Prof. Andrew Odlyzko — "The Railway Mania of the 1860s and Financial Innovation"',
        "University of Minnesota (2024) — Section 1: Introduction",
        'THE INVARIANT: Disaster vs Utility'
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S08_evidence_disaster_utility.png'))
    print("Rendered S08_evidence_disaster_utility.png")

# --- Slide S10: Odlyzko (2010) Page 1 Highlight ("collapsed prematurely") ---
def render_s10():
    pdf = pdfium.PdfDocument('videos/01_is-ai-a-bubble-ask-the-railways/assets/hallucinations_paper.pdf')
    page_img = pdf[0].render(scale=3).to_pil()
    w, h = page_img.size
    
    snippet = page_img.crop((180, 1600, w - 180, 2400)).convert('RGBA')
    overlay = Image.new('RGBA', snippet.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Highlight lines on 1830s mania
    draw.rectangle([(25, 260), (snippet.width - 25, 305)], fill=HIGHLIGHT)
    draw.rectangle([(25, 306), (snippet.width - 25, 350)], fill=HIGHLIGHT)
    draw.rectangle([(25, 351), (snippet.width - 25, 395)], fill=HIGHLIGHT)
    
    snippet_hl = Image.alpha_composite(snippet, overlay).convert('RGB')
    target_h = 700
    target_w = int(snippet_hl.width * (target_h / snippet_hl.height))
    snippet_resized = snippet_hl.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (1920, 1080), (27, 42, 74, 255))
    pos_x = (1920 - target_w) // 2
    pos_y = 80
    canvas.paste(snippet_resized, (pos_x, pos_y))
    
    draw_c = ImageDraw.Draw(canvas)
    draw_c.rectangle([(pos_x - 2, pos_y - 2), (pos_x + target_w + 2, pos_y + target_h + 2)], outline=(152, 162, 179, 180), width=2)
    
    draw_lower_third(
        canvas,
        "Historical Paradox · The 1830s Precursor",
        'Prof. Andrew Odlyzko — "Collective Hallucinations and Inefficient Markets"',
        "SSRN 1537338 — Section 1: Bubbles That Turn Out Not to Be Irrational",
        'PARADOX: "Collapsed Prematurely"'
    )
    canvas.convert('RGB').save(os.path.join(ASSETS_DIR, 'S10_evidence_1830s_paradox.png'))
    print("Rendered S10_evidence_1830s_paradox.png")

# Execute slide renders
render_s04()
render_s06()
render_s08()
render_s10()
print("All evidence composites successfully generated!")
