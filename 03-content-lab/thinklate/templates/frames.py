#!/usr/bin/env python3
"""
ThinkLate frame generator.

Produces editable SVG frames for every reusable frame type in the asset pipeline.
SVG because: text stays editable in Affinity, fonts resolve on your machine,
and Resolve/Fusion imports it cleanly.

Usage
-----
    python3 frames.py                      # render the sample set into preview/
    python3 frames.py --demo               # same, explicit

    # or import and call directly:
    from frames import title_card, chapter_card, kicker, quote_card
    title_card("Is AI a Bubble?", "Ask the Railways", out="frames/v01_title.svg")

Every function writes an SVG and returns its path.
"""

import argparse
import html
import os
import textwrap

from brand import (
    INK, PAPER, AMBER, SLATE, BRICK, INK_SOFT, PAPER_DIM, GRID,
    SERIF, SANS, MONO, W, H, TW, TH, MARGIN, SIZE, CHANNEL, TAGLINE, HANDLE,
)

HERE = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------- helpers
def _esc(s):
    return html.escape(str(s), quote=True)


def _write(svg, out):
    path = out if os.path.isabs(out) else os.path.join(HERE, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    return path


def _open(w=W, h=H, bg=INK):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">\n'
        f'  <rect width="{w}" height="{h}" fill="{bg}"/>\n'
    )


def _text(x, y, s, size=SIZE["body"], fill=PAPER, family=SANS,
          weight="400", anchor="start", spacing="0", opacity="1"):
    return (
        f'  <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
        f'letter-spacing="{spacing}" opacity="{opacity}">{_esc(s)}</text>\n'
    )


def _wrapped(x, y, s, width_chars, size, line_height, **kw):
    """Manual wrap — SVG has no auto-wrap."""
    out = ""
    for i, line in enumerate(textwrap.wrap(str(s), width_chars)):
        out += _text(x, y + i * line_height, line, size=size, **kw)
    return out


def _rule(x, y, w, color=AMBER, h=6):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>\n'


def _source_strip(text, w=W, h=H):
    """Bottom-left citation. Present on every frame carrying a figure."""
    return _text(MARGIN, h - 56, text, size=SIZE["caption"],
                 fill=PAPER_DIM, family=MONO)


def _wordmark(w=W, h=H, muted=True):
    return _text(w - MARGIN, h - 56, CHANNEL, size=SIZE["caption"],
                 fill=PAPER_DIM if muted else PAPER, family=SERIF,
                 anchor="end", spacing="1.5")


GRAIN = False  # SVG feTurbulence renders inconsistently across Resolve /
               # Affinity / ImageMagick. Add grain as an adjustment layer in
               # Resolve instead — one setting, applied to the whole timeline.


def _grain(w=W, h=H, opacity=0.05):
    """Optional archival texture. Off by default — see GRAIN above."""
    if not GRAIN:
        return ""
    return (
        f'  <defs><filter id="grain"><feTurbulence type="fractalNoise" '
        f'baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"/>'
        f'<feColorMatrix type="saturate" values="0"/></filter></defs>\n'
        f'  <rect width="{w}" height="{h}" filter="url(#grain)" '
        f'opacity="{opacity}"/>\n'
    )


# ----------------------------------------------------------------- 1. title card
def title_card(line1, line2="", out="preview/01_title.svg"):
    s = _open() + _grain()
    s += _rule(MARGIN, 300, 180)
    s += _text(MARGIN, 480, line1, size=SIZE["hero"], family=SERIF, fill=PAPER)
    if line2:
        s += _text(MARGIN, 620, line2, size=SIZE["hero"], family=SERIF, fill=AMBER)
    s += _text(MARGIN, 760, TAGLINE, size=SIZE["body"], fill=PAPER_DIM,
               family=SANS, spacing="1")
    s += _wordmark()
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 2. chapter card
def chapter_card(number, title, out="preview/02_chapter.svg"):
    s = _open() + _grain()
    s += _text(MARGIN, 470, f"{int(number):02d}", size=SIZE["hero"],
               family=MONO, fill=AMBER)
    s += _rule(MARGIN, 520, 900, color=GRID, h=2)
    s += _wrapped(MARGIN, 650, title, 34, SIZE["h1"], 112,
                  family=SERIF, fill=PAPER)
    s += _wordmark()
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 3. kicker
def kicker(number, label, sub="", out="preview/03_kicker.svg"):
    """The one number that is the story. 3-6 seconds, full screen."""
    s = _open() + _grain()
    s += _text(W // 2, 560, number, size=SIZE["kicker"], family=SERIF,
               fill=AMBER, anchor="middle")
    s += _text(W // 2, 680, label, size=48, family=SANS,
               fill=PAPER, anchor="middle", spacing="4")
    if sub:
        s += _text(W // 2, 760, sub, size=SIZE["body"], family=SANS,
                   fill=PAPER_DIM, anchor="middle")
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 4. quote card
def quote_card(quote, speaker, date_or_role, source="", out="preview/04_quote.svg"):
    s = _open() + _grain()
    s += _text(MARGIN, 330, "“", size=200, family=SERIF, fill=AMBER,
               opacity="0.35")
    s += _wrapped(MARGIN, 440, quote, 46, SIZE["quote"], 86,
                  family=SERIF, fill=PAPER)
    s += _rule(MARGIN, 800, 90)
    s += _text(MARGIN, 880, speaker, size=SIZE["body"], family=SANS,
               fill=PAPER, weight="600")
    s += _text(MARGIN, 928, date_or_role, size=SIZE["caption"],
               family=MONO, fill=PAPER_DIM)
    if source:
        s += _source_strip(source)
    s += _wordmark()
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 5. timeline
def timeline(events, title="", source="", out="preview/05_timeline.svg"):
    """events: [(year, label), ...] — 3 to 6 items."""
    s = _open() + _grain()
    if title:
        s += _text(MARGIN, 200, title, size=SIZE["h2"], family=SERIF, fill=PAPER)
    y = 560
    x0, x1 = MARGIN, W - MARGIN
    s += f'  <rect x="{x0}" y="{y}" width="{x1 - x0}" height="3" fill="{GRID}"/>\n'
    n = max(len(events), 2)
    step = (x1 - x0) / (n - 1)
    for i, (year, label) in enumerate(events):
        x = x0 + i * step
        s += f'  <circle cx="{x:.0f}" cy="{y + 1}" r="14" fill="{AMBER}"/>\n'
        s += _text(x, y - 60, year, size=SIZE["h2"], family=MONO,
                   fill=AMBER, anchor="middle")
        for j, line in enumerate(textwrap.wrap(str(label), 18)):
            s += _text(x, y + 90 + j * 44, line, size=SIZE["label"],
                       family=SANS, fill=PAPER, anchor="middle")
    if source:
        s += _source_strip(source)
    s += _wordmark()
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 6. comparison table
def table(headers, rows, title="", source="", highlight_col=None,
          out="preview/06_table.svg"):
    s = _open() + _grain()
    if title:
        s += _text(MARGIN, 190, title, size=SIZE["h2"], family=SERIF, fill=PAPER)
    ncol = len(headers)
    x0 = MARGIN
    colw = (W - 2 * MARGIN - 80) / ncol
    y = 300
    for c, head in enumerate(headers):
        s += _text(x0 + c * colw, y, head, size=28, family=SANS,
                   fill=PAPER_DIM, weight="600", spacing="0")
    s += _rule(x0, y + 28, W - 2 * MARGIN, color=GRID, h=2)
    for r, row in enumerate(rows):
        ry = y + 110 + r * 92
        if r % 2 == 0:
            s += (f'  <rect x="{x0 - 30}" y="{ry - 58}" '
                  f'width="{W - 2 * MARGIN + 60}" height="84" '
                  f'fill="{INK_SOFT}"/>\n')
        for c, cell in enumerate(row):
            fill = AMBER if highlight_col == c else PAPER
            fam = MONO if c > 0 else SANS
            s += _text(x0 + c * colw, ry, cell, size=SIZE["body"],
                       family=fam, fill=fill)
    if source:
        s += _source_strip(source)
    s += _wordmark()
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 7. lower third
def lower_third(primary, secondary="", out="preview/07_lowerthird.svg"):
    """Transparent background — overlay in Resolve."""
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">\n')
    s += f'  <rect x="0" y="{H - 300}" width="1100" height="180" fill="{INK}" opacity="0.92"/>\n'
    s += _rule(0, H - 300, 10, h=180)
    s += _text(60, H - 210, primary, size=SIZE["body"], family=SANS,
               fill=PAPER, weight="600")
    if secondary:
        s += _text(60, H - 158, secondary, size=SIZE["caption"],
                   family=MONO, fill=PAPER_DIM)
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 8. source strip
def source_overlay(text, out="preview/08_source.svg"):
    """Transparent citation overlay. Sits on charts and archival images."""
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">\n')
    s += f'  <rect x="0" y="{H - 92}" width="{W}" height="92" fill="{INK}" opacity="0.78"/>\n'
    s += _text(MARGIN, H - 36, text, size=SIZE["caption"], family=MONO, fill=PAPER)
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 9. end card
def end_card(next_title, out="preview/09_endcard.svg"):
    s = _open() + _grain()
    s += _text(MARGIN, 260, CHANNEL, size=SIZE["h1"], family=SERIF,
               fill=PAPER, spacing="1")
    s += _text(MARGIN, 330, TAGLINE, size=SIZE["body"], family=SANS,
               fill=PAPER_DIM, spacing="1")
    s += _rule(MARGIN, 400, 180)
    s += _text(MARGIN, 520, "NEXT", size=SIZE["caption"], family=MONO,
               fill=AMBER, spacing="4")
    s += _wrapped(MARGIN, 600, next_title, 30, SIZE["h2"], 80,
                  family=SERIF, fill=PAPER)
    s += _text(MARGIN, 880, "Newsletter + sources in the description",
               size=SIZE["body"], family=SANS, fill=PAPER_DIM)
    s += _text(MARGIN, 940, HANDLE, size=SIZE["body"], family=MONO, fill=AMBER)
    # reserved zones for YouTube end-screen elements
    s += (f'  <rect x="1180" y="300" width="560" height="315" fill="none" '
          f'stroke="{GRID}" stroke-width="2" stroke-dasharray="12 10"/>\n')
    s += _text(1460, 470, "end-screen element", size=SIZE["caption"],
               family=MONO, fill=SLATE, anchor="middle")
    s += (f'  <rect x="1180" y="660" width="270" height="270" fill="none" '
          f'stroke="{GRID}" stroke-width="2" stroke-dasharray="12 10"/>\n')
    s += _text(1315, 800, "subscribe", size=SIZE["caption"],
               family=MONO, fill=SLATE, anchor="middle")
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- 10. thumbnail
def thumbnail(text_lines, visual_note="chart / map / archival image",
              out="preview/10_thumbnail.svg"):
    """
    1280x720. Left 60% visual, right 40% text. Max 5 words total.
    Replace the placeholder rect with your chart or archival image in Affinity.
    """
    s = _open(TW, TH) + _grain(TW, TH, 0.06)
    split = int(TW * 0.60)
    # visual zone placeholder
    s += f'  <rect x="0" y="0" width="{split}" height="{TH}" fill="{INK_SOFT}"/>\n'
    s += _text(split // 2, TH // 2, visual_note, size=26, family=MONO,
               fill=SLATE, anchor="middle")
    # text zone
    y = 300 if len(text_lines) <= 2 else 250
    for i, line in enumerate(text_lines):
        s += _text(split + 48, y + i * 96, line, size=84, family=SERIF,
                   fill=PAPER if i else AMBER, weight="600")
    s += _rule(split + 48, y - 110, 80, h=8)
    s += _text(TW - 40, TH - 32, CHANNEL, size=24, family=SERIF,
               fill=PAPER_DIM, anchor="end", spacing="1.5")
    s += "</svg>\n"
    return _write(s, out)


# ----------------------------------------------------------------- demo set
def render_demo():
    made = []
    made.append(title_card("Is AI a Bubble?", "Ask the Railways"))
    made.append(chapter_card(2, "What the railways actually built"))
    made.append(kicker("90%", "OF ADVANCED CHIPS", "made on one island"))
    made.append(quote_card(
        "The traffic will be there. The only question is who owns the line.",
        "Railway prospectus", "1845",
        source="Illustrative — replace with a verified quotation"))
    made.append(timeline(
        [("1830", "First intercity line"),
         ("1845", "Mania peaks"),
         ("1847", "Credit tightens"),
         ("1850", "Shares down ~85%"),
         ("1870", "Network still running")],
        title="Railway mania, start to finish",
        source="Source: replace before publishing"))
    made.append(table(
        ["Bubble", "Peak", "Drawdown", "Asset survived?"],
        [["Railways", "1845", "~85%", "Yes"],
         ["Telecom fibre", "2000", "~90%", "Yes"],
         ["Dot-com", "2000", "~78%", "Partly"],
         ["AI capex", "?", "?", "?"]],
        title="The asset being real has never prevented a bubble",
        source="Source: replace before publishing",
        highlight_col=3))
    made.append(lower_third("Suez Canal", "193 km · opened 1869"))
    made.append(source_overlay("USGS Mineral Commodity Summaries 2026 · p.4"))
    made.append(end_card("Why Ships Now Avoid the Suez Canal"))
    made.append(thumbnail(["IS AI", "NEXT?"], "1840s share certificate + capex chart"))
    return made


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true", default=True)
    ap.parse_args()
    for p in render_demo():
        print(p)
