#!/usr/bin/env python3
"""
ThinkLate Episode L07 ("Why You Can't Cancel Anything") — Teleprompter Recording Deck Generator
Compiles script_final.md into an ergonomic studio teleprompter: recording_deck.html
"""

import os
import pathlib
import re

L07_DIR = pathlib.Path(__file__).resolve().parent
SCRIPT_MD = L07_DIR / "script_final.md"
OUT_HTML = L07_DIR / "recording_deck.html"

BEAT_METADATA = [
    {"id": "b1", "tab": "Q1: Iliad Flow", "title": "Why Did Amazon Name Its Cancel Button After a 24-Book War?", "color": "#06B6D4"},
    {"id": "b2", "tab": "Q2: Churn Math", "title": "What Happens to Wall Street Stock Prices If You Click Cancel?", "color": "#F59E0B"},
    {"id": "b3", "tab": "Q3: The Rule Died", "title": "Why Did a Federal Appeals Court Kill the Click-to-Cancel Rule?", "color": "#EF4444"},
    {"id": "b4", "tab": "Q4: India 2FA", "title": "How Did India's Central Bank Force Big Tech to Ask Permission?", "color": "#10B981"},
    {"id": "b5", "tab": "Q5: The Reckoning", "title": "Why Were You Engineered to Give Up on a $12 Charge?", "color": "#E2FF00"},
]

def build_deck():
    raw_text = SCRIPT_MD.read_text(encoding="utf-8")
    
    # Split beats by "### "
    raw_beats = re.split(r'\n(?=### \d+\.)', raw_text)
    header_block = raw_beats[0]
    beat_blocks = raw_beats[1:]

    nav_tabs_html = []
    beats_html = []

    for idx, block in enumerate(beat_blocks):
        lines = block.strip().splitlines()
        first_line = lines[0].replace('### ', '').strip()
        body_lines = lines[1:]

        meta = BEAT_METADATA[idx] if idx < len(BEAT_METADATA) else {
            "id": f"b{idx+1}", "tab": f"Q{idx+1}", "title": first_line, "color": "#06B6D4"
        }

        spoken_text = " ".join([l for l in body_lines if not l.startswith('[') and not l.startswith('#') and l.strip()])
        words = [w for w in spoken_text.replace('//', ' ').replace('///', ' ').split() if re.search(r'[a-zA-Z0-9]', w)]
        word_count = len(words)
        runtime_sec = int((word_count / 145) * 60)
        mins = runtime_sec // 60
        secs = runtime_sec % 60
        time_str = f"~{mins}m {secs:02d}s ({word_count} words @ 145 WPM)"

        nav_tabs_html.append(f'<a href="#{meta["id"]}" class="act-tab{" active" if idx==0 else ""}" id="tab{idx+1}">{meta["tab"]}</a>')

        beat_elements = []
        for line in body_lines:
            line_str = line.strip()
            if not line_str:
                continue

            # Visual Cues
            if line_str.startswith('[VISUAL:'):
                vc_text = line_str[8:-1].strip()
                beat_elements.append(f'<div class="vis-pill"><span class="vis-tag">VISUAL</span> {vc_text}</div>')
            # SFX Cues
            elif line_str.startswith('[SFX:'):
                sfx_text = line_str[5:-1].strip()
                beat_elements.append(f'<div class="sfx-pill"><span class="sfx-tag">🎧 SFX</span> {sfx_text}</div>')
            # Dead Air Cues
            elif line_str.startswith('[DEAD AIR:'):
                da_text = line_str[10:-1].strip()
                beat_elements.append(f'<div class="deadair-pill"><span class="da-tag">⚠️ DEAD AIR</span> {da_text}</div>')
            # Spoken dialogue lines with breath markers
            else:
                formatted_line = line_str
                # Highlight full stops /// (Cyan badge)
                formatted_line = formatted_line.replace('///', '<span class="b-full">///</span>')
                # Highlight half-beat pauses // (Amber badge)
                formatted_line = formatted_line.replace('//', '<span class="b-half">//</span>')
                beat_elements.append(f'<p class="sentence">{formatted_line}</p>')

        elements_markup = "\n".join(beat_elements)
        beats_html.append(f"""
        <section class="beat-card" id="{meta['id']}" style="border-top: 4px solid {meta['color']};">
            <div class="beat-header">
                <div>
                    <span class="beat-badge" style="background: {meta['color']}20; color: {meta['color']}; border: 1px solid {meta['color']}40;">BEAT {idx+1}</span>
                    <h2 class="beat-title">{meta['title']}</h2>
                </div>
                <div class="beat-timing">{time_str}</div>
            </div>
            <div class="beat-body">
                {elements_markup}
            </div>
        </section>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recording Deck — Why You Can't Cancel Anything | ThinkLate L07</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #080C14;
      --card: #0F1626;
      --bdr: #1E2C48;
      --txt: #F1F5F9;
      --dim: #94A3B8;
      --cyan: #06B6D4;
      --amber: #F59E0B;
      --lime: #E2FF00;
      --crimson: #FF2A4B;
      --fs: 32px;
      --lh: 2.0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--txt);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: var(--fs);
      line-height: var(--lh);
      padding-bottom: 300px;
      -webkit-font-smoothing: antialiased;
    }}
    #pgwrap {{ position: fixed; top: 0; left: 0; width: 100%; height: 5px; background: rgba(255,255,255,.05); z-index: 200; }}
    #pg {{ height: 100%; width: 0%; background: linear-gradient(90deg, var(--cyan), var(--lime)); transition: width .1s ease-out; }}
    nav {{
      position: fixed; top: 5px; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 12px 28px; background: rgba(8, 12, 20, 0.96);
      backdrop-filter: blur(16px); border-bottom: 1px solid var(--bdr);
    }}
    .nav-left {{ display: flex; align-items: center; gap: 14px; }}
    .brand {{ font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 800; color: var(--lime); letter-spacing: 1px; }}
    .nav-tabs {{ display: flex; gap: 8px; }}
    .act-tab {{
      color: var(--dim); text-decoration: none; font-size: 13px; font-weight: 700;
      padding: 6px 14px; border-radius: 6px; background: rgba(255,255,255,.04); border: 1px solid transparent;
      transition: all .2s; font-family: 'JetBrains Mono', monospace;
    }}
    .act-tab:hover, .act-tab.active {{ color: #FFF; background: rgba(6, 182, 212, 0.15); border-color: var(--cyan); }}
    .hud {{ display: flex; align-items: center; gap: 16px; font-family: 'JetBrains Mono', monospace; font-size: 14px; }}
    .timer {{ color: var(--lime); font-size: 20px; font-weight: 800; }}
    .btn {{
      background: rgba(255,255,255,.08); color: #FFF; border: 1px solid var(--bdr);
      padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 700;
    }}
    .btn:hover {{ background: rgba(255,255,255,.15); }}
    main {{ max-width: 1000px; margin: 90px auto 0; padding: 0 24px; }}
    .beat-card {{
      background: var(--card); border: 1px solid var(--bdr); border-radius: 16px;
      padding: 36px 42px; margin-bottom: 40px; box-shadow: 0 12px 32px rgba(0,0,0,0.4);
    }}
    .beat-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,.08); }}
    .beat-badge {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }}
    .beat-title {{ font-size: 26px; font-weight: 800; color: #FFF; line-height: 1.3; }}
    .beat-timing {{ font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--dim); white-space: nowrap; }}
    .sentence {{ margin-bottom: 24px; color: #F1F5F9; font-weight: 600; }}
    .b-full {{
      display: inline-block; background: rgba(6, 182, 212, 0.2); color: var(--cyan);
      border: 1px solid var(--cyan); border-radius: 4px; font-family: 'JetBrains Mono', monospace;
      font-size: 14px; font-weight: 800; padding: 0 6px; margin: 0 4px; vertical-align: middle;
    }}
    .b-half {{
      display: inline-block; background: rgba(245, 158, 11, 0.2); color: var(--amber);
      border: 1px solid var(--amber); border-radius: 4px; font-family: 'JetBrains Mono', monospace;
      font-size: 14px; font-weight: 800; padding: 0 6px; margin: 0 4px; vertical-align: middle;
    }}
    .vis-pill {{
      background: rgba(148, 163, 184, 0.1); border-left: 4px solid var(--dim);
      padding: 10px 16px; border-radius: 6px; font-size: 16px; color: var(--dim);
      margin: 16px 0; font-family: 'JetBrains Mono', monospace;
    }}
    .vis-tag {{ color: #FFF; font-weight: 800; margin-right: 6px; }}
    .sfx-pill {{
      background: rgba(226, 255, 0, 0.08); border-left: 4px solid var(--lime);
      padding: 8px 16px; border-radius: 6px; font-size: 15px; color: var(--lime);
      margin: 14px 0; font-family: 'JetBrains Mono', monospace;
    }}
    .sfx-tag {{ font-weight: 800; margin-right: 6px; }}
    .deadair-pill {{
      background: rgba(255, 42, 75, 0.12); border: 2px dashed var(--crimson);
      padding: 12px 18px; border-radius: 8px; font-size: 16px; color: var(--crimson);
      margin: 20px 0; font-family: 'JetBrains Mono', monospace; font-weight: 700; text-align: center;
    }}
    .hide-vis .vis-pill {{ display: none !important; }}
  </style>
</head>
<body>
  <div id="pgwrap"><div id="pg"></div></div>
  <nav>
    <div class="nav-left">
      <div class="brand">THINKLATE // L07</div>
      <div class="nav-tabs">
        {"".join(nav_tabs_html)}
      </div>
    </div>
    <div class="hud">
      <div class="timer" id="timerDisplay">00:00</div>
      <button class="btn" onclick="toggleTimer()">⏱️ START</button>
      <button class="btn" onclick="toggleVisuals()">👁️ VISUALS</button>
      <button class="btn" onclick="adjustFont(2)">A+</button>
      <button class="btn" onclick="adjustFont(-2)">A-</button>
    </div>
  </nav>

  <main id="mainContent">
    {"".join(beats_html)}
  </main>

  <script>
    let fontSz = 32;
    function adjustFont(delta) {{
      fontSz = Math.max(22, Math.min(48, fontSz + delta));
      document.body.style.setProperty('--fs', fontSz + 'px');
    }}

    function toggleVisuals() {{
      document.body.classList.toggle('hide-vis');
    }}

    let timerInterval = null;
    let timerSec = 0;
    function toggleTimer() {{
      const disp = document.getElementById('timerDisplay');
      if (timerInterval) {{
        clearInterval(timerInterval);
        timerInterval = null;
      }} else {{
        timerInterval = setInterval(() => {{
          timerSec++;
          const m = String(Math.floor(timerSec / 60)).padStart(2, '0');
          const s = String(timerSec % 60).padStart(2, '0');
          disp.innerText = m + ':' + s;
        }}, 1000);
      }}
    }}

    window.addEventListener('scroll', () => {{
      const h = document.documentElement.scrollHeight - window.innerHeight;
      const pct = (window.scrollY / Math.max(1, h)) * 100;
      document.getElementById('pg').style.width = pct + '%';
    }});
  </script>
</body>
</html>
"""

    OUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"[+] Broadcast Recording Deck compiled successfully to: {OUT_HTML}")

if __name__ == "__main__":
    build_deck()

