#!/usr/bin/env python3
"""ThinkLate brand assets — avatar, watermark, banner, thumbnail. From owl A."""
import os
INK="#111827"; PAPER="#F4F1EA"; AMBER="#D99A2B"; AMBER_P="#A8741A"
DIM="#A8A29A"; PANEL="#1C2433"; RULE="#2A3341"; PAPER_DIM="#6E6A61"
SERIF="Instrument Serif, Playfair Display, Georgia, serif"
SANS="IBM Plex Sans, Inter, Helvetica, sans-serif"

def owl(cx, cy, s, head=PAPER, eye=AMBER, pupil=INK):
    """Owl head, scaled. s = 1.0 → ~300px wide."""
    def p(x, y): return f"{cx + (x-256)*s:.1f} {cy + (y-256)*s:.1f}"
    return f'''<path d="M {p(256,96)}
   C {p(210,96)}, {p(176,118)}, {p(158,150)}
   L {p(132,112)} L {p(138,168)}
   C {p(118,196)}, {p(110,232)}, {p(110,264)}
   C {p(110,344)}, {p(176,412)}, {p(256,412)}
   C {p(336,412)}, {p(402,344)}, {p(402,264)}
   C {p(402,232)}, {p(394,196)}, {p(374,168)}
   L {p(380,112)} L {p(354,150)}
   C {p(336,118)}, {p(302,96)}, {p(256,96)} Z" fill="{head}"/>
<circle cx="{cx-58*s:.1f}" cy="{cy-4*s:.1f}" r="{54*s:.1f}" fill="{pupil}"/>
<circle cx="{cx+58*s:.1f}" cy="{cy-4*s:.1f}" r="{54*s:.1f}" fill="{pupil}"/>
<circle cx="{cx-58*s:.1f}" cy="{cy-4*s:.1f}" r="{30*s:.1f}" fill="{eye}"/>
<circle cx="{cx+58*s:.1f}" cy="{cy-4*s:.1f}" r="{30*s:.1f}" fill="{eye}"/>
<path d="M {p(256,286)} L {p(238,316)} L {p(256,332)} L {p(274,316)} Z" fill="{pupil}"/>'''

def txt(x,y,s,size,fill,fam=SANS,w="400",anch="start",sp="0",op="1"):
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{w}" fill="{fill}" text-anchor="{anch}" '
            f'letter-spacing="{sp}" opacity="{op}">{s}</text>')

# ---------- 1. AVATAR 800x800
av = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
<rect width="800" height="800" fill="{INK}"/>
{owl(400, 400, 1.12)}
</svg>'''
open("01_avatar_800.svg","w").write(av)

# ---------- 2. WATERMARK 150x150 — ring so it survives light footage
wm = f'''<svg xmlns="http://www.w3.org/2000/svg" width="150" height="150" viewBox="0 0 150 150">
<circle cx="75" cy="75" r="72" fill="{INK}"/>
<circle cx="75" cy="75" r="72" fill="none" stroke="{PAPER}" stroke-width="5"/>
{owl(75, 76, 0.205)}
</svg>'''
open("02_watermark_150.svg","w").write(wm)

# ---------- 3. BANNER 2560x1440, safe area 1235x338 centred
W,H=2560,1440; SW,SH=1235,338
sx,sy=(W-SW)//2,(H-SH)//2
bn = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="{INK}"/>
<g opacity="0.055" stroke="{PAPER}" stroke-width="1.5" fill="none">
{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0,H,80))}
{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0,W,80))}
</g>
{owl(sx+108, sy+150, 0.40)}
{txt(sx+238, sy+126, "ThinkLate", 108, PAPER, SERIF, "400", "start", "1")}
{txt(sx+242, sy+186, "Master of none, expert of after", 34, DIM, SANS)}
<rect x="{sx+242}" y="{sy+216}" width="92" height="5" fill="{AMBER}"/>
{txt(sx+242, sy+272, "Work · Money · Power — explained in hindsight", 30, PAPER, SANS)}
{txt(sx+242, sy+318, "New video every two weeks", 26, DIM, SANS)}
</svg>'''
open("03_banner_2560.svg","w").write(bn)

# ---------- 4. THUMBNAIL TEMPLATE 1280x720, paper surface
TW,TH=1280,720; split=int(TW*0.60)
th = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{TW}" height="{TH}" viewBox="0 0 {TW} {TH}">
<rect width="{TW}" height="{TH}" fill="{PAPER}"/>
<rect x="0" y="0" width="{split}" height="{TH}" fill="#EAE5DA"/>
{txt(split//2, TH//2-8, "VISUAL ZONE", 30, PAPER_DIM, SANS, "600", "middle", "4")}
{txt(split//2, TH//2+34, "real chart / map / archival image", 22, PAPER_DIM, SANS, "400", "middle")}
<rect x="{split+52}" y="228" width="84" height="9" fill="{AMBER_P}"/>
{txt(split+52, 340, "IS AI", 92, AMBER_P, SERIF, "600")}
{txt(split+52, 438, "NEXT?", 92, "#1A1A17", SERIF, "600")}
{txt(TW-44, TH-34, "ThinkLate", 24, PAPER_DIM, SERIF, "400", "end", "1.5")}
</svg>'''
open("04_thumbnail_1280.svg","w").write(th)
print("4 assets written")
