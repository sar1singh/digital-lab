#!/usr/bin/env python3
"""Render owl A in 5 candidate palettes, at 800px and 32px."""
import os, subprocess, importlib.util
spec = importlib.util.spec_from_file_location("ba", "build_assets.py")

def owl(cx, cy, s, head, eye, pupil):
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

# name, field, head, eye, pupil
PAL = [
 ("P1 INK + AMBER (current spec)",   "#111827", "#F4F1EA", "#D99A2B", "#111827"),
 ("P2 INDIGO + MARIGOLD",            "#1B2A4A", "#F4F1EA", "#E0A72E", "#1B2A4A"),
 ("P3 CHARCOAL + TERRACOTTA",        "#1A1A17", "#EDE7DA", "#C2532F", "#1A1A17"),
 ("P4 DEEP GREEN + BRASS",           "#14241F", "#F2EFE4", "#C9A227", "#14241F"),
 ("P5 PAPER-PRIMARY (inverted)",     "#F4F1EA", "#111827", "#A8741A", "#F4F1EA"),
]

rows = []
for i,(name, field, head, eye, pupil) in enumerate(PAL, 1):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" '
           f'viewBox="0 0 800 800"><rect width="800" height="800" fill="{field}"/>'
           f'{owl(400,400,1.12,head,eye,pupil)}</svg>')
    f = f"pal{i}.svg"; open(f,"w").write(svg)
    subprocess.run(["convert","-background","none",f,"-resize","420x",f"p{i}_420.png"],check=True)
    subprocess.run(["convert","-background","none",f,"-resize","32x",f"p{i}_32.png"],check=True)
    subprocess.run(["convert",f"p{i}_32.png","-filter","point","-resize","420x",
                    f"p{i}_32z.png"],check=True)
    subprocess.run(["convert",f"p{i}_420.png",f"p{i}_32z.png","+append",
                    "-bordercolor","#333","-border","6",
                    "-background","#222","-fill","white","-pointsize","30",
                    "label:"+name,"-gravity","center","-append",f"row{i}.png"],check=True)
    rows.append(f"row{i}.png")

subprocess.run(["convert"]+rows+["-background","#222","-gravity","center",
                "-append","_palettes.png"],check=True)
print("done")
