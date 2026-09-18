#!/usr/bin/env python3
"""ThinkLate owl mark — three geometric variants. Renders at 800 / 98 / 32 px."""
import os
INK="#111827"; PAPER="#F4F1EA"; AMBER="#D99A2B"; DIM="#6E6A61"

def wrap(body, bg=INK, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 512 512">\n<rect width="512" height="512" fill="{bg}"/>\n{body}</svg>\n')

# ---------- A. Solid head. Ear tufts, wide facial disc, tapering chin.
A = f'''
<path d="M 256 96
         C 210 96, 176 118, 158 150
         L 132 112 L 138 168
         C 118 196, 110 232, 110 264
         C 110 344, 176 412, 256 412
         C 336 412, 402 344, 402 264
         C 402 232, 394 196, 374 168
         L 380 112 L 354 150
         C 336 118, 302 96, 256 96 Z" fill="{PAPER}"/>
<circle cx="198" cy="252" r="54" fill="{INK}"/>
<circle cx="314" cy="252" r="54" fill="{INK}"/>
<circle cx="198" cy="252" r="30" fill="{AMBER}"/>
<circle cx="314" cy="252" r="30" fill="{AMBER}"/>
<path d="M 256 286 L 238 316 L 256 332 L 274 316 Z" fill="{INK}"/>
'''

# ---------- B. Outline head. Lighter, more editorial.
B = f'''
<path d="M 256 100
         C 212 100, 180 122, 163 153
         L 140 120 L 145 172
         C 126 199, 118 233, 118 264
         C 118 340, 180 404, 256 404
         C 332 404, 394 340, 394 264
         C 394 233, 386 199, 367 172
         L 372 120 L 349 153
         C 332 122, 300 100, 256 100 Z"
      fill="none" stroke="{PAPER}" stroke-width="20" stroke-linejoin="round"/>
<circle cx="200" cy="254" r="42" fill="none" stroke="{PAPER}" stroke-width="18"/>
<circle cx="312" cy="254" r="42" fill="none" stroke="{PAPER}" stroke-width="18"/>
<circle cx="200" cy="254" r="19" fill="{AMBER}"/>
<circle cx="312" cy="254" r="19" fill="{AMBER}"/>
<path d="M 256 292 L 240 318 L 256 332 L 272 318 Z" fill="{PAPER}"/>
'''

# ---------- C. Most abstract. Two arcs (brow) + eyes + beak. No head outline.
C = f'''
<path d="M 120 212 C 120 150, 182 128, 226 168" fill="none" stroke="{PAPER}"
      stroke-width="26" stroke-linecap="round"/>
<path d="M 392 212 C 392 150, 330 128, 286 168" fill="none" stroke="{PAPER}"
      stroke-width="26" stroke-linecap="round"/>
<circle cx="186" cy="258" r="62" fill="{PAPER}"/>
<circle cx="326" cy="258" r="62" fill="{PAPER}"/>
<circle cx="186" cy="258" r="32" fill="{AMBER}"/>
<circle cx="326" cy="258" r="32" fill="{AMBER}"/>
<path d="M 256 300 L 232 340 L 256 362 L 280 340 Z" fill="{PAPER}"/>
'''

for name, body in (("A_solid",A),("B_outline",B),("C_abstract",C)):
    open(f"owl_{name}.svg","w").write(wrap(body))
    print(f"owl_{name}.svg")
