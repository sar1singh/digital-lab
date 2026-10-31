#!/usr/bin/env python3
"""
ThinkLate Video 04 — Recording Deck Teleprompter Generator
Compiles script_final.md (Story Edition v2) into a Broadcast-Grade HTML teleprompter
Output: videos/04_the-subscription-trap/recording_deck.html
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_MD = os.path.join(SCRIPT_DIR, "script_final.md")
OUT_HTML = os.path.join(SCRIPT_DIR, "recording_deck.html")

def build_deck():
    with open(SCRIPT_MD, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into narrative beats by "## "
    raw_beats = re.split(r'\n(?=## )', content)
    header_block = raw_beats[0]
    beat_blocks = raw_beats[1:]

    # Beat metadata
    beat_meta = [
        {"id": "b1", "tab": "Q1: $18 Seat", "title": "Why did a sixty-thousand-dollar car ask for eighteen dollars to warm a seat?", "theme": "b1", "color": "#06B6D4", "accent": "Cyan / Cold Frost"},
        {"id": "b2", "tab": "Q2: HP Printer", "title": "Who decided your printer should die overnight?", "theme": "b2", "color": "#F59E0B", "accent": "Amber / Ink Glow"},
        {"id": "b3", "tab": "Q3: Tractor Hack", "title": "What happens when the locked machine is a tractor?", "theme": "b3", "color": "#FB923C", "accent": "Rust / Harvest Dusk"},
        {"id": "b4", "tab": "Q4: Wall St 6.7x", "title": "Why would any CEO want this?", "theme": "b4", "color": "#10B981", "accent": "Emerald / Valuation Surge"},
        {"id": "b5", "tab": "Q5: 1924 Cartel", "title": "Is this actually new?", "theme": "b5", "color": "#E879F9", "accent": "Fuchsia / Geneva Sepia"},
        {"id": "b6", "tab": "Q6: Phone Lock", "title": "What does it cost the person who cannot pay?", "theme": "b6", "color": "#EF4444", "accent": "Crimson / Night Lock"},
        {"id": "b7", "tab": "Q7: BMW U-Turn", "title": "What happened to the seat?", "theme": "b7", "color": "#FACC15", "accent": "Gold / Sovereignty"},
    ]

    beats_html = []
    nav_tabs_html = []

    for idx, block in enumerate(beat_blocks):
        lines = block.strip().splitlines()
        first_line = lines[0].replace('## ', '').strip()
        body_lines = lines[1:]

        meta = beat_meta[idx] if idx < len(beat_meta) else {
            "id": f"b{idx+1}", "tab": f"Q{idx+1}", "title": first_line, "theme": f"b{idx+1}", "color": "#38BDF8"
        }

        # Calculate spoken word count
        spoken_text = " ".join([l for l in body_lines if not l.startswith('[') and not l.startswith('*') and not l.startswith('#') and l.strip()])
        word_count = len(spoken_text.split())
        runtime_sec = int((word_count / 135) * 60)
        mins = runtime_sec // 60
        secs = runtime_sec % 60
        time_str = f"~{mins}m {secs:02d}s ({word_count} words)"

        nav_tabs_html.append(f'<a href="#{meta["id"]}" class="act-tab{" active" if idx==0 else ""}" id="tab{idx+1}">{meta["tab"]}</a>')

        beat_elements = []
        for line in body_lines:
            line_str = line.strip()
            if not line_str:
                continue

            # SFX Cue
            if line_str.startswith('[SFX:'):
                sfx_text = line_str[5:-1].strip()
                beat_elements.append(f'<div class="sfx">🎧 SFX: {sfx_text}</div>')
            
            # Visual Cue
            elif line_str.startswith('[VISUAL:'):
                vc_text = line_str[8:-1].strip()
                beat_elements.append(f'<div class="vc">🎬 VISUAL: {vc_text}</div>')

            # Delivery Cue
            elif line_str.startswith('*Delivery:'):
                deliv_text = line_str[10:-1].strip()
                beat_elements.append(f'<div class="delivery-cue">🎙️ Delivery Note: {deliv_text}</div>')

            # Spoken Dialogue Line
            else:
                formatted = line_str
                # Replace breath markers with placeholders first to prevent nested collisions
                formatted = formatted.replace('///', '___FS_MARKER___')
                formatted = formatted.replace('//', '___HB_MARKER___')
                formatted = formatted.replace('___FS_MARKER___', '<span class="p-fs">///</span>')
                formatted = formatted.replace('___HB_MARKER___', '<span class="p-hb">//</span>')
                beat_elements.append(f'<div class="ln">{formatted}</div>')

        beat_card = f"""
    <section class="beat {meta['theme']}" id="{meta['id']}">
      <div class="ah">
        <div class="ah-left">
          <span class="dot"></span>
          <span class="beat-label">NARRATIVE QUESTION 0{idx+1}</span>
          <span class="beat-title-main">&mdash; {first_line}</span>
        </div>
        <div class="act-timing">{time_str}</div>
      </div>
      <div class="ab">
        {"".join(beat_elements)}
      </div>
    </section>
"""
        beats_html.append(beat_card)

    nav_tabs_str = "\n        ".join(nav_tabs_html)
    beats_str = "\n".join(beats_html)

    deck_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recording Deck &mdash; Why You Will Never Own Anything Again | ThinkLate Video 04</title>
  <meta name="description" content="ThinkLate broadcast teleprompter deck for Video 04: The Subscription Trap. Faceless Roast and Reveal storytelling with 12-word breath markers, diegetic Foley cues, and verified source grounding.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,600;0,700;0,800;1,400;1,700&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #080C14;
      --surf: #0F1626;
      --card: #141D30;
      --bdr: #1E2C48;
      --txt: #F1F5F9;
      --muted: #64748B;
      --dim: #94A3B8;
      --gold: #F59E0B;
      --cyan: #06B6D4;
      --red: #EF4444;
      --grn: #10B981;
      --purp: #8B5CF6;
      --orange: #FB923C;
      --fs: 32px;
      --lh: 1.95;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background: var(--bg);
      color: var(--txt);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: var(--fs);
      line-height: var(--lh);
      padding-bottom: 380px;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Progress Bar */
    #pgwrap {{ position: fixed; top: 0; left: 0; width: 100%; height: 5px; background: rgba(255,255,255,.05); z-index: 200; }}
    #pg {{ height: 100%; width: 0%; background: linear-gradient(90deg, var(--cyan), var(--gold)); transition: width .1s ease-out; }}

    /* Sticky Navigation Header */
    nav {{
      position: fixed;
      top: 5px;
      left: 0;
      right: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 24px;
      background: rgba(8, 12, 20, 0.96);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--bdr);
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand {{
      font-size: 13px;
      font-weight: 800;
      color: var(--gold);
      letter-spacing: .12em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .act-tabs {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      max-width: 520px;
      scrollbar-width: none;
    }}
    .act-tabs::-webkit-scrollbar {{ display: none; }}

    .act-tab {{
      background: var(--card);
      border: 1px solid var(--bdr);
      color: var(--dim);
      font-size: 11px;
      font-weight: 700;
      padding: 5px 11px;
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      white-space: nowrap;
      transition: all .15s ease;
    }}

    .act-tab:hover {{ background: var(--bdr); color: var(--txt); }}
    .act-tab.active {{ background: var(--cyan); color: #000; border-color: var(--cyan); }}

    .ctrl-group {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    /* Audacity Stopwatch HUD */
    .hud-timer {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #0B111E;
      border: 1px solid #1E293B;
      padding: 4px 10px;
      border-radius: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #38BDF8;
    }}

    .timer-display {{
      font-weight: 700;
      min-width: 48px;
    }}

    button {{
      background: var(--card);
      border: 1px solid var(--bdr);
      color: var(--dim);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all .18s;
      font-family: inherit;
    }}

    button:hover {{ background: var(--bdr); color: var(--txt); }}
    button.on {{ background: var(--cyan); color: #000; border-color: var(--cyan); }}
    button.danger {{ background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.4); color: #FCA5A5; }}
    button.danger:hover {{ background: var(--red); color: #FFF; }}

    #fsc {{ display: flex; gap: 4px; }}
    #fsc button {{ padding: 6px 10px; font-size: 14px; }}

    /* Scroll Speed Adjuster */
    .speed-ctrl {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--card);
      border: 1px solid var(--bdr);
      padding: 4px 8px;
      border-radius: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--dim);
    }}

    .speed-btn {{
      background: none;
      border: none;
      color: var(--cyan);
      font-size: 14px;
      padding: 0 4px;
      cursor: pointer;
    }}

    /* Main Container */
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 110px 40px 60px;
    }}

    /* Teleprompter Focus Mask / Reading Guide */
    .focus-guide {{
      position: fixed;
      top: 35%;
      left: 0;
      right: 0;
      height: 140px;
      background: rgba(6, 182, 212, 0.025);
      border-top: 1px dashed rgba(6, 182, 212, 0.2);
      border-bottom: 1px dashed rgba(6, 182, 212, 0.2);
      pointer-events: none;
      z-index: 50;
      display: none;
    }}

    body.show-guide .focus-guide {{ display: block; }}

    /* Pre-Flight Audio Brief Card */
    .preflight-card {{
      background: linear-gradient(135deg, rgba(15, 22, 38, 0.95), rgba(20, 29, 48, 0.85));
      border: 1px solid var(--bdr);
      border-left: 4px solid var(--gold);
      border-radius: 14px;
      padding: 22px 28px;
      margin-bottom: 48px;
      font-size: 14px;
      line-height: 1.6;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}

    .preflight-title {{
      font-size: 12px;
      font-weight: 800;
      color: var(--gold);
      letter-spacing: .12em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .badge-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 6px;
    }}

    .badge {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 3px 10px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
    }}

    .badge.pro {{ color: #38BDF8; border-color: rgba(56, 189, 248, 0.3); }}
    .badge.pacing {{ color: #FBBF24; border-color: rgba(251, 191, 36, 0.3); }}
    .badge.verified {{ color: #34D399; border-color: rgba(52, 211, 153, 0.3); }}

    /* Beat Section Cards */
    .beat {{
      margin-bottom: 56px;
      border: 1px solid var(--bdr);
      border-radius: 18px;
      overflow: hidden;
      background: var(--surf);
      transition: transform .2s ease;
    }}

    .ah {{
      padding: 16px 28px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: .14em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .ah-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .beat-title-main {{
      font-size: 13px;
      letter-spacing: normal;
      text-transform: none;
      font-weight: 700;
      color: #E2E8F0;
    }}

    /* Themes per Beat */
    .beat.b1 .ah {{ background: linear-gradient(135deg, #0e1e38, #161230); color: var(--cyan); border-bottom: 1px solid #1E2C48; }}
    .beat.b2 .ah {{ background: linear-gradient(135deg, #241604, #2b1c06); color: var(--gold); border-bottom: 1px solid #3d2a08; }}
    .beat.b3 .ah {{ background: linear-gradient(135deg, #1f140d, #2d1e11); color: var(--orange); border-bottom: 1px solid #452c16; }}
    .beat.b4 .ah {{ background: linear-gradient(135deg, #0d2215, #112d1b); color: var(--grn); border-bottom: 1px solid #143e24; }}
    .beat.b5 .ah {{ background: linear-gradient(135deg, #221820, #2c1a29); color: var(--purp); border-bottom: 1px solid #44263f; }}
    .beat.b6 .ah {{ background: linear-gradient(135deg, #200d0d, #2d1111); color: var(--red); border-bottom: 1px solid #3a1515; }}
    .beat.b7 .ah {{ background: linear-gradient(135deg, #1d1b0d, #272210); color: #FACC15; border-bottom: 1px solid #3c3516; }}

    .act-timing {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      opacity: .8;
      font-weight: 600;
      white-space: nowrap;
    }}

    .dot {{ width: 8px; height: 8px; border-radius: 50%; background: currentColor; flex-shrink: 0; }}

    .ab {{
      padding: 34px 40px;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }}

    /* Visual Cues */
    .vc {{
      background: rgba(6, 182, 212, 0.05);
      border: 1px dashed rgba(6, 182, 212, 0.35);
      border-radius: 10px;
      padding: 10px 18px;
      font-size: 13px;
      font-family: 'JetBrains Mono', monospace;
      color: #5EEAD4;
      line-height: 1.5;
      transition: opacity .2s;
    }}

    body.hide-vc .vc {{ display: none; }}

    /* SFX Cues */
    .sfx {{
      background: rgba(139, 92, 246, 0.08);
      border: 1px solid rgba(139, 92, 246, 0.4);
      border-radius: 10px;
      padding: 8px 16px;
      font-size: 13px;
      font-family: 'JetBrains Mono', monospace;
      color: #C084FC;
      line-height: 1.5;
    }}

    body.hide-vc .sfx {{ display: none; }}

    /* Delivery Coaching */
    .delivery-cue {{
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--gold);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 14px;
      color: var(--gold);
      font-style: italic;
      font-weight: 500;
      line-height: 1.5;
    }}

    /* Spoken Lines */
    .ln {{
      font-size: var(--fs);
      line-height: var(--lh);
      font-weight: 600;
      color: var(--txt);
      position: relative;
    }}

    /* Breath Marker Badges */
    .p-hb {{
      background: rgba(245, 158, 11, 0.15);
      color: #FBBF24;
      border: 1px solid rgba(245, 158, 11, 0.4);
      padding: 1px 7px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68em;
      font-weight: 700;
      vertical-align: middle;
      margin: 0 4px;
      user-select: none;
    }}

    .p-fs {{
      background: rgba(6, 182, 212, 0.18);
      color: #38BDF8;
      border: 1px solid rgba(6, 182, 212, 0.45);
      padding: 1px 7px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68em;
      font-weight: 800;
      vertical-align: middle;
      margin: 0 4px;
      user-select: none;
    }}

    /* Bottom Retake HUD Drawer */
    #retake-drawer {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(11, 17, 30, 0.98);
      backdrop-filter: blur(16px);
      border-top: 1px solid var(--bdr);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 150;
      font-size: 12px;
    }}

    .retake-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .retake-stats {{
      font-family: 'JetBrains Mono', monospace;
      color: var(--dim);
    }}

    .retake-stats strong {{
      color: var(--gold);
    }}

    .hotkey-guide {{
      display: flex;
      align-items: center;
      gap: 14px;
      color: var(--muted);
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .kbd {{
      background: var(--card);
      border: 1px solid var(--bdr);
      color: var(--txt);
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
    }}

    /* Retake List Modal / Log */
    #retake-log {{
      position: fixed;
      bottom: 60px;
      right: 28px;
      width: 340px;
      max-height: 280px;
      background: var(--card);
      border: 1px solid var(--bdr);
      border-radius: 12px;
      padding: 14px;
      display: none;
      flex-direction: column;
      gap: 8px;
      overflow-y: auto;
      z-index: 160;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }}

    #retake-log.open {{ display: flex; }}

    .retake-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 10px;
      background: rgba(255,255,255,0.03);
      border-radius: 6px;
      border-left: 3px solid var(--red);
    }}
  </style>
</head>
<body>

<div id="pgwrap"><div id="pg"></div></div>

<!-- Sticky Teleprompter Navbar -->
<nav>
  <div class="brand-group">
    <div class="brand">
      <span>🦉</span>
      <span>ThinkLate</span>
      <span style="opacity:.4; font-weight:400;">//</span>
      <span style="color:var(--txt); font-size:11px;">VIDEO 04</span>
    </div>
    <div class="act-tabs">
      {nav_tabs_str}
    </div>
  </div>

  <div class="ctrl-group">
    <!-- Audacity Stopwatch HUD -->
    <div class="hud-timer">
      <span>🎙️</span>
      <span class="timer-display" id="hudTimer">00:00</span>
      <button id="timerBtn" onclick="toggleTimer()" style="padding:2px 8px; font-size:11px;">Start</button>
      <button onclick="resetTimer()" style="padding:2px 6px; font-size:11px;">↺</button>
    </div>

    <!-- Scroll Speed Controls -->
    <div class="speed-ctrl">
      <span>SPEED</span>
      <button class="speed-btn" onclick="adjustSpeed(-0.5)" title="Slower ([)">-</button>
      <span id="speedVal" style="color:var(--txt); min-width:28px; text-align:center;">2.0x</span>
      <button class="speed-btn" onclick="adjustSpeed(0.5)" title="Faster (])">+</button>
    </div>

    <!-- Font Sizer -->
    <div id="fsc">
      <button onclick="changeFontSize(-2)" title="Smaller font">A-</button>
      <button onclick="changeFontSize(2)" title="Larger font">A+</button>
    </div>

    <!-- Toggles -->
    <button id="tvc" onclick="toggleVisuals()" title="Toggle Visuals (V)">Hide Visuals</button>
    <button id="tguide" onclick="toggleGuide()" title="Toggle Reading Focus Guide">Focus</button>
    <button id="scrollBtn" class="on" onclick="toggleScroll()" style="background:var(--cyan); color:#000;">Pause (Space)</button>
  </div>
</nav>

<div class="focus-guide"></div>

<main>
  <!-- Pre-Flight Briefing Card -->
  <div class="preflight-card">
    <div>
      <div class="preflight-title">🎙️ Audio Recording Brief &mdash; Video 04</div>
      <p style="color:var(--dim); font-size:13px; margin-bottom:10px;">
        <strong>Working Title:</strong> Why You Will Never Own Anything Again<br>
        <strong>Voiceover Format:</strong> Faceless Roast & Reveal Story (One Continuous Take)<br>
        <strong>Rule 14 & 15 Certified:</strong> 0 Syllabus breaks, 100% Fact-Check Verified
      </p>
      <div class="badge-list">
        <span class="badge pro">1,082 Spoken Words</span>
        <span class="badge pacing">Target: 135 WPM (~8m 01s)</span>
        <span class="badge verified">15 Sourced Claims Verified</span>
      </div>
    </div>
    <div>
      <div class="preflight-title">⚙️ Performance Keys & Markers</div>
      <p style="color:var(--dim); font-size:13px;">
        <span class="p-hb">//</span> = Half-beat catch breath (quick diaphragm catch)<br>
        <span class="p-fs">///</span> = Full stop reset & drop pitch (complete chest reset)<br>
        <strong>Pronunciation:</strong> <em>Phoebus</em> = <code>FEE-bus</code> | <em>Osram</em> = <code>OZ-ram</code><br>
        <strong>Tone:</strong> Sarcastic, street-smart insider tearing apart corporate spin over drinks.
      </p>
    </div>
  </div>

  <!-- Narrative Beat Sections -->
  {beats_str}
</main>

<!-- Bottom Retake & Status Drawer -->
<div id="retake-drawer">
  <div class="retake-left">
    <button class="danger" onclick="flagRetake()">🚩 Flag Retake (R)</button>
    <button onclick="toggleRetakeLog()">View Retakes (<span id="retakeCount">0</span>)</button>
    <button onclick="copyRetakes()">Copy Retakes for Audacity</button>
    <div class="retake-stats">
      Current Beat: <strong id="curBeatName">Q1: $18 Seat</strong>
    </div>
  </div>

  <div class="hotkey-guide">
    <span><span class="kbd">Space</span> Play/Pause</span>
    <span><span class="kbd">[</span> <span class="kbd">]</span> Speed</span>
    <span><span class="kbd">T</span> Timer</span>
    <span><span class="kbd">R</span> Retake</span>
    <span><span class="kbd">V</span> Visuals</span>
  </div>
</div>

<!-- Retake Log Modal -->
<div id="retake-log">
  <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">
    <strong>Logged Retakes</strong>
    <span style="cursor:pointer; color:var(--muted);" onclick="toggleRetakeLog()">✕</span>
  </div>
  <div id="retake-list" style="display:flex; flex-direction:column; gap:6px; margin-top:4px;">
    <div id="emptyMsg" style="color:var(--muted); text-align:center; padding:12px;">No retakes logged yet.</div>
  </div>
</div>

<script>
  // High-Precision Teleprompter Delta-Time Engine
  let isScrolling = false;
  let scrollSpeed = 2.0; // Default 2.0x
  let lastTimestamp = null;
  let animFrameId = null;
  let scrollAccumulator = window.scrollY || 0;

  function toggleScroll() {{
    isScrolling = !isScrolling;
    const btn = document.getElementById('scrollBtn');
    if (btn) {{
      btn.innerText = isScrolling ? 'Pause (Space)' : 'Auto Scroll (Space)';
      btn.style.background = isScrolling ? 'var(--cyan)' : 'var(--card)';
      btn.style.color = isScrolling ? '#000' : 'var(--txt)';
    }}
    if (isScrolling) {{
      lastTimestamp = null;
      scrollAccumulator = window.scrollY || window.pageYOffset || 0;
      animFrameId = requestAnimationFrame(scrollLoop);
    }} else {{
      if (animFrameId) cancelAnimationFrame(animFrameId);
    }}
  }}

  function scrollLoop(timestamp) {{
    if (!isScrolling) return;

    if (!lastTimestamp) {{
      lastTimestamp = timestamp;
      animFrameId = requestAnimationFrame(scrollLoop);
      return;
    }}

    const deltaMs = timestamp - lastTimestamp;
    lastTimestamp = timestamp;

    const basePixelsPerSec = 50.0;
    const pxToMove = (basePixelsPerSec * scrollSpeed) * (deltaMs / 1000.0);

    scrollAccumulator += pxToMove;

    const maxScroll = (document.documentElement.scrollHeight || document.body.scrollHeight) - window.innerHeight;
    if (scrollAccumulator >= maxScroll) {{
      scrollAccumulator = maxScroll;
      window.scrollTo({{ top: scrollAccumulator, left: 0, behavior: 'instant' }});
      toggleScroll();
      return;
    }}

    window.scrollTo({{
      top: scrollAccumulator,
      left: 0,
      behavior: 'instant'
    }});

    updateProgress();
    animFrameId = requestAnimationFrame(scrollLoop);
  }}

  window.addEventListener('wheel', () => {{
    scrollAccumulator = window.scrollY || window.pageYOffset || 0;
  }}, {{ passive: true }});
  window.addEventListener('touchmove', () => {{
    scrollAccumulator = window.scrollY || window.pageYOffset || 0;
  }}, {{ passive: true }});

  function adjustSpeed(delta) {{
    scrollSpeed = Math.max(0.5, Math.min(8.0, Math.round((scrollSpeed + delta) * 10) / 10));
    const speedEl = document.getElementById('speedVal');
    if (speedEl) {{
      speedEl.innerText = scrollSpeed.toFixed(1) + 'x';
    }}
  }}

  function updateProgress() {{
    const d = document.documentElement;
    const t = window.scrollY || d.scrollTop || document.body.scrollTop;
    const h = d.scrollHeight - d.clientHeight;
    const p = Math.min(100, Math.max(0, (t / h) * 100));
    const pgEl = document.getElementById('pg');
    if (pgEl) pgEl.style.width = p + '%';

    // Update active beat tab & current beat display
    const beats = document.querySelectorAll('.beat');
    beats.forEach((b, idx) => {{
      const r = b.getBoundingClientRect();
      if (r.top <= 250 && r.bottom >= 180) {{
        document.querySelectorAll('.act-tab').forEach(t => t.classList.remove('active'));
        const activeTab = document.getElementById('tab' + (idx + 1));
        if (activeTab) {{
          activeTab.classList.add('active');
          const curBeatName = document.getElementById('curBeatName');
          if (curBeatName) curBeatName.innerText = activeTab.innerText;
        }}
      }}
    }});
  }}

  window.addEventListener('scroll', updateProgress);

  // Smooth scroll for Beat Tabs
  document.querySelectorAll('.act-tab').forEach(tab => {{
    tab.addEventListener('click', (e) => {{
      e.preventDefault();
      const targetId = tab.getAttribute('href');
      const targetEl = document.querySelector(targetId);
      if (targetEl) {{
        const topOffset = targetEl.getBoundingClientRect().top + window.scrollY - 80;
        scrollAccumulator = topOffset;
        window.scrollTo({{ top: topOffset, behavior: 'smooth' }});
      }}
    }});
  }});

  function changeFontSize(delta) {{
    let root = document.documentElement;
    let cur = parseInt(getComputedStyle(root).getPropertyValue('--fs')) || 32;
    let n = Math.max(22, Math.min(50, cur + delta));
    root.style.setProperty('--fs', n + 'px');
  }}

  function toggleVisuals() {{
    document.body.classList.toggle('hide-vc');
    const btn = document.getElementById('tvc');
    if (btn) btn.classList.toggle('on');
  }}

  function toggleGuide() {{
    document.body.classList.toggle('show-guide');
    const btn = document.getElementById('tguide');
    if (btn) btn.classList.toggle('on');
  }}

  // Stopwatch Timer HUD
  let timerInterval = null;
  let timerSeconds = 0;
  let timerRunning = false;

  function toggleTimer() {{
    const btn = document.getElementById('timerBtn');
    if (!timerRunning) {{
      timerRunning = true;
      if (btn) {{
        btn.innerText = 'Pause';
        btn.style.color = '#F59E0B';
      }}
      timerInterval = setInterval(() => {{
        timerSeconds++;
        const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
        const secs = String(timerSeconds % 60).padStart(2, '0');
        const hudEl = document.getElementById('hudTimer');
        if (hudEl) hudEl.innerText = `${{mins}}:${{secs}}`;
      }}, 1000);
    }} else {{
      timerRunning = false;
      if (btn) {{
        btn.innerText = 'Resume';
        btn.style.color = 'inherit';
      }}
      clearInterval(timerInterval);
    }}
  }}

  function resetTimer() {{
    clearInterval(timerInterval);
    timerRunning = false;
    timerSeconds = 0;
    const hudEl = document.getElementById('hudTimer');
    const btn = document.getElementById('timerBtn');
    if (hudEl) hudEl.innerText = '00:00';
    if (btn) {{
      btn.innerText = 'Start';
      btn.style.color = 'inherit';
    }}
  }}

  // Retake Flagger
  const retakes = [];

  function flagRetake() {{
    const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
    const secs = String(timerSeconds % 60).padStart(2, '0');
    const timeStr = `${{mins}}:${{secs}}`;
    
    // Get current beat
    let curBeat = 'Q1';
    const beats = document.querySelectorAll('.beat');
    beats.forEach((b, idx) => {{
      const r = b.getBoundingClientRect();
      if (r.top <= 350 && r.bottom >= 150) {{
        const tab = document.getElementById('tab' + (idx + 1));
        if (tab) curBeat = tab.innerText;
      }}
    }});

    const retakeItem = {{ time: timeStr, beat: curBeat, id: retakes.length + 1 }};
    retakes.push(retakeItem);

    const list = document.getElementById('retake-list');
    const emptyMsg = document.getElementById('emptyMsg');
    if (emptyMsg) emptyMsg.remove();

    const row = document.createElement('div');
    row.className = 'retake-item';
    row.innerHTML = `<span>🚩 Retake #${{retakeItem.id}} (${{retakeItem.beat}})</span><strong>${{retakeItem.time}}</strong>`;
    if (list) list.prepend(row);

    const countEl = document.getElementById('retakeCount');
    if (countEl) countEl.innerText = retakes.length;
  }}

  function toggleRetakeLog() {{
    const log = document.getElementById('retake-log');
    if (log) log.classList.toggle('open');
  }}

  function copyRetakes() {{
    if (retakes.length === 0) {{
      alert('No retakes logged yet.');
      return;
    }}
    const text = retakes.map(r => `Retake #${{r.id}} at ${{r.time}} (${{r.beat}})`).join('\\n');
    navigator.clipboard.writeText(text).then(() => {{
      alert('Copied ' + retakes.length + ' retake markers to clipboard!');
    }});
  }}

  // Global Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    if (e.code === 'Space') {{
      e.preventDefault();
      toggleScroll();
    }} else if (e.key === 't' || e.key === 'T') {{
      toggleTimer();
    }} else if (e.key === 'r' || e.key === 'R') {{
      flagRetake();
    }} else if (e.key === 'v' || e.key === 'V') {{
      toggleVisuals();
    }} else if (e.key === '[' || e.key === '{{') {{
      adjustSpeed(-0.5);
    }} else if (e.key === ']' || e.key === '}}') {{
      adjustSpeed(0.5);
    }}
  }});
</script>

</body>
</html>
"""

    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(deck_template)

    print(f"[SUCCESS] Compiled {len(beat_blocks)} narrative beats into: {OUT_HTML}")

if __name__ == "__main__":
    build_deck()
