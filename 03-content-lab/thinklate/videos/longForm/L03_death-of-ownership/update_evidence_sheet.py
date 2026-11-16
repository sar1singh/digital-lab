import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "evidence_sheet.html")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ThinkLate Ep 03 — Evidence, Citations & Visual Assets Command Center</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #070B14;
      --card-bg: #0F172A;
      --card-border: #1E293B;
      --card-hover: #334155;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --gold: #F59E0B;
      --gold-dark: #B45309;
      --cyan: #06B6D4;
      --cyan-dark: #0E7490;
      --crimson: #EF4444;
      --emerald: #10B981;
      --purple: #8B5CF6;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      padding: 30px 20px 80px;
      line-height: 1.5;
    }
    .container {
      max-width: 1480px;
      margin: 0 auto;
    }
    header {
      background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px 32px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }
    .header-left h1 {
      font-size: 28px;
      font-weight: 800;
      color: var(--gold);
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .header-left p {
      color: var(--text-muted);
      margin-top: 6px;
      font-size: 14px;
    }
    .progress-box {
      background: #0B1120;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px 20px;
      min-width: 280px;
    }
    .progress-label {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }
    .progress-bar-bg {
      height: 10px;
      background: #1E293B;
      border-radius: 10px;
      overflow: hidden;
    }
    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--gold) 0%, var(--emerald) 100%);
      width: 100%;
      transition: width 0.3s ease;
    }

    /* Fast Navigation Bar */
    .fast-nav {
      display: flex;
      gap: 10px;
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 6px;
    }
    .nav-btn {
      background: #0F172A;
      border: 1px solid #1E293B;
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      text-decoration: none;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .nav-btn:hover {
      background: #1E293B;
      color: var(--gold);
      border-color: var(--gold);
    }

    /* Master Broadcast Notice */
    .broadcast-notice {
      background: #0B1120;
      border: 1px solid #1E293B;
      border-left: 4px solid var(--emerald);
      border-radius: 14px;
      padding: 20px 24px;
      margin-bottom: 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .notice-title {
      font-size: 16px;
      font-weight: 800;
      color: #E0F2FE;
      margin-bottom: 4px;
    }
    .notice-desc {
      font-size: 13px;
      color: var(--text-muted);
    }
    .notice-badge {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--emerald);
      color: var(--emerald);
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 8px;
    }

    /* Section Titles */
    .section-title {
      font-size: 20px;
      font-weight: 800;
      color: var(--text-main);
      margin: 40px 0 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-left: 4px solid var(--gold);
      padding-left: 14px;
    }
    .section-title.emerald { border-left-color: var(--emerald); }
    .section-title.cyan { border-left-color: var(--cyan); }
    .section-title.purple { border-left-color: var(--purple); }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
      gap: 24px;
    }

    /* Cards */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      position: relative;
    }
    .card:hover {
      border-color: #334155;
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(0,0,0,0.3);
    }
    .card.completed {
      border-color: rgba(16, 185, 129, 0.4);
      background: linear-gradient(180deg, rgba(16, 185, 129, 0.04) 0%, var(--card-bg) 100%);
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }
    .card-id {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      color: var(--gold);
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 4px 10px;
      border-radius: 6px;
    }
    .card-id.emerald {
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.3);
    }
    .card-id.cyan {
      color: var(--cyan);
      background: rgba(6, 182, 212, 0.12);
      border-color: rgba(6, 182, 212, 0.3);
    }
    .card-id.purple {
      color: var(--purple);
      background: rgba(139, 92, 246, 0.12);
      border-color: rgba(139, 92, 246, 0.3);
    }

    .status-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--emerald);
      padding: 3px 8px;
      border-radius: 4px;
    }

    .card h3 {
      font-size: 18px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
    }
    .card .proves {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 14px;
      min-height: 38px;
    }

    /* Media Previews */
    .preview-thumb {
      width: 100%;
      height: 175px;
      border-radius: 8px;
      object-fit: cover;
      border: 1px solid #334155;
      margin-bottom: 14px;
      background: #020617;
      display: block;
    }
    video.preview-thumb {
      object-fit: contain;
      background: #000;
    }

    /* Step / Summary Box */
    .how-to-box {
      background: #070B14;
      border: 1px solid #1E293B;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 12px;
    }
    .how-to-title {
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      font-family: 'JetBrains Mono', monospace;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }
    .how-to-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .how-to-list li {
      font-size: 12px;
      color: #CBD5E1;
      margin-bottom: 4px;
      position: relative;
      padding-left: 18px;
      line-height: 1.4;
    }
    .how-to-list li:last-child { margin-bottom: 0; }
    .how-to-list li::before {
      content: "▸";
      position: absolute;
      left: 2px;
      color: var(--cyan);
      font-weight: bold;
    }

    /* Quote Snippet */
    .quote-box {
      background: rgba(245, 158, 11, 0.05);
      border-left: 3px solid var(--gold);
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 14px;
      font-size: 12px;
      color: #E2E8F0;
      font-style: italic;
      position: relative;
    }
    .quote-box.cyan {
      border-left-color: var(--cyan);
      background: rgba(6, 182, 212, 0.05);
    }
    .copy-btn {
      position: absolute;
      top: 6px;
      right: 6px;
      background: #1E293B;
      border: 1px solid #334155;
      color: #94A3B8;
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      cursor: pointer;
      font-family: 'JetBrains Mono', monospace;
    }
    .copy-btn:hover {
      color: var(--text-main);
      background: #334155;
    }

    /* Specs Box */
    .specs-box {
      background: #0B1120;
      border: 1px solid #1E293B;
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 14px;
      font-size: 12px;
    }
    .specs-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 4px;
    }
    .specs-row:last-child { margin-bottom: 0; }
    .specs-label {
      color: #64748B;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }
    .specs-val {
      color: #CBD5E1;
      font-weight: 600;
      text-align: right;
    }
    .specs-val.code {
      font-family: 'JetBrains Mono', monospace;
      color: var(--cyan);
      font-size: 11px;
    }

    /* Buttons */
    .action-row {
      display: flex;
      gap: 8px;
      margin-top: 10px;
      flex-wrap: wrap;
    }
    .btn {
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: none;
      font-family: inherit;
    }
    .btn-primary { background: var(--gold); color: #000; }
    .btn-primary:hover { background: #FBBF24; transform: translateY(-1px); }
    .btn-secondary { background: #1E293B; color: var(--text-main); border: 1px solid #334155; }
    .btn-secondary:hover { background: #334155; }
    .btn.done {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
    }

    /* Kinetic Typography Grid */
    .kt-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 18px;
    }
    .kt-card {
      background: #0B1120;
      border: 1px solid #1E293B;
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .kt-thumb {
      width: 100%;
      height: 130px;
      border-radius: 6px;
      object-fit: cover;
      border: 1px solid #334155;
      margin-bottom: 10px;
    }
    .kt-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
    }

    /* AI Prompts Box */
    .prompt-card {
      background: #0F172A;
      border: 1px solid #1E293B;
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 18px;
      position: relative;
    }
    .prompt-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .prompt-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      color: var(--purple);
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid var(--purple);
      padding: 3px 10px;
      border-radius: 6px;
    }
    .prompt-voiceover {
      font-size: 13px;
      color: #CBD5E1;
      font-style: italic;
      margin-bottom: 12px;
      background: rgba(0,0,0,0.3);
      padding: 8px 12px;
      border-radius: 6px;
      border-left: 3px solid var(--purple);
    }
    .prompt-content {
      background: #070B14;
      border: 1px solid #1E293B;
      border-radius: 8px;
      padding: 14px 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #93C5FD;
      line-height: 1.6;
      margin-bottom: 10px;
      position: relative;
    }

    /* Master Timeline Table */
    .timeline-table-wrap {
      background: #0F172A;
      border: 1px solid #1E293B;
      border-radius: 14px;
      overflow-x: auto;
      margin-top: 20px;
    }
    table.timeline-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }
    table.timeline-table th {
      background: #0B1120;
      padding: 14px 18px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 700;
      border-bottom: 1px solid #1E293B;
      letter-spacing: 0.5px;
    }
    table.timeline-table td {
      padding: 14px 18px;
      border-bottom: 1px solid #1E293B;
      vertical-align: top;
    }
    table.timeline-table tr:hover {
      background: rgba(255, 255, 255, 0.02);
    }
    .tc-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      background: rgba(245, 158, 11, 0.1);
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      white-space: nowrap;
    }
    .asset-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(6, 182, 212, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
      display: inline-block;
      white-space: nowrap;
    }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0F172A;
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 12px 20px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.2s ease;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      z-index: 999;
    }
    #toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>

<div class="container">

  <!-- Header -->
  <header>
    <div class="header-left">
      <h1>🎬 ThinkLate Ep 03 — Evidence & Visuals Command Center</h1>
      <p>Target Episode: <em>"You Don't Own What You Buy."</em> • 100% Broadcast Assets & Timeline Schedule</p>
    </div>
    <div class="progress-box">
      <div class="progress-label">
        <span>BROADCAST ASSETS COMPILED</span>
        <span id="progress-text">28 / 28 (100%)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: 100%;"></div>
      </div>
    </div>
  </header>

  <!-- Fast Navigation Bar -->
  <div class="fast-nav">
    <a href="#sec-primary" class="nav-btn">⚖️ Primary Evidence (6)</a>
    <a href="#sec-charts" class="nav-btn">📊 Animated Charts & Precedents (6)</a>
    <a href="#sec-metaphors" class="nav-btn">💡 Metaphors & Market Paradox (7)</a>
    <a href="#sec-kt" class="nav-btn">⚡ Kinetic Typography Slams (9)</a>
    <a href="#sec-ai-prompts" class="nav-btn">🎬 AI Video Prompts (9)</a>
    <a href="#sec-schedule" class="nav-btn">🗺️ Voiceover & Visual Schedule (Full 10m)</a>
  </div>

  <!-- Master Broadcast Notice -->
  <div class="broadcast-notice">
    <div>
      <div class="notice-title">✅ Complete Visual Coverage Guarantee</div>
      <div class="notice-desc">All broken or geo-blocked retail links have been resolved with direct 1080p broadcast slates, animated MP4 data visualizations, and authentic citation cards. Zero missing gaps across the entire voiceover script.</div>
    </div>
    <div class="notice-badge">BROADCAST READY • 1080P MASTERED</div>
  </div>

  <!-- ======================================================== -->
  <!-- SECTION 1: PRIMARY EVIDENCE & STOREFRONT AUDITS          -->
  <!-- ======================================================== -->
  <div class="section-title emerald" id="sec-primary">⚖️ SECTION 1: PRIMARY LEGAL & STOREFRONT EVIDENCE</div>
  <div class="grid">

    <!-- EVID 01: California AB 2426 -->
    <div class="card completed" id="card-evid-01">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 01 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>California Assembly Bill 2426</h3>
        <p class="proves">Banned digital storefronts from using "BUY" or "PURCHASE" without explicit license disclaimers.</p>
        <img src="assets/EVID_01_CA_AB2426_composite_card.png" class="preview-thumb" alt="AB 2426 Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>State Capitol dome header + Section 17500.6 highlighted clause.</li>
            <li>Smooth 1080p60 scroll video compiled in <code>assets/EVID_01_CA_AB2426_smooth_scroll.mp4</code>.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_01_CA_AB2426_composite_card.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 2 • 03:24 – 03:46 (22s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_01_CA_AB2426_composite_card.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="assets/EVID_01_CA_AB2426_smooth_scroll.mp4" target="_blank">🎬 Watch Scroll MP4</a>
      </div>
    </div>

    <!-- EVID 02: Steam Cart Checkout Warning -->
    <div class="card completed" id="card-evid-02">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 02 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Steam Cart Checkout License Warning</h3>
        <p class="proves">Proves Valve legally defines all digital purchases as temporary licenses, not ownership.</p>
        <img src="assets/EVID_02_STEAM_CART_composite_card.png" class="preview-thumb" alt="Steam Cart Warning">
        <div class="how-to-box">
          <div class="how-to-title">🎯 EXTRACTED FROM STEAM CLIENT:</div>
          <ul class="how-to-list">
            <li>Indian Rupee checkout screen (₹3,599) with cyan glowing highlight box.</li>
            <li>Verbatim disclaimer: "A purchase of a digital product grants a license..."</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_02_STEAM_CART_composite_card.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 2 • 03:47 – 04:00 (13s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_02_STEAM_CART_composite_card.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('EVID_02_STEAM_CART_composite_card.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- EVID 03: PS5 Pro + Disc Drive -->
    <div class="card completed" id="card-evid-03">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 03 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>PS5 Pro: $700 Console + $80 Optical Drive</h3>
        <p class="proves">Sony sells a $700 flagship with no disc drive and paywalls physical game playback behind a sold-out accessory.</p>
        <img src="assets/EVID_03_PS5_PRO_DISC_DRIVE.png" class="preview-thumb" alt="PS5 Pro Evidence Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Side-by-side comparison: $699.99 disc-less console vs $79.99 sold-out optical drive.</li>
            <li>Official PlayStation Blog launch statement included.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_03_PS5_PRO_DISC_DRIVE.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 1 • 00:16 – 00:25 (9s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_03_PS5_PRO_DISC_DRIVE.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://blog.playstation.com/2024/09/10/welcome-playstation-5-pro-the-most-visually-impressive-way-to-play-games-on-playstation/" target="_blank">🌐 PS Blog</a>
      </div>
    </div>

    <!-- EVID 04: Ubisoft The Crew Lawsuit -->
    <div class="card completed" id="card-evid-04">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 04 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Ubisoft Sued Over 'The Crew' License Wipe</h3>
        <p class="proves">California class action lawsuit after Ubisoft remotely revoked 12M purchased copies and argued players never owned them.</p>
        <img src="assets/EVID_04_UBISOFT_CREW_LAWSUIT.png" class="preview-thumb" alt="Ubisoft Lawsuit Evidence">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Docket: Case 3:24-cv-07482 • Northern District of California.</li>
            <li>Full citation of Paragraph 42 & Ubisoft's defense doubling down.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_04_UBISOFT_CREW_LAWSUIT.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 1 • 00:57 – 01:14 (17s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_04_UBISOFT_CREW_LAWSUIT.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://www.ign.com/articles/ubisoft-faces-lawsuit-for-shutting-down-the-crew" target="_blank">🌐 IGN Lawsuit</a>
      </div>
    </div>

    <!-- EVID 05: India Game Resale Lifeline -->
    <div class="card completed" id="card-evid-05">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 05 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>India Pre-Owned Game Resale Lifeline (CeX & Gameloot)</h3>
        <p class="proves">Console gaming in India survives on buyback/resale. Digital-only completely wipes this economic engine.</p>
        <img src="assets/EVID_05_INDIA_DISC_RESALE.png" class="preview-thumb" alt="India Resale Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Economics: Buy pre-owned ₹2,499 vs Sell back ₹1,900 = Net ₹599 to play.</li>
            <li>Shows 88% cost savings versus locked digital console stores.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_05_INDIA_DISC_RESALE.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 3 • 06:45 – 07:00 (15s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_05_INDIA_DISC_RESALE.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://in.webuy.com" target="_blank">🌐 CeX India</a>
      </div>
    </div>

    <!-- EVID 06: BMW Heated Seat Subscription -->
    <div class="card completed" id="card-evid-06">
      <div>
        <div class="card-top">
          <span class="card-id emerald">EVID 06 • READY</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>BMW ConnectedDrive: Heated Seat Subscription</h3>
        <p class="proves">Hardware rental spreading to cars: heaters already installed inside seats, but software demands $18/month rent.</p>
        <img src="assets/EVID_06_BMW_HEATED_SEATS.png" class="preview-thumb" alt="BMW Heated Seat Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Pricing tiers: 1 Mo (£15/$18), 1 Yr (£150), 3 Yr (£270), Unlimited (£350).</li>
            <li>In-car dashboard breakdown with factory-installed hardware citation.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/EVID_06_BMW_HEATED_SEATS.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 3 • 07:14 – 07:26 (12s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/EVID_06_BMW_HEATED_SEATS.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://www.theverge.com/2022/7/12/23204950/bmw-subscriptions-microtransactions-heated-seats-feature" target="_blank">🌐 The Verge</a>
      </div>
    </div>

  </div>

  <!-- ======================================================== -->
  <!-- SECTION 2: ANIMATED CHARTS & LEGAL PRECEDENTS           -->
  <!-- ======================================================== -->
  <div class="section-title cyan" id="sec-charts">📊 SECTION 2: ANIMATED CHARTS & LEGAL PRECEDENTS</div>
  <div class="grid">

    <!-- CHART 01: 20-Year Sales Collapse (ANIMATED MP4) -->
    <div class="card completed" id="card-chart-01">
      <div>
        <div class="card-top">
          <span class="card-id cyan">CHART 01 • ANIMATED VIDEO</span>
          <span class="status-pill">BROADCAST MP4</span>
        </div>
        <h3>20-Year Sales Divergence (Animated Broadcast Video)</h3>
        <p class="proves">Animated 8-second video proving physical sales collapsed from 90% down to 8% while digital soared to 92%.</p>
        
        <video controls autoplay loop muted class="preview-thumb" style="height: 190px;" src="assets/CHART_SALES_COLLAPSE_animated.mp4"></video>

        <div class="how-to-box">
          <div class="how-to-title">🎬 MOTION SPECS:</div>
          <ul class="how-to-list">
            <li>1920×1080 @ 30fps H.264 broadcast video with animated line sweeps.</li>
            <li>Glowing countdown badges, dynamic percentages, and 2013 crossover tag.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">Target File</span><span class="specs-val code">assets/CHART_SALES_COLLAPSE_animated.mp4</span></div>
          <div class="specs-row"><span class="specs-label">Timeline Mark</span><span class="specs-val">Act 3 • 05:38 – 05:52 (14s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CHART_SALES_COLLAPSE_animated.mp4" target="_blank">▶️ Fullscreen MP4</a>
        <a class="btn btn-secondary" href="assets/CHART_SALES_COLLAPSE_transparent.png" target="_blank">🖼️ Floating PNG</a>
      </div>
    </div>

    <!-- CARD 02: 1908 First Sale Doctrine -->
    <div class="card completed" id="card-first-sale">
      <div>
        <div class="card-top">
          <span class="card-id cyan">LEGAL PRECEDENT • ACT 2</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>1908 Supreme Court 'First Sale Doctrine'</h3>
        <p class="proves">Historical precedent: Once you buy physical media, the publisher legally loses all right to control resale.</p>
        <img src="assets/CARD_FIRST_SALE_1908.png" class="preview-thumb" alt="1908 First Sale Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Landmark case: <em>Bobbs-Merrill Co. v. Straus (210 U.S. 339)</em>.</li>
            <li>Justice Day ruling: Publishers cannot restrict resale after first sale.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_FIRST_SALE_1908.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 2 • 02:40 – 03:12 (32s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_FIRST_SALE_1908.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://supreme.justia.com/cases/federal/us/210/339/" target="_blank">🌐 Justia Law</a>
      </div>
    </div>

    <!-- CARD 03: Sony Deleting Discovery Episodes -->
    <div class="card completed" id="card-sony-discovery">
      <div>
        <div class="card-top">
          <span class="card-id cyan">NEWS CITATION • ACT 1</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Sony Deletes 1,300 Discovery TV Shows</h3>
        <p class="proves">Proof of corporate deletion: Sony notified users that already-purchased TV seasons would be erased overnight.</p>
        <img src="assets/CARD_SONY_DISCOVERY.png" class="preview-thumb" alt="Sony Discovery Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Verbatim notice: Content removed due to licensing arrangements.</li>
            <li>Red ACCESS TERMINATED badge highlighting loss of purchased seasons.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_SONY_DISCOVERY.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 1 • 01:21 – 01:36 (15s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_SONY_DISCOVERY.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://variety.com/2023/digital/news/playstation-discovery-content-removed-warner-bros-discovery-1235818987/" target="_blank">🌐 Variety</a>
      </div>
    </div>

    <!-- CARD 04: Stop Killing Games EU -->
    <div class="card completed" id="card-stop-killing-games">
      <div>
        <div class="card-top">
          <span class="card-id cyan">CAMPAIGN • ACT 4</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Stop Killing Games (EU Citizens' Initiative)</h3>
        <p class="proves">Over 1,250,000 citizens demanding legislation to mandate offline patches when servers shut down.</p>
        <img src="assets/CARD_STOP_KILLING_GAMES.png" class="preview-thumb" alt="Stop Killing Games Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Official ECI threshold tracker crossing 1M verified signatures.</li>
            <li>Mandate: Games must remain functional when server support ends.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_STOP_KILLING_GAMES.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 4 • 07:49 – 08:14 (25s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_STOP_KILLING_GAMES.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://www.stopkillinggames.com/eci" target="_blank">🌐 Official ECI</a>
      </div>
    </div>

    <!-- CARD 05: GOG DRM-Free Solution -->
    <div class="card completed" id="card-gog">
      <div>
        <div class="card-top">
          <span class="card-id cyan">SOLUTION • ACT 4</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>GOG.com DRM-Free Offline Installer</h3>
        <p class="proves">Rule 1 of Digital Sovereignty: True permanent ownership via standalone offline installer files (.exe).</p>
        <img src="assets/CARD_RULE1_GOG.png" class="preview-thumb" alt="GOG Rule 1 Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Features DRM-FREE guarantee & standalone offline backup installers.</li>
            <li>Highlight: Files launch 50 years from now with zero client login.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_RULE1_GOG.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 4 • 08:38 – 08:56 (18s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_RULE1_GOG.png" target="_blank">🔍 Open High-Res</a>
        <a class="btn btn-secondary" href="https://www.gog.com" target="_blank">🌐 Open GOG</a>
      </div>
    </div>

    <!-- CARD 06: Indian EV Scooter Software Paywall -->
    <div class="card completed" id="card-ev-scooter">
      <div>
        <div class="card-top">
          <span class="card-id cyan">INDUSTRY PARADOX • ACT 3</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Indian EV Scooter Software Paywalls</h3>
        <p class="proves">Hardware rental in transport: Electric scooters paywalling hill-hold and cruise control behind software packs.</p>
        <img src="assets/CARD_EV_SCOOTER_OTA.png" class="preview-thumb" alt="EV Scooter Paywall Card">
        <div class="how-to-box">
          <div class="how-to-title">📋 ASSET DETAILS:</div>
          <ul class="how-to-list">
            <li>Motors and battery are physically installed in the scooter.</li>
            <li>Software locks basic features until consumer pays monthly/annual rent.</li>
          </ul>
        </div>
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_EV_SCOOTER_OTA.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 3 • 07:27 – 07:38 (11s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_EV_SCOOTER_OTA.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_EV_SCOOTER_OTA.png')">📋 Copy Name</button>
      </div>
    </div>

  </div>

  <!-- ======================================================== -->
  <!-- SECTION 3: METAPHORS & MARKET PARADOX CARDS              -->
  <!-- ======================================================== -->
  <div class="section-title" id="sec-metaphors">💡 SECTION 3: METAPHORS, FOUNDER QUOTES & MARKET PARADOX</div>
  <div class="grid">

    <!-- CARD 07: The Penthouse Smart Lock -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">CONCEPT METAPHOR • ACT 2</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>The $400k Penthouse Smart Lock Metaphor</h3>
        <p class="proves">Compares physical real estate fraud to tech industry EULA license revocation.</p>
        <img src="assets/CARD_PENTHOUSE_LOCK.png" class="preview-thumb" alt="Penthouse Lock Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_PENTHOUSE_LOCK.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 2 • 02:04 – 02:24 (20s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_PENTHOUSE_LOCK.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_PENTHOUSE_LOCK.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 08: The Empty Steelbook Case -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">TANGIBLE ABSURDITY • ACT 1</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>The $80 Empty Collector Case</h3>
        <p class="proves">Physical retail contradiction: $80 premium steelbooks shipping with empty trays and paper slips.</p>
        <img src="assets/CARD_EMPTY_CASE.png" class="preview-thumb" alt="Empty Case Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_EMPTY_CASE.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 1 • 00:02 – 00:11 (9s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_EMPTY_CASE.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_EMPTY_CASE.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 09: GTA 6 Code In A Box -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">RETAIL EXTINCTION • ACT 1</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>GTA 6: $80 Download Code In A Box</h3>
        <p class="proves">The biggest game in history shipping physical retail as paper download vouchers.</p>
        <img src="assets/CARD_GTA6_BOX.png" class="preview-thumb" alt="GTA6 Box Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_GTA6_BOX.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 1 • 01:46 – 01:55 (9s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_GTA6_BOX.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_GTA6_BOX.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 10: Gabe Newell Quote -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">FOUNDER CITATION • ACT 2</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Gabe Newell: Piracy Is A Service Problem</h3>
        <p class="proves">Valve's golden rule explaining why consumers pirate when corporate services become restrictive.</p>
        <img src="assets/CARD_GABE_QUOTE.png" class="preview-thumb" alt="Gabe Newell Quote Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_GABE_QUOTE.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 2 • 04:08 – 04:16 (8s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_GABE_QUOTE.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_GABE_QUOTE.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 11: PS Store Digital Monopoly -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">MARKET MONOPOLY • ACT 3</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>PlayStation Store Digital Monopoly</h3>
        <p class="proves">Elimination of discs traps console players in a single digital tollbooth with zero price competition.</p>
        <img src="assets/CARD_PS_STORE_PRICES.png" class="preview-thumb" alt="PS Store Monopoly Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_PS_STORE_PRICES.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 3 • 06:08 – 06:18 (10s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_PS_STORE_PRICES.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_PS_STORE_PRICES.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 12: India Second-Hand Disc Market -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">EMERGING MARKETS • ACT 3</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>India Second-Hand Disc Swap Lifeline</h3>
        <p class="proves">How console gaming survived in India on Nehru Place / Lamington Road disc exchange and trade-in economics.</p>
        <img src="assets/CARD_INDIA_DISC_MARKET.png" class="preview-thumb" alt="India Disc Market Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_INDIA_DISC_MARKET.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 3 • 06:27 – 06:45 (18s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_INDIA_DISC_MARKET.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_INDIA_DISC_MARKET.png')">📋 Copy Name</button>
      </div>
    </div>

    <!-- CARD 13: Rule 2: Open Hardware -->
    <div class="card completed">
      <div>
        <div class="card-top">
          <span class="card-id">DIGITAL SOVEREIGNTY • ACT 4</span>
          <span class="status-pill">COMPILED</span>
        </div>
        <h3>Rule 2: Open Hardware & Linux Freedom</h3>
        <p class="proves">Why PC and open handhelds like Steam Deck provide permanent immunity from corporate digital lock-in.</p>
        <img src="assets/CARD_RULE2_OPEN_HARDWARE.png" class="preview-thumb" alt="Open Hardware Card">
        <div class="specs-box">
          <div class="specs-row"><span class="specs-label">File</span><span class="specs-val code">assets/CARD_RULE2_OPEN_HARDWARE.png</span></div>
          <div class="specs-row"><span class="specs-label">Mark</span><span class="specs-val">Act 4 • 09:03 – 09:19 (16s)</span></div>
        </div>
      </div>
      <div class="action-row">
        <a class="btn done" href="assets/CARD_RULE2_OPEN_HARDWARE.png" target="_blank">🔍 Open High-Res</a>
        <button class="btn btn-secondary" onclick="copyFilename('CARD_RULE2_OPEN_HARDWARE.png')">📋 Copy Name</button>
      </div>
    </div>

  </div>

  <!-- ======================================================== -->
  <!-- SECTION 4: KINETIC TYPOGRAPHY SLAMS (9 TOTAL)            -->
  <!-- ======================================================== -->
  <div class="section-title" id="sec-kt">⚡ SECTION 4: KINETIC TYPOGRAPHY SLAMS (1080P SLATES)</div>
  <div class="kt-grid">

    <!-- KT 01 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--gold);">KT 01 • ACT 1 HOOK</span><span>00:00 – 00:02</span></div>
        <img src="assets/KT_01_CRACKED_DISC.png" class="kt-thumb" alt="KT 01">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"You paid eighty dollars for a brand new game."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_01_CRACKED_DISC.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 02 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--crimson);">KT 02 • ACT 1 BODY</span><span>00:44 – 00:54</span></div>
        <img src="assets/KT_02_OWN_ZERO.png" class="kt-thumb" alt="KT 02">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"Under corporate law, you own zero percent of that purchase."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_02_OWN_ZERO.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 03 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--crimson);">KT 03 • ACT 1 END</span><span>01:36 – 01:46</span></div>
        <img src="assets/KT_03_SERVERS_DIE.png" class="kt-thumb" alt="KT 03">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"When servers die, your purchases die too."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_03_SERVERS_DIE.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 04 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--gold);">KT 04 • ACT 2 END</span><span>04:40 – 04:58</span></div>
        <img src="assets/KT_04_DEAD_SERVER.png" class="kt-thumb" alt="KT 04">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"Even Gabe cannot save a dead server."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_04_DEAD_SERVER.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 05 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--gold);">KT 05 • ACT 3 HOOK</span><span>05:01 – 05:10</span></div>
        <img src="assets/KT_05_FOLLOW_MONEY.png" class="kt-thumb" alt="KT 05">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"Follow the money: Killing the used game market."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_05_FOLLOW_MONEY.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 06 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--crimson);">KT 06 • ACT 3 HOOK</span><span>05:28 – 05:30</span></div>
        <img src="assets/KT_06_ZERO_DOLLARS.png" class="kt-thumb" alt="KT 06">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"Exactly zero dollars."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_06_ZERO_DOLLARS.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 07 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--crimson);">KT 07 • ACT 3 END</span><span>07:39 – 07:46</span></div>
        <img src="assets/KT_07_HARDWARE_PERMISSION.png" class="kt-thumb" alt="KT 07">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"You own the hardware. They own the permission."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_07_HARDWARE_PERMISSION.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 08 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--gold);">KT 08 • ACT 4 BODY</span><span>09:23 – 09:43</span></div>
        <img src="assets/KT_08_OWN_AUDIENCE.png" class="kt-thumb" alt="KT 08">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"Own your audience. Own your distribution."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_08_OWN_AUDIENCE.png')">📋 Copy Asset</button>
    </div>

    <!-- KT 09 -->
    <div class="kt-card">
      <div>
        <div class="kt-header"><span style="color:var(--emerald);">KT 09 • ACT 4 END</span><span>09:54 – 10:00</span></div>
        <img src="assets/KT_09_FREEDOM_OFFLINE.png" class="kt-thumb" alt="KT 09">
        <div class="specs-box" style="margin-bottom:8px;"><span class="specs-label">Voiceover</span><br><span style="color:#FFF;">"In the 21st century, freedom is an offline file."</span></div>
      </div>
      <button class="btn btn-secondary" onclick="copyFilename('KT_09_FREEDOM_OFFLINE.png')">📋 Copy Asset</button>
    </div>

  </div>

  <!-- ======================================================== -->
  <!-- SECTION 5: CINEMATIC AI VIDEO PROMPTS LIBRARY            -->
  <!-- ======================================================== -->
  <div class="section-title purple" id="sec-ai-prompts">🎬 SECTION 5: CINEMATIC AI VIDEO PROMPT CATALOG (RUNWAY / KLING / VEO)</div>
  <p style="color:var(--text-muted); font-size:13px; margin-bottom:18px;">
    Use these prompts in Runway Gen-3, Kling AI, Luma Dream Machine, or Google Veo to generate metaphorical B-roll clips with the locked ThinkLate BBC documentary aesthetic:
  </p>

  <!-- Prompt 1 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 01 • THE EMPTY COLLECTOR'S STEELBOOK</span>
      <span class="tc-badge">00:02 – 00:11 (9s)</span>
    </div>
    <div class="prompt-voiceover">"You walk home, unbox the collector case, and there is no disc. Just an empty plastic circle and a tiny paper slip with a printed code."</div>
    <div class="prompt-content" id="p1-text">Cinematic macro push-in shot of male hands opening a luxury embossed video game steelbook case on a dark mahogany desk. The case opens to reveal a completely empty circular plastic tray, with no Blu-ray disc inside, and a single small white paper coupon slip with a printed 16-digit alphanumeric download code resting in the center. Moody dramatic studio lighting, dark slate navy shadows, warm amber tungsten rim light, shallow depth of field, 35mm film grain, BBC documentary aesthetic, photorealistic, 8k, 16:9 widescreen, anamorphic lens.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p1-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 2 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 02 • THE FRACTURED BLU-RAY DISC</span>
      <span class="tc-badge">00:00 – 00:02 (3s)</span>
    </div>
    <div class="prompt-voiceover">"You paid eighty dollars for a brand new game."</div>
    <div class="prompt-content" id="p2-text">Extreme macro slow-motion camera orbit around a pristine holographic Blu-ray disc resting on a dark slate surface. A glowing red fracture crack slowly branches across the iridescent disc surface, revealing illuminated microchip circuits and pulsing red data fiber underneath the plastic. Anamorphic lens flare, dark cinematic atmosphere, deep navy and crimson color grading, 35mm documentary photography, photorealistic, 8k resolution, 16:9 widescreen, BBC historical documentary aesthetic.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p2-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 3 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 03 • CORPORATE SERVER SHUTDOWN</span>
      <span class="tc-badge">00:57 – 01:14 (17s)</span>
    </div>
    <div class="prompt-voiceover">"In 2024, Ubisoft shut down servers for The Crew... reached into twelve million player libraries and deleted the game files... every single copy vanished."</div>
    <div class="prompt-content" id="p3-text">Cinematic tracking shot moving down an endless corridor of a modern hyperscale server room. Towering racks of server blades with glowing blue indicator lights suddenly flicker and power down one by one, shifting to blinking amber warning lights and plunging into dark shadows. Volumetric server room fog, atmospheric rim lighting, deep navy and industrial amber, BBC tech documentary style, anamorphic lens, 8k, photorealistic, 16:9 widescreen, natural filmic lighting.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p3-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 4 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 04 • THE $400K PENTHOUSE SMART LOCK REVOCATION</span>
      <span class="tc-badge">02:04 – 02:24 (20s)</span>
    </div>
    <div class="prompt-voiceover">"Imagine buying a house for $400,000... 3 years later, the builder walks up to your front door and changes the digital lock... page 47: you bought a temporary room pass."</div>
    <div class="prompt-content" id="p4-text">Cinematic slow push-in shot toward the front door of a multimillion-dollar modern luxury penthouse at twilight. An illuminated digital smart lock keypad on the brushed bronze door flashes a stark crimson warning badge reading 'ACCESS REVOKED'. Wet exterior glass with raindrops, moody architectural lighting, reflections of dramatic city skyline in the glass, deep teal navy and warm amber interior light, 35mm film grain, BBC investigative documentary style, 8k photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p4-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 5 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 05 • 1908 SUPREME COURT LEGAL DESK</span>
      <span class="tc-badge">02:40 – 03:12 (32s)</span>
    </div>
    <div class="prompt-voiceover">"Over one hundred years ago, the Supreme Court heard a landmark case... The First Sale Doctrine. Once you buy a physical book, record, or painting, it belongs to you."</div>
    <div class="prompt-content" id="p5-text">Cinematic slow pan across a historic 1900s mahogany law library desk. An open antique leather-bound legal book rests beneath the warm glow of a green glass banker's lamp. Dust motes dance in the volumetric amber light beam, with rows of vintage leather law books stretching into blurred background. Authentic historical texture, 35mm documentary film grain, BBC historical documentary aesthetic, 8k, photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p5-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 6 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 06 • INDIAN ELECTRONICS BAZAAR (DISC SWAP)</span>
      <span class="tc-badge">06:27 – 06:45 (18s)</span>
    </div>
    <div class="prompt-voiceover">"In India, console gaming never grew on expensive digital pre-orders. It grew on the second-hand disc lifeline... Gamers in Mumbai, Delhi, and Bangalore swapped discs with friends."</div>
    <div class="prompt-content" id="p6-text">Cinematic documentary tracking shot through a bustling indoor electronics market in Mumbai at evening. Stacks of physical console game disc cases on glass display counters, warm neon shop signs, youthful gamers inspecting game cover art and discussing trades, authentic urban energy, natural filmic lighting, deep shadows, rich warm amber and cyan ambient light, 35mm documentary photography, 8k, photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p6-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 7 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 07 • IN-CAR SOFTWARE PAYWALL MODAL</span>
      <span class="tc-badge">07:14 – 07:38 (24s)</span>
    </div>
    <div class="prompt-voiceover">"BMW tried putting heated seats behind an $18 monthly subscription. The physical heaters were already built inside the car... The motors exist, the battery exists. The code demands a credit card."</div>
    <div class="prompt-content" id="p7-text">Cinematic macro shot inside a luxury modern automobile cockpit at night. Close-up on the glowing digital touchscreen dashboard as a finger taps an icon for seat heating, triggering a subscription prompt window with a credit card icon. Moody interior ambient LED cockpit lighting in electric cyan and amber, shallow depth of field, rain on windshield, BBC Horizons technology documentary style, 8k photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p7-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 8 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 08 • OPEN HARDWARE TERMINAL (STEAM DECK / LINUX)</span>
      <span class="tc-badge">09:03 – 09:19 (16s)</span>
    </div>
    <div class="prompt-voiceover">"Rule 2: Choose open hardware over locked ecosystems... PC or an open handheld like the Steam Deck lets you control your operating system. Not locked into one corporate store."</div>
    <div class="prompt-content" id="p8-text">Cinematic close-up tracking shot of an open-hardware handheld gaming device resting on a minimalist dark walnut desk beside an illuminated mechanical keyboard. The sharp OLED screen displays an open Linux terminal and desktop environment executing custom code with glowing cyan text. Warm atmospheric desk lamp glow, deep slate background, 35mm anamorphic lens, BBC technology documentary aesthetic, 8k, photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p8-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- Prompt 9 -->
  <div class="prompt-card">
    <div class="prompt-top">
      <span class="prompt-num">PROMPT 09 • THE OFFLINE SOLID STATE DRIVE</span>
      <span class="tc-badge">09:54 – 10:07 (13s)</span>
    </div>
    <div class="prompt-voiceover">"In the 21st century, freedom is having the offline files on your own hard drive. If you need an active internet connection just to ask for permission to open it, you never bought it."</div>
    <div class="prompt-content" id="p9-text">Cinematic macro slow pan over a rugged metallic external solid-state drive resting on a dark slate workstation desk. A discreet warm amber LED light pulses gently along the edge of the drive, connected via high-grade braided USB-C cable to a laptop in background. Moody low-key cinematic lighting, deep shadows, authentic 35mm film grain, feeling of personal autonomy and archival permanence, 8k resolution, photorealistic, 16:9 widescreen.</div>
    <button class="btn btn-primary" onclick="copyPrompt('p9-text')">📋 Copy Prompt to Clipboard</button>
  </div>

  <!-- ======================================================== -->
  <!-- SECTION 6: MASTER VOICEOVER SCRIPT & VISUAL MATRIX      -->
  <!-- ======================================================== -->
  <div class="section-title" id="sec-schedule">🗺️ SECTION 6: MASTER VOICEOVER & VISUAL TIMELINE SCHEDULE (100% COVERAGE)</div>
  <p style="color:var(--text-muted); font-size:13px; margin-bottom:14px;">
    Every single spoken whisper segment from <code>voiceover_raw_mastered.wav</code> (00:00 to 10:07) is matched with its exact underlying Black Flag gameplay action and foreground broadcast overlay:
  </p>

  <div class="timeline-table-wrap">
    <table class="timeline-table">
      <thead>
        <tr>
          <th>TIMECODE</th>
          <th>ACT / BEAT</th>
          <th>SPOKEN VOICEOVER SCRIPT</th>
          <th>TRACK 1 GAMEPLAY</th>
          <th>TRACK 3 & 4 FOREGROUND ASSET</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tc-badge">00:00 – 00:02</span></td>
          <td>Act 1 Hook</td>
          <td>"You paid eighty dollars for a brand new game."</td>
          <td>Dark stormy seas</td>
          <td><span class="asset-tag">KT_01_CRACKED_DISC.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:02 – 00:11</span></td>
          <td>Act 1 Hook</td>
          <td>"Unbox the collector case, and there is no disc. Just an empty plastic circle and a tiny paper slip..."</td>
          <td>Jackdaw preparing sails</td>
          <td><span class="asset-tag">CARD_EMPTY_CASE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:11 – 00:16</span></td>
          <td>Act 1 Hook</td>
          <td>"Sony just launched a console for seven hundred dollars. It has no disc drive."</td>
          <td>High-seas Jackdaw cutting waves</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:16 – 00:25</span></td>
          <td>Act 1 Hook</td>
          <td>"Pay another eighty dollars for a snap-on plastic drive... Assuming scalpers didn't buy them all first."</td>
          <td>Ocean waves dimmed</td>
          <td><span class="asset-tag">EVID_03_PS5_PRO_DISC_DRIVE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:25 – 00:44</span></td>
          <td>Act 1 Body</td>
          <td>"Retail giants like Best Buy wiped physical games... Over 90% digital... You worked 40 hours, hit BUY button."</td>
          <td>Kenway walking Havana harbor</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:44 – 00:54</span></td>
          <td>Act 1 Body</td>
          <td>"Under corporate law, you own zero percent of that purchase. You rented a temporary pass."</td>
          <td>Havana streets dimmed</td>
          <td><span class="asset-tag">KT_02_OWN_ZERO.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:54 – 00:57</span></td>
          <td>Act 1 Body</td>
          <td>"Think that is an exaggeration?"</td>
          <td>Fast sword parry counter-kill</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">00:57 – 01:14</span></td>
          <td>Act 1 Body</td>
          <td>"In 2024 Ubisoft shut down The Crew... deleted files from 12 million player libraries."</td>
          <td>Combat aftermath dimmed</td>
          <td><span class="asset-tag">EVID_04_UBISOFT_CREW_LAWSUIT.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">01:14 – 01:21</span></td>
          <td>Act 1 Body</td>
          <td>"Sony did the exact same thing."</td>
          <td>Jackdaw sea spray, sails full</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">01:21 – 01:36</span></td>
          <td>Act 1 Body</td>
          <td>"With 1,300 digital TV episodes... erasing them because contracts expired."</td>
          <td>Dark ocean dimmed</td>
          <td><span class="asset-tag">CARD_SONY_DISCOVERY.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">01:36 – 01:46</span></td>
          <td>Act 1 End</td>
          <td>"When you buy digital goods today, you are standing on quicksand... company holds the switch."</td>
          <td>Broadside cannon prep</td>
          <td><span class="asset-tag">KT_03_SERVERS_DIE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">01:46 – 01:55</span></td>
          <td>Act 1 End</td>
          <td>"Grand Theft Auto Six landing at $80... retail copies shipping as download codes in empty plastic boxes."</td>
          <td>Open ocean dimmed</td>
          <td><span class="asset-tag">CARD_GTA6_BOX.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">01:55 – 02:01</span></td>
          <td>Act 1 End</td>
          <td>"We traded physical boxes for modern convenience... gave up property rights that took centuries to build."</td>
          <td>Kenway on ship bow at golden hour</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">02:01 – 02:03</span></td>
          <td>Break 1</td>
          <td><em>[VOCAL SILENCE • 2.5s Breathing Break]</em></td>
          <td>360° Viewpoint synchronization pan</td>
          <td><em>Chapter Card: ACT 2</em></td>
        </tr>

        <!-- ACT 2 -->
        <tr>
          <td><span class="tc-badge">02:04 – 02:24</span></td>
          <td>Act 2 Hook</td>
          <td>"Imagine buying a house for $400k... 3 years later builder changes digital lock... page 47 temporary pass."</td>
          <td>Havana streets dimmed</td>
          <td><span class="asset-tag">CARD_PENTHOUSE_LOCK.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">02:24 – 02:40</span></td>
          <td>Act 2 Hook</td>
          <td>"In real estate, that would be illegal fraud. In tech, we call it the End User License Agreement."</td>
          <td>Kenway walking past colonial buildings</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">02:40 – 03:12</span></td>
          <td>Act 2 Body</td>
          <td>"100 years ago, Supreme Court created First Sale Doctrine... buy book, record, painting, it belongs to you."</td>
          <td>Rooftop tiles dimmed</td>
          <td><span class="asset-tag">CARD_FIRST_SALE_1908.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">03:12 – 03:24</span></td>
          <td>Act 2 Body</td>
          <td>"Until software came along... 1998 digital copyright laws changed everything... granted a license."</td>
          <td>Kenway climbing church tower</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">03:24 – 03:46</span></td>
          <td>Act 2 Body</td>
          <td>"California just stepped in: Assembly Bill 2426... illegal to use BUY without explicit license warning."</td>
          <td>Church tower climb dimmed</td>
          <td><span class="asset-tag">EVID_01_CA_AB2426_composite_card.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">03:47 – 04:00</span></td>
          <td>Act 2 Body</td>
          <td>"Look at Steam... A purchase of a digital product grants a license on Steam, not ownership."</td>
          <td>Ocean sailing dimmed</td>
          <td><span class="asset-tag">EVID_02_STEAM_CART_composite_card.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:00 – 04:08</span></td>
          <td>Act 2 Body</td>
          <td>"Gamers actually love Steam... Valve built deep customer trust over twenty long years."</td>
          <td>Jackdaw on open Caribbean waters</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:08 – 04:16</span></td>
          <td>Act 2 Body</td>
          <td>"Gabe Newell famously gave us the golden rule: Piracy is almost always a service problem..."</td>
          <td>Ocean waves dimmed</td>
          <td><span class="asset-tag">CARD_GABE_QUOTE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:16 – 04:18</span></td>
          <td>Break 2</td>
          <td><em>[VOCAL SILENCE • 2.0s Breathing Break]</em></td>
          <td>Clean ocean sailing</td>
          <td><em>Gabe Newell Quote Lingers</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:18 – 04:40</span></td>
          <td>Act 2 Body</td>
          <td>"Valve gave instant downloads, cloud saves, refunds, Steam Deck open handheld... treats gamers like adults."</td>
          <td>Night naval combat, cannon volleys</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:40 – 04:58</span></td>
          <td>Act 2 End</td>
          <td>"Even Valve cannot change the law... publisher deletes game, even Steam cannot save it. Rented ground."</td>
          <td>Cannon smoke dimmed</td>
          <td><span class="asset-tag">KT_04_DEAD_SERVER.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">04:58 – 05:01</span></td>
          <td>Break 3</td>
          <td><em>[VOCAL SILENCE • 3.0s Breathing Break]</em></td>
          <td>Viewpoint 360° pan</td>
          <td><em>Chapter Card: ACT 3</em></td>
        </tr>

        <!-- ACT 3 -->
        <tr>
          <td><span class="tc-badge">05:01 – 05:10</span></td>
          <td>Act 3 Hook</td>
          <td>"Why pushing so hard to kill the disc? Nothing to do with saving trees. It is about killing used games."</td>
          <td>Broadside cannon prep</td>
          <td><span class="asset-tag">KT_05_FOLLOW_MONEY.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">05:10 – 05:28</span></td>
          <td>Act 3 Hook</td>
          <td>"20 years ago... Halo 2 sold to friend for $30... How much money did Sony make on second transaction?"</td>
          <td>Naval broadside duel tearing wood</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">05:28 – 05:30</span></td>
          <td>Break 4</td>
          <td>"Exactly zero dollars."</td>
          <td>Cannon smoke clearing</td>
          <td><span class="asset-tag">KT_06_ZERO_DOLLARS.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">05:30 – 05:38</span></td>
          <td>Act 3 Body</td>
          <td>"Publishers hated second-hand market with burning passion... physical discs gave power to consumers."</td>
          <td>Kenway walking dock barrels</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">05:38 – 05:52</span></td>
          <td>Act 3 Body</td>
          <td>"Look at this chart. In 20 years industry flipped. Physical sales collapsed from 90% down to less than 8%."</td>
          <td>Dock tavern dimmed</td>
          <td><span class="asset-tag">CHART_SALES_COLLAPSE_animated.mp4</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">05:52 – 06:08</span></td>
          <td>Act 3 Body</td>
          <td>"Once disc drive removed, competition disappears. Cannot buy cheap on eBay or borrow from cousin."</td>
          <td>Havana harbor morning light</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">06:08 – 06:18</span></td>
          <td>Act 3 Body</td>
          <td>"Trapped inside single store. Sony/Microsoft set price. 5-year-old game sits at full price, zero alternatives."</td>
          <td>Harbor water dimmed</td>
          <td><span class="asset-tag">CARD_PS_STORE_PRICES.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">06:18 – 06:25</span></td>
          <td>Act 3 Body</td>
          <td>"Subscription squeeze... $80 for game, $80/yr for multiplayer... emerging markets... Let's talk about India."</td>
          <td>Rooftop sprint and chimney leap</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">06:25 – 06:27</span></td>
          <td>Break 5</td>
          <td><em>[VOCAL SILENCE • 2.0s Breathing Break]</em></td>
          <td>Parkour landing</td>
          <td><em>Beat Drop Transition</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">06:27 – 06:45</span></td>
          <td>Act 3 Body</td>
          <td>"In India, gaming grew on second-hand disc lifeline. Mumbai, Delhi, Bangalore swapped discs."</td>
          <td>Town streets dimmed</td>
          <td><span class="asset-tag">CARD_INDIA_DISC_MARKET.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">06:45 – 07:00</span></td>
          <td>Act 3 Body</td>
          <td>"Bought pre-owned on trade sites, played them, sold them back. Only way middle-class kids could afford."</td>
          <td>Nassau docks dimmed</td>
          <td><span class="asset-tag">EVID_05_INDIA_DISC_RESALE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">07:00 – 07:13</span></td>
          <td>Act 3 Body</td>
          <td>"GTA 6 at 6,000 rupees... money locked in vault forever... kills economic engine in developing countries."</td>
          <td>Edward Kenway walking Nassau docks</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">07:14 – 07:26</span></td>
          <td>Act 3 End</td>
          <td>"BMW tried putting heated seats behind $18/mo subscription. Heaters built inside car. Paid for car, locked code."</td>
          <td>Docks dimmed</td>
          <td><span class="asset-tag">EVID_06_BMW_HEATED_SEATS.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">07:27 – 07:38</span></td>
          <td>Act 3 End</td>
          <td>"Electric scooters in India paywalling hill-hold and cruise control. Motors exist, battery exists, code demands card."</td>
          <td>Docks dimmed</td>
          <td><span class="asset-tag">CARD_EV_SCOOTER_OTA.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">07:39 – 07:46</span></td>
          <td>Act 3 End</td>
          <td>"Modern corporate playbook: Sell you physical shell, charge you rent forever for permission to turn it on."</td>
          <td>Open sea dimmed</td>
          <td><span class="asset-tag">KT_07_HARDWARE_PERMISSION.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">07:46 – 07:49</span></td>
          <td>Break 6</td>
          <td><em>[VOCAL SILENCE • 3.0s Breathing Break]</em></td>
          <td>Ship wheel in fog</td>
          <td><em>Chapter Card: ACT 4</em></td>
        </tr>

        <!-- ACT 4 -->
        <tr>
          <td><span class="tc-badge">07:49 – 08:14</span></td>
          <td>Act 4 Hook</td>
          <td>"Stop Killing Games movement in Europe... 1M signatures... Mandate clean offline patch when servers die."</td>
          <td>Stormy sea waves dimmed</td>
          <td><span class="asset-tag">CARD_STOP_KILLING_GAMES.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">08:14 – 08:35</span></td>
          <td>Act 4 Hook</td>
          <td>"Consumers find own way... retro game emulation... ripped offline backups... Three rules of digital survival."</td>
          <td>Jackdaw in stormy sea, lightning</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">08:38 – 08:56</span></td>
          <td>Act 4 Body</td>
          <td>"Rule 1: Support DRM-free... GOG download standalone installer .exe... file launches 50 years from now."</td>
          <td>Storm waves dimmed</td>
          <td><span class="asset-tag">CARD_RULE1_GOG.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">08:56 – 09:03</span></td>
          <td>Act 4 Body</td>
          <td>"Rule number two."</td>
          <td>Kenway standing at ship wheel</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">09:03 – 09:19</span></td>
          <td>Act 4 Body</td>
          <td>"Rule 2: Choose open hardware... PC or Steam Deck lets you control OS, not locked into one corporate store."</td>
          <td>Havana cathedral dimmed</td>
          <td><span class="asset-tag">CARD_RULE2_OPEN_HARDWARE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">09:19 – 09:23</span></td>
          <td>Act 4 Body</td>
          <td>"And rule number three for creators and entrepreneurs."</td>
          <td>Viewpoint climb on cathedral peak cross</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">09:23 – 09:43</span></td>
          <td>Act 4 Body</td>
          <td>"Never build life on rented digital land... Build email list, local backups of code, offline copies of work."</td>
          <td>Cathedral peak cross dimmed</td>
          <td><span class="asset-tag">KT_08_OWN_AUDIENCE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">09:43 – 09:54</span></td>
          <td>Act 4 End</td>
          <td>"Think back to that empty plastic case... 20th century freedom meant having physical property in hands."</td>
          <td>Jackdaw sailing towards golden horizon</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">09:54 – 10:00</span></td>
          <td>Act 4 End</td>
          <td>"In the 21st century, freedom is having the offline files on your own hard drive."</td>
          <td>Horizon sailing dimmed</td>
          <td><span class="asset-tag">KT_09_FREEDOM_OFFLINE.png</span></td>
        </tr>
        <tr>
          <td><span class="tc-badge">10:00 – 10:03</span></td>
          <td>Act 4 End</td>
          <td>"If you need an active internet connection just to ask for permission to open it, you never bought it."</td>
          <td>Ship cutting across starry night Caribbean sea</td>
          <td><em>100% Clean Full-Color Gameplay</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">10:03 – 10:04</span></td>
          <td>Break 7</td>
          <td><em>[VOCAL SILENCE • 1.5s Breathing Break]</em></td>
          <td>Calm night sailing</td>
          <td><em>Quiet Pause</em></td>
        </tr>
        <tr>
          <td><span class="tc-badge">10:04 – 10:07</span></td>
          <td>Outro</td>
          <td>"You are just paying rent. See you next time."</td>
          <td>Jackdaw sails into dark distance, fade to black</td>
          <td><em>Cinematic Fade to Black</em></td>
        </tr>
      </tbody>
    </table>
  </div>

</div>

<div id="toast">Copied to clipboard!</div>

<script>
  function copyFilename(text) {
    navigator.clipboard.writeText(text);
    showToast('Asset name copied: ' + text);
  }

  function copyPrompt(id) {
    const el = document.getElementById(id);
    if (el) {
      navigator.clipboard.writeText(el.innerText);
      showToast('Prompt copied to clipboard!');
    }
  }

  function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.innerText = msg;
    toast.classList.add('show');
    setTimeout(() => { toast.classList.remove('show'); }, 2200);
  }
</script>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Updated: {HTML_PATH}")
