#!/usr/bin/env python3
"""Three mark concepts for ThinkLate. Rendered at 800px and real 32px."""
import subprocess

INK="#1B2A4A"; PAPER="#F4F1EA"; AMBER="#D99A2B"; AMBER_DIM="#8C6B2F"

def wrap(body, field=INK):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" '
            f'viewBox="0 0 512 512"><rect width="512" height="512" fill="{field}"/>'
            f'{body}</svg>')

# ---------- C1: OWL LOOKING BACK (asymmetric three-quarter turn)
c1 = f'''
<!-- tufts: right full, left foreshortened -->
<path d="M 352 178 L 408 112 L 386 196 Z" fill="{PAPER}"/>
<path d="M 246 184 L 212 136 L 236 198 Z" fill="{PAPER}"/>
<!-- head, wider on the left = back of skull turned toward us -->
<ellipse cx="272" cy="282" rx="166" ry="152" fill="{PAPER}"/>
<!-- heart-shaped facial disc, pushed right toward the viewer -->
<path d="M 306 208
   C 292 172, 250 168, 234 206
   C 222 236, 226 286, 252 322
   C 272 352, 296 374, 306 392
   C 316 374, 340 352, 360 322
   C 386 286, 390 236, 378 206
   C 362 168, 320 172, 306 208 Z" fill="{INK}"/>
<!-- eyes: near eye large, far eye foreshortened -->
<circle cx="344" cy="258" r="36" fill="{AMBER}"/>
<circle cx="266" cy="262" r="24" fill="{AMBER}"/>
<!-- beak -->
<path d="M 306 300 L 294 326 L 306 344 L 318 326 Z" fill="{PAPER}"/>
'''

# ---------- C2: THE LAG MARK (offset echo — understanding arrives after)
c2 = f'''
<g stroke-linejoin="miter" fill="none">
  <!-- the event: amber, behind -->
  <path d="M 344 132 L 210 256 L 344 380" stroke="{AMBER}" stroke-width="74"/>
  <!-- the understanding: paper, offset back -->
  <path d="M 300 132 L 166 256 L 300 380" stroke="{PAPER}" stroke-width="74"/>
</g>
'''

# ---------- C3: JANUS (one head, two faces — back and forward)
c3 = f'''
<path d="M 150 402 L 150 258
   C 150 186, 196 128, 256 128
   C 316 128, 362 186, 362 258
   L 362 402 Z" fill="{PAPER}"/>
<!-- profile noses, one each side -->
<path d="M 150 262 L 108 292 L 150 322 Z" fill="{PAPER}"/>
<path d="M 362 262 L 404 292 L 362 322 Z" fill="{PAPER}"/>
<!-- the backward face sees clearly: amber. the forward face does not: ink -->
<circle cx="192" cy="256" r="31" fill="{AMBER}"/>
<circle cx="320" cy="256" r="31" fill="{INK}"/>
'''

SETS = [("C1", "C1  OWL LOOKING BACK", c1),
        ("C2", "C2  THE LAG MARK", c2),
        ("C3", "C3  JANUS", c3)]

rows = []
for tag, label, body in SETS:
    f = f"{tag}.svg"; open(f, "w").write(wrap(body))
    subprocess.run(["convert","-background","none",f,"-resize","420x",f"{tag}_420.png"],check=True)
    subprocess.run(["convert","-background","none",f,"-resize","98x", f"{tag}_98.png"],check=True)
    subprocess.run(["convert","-background","none",f,"-resize","32x", f"{tag}_32.png"],check=True)
    for n in (98,32):
        subprocess.run(["convert",f"{tag}_{n}.png","-filter","point","-resize","420x",
                        f"{tag}_{n}z.png"],check=True)
    subprocess.run(["convert",f"{tag}_420.png",f"{tag}_98z.png",f"{tag}_32z.png","+append",
                    "-bordercolor","#2b2b2b","-border","8",
                    "-background","#1a1a1a","-fill","white","-pointsize","32",
                    f"label:{label}          800px            98px             32px",
                    "-gravity","center","-append",f"c_{tag}.png"],check=True)
    rows.append(f"c_{tag}.png")

subprocess.run(["convert"]+rows+["-background","#1a1a1a","-gravity","center","-append",
                "_concepts.png"],check=True)
print("done")
