#!/usr/bin/env python3
"""
Side-by-side comparison: the same frames on ink vs paper surface.
Renders to preview/surf_* so the two can be judged against each other
rather than argued about.

    python3 surface_demo.py
"""
import html
import os
import textwrap

from brand import SURFACES, SERIF, SANS, MONO, W, H, MARGIN, SIZE, CHANNEL

HERE = os.path.dirname(os.path.abspath(__file__))


def _t(x, y, s, size, fill, family=SANS, weight="400", anchor="start",
       spacing="0", opacity="1"):
    return (f'  <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}" opacity="{opacity}">'
            f'{html.escape(str(s))}</text>\n')


def _wrap(x, y, s, chars, size, lh, **kw):
    out = ""
    for i, ln in enumerate(textwrap.wrap(str(s), chars)):
        out += _t(x, y + i * lh, ln, size, **kw)
    return out


def _write(svg, out):
    p = os.path.join(HERE, out)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(svg)
    return p


def quote(surface, out):
    c = SURFACES[surface]
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">\n'
         f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>\n')
    s += _t(MARGIN, 330, "“", 200, c["accent"], SERIF, opacity="0.35")
    s += _wrap(MARGIN, 440,
               "The traffic will be there. The only question is who owns the line.",
               46, SIZE["quote"], 86, fill=c["fg"], family=SERIF)
    s += (f'  <rect x="{MARGIN}" y="800" width="90" height="6" '
          f'fill="{c["accent"]}"/>\n')
    s += _t(MARGIN, 880, "Railway prospectus", SIZE["body"], c["fg"], SANS,
            weight="600")
    s += _t(MARGIN, 928, "1845", SIZE["caption"], c["dim"], MONO)
    s += _t(MARGIN, H - 56, "Source: illustrative — replace before publishing",
            SIZE["caption"], c["dim"], MONO)
    s += _t(W - MARGIN, H - 56, CHANNEL, SIZE["caption"], c["dim"], SERIF,
            anchor="end", spacing="1.5")
    s += "</svg>\n"
    return _write(s, out)


def timeline(surface, out):
    c = SURFACES[surface]
    events = [("1830", "First intercity line"), ("1845", "Mania peaks"),
              ("1847", "Credit tightens"), ("1850", "Shares down ~85%"),
              ("1870", "Network still running")]
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">\n'
         f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>\n')
    s += _t(MARGIN, 200, "Railway mania, start to finish", SIZE["h2"],
            c["fg"], SERIF)
    y, x0, x1 = 560, MARGIN, W - MARGIN
    s += f'  <rect x="{x0}" y="{y}" width="{x1-x0}" height="3" fill="{c["rule"]}"/>\n'
    step = (x1 - x0) / (len(events) - 1)
    for i, (yr, lb) in enumerate(events):
        x = x0 + i * step
        s += f'  <circle cx="{x:.0f}" cy="{y+1}" r="14" fill="{c["accent"]}"/>\n'
        s += _t(x, y - 60, yr, SIZE["h2"], c["accent"], MONO, anchor="middle")
        for j, ln in enumerate(textwrap.wrap(lb, 18)):
            s += _t(x, y + 90 + j * 44, ln, SIZE["label"], c["fg"], SANS,
                    anchor="middle")
    s += _t(MARGIN, H - 56, "Source: illustrative", SIZE["caption"], c["dim"], MONO)
    s += _t(W - MARGIN, H - 56, CHANNEL, SIZE["caption"], c["dim"], SERIF,
            anchor="end", spacing="1.5")
    s += "</svg>\n"
    return _write(s, out)


def thumb(surface, out):
    c = SURFACES[surface]
    TW, TH = 1280, 720
    split = int(TW * 0.60)
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW}" height="{TH}" '
         f'viewBox="0 0 {TW} {TH}">\n'
         f'  <rect width="{TW}" height="{TH}" fill="{c["bg"]}"/>\n')
    s += f'  <rect x="0" y="0" width="{split}" height="{TH}" fill="{c["panel"]}"/>\n'
    s += _t(split // 2, TH // 2, "chart / archival image", 26, c["dim"], MONO,
            anchor="middle")
    s += f'  <rect x="{split+48}" y="190" width="80" height="8" fill="{c["accent"]}"/>\n'
    s += _t(split + 48, 300, "IS AI", 84, c["accent"], SERIF, weight="600")
    s += _t(split + 48, 396, "NEXT?", 84, c["fg"], SERIF, weight="600")
    s += _t(TW - 40, TH - 32, CHANNEL, 24, c["dim"], SERIF, anchor="end",
            spacing="1.5")
    s += "</svg>\n"
    return _write(s, out)


if __name__ == "__main__":
    made = []
    for surf in ("ink", "paper"):
        made.append(quote(surf, f"preview/surf_quote_{surf}.svg"))
        made.append(timeline(surf, f"preview/surf_timeline_{surf}.svg"))
        made.append(thumb(surf, f"preview/surf_thumb_{surf}.svg"))
    for m in made:
        print(m)
