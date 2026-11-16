/**
 * Prestige 2D Vector Thumbnail Templates for ThinkLate
 * Rule 15 Infographics Show 2.0 / Kurzgesagt Style
 */

export const SVG_CONCEPT_A = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&amp;family=JetBrains+Mono:wght@700;800&amp;display=swap');
      .title-text {
        font-family: 'Montserrat', 'Impact', 'Arial Black', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -1px;
      }
      .mono-text {
        font-family: 'JetBrains Mono', 'Courier New', monospace;
        font-weight: 800;
      }
    </style>
    
    <radialGradient id="bgGradA" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#141E33"/>
      <stop offset="60%" stop-color="#0B101D"/>
      <stop offset="100%" stop-color="#04060B"/>
    </radialGradient>

    <radialGradient id="lampGlow" cx="20%" cy="45%" r="40%">
      <stop offset="0%" stop-color="#FFAA00" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#FF5500" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="crimsonGlow" cx="80%" cy="65%" r="45%">
      <stop offset="0%" stop-color="#FF2A4B" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#990018" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <filter id="shadowHeavy" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#000000" flood-opacity="0.95"/>
    </filter>

    <filter id="shadowReceipt" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="12" dy="24" stdDeviation="24" flood-color="#000000" flood-opacity="0.9"/>
    </filter>

    <filter id="neonRedGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="neonCyanGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="1920" height="1080" fill="url(#bgGradA)"/>
  <rect width="1920" height="1080" fill="url(#lampGlow)"/>
  <rect width="1920" height="1080" fill="url(#crimsonGlow)"/>

  <polygon points="0,760 1920,760 1920,1080 0,1080" fill="#070A12"/>
  <line x1="0" y1="760" x2="1920" y2="760" stroke="#1E293B" stroke-width="6"/>
  <line x1="150" y1="760" x2="0" y2="1080" stroke="#131B2E" stroke-width="3"/>
  <line x1="450" y1="760" x2="300" y2="1080" stroke="#131B2E" stroke-width="3"/>
  <line x1="800" y1="760" x2="720" y2="1080" stroke="#131B2E" stroke-width="3"/>
  <line x1="1120" y1="760" x2="1200" y2="1080" stroke="#131B2E" stroke-width="3"/>
  <line x1="1470" y1="760" x2="1620" y2="1080" stroke="#131B2E" stroke-width="3"/>
  <line x1="1770" y1="760" x2="1920" y2="980" stroke="#131B2E" stroke-width="3"/>

  <path d="M 60 480 Q 240 440 420 480 L 420 760 L 60 760 Z" fill="#151A2E" stroke="#000000" stroke-width="5"/>
  <rect x="90" y="520" width="130" height="80" rx="12" fill="#E2E8F0" opacity="0.3" stroke="#000000" stroke-width="4"/>
  <rect x="250" y="520" width="130" height="80" rx="12" fill="#E2E8F0" opacity="0.3" stroke="#000000" stroke-width="4"/>
  <polygon points="120,440 180,440 195,500 105,500" fill="#FBBF24" stroke="#000000" stroke-width="4"/>
  <rect x="145" y="500" width="10" height="80" fill="#475569" stroke="#000000" stroke-width="3"/>
  <ellipse cx="150" cy="580" rx="25" ry="8" fill="#1E293B" stroke="#000000" stroke-width="4"/>

  <g transform="translate(1500, 640)" filter="url(#shadowHeavy)">
    <line x1="-30" y1="-180" x2="20" y2="120" stroke="#D97706" stroke-width="12" stroke-linecap="round"/>
    <path d="M 10 100 L 45 130 L -5 130 Z" fill="#B45309" stroke="#000000" stroke-width="4"/>
    <polygon points="10,20 110,20 95,95 25,95" fill="#FACC15" stroke="#000000" stroke-width="6"/>
    <path d="M 15 25 Q 60 -15 105 25" fill="none" stroke="#475569" stroke-width="5"/>
    <circle cx="45" cy="20" r="14" fill="#E0F2FE" stroke="#000000" stroke-width="3"/>
    <circle cx="70" cy="18" r="16" fill="#E0F2FE" stroke="#000000" stroke-width="3"/>
    <path d="M 115 40 Q 155 10 185 45 Q 210 90 170 100 L 115 100 Z" fill="#0F172A" stroke="#000000" stroke-width="5"/>
    <path d="M 150 15 L 160 30 L 140 30 Z" fill="#EF4444" stroke="#000000" stroke-width="3"/>
  </g>

  <g id="hero-receipt" transform="translate(940, 260) rotate(5)" filter="url(#shadowReceipt)">
    <path d="M 0 40 L 20 20 L 40 40 L 60 20 L 80 40 L 100 20 L 120 40 L 140 20 L 160 40 L 180 20 L 200 40 L 220 20 L 240 40 L 260 20 L 280 40 L 300 20 L 320 40 L 340 20 L 360 40 L 380 20 L 400 40 L 420 20 L 440 40 L 460 20 L 480 40 L 500 20 L 520 40 L 540 20 L 560 40 L 560 760 L 0 760 Z" fill="#FAFAFA" stroke="#000000" stroke-width="8" stroke-linejoin="round"/>
    <line x1="35" y1="95" x2="525" y2="95" stroke="#CBD5E1" stroke-width="3" stroke-dasharray="8 6"/>
    <text x="280" y="80" text-anchor="middle" class="mono-text" font-size="24" fill="#0F172A" letter-spacing="2">★ VACATION RENTAL INVOICE ★</text>
    <text x="50" y="130" class="mono-text" font-size="16" fill="#64748B">GUEST: D. MILLER (2 NIGHTS)</text>
    <text x="400" y="130" class="mono-text" font-size="16" fill="#64748B">CODE: #8821-X</text>
    <line x1="35" y1="150" x2="525" y2="150" stroke="#000000" stroke-width="4"/>
    <text x="50" y="195" class="mono-text" font-size="20" fill="#1E293B">NIGHTLY STAY (2X $80.00)</text>
    <text x="440" y="195" class="mono-text" font-size="20" fill="#1E293B" font-weight="900">$160.00</text>
    <text x="50" y="240" class="mono-text" font-size="20" fill="#1E293B">PLATFORM SERVICE FEE</text>
    <text x="450" y="240" class="mono-text" font-size="20" fill="#1E293B" font-weight="900">$42.50</text>
    <text x="50" y="285" class="mono-text" font-size="20" fill="#1E293B">LOCAL TOURISM TAX (14%)</text>
    <text x="450" y="285" class="mono-text" font-size="20" fill="#1E293B" font-weight="900">$28.30</text>
    <line x1="35" y1="315" x2="525" y2="315" stroke="#E2E8F0" stroke-width="3"/>
    <rect x="35" y="335" width="490" height="90" rx="8" fill="#FEF08A" stroke="#000000" stroke-width="4"/>
    <text x="50" y="388" class="title-text" font-size="34" fill="#DC2626">CLEANING FEE:</text>
    <text x="350" y="392" class="title-text" font-size="52" fill="#DC2626">$300</text>
    <ellipse cx="420" cy="385" rx="105" ry="52" fill="none" stroke="#FF1E40" stroke-width="9" stroke-linecap="round" stroke-dasharray="520 20" transform="rotate(-6 420 385)" filter="url(#neonRedGlow)"/>
    <path d="M 520 440 Q 480 430 455 415" fill="none" stroke="#FF1E40" stroke-width="8" stroke-linecap="round" filter="url(#neonRedGlow)"/>
    <polygon points="445,410 465,410 458,425" fill="#FF1E40"/>
    <line x1="35" y1="450" x2="525" y2="450" stroke="#000000" stroke-width="4"/>
    <text x="50" y="485" class="mono-text" font-size="18" fill="#B91C1C" font-weight="900">MANDATORY CHECKOUT CHORES:</text>
    <text x="50" y="525" class="mono-text" font-size="17" fill="#0F172A">☒ STRIP BEDS &amp; WASH ALL LINENS</text>
    <text x="50" y="560" class="mono-text" font-size="17" fill="#0F172A">☒ MOW FRONT &amp; BACK YARD</text>
    <text x="50" y="595" class="mono-text" font-size="17" fill="#0F172A">☒ TAKE TRASH 3 MILES TO DUMP</text>
    <text x="50" y="630" class="mono-text" font-size="17" fill="#0F172A">☒ WASH &amp; POLISH ALL WINDOWS</text>
    <g transform="translate(180, 520) rotate(-14)">
      <rect x="-20" y="-35" width="360" height="70" rx="8" fill="rgba(239, 68, 68, 0.12)" stroke="#EF4444" stroke-width="7" stroke-dasharray="320 12"/>
      <text x="160" y="14" text-anchor="middle" class="title-text" font-size="34" fill="#EF4444" letter-spacing="4">UNPAID CHORES</text>
    </g>
  </g>

  <g id="hero-character" filter="url(#shadowHeavy)">
    <path d="M 460 760 L 520 620 L 680 580 L 860 620 L 920 760 L 820 1080 L 480 1080 Z" fill="#EF4444" stroke="#000000" stroke-width="8"/>
    <path d="M 540 680 Q 580 640 610 690 Q 570 720 540 680 Z" fill="#F87171" stroke="#000000" stroke-width="4"/>
    <path d="M 720 690 Q 760 650 790 700 Q 750 730 720 690 Z" fill="#F87171" stroke="#000000" stroke-width="4"/>
    <polygon points="630,580 680,680 730,580" fill="#FEF2F2" stroke="#000000" stroke-width="6"/>
    <polygon points="610,580 660,670 680,640" fill="#FFFFFF" stroke="#000000" stroke-width="5"/>
    <polygon points="750,580 700,670 680,640" fill="#FFFFFF" stroke="#000000" stroke-width="5"/>
    <path d="M 510 650 Q 620 720 760 680 L 780 740 Q 620 800 480 730 Z" fill="#EF4444" stroke="#000000" stroke-width="7"/>
    <g transform="translate(760, 660)">
      <path d="M -20 20 L 30 10 L 25 60 L -25 50 Z" fill="#FDBA74" stroke="#000000" stroke-width="6"/>
      <circle cx="28" cy="15" r="14" fill="#FED7AA" stroke="#000000" stroke-width="5"/>
      <circle cx="34" cy="35" r="14" fill="#FED7AA" stroke="#000000" stroke-width="5"/>
      <circle cx="28" cy="55" r="14" fill="#FED7AA" stroke="#000000" stroke-width="5"/>
      <ellipse cx="12" cy="20" rx="12" ry="18" fill="#FDBA74" stroke="#000000" stroke-width="5"/>
    </g>
    <polygon points="630,500 730,500 745,600 615,600" fill="#FDBA74" stroke="#000000" stroke-width="7"/>
    <polygon points="630,500 730,500 680,560" fill="#EA580C" opacity="0.45"/>
    <path d="M 570 360 C 570 240, 790 240, 790 360 C 790 480, 750 530, 680 540 C 610 530, 570 480, 570 360 Z" fill="#FED7AA" stroke="#000000" stroke-width="8"/>
    <path d="M 570 360 C 545 360, 545 420, 570 420 Z" fill="#FDBA74" stroke="#000000" stroke-width="6"/>
    <path d="M 790 360 C 815 360, 815 420, 790 420 Z" fill="#FDBA74" stroke="#000000" stroke-width="6"/>
    <path d="M 550 340 C 550 200, 810 180, 810 320 L 815 370 L 785 340 L 775 280 L 730 240 L 690 270 L 640 230 L 600 270 L 565 310 Z" fill="#18181B" stroke="#000000" stroke-width="8"/>
    <ellipse cx="635" cy="365" rx="42" ry="54" fill="#FFFFFF" stroke="#000000" stroke-width="7"/>
    <ellipse cx="725" cy="365" rx="42" ry="54" fill="#FFFFFF" stroke="#000000" stroke-width="7"/>
    <g transform="translate(10, 8)">
      <ellipse cx="638" cy="368" rx="24" ry="30" fill="#09090B"/>
      <circle cx="645" cy="358" r="8" fill="#FFFFFF"/>
      <circle cx="632" cy="378" r="4" fill="#FFFFFF"/>
      <ellipse cx="728" cy="368" rx="24" ry="30" fill="#09090B"/>
      <circle cx="735" cy="358" r="8" fill="#FFFFFF"/>
      <circle cx="722" cy="378" r="4" fill="#FFFFFF"/>
    </g>
    <path d="M 585 305 Q 635 270 670 300" fill="none" stroke="#000000" stroke-width="9" stroke-linecap="round"/>
    <path d="M 775 305 Q 725 270 690 300" fill="none" stroke="#000000" stroke-width="9" stroke-linecap="round"/>
    <path d="M 675 365 L 685 410 L 665 415" fill="none" stroke="#000000" stroke-width="6" stroke-linecap="round"/>
    <g transform="translate(680, 470)">
      <path d="M -55 -15 Q 0 10 55 -15 Q 45 55 0 60 Q -45 55 -55 -15 Z" fill="#7F1D1D" stroke="#000000" stroke-width="7"/>
      <path d="M -42 -12 L 42 -12 L 35 5 L -35 5 Z" fill="#FFFFFF" stroke="#000000" stroke-width="4"/>
      <path d="M -30 40 Q 0 20 30 40 Q 0 60 -30 40 Z" fill="#F43F5E" stroke="#000000" stroke-width="4"/>
    </g>
    <g filter="url(#neonCyanGlow)">
      <path d="M 540 310 Q 520 330 535 345 Q 550 345 545 325 Z" fill="#00F0FF" stroke="#000000" stroke-width="3"/>
      <circle cx="510" cy="305" r="8" fill="#00F0FF" stroke="#000000" stroke-width="3"/>
      <path d="M 810 320 Q 830 340 815 355 Q 800 355 805 335 Z" fill="#00F0FF" stroke="#000000" stroke-width="3"/>
      <circle cx="835" cy="310" r="7" fill="#00F0FF" stroke="#000000" stroke-width="3"/>
    </g>
    <path d="M 555 350 L 550 330 C 550 240, 620 200, 670 195" fill="none" stroke="#00F0FF" stroke-width="12" stroke-linecap="round" opacity="0.9" filter="url(#neonCyanGlow)"/>
    <path d="M 465 760 L 520 625 L 560 600" fill="none" stroke="#00F0FF" stroke-width="14" stroke-linecap="round" opacity="0.9" filter="url(#neonCyanGlow)"/>
    <path d="M 780 250 C 810 290 815 340 805 390" fill="none" stroke="#FF2A4B" stroke-width="12" stroke-linecap="round" opacity="0.95" filter="url(#neonRedGlow)"/>
  </g>

  <g transform="translate(100, 780)" filter="url(#shadowHeavy)">
    <rect x="0" y="0" width="380" height="150" rx="16" fill="#0F172A" stroke="#10B981" stroke-width="6"/>
    <rect x="0" y="0" width="380" height="42" rx="10" fill="#10B981"/>
    <text x="190" y="28" text-anchor="middle" class="title-text" font-size="18" fill="#042F2E" letter-spacing="2">HOTEL COMPARISON</text>
    <text x="30" y="105" class="title-text" font-size="54" fill="#34D399">$0.00</text>
    <text x="210" y="85" class="mono-text" font-size="16" fill="#FFFFFF" font-weight="900">CLEANING FEE</text>
    <text x="210" y="112" class="mono-text" font-size="15" fill="#94A3B8">ZERO CHORES</text>
    <text x="210" y="132" class="mono-text" font-size="14" fill="#10B981">MAID INCLUDED</text>
  </g>

  <g transform="translate(960, 45)" filter="url(#shadowHeavy)">
    <rect x="-170" y="0" width="340" height="40" rx="8" fill="#E2FF00" stroke="#000000" stroke-width="4"/>
    <text x="0" y="27" text-anchor="middle" class="title-text" font-size="20" fill="#000000" letter-spacing="3">VACATION EXPOSÉ</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="122" fill="#000000" stroke="#000000" stroke-width="26" stroke-linejoin="round">THE $300 CHORE</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="122" fill="#FFFFFF" stroke="#000000" stroke-width="6" stroke-linejoin="round">THE $300 CHORE</text>
  </g>

  <rect x="0" y="0" width="1920" height="1080" fill="none" stroke="#E2FF00" stroke-width="8" opacity="0.85"/>
</svg>`;

export const SVG_CONCEPT_B = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&amp;family=JetBrains+Mono:wght@700;800&amp;display=swap');
      .title-text {
        font-family: 'Montserrat', 'Impact', 'Arial Black', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -1px;
      }
      .mono-text {
        font-family: 'JetBrains Mono', 'Courier New', monospace;
        font-weight: 800;
      }
    </style>

    <radialGradient id="bgSkyB" cx="70%" cy="30%" r="85%">
      <stop offset="0%" stop-color="#2D1B69"/>
      <stop offset="40%" stop-color="#1E163B"/>
      <stop offset="70%" stop-color="#0E1220"/>
      <stop offset="100%" stop-color="#03050A"/>
    </radialGradient>

    <radialGradient id="hazardGlow" cx="65%" cy="55%" r="60%">
      <stop offset="0%" stop-color="#FF2A4B" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#B91C1C" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="arrowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FF6B8B"/>
      <stop offset="50%" stop-color="#FF1E40"/>
      <stop offset="100%" stop-color="#BE123C"/>
    </linearGradient>

    <linearGradient id="arrowSideGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9F1239"/>
      <stop offset="100%" stop-color="#4C0519"/>
    </linearGradient>

    <filter id="shadowHeavyB" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#000000" flood-opacity="0.95"/>
    </filter>

    <filter id="neonRedGlowB" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="stampDistress" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
  </defs>

  <rect width="1920" height="1080" fill="url(#bgSkyB)"/>
  <rect width="1920" height="1080" fill="url(#hazardGlow)"/>

  <g fill="#0D1527" opacity="0.9">
    <rect x="680" y="290" width="130" height="510"/>
    <rect x="740" y="240" width="20" height="50"/>
    <rect x="850" y="360" width="100" height="440"/>
    <rect x="1560" y="270" width="150" height="530"/>
    <rect x="1630" y="210" width="15" height="60"/>
    <rect x="1750" y="340" width="120" height="460"/>
  </g>

  <polygon points="0,800 1920,800 1920,1080 0,1080" fill="#070B14"/>
  <line x1="0" y1="800" x2="1920" y2="800" stroke="#334155" stroke-width="6"/>
  <ellipse cx="1250" cy="840" rx="380" ry="25" fill="#FF2A4B" opacity="0.25"/>

  <g id="hero-building" filter="url(#shadowHeavyB)">
    <rect x="850" y="240" width="760" height="600" fill="#243048" stroke="#000000" stroke-width="8"/>
    <rect x="820" y="215" width="820" height="30" fill="#3B4B68" stroke="#000000" stroke-width="6"/>
    <rect x="840" y="195" width="780" height="22" fill="#4B5E82" stroke="#000000" stroke-width="5"/>

    <g transform="translate(1080, 140)">
      <rect x="-140" y="0" width="280" height="55" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="4"/>
      <text x="0" y="36" text-anchor="middle" class="mono-text" font-size="20" fill="#38BDF8" letter-spacing="3">RENTAL CONDOS</text>
      <line x1="-135" y1="5" x2="135" y2="50" stroke="#FF1E40" stroke-width="8" stroke-linecap="round"/>
      <line x1="135" y1="5" x2="-135" y2="50" stroke="#FF1E40" stroke-width="8" stroke-linecap="round"/>
    </g>

    <rect x="890" y="280" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1035" y="280" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1180" y="280" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1325" y="280" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1470" y="280" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="890" y="420" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1035" y="420" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1180" y="420" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1325" y="420" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1470" y="420" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="890" y="560" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1035" y="560" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1180" y="560" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="1325" y="560" width="105" height="110" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1470" y="560" width="105" height="110" fill="#FEF08A" stroke="#000000" stroke-width="6"/>
    <rect x="890" y="700" width="160" height="140" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <rect x="1150" y="700" width="180" height="140" fill="#38BDF8" opacity="0.35" stroke="#000000" stroke-width="6"/>
    <rect x="1430" y="700" width="160" height="140" fill="#0F172A" stroke="#000000" stroke-width="6"/>

    <g stroke="#FF1E40" stroke-width="7" stroke-linecap="round">
      <line x1="1040" y1="285" x2="1135" y2="385"/>
      <line x1="1135" y1="285" x2="1040" y2="385"/>
      <line x1="1330" y1="285" x2="1425" y2="385"/>
      <line x1="1425" y1="285" x2="1330" y2="385"/>
      <line x1="895" y1="425" x2="990" y2="525"/>
      <line x1="990" y1="425" x2="895" y2="525"/>
    </g>

    <g transform="translate(1360, 200) rotate(16)" filter="url(#shadowHeavyB)">
      <polygon points="50,0 140,0 140,460 250,460 90,660 50,660 50,0" fill="url(#arrowSideGrad)" stroke="#000000" stroke-width="8"/>
      <polygon points="0,0 90,0 90,460 200,460 45,660 -110,460 0,460" fill="url(#arrowGrad)" stroke="#000000" stroke-width="8"/>
      <line x1="0" y1="12" x2="80" y2="12" stroke="#FFFFFF" stroke-width="8"/>
      <text x="45" y="250" text-anchor="middle" class="title-text" font-size="56" fill="#FFFFFF" stroke="#000000" stroke-width="7" transform="rotate(90 45 250)">-$100B</text>
    </g>

    <g transform="translate(1190, 410) rotate(-12)" filter="url(#stampDistress)">
      <rect x="-320" y="-85" width="640" height="170" rx="16" fill="#FFFFFF" stroke="#000000" stroke-width="8"/>
      <rect x="-310" y="-75" width="620" height="150" rx="12" fill="#FFE4E6" stroke="#FF1E40" stroke-width="12" stroke-dasharray="580 18"/>
      <text x="0" y="24" text-anchor="middle" class="title-text" font-size="82" fill="#FF1E40" stroke="#000000" stroke-width="6" letter-spacing="4">BANNED BY LAW</text>
      <text x="0" y="55" text-anchor="middle" class="mono-text" font-size="22" fill="#000000" font-weight="900" letter-spacing="4">NYC • BARCELONA • FLORENCE</text>
    </g>

    <g transform="translate(800, 820)" filter="url(#shadowHeavyB)">
      <polygon points="0,0 860,0 860,50 0,50" fill="#FACC15" stroke="#000000" stroke-width="6"/>
      <rect x="150" y="10" width="560" height="30" fill="#000000"/>
      <text x="430" y="32" text-anchor="middle" class="mono-text" font-size="16" fill="#FACC15" letter-spacing="2">POLICE LINE: SHORT-TERM RENTALS SHUT DOWN</text>
    </g>
  </g>

  <g id="panic-character" transform="translate(380, 480)" filter="url(#shadowHeavyB)">
    <path d="M -220 540 L -180 200 L 0 150 L 180 200 L 220 540 Z" fill="#1E293B" stroke="#000000" stroke-width="8"/>
    <polygon points="-120,200 0,380 0,150" fill="#334155" stroke="#000000" stroke-width="6"/>
    <polygon points="120,200 0,380 0,150" fill="#334155" stroke="#000000" stroke-width="6"/>
    <polygon points="-60,180 0,280 60,180" fill="#F8FAFC" stroke="#000000" stroke-width="5"/>
    <polygon points="-15,240 15,240 25,440 0,470 -25,440" fill="#EF4444" stroke="#000000" stroke-width="5"/>
    <polygon points="-45,70 45,70 55,180 -55,180" fill="#FDBA74" stroke="#000000" stroke-width="7"/>
    <path d="M -95 -70 C -95 -200, 95 -200, 95 -70 C 95 60, 60 110, 0 120 C -60 110, -95 60, -95 -70 Z" fill="#FED7AA" stroke="#000000" stroke-width="8"/>
    <path d="M -115 -80 C -120 -230, 120 -230, 115 -80 L 125 -30 L 95 -50 L 85 -110 L 40 -160 L 0 -120 L -40 -170 L -80 -120 L -115 -60 Z" fill="#1E1B4B" stroke="#000000" stroke-width="8"/>
    <ellipse cx="-45" cy="-65" rx="42" ry="54" fill="#FFFFFF" stroke="#000000" stroke-width="7"/>
    <ellipse cx="45" cy="-65" rx="42" ry="54" fill="#FFFFFF" stroke="#000000" stroke-width="7"/>
    <g transform="translate(16, 2)">
      <ellipse cx="-45" cy="-65" rx="16" ry="20" fill="#09090B"/>
      <circle cx="-42" cy="-70" r="5" fill="#FFFFFF"/>
      <ellipse cx="45" cy="-65" rx="16" ry="20" fill="#09090B"/>
      <circle cx="48" cy="-70" r="5" fill="#FFFFFF"/>
    </g>
    <path d="M -85 -125 Q -40 -160 -10 -130" fill="none" stroke="#000000" stroke-width="9" stroke-linecap="round"/>
    <path d="M 85 -125 Q 40 -160 10 -130" fill="none" stroke="#000000" stroke-width="9" stroke-linecap="round"/>
    <g transform="translate(0, 45)">
      <path d="M -45 -10 Q 0 -25 45 -10 Q 40 55 0 60 Q -40 55 -45 -10 Z" fill="#7F1D1D" stroke="#000000" stroke-width="7"/>
      <path d="M -35 -8 L 35 -8 L 28 8 L -28 8 Z" fill="#FFFFFF" stroke="#000000" stroke-width="4"/>
    </g>
    <g transform="translate(-110, -80)">
      <circle cx="0" cy="0" r="22" fill="#FED7AA" stroke="#000000" stroke-width="6"/>
      <path d="M -10 -15 L -10 -40 L 10 -40 L 10 -15" fill="#FED7AA" stroke="#000000" stroke-width="5"/>
    </g>
    <g transform="translate(110, -80)">
      <circle cx="0" cy="0" r="22" fill="#FED7AA" stroke="#000000" stroke-width="6"/>
      <path d="M 10 -15 L 10 -40 L -10 -40 L -10 -15" fill="#FED7AA" stroke="#000000" stroke-width="5"/>
    </g>
    <path d="M -95 -160 C -125 -100 -125 0 -115 80 L -180 210 L -220 540" fill="none" stroke="#FF2A4B" stroke-width="16" stroke-linecap="round" opacity="0.95" filter="url(#neonRedGlowB)"/>
  </g>

  <g transform="translate(960, 45)" filter="url(#shadowHeavyB)">
    <rect x="-160" y="0" width="320" height="40" rx="8" fill="#FF2A4B" stroke="#000000" stroke-width="4"/>
    <text x="0" y="27" text-anchor="middle" class="title-text" font-size="20" fill="#FFFFFF" letter-spacing="3">GLOBAL CRACKDOWN</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="124" fill="#000000" stroke="#000000" stroke-width="26" stroke-linejoin="round">CITIES BAN IT</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="124" fill="#FFFFFF" stroke="#000000" stroke-width="6" stroke-linejoin="round">CITIES BAN IT</text>
  </g>

  <rect x="0" y="0" width="1920" height="1080" fill="none" stroke="#FF2A4B" stroke-width="8" opacity="0.9"/>
</svg>`;

export const SVG_CONCEPT_C = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&amp;family=JetBrains+Mono:wght@700;800&amp;display=swap');
      .title-text {
        font-family: 'Montserrat', 'Impact', 'Arial Black', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -1px;
      }
      .mono-text {
        font-family: 'JetBrains Mono', 'Courier New', monospace;
        font-weight: 800;
      }
    </style>

    <radialGradient id="bgNoirC" cx="75%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#141E33"/>
      <stop offset="45%" stop-color="#080D1A"/>
      <stop offset="100%" stop-color="#020306"/>
    </radialGradient>

    <linearGradient id="laserBeamGrad" x1="100%" y1="50%" x2="0%" y2="50%">
      <stop offset="0%" stop-color="#FF2A4B" stop-opacity="0.85"/>
      <stop offset="40%" stop-color="#FF1E40" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#990018" stop-opacity="0.05"/>
    </linearGradient>

    <radialGradient id="lensGlass" cx="35%" cy="35%" r="70%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.9"/>
      <stop offset="35%" stop-color="#7000FF" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#FF0055" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0.95"/>
    </radialGradient>

    <filter id="shadowHeavyC" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000000" flood-opacity="0.95"/>
    </filter>

    <filter id="neonRedGlowC" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="laserGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="1920" height="1080" fill="url(#bgNoirC)"/>
  <polygon points="0,780 1920,780 1920,1080 0,1080" fill="#080C16"/>
  <line x1="0" y1="780" x2="1920" y2="780" stroke="#1E293B" stroke-width="6"/>

  <polygon points="1280,510 0,180 0,950 1280,530" fill="url(#laserBeamGrad)" filter="url(#laserGlow)"/>

  <g stroke="#FF2A4B" stroke-width="2" opacity="0.6">
    <line x1="1280" y1="520" x2="150" y2="350"/>
    <line x1="1280" y1="520" x2="150" y2="520"/>
    <circle cx="480" cy="520" r="180" fill="none" stroke="#FF2A4B" stroke-width="3" stroke-dasharray="24 16"/>
    <circle cx="480" cy="520" r="6" fill="#FF2A4B"/>
  </g>

  <g transform="translate(340, 310)" filter="url(#neonRedGlowC)">
    <rect x="0" y="0" width="280" height="60" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#FF2A4B" stroke-width="3"/>
    <circle cx="25" cy="30" r="10" fill="#FF2A4B"/>
    <text x="50" y="28" class="mono-text" font-size="16" fill="#FFFFFF">TARGET: GUEST IN BED</text>
    <text x="50" y="48" class="mono-text" font-size="14" fill="#FF2A4B">AUDIO CAPTURE: 100%</text>
  </g>

  <g transform="translate(420, 480)" filter="url(#shadowHeavyC)">
    <polygon points="-120,240 180,240 160,300 -140,300" fill="#0B101D" stroke="#000000" stroke-width="5"/>
    <path d="M -50 180 L -30 60 L 50 60 L 70 180 Z" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <circle cx="10" cy="0" r="45" fill="#0F172A" stroke="#000000" stroke-width="6"/>
    <ellipse cx="20" cy="-5" rx="14" ry="18" fill="#FFFFFF" stroke="#000000" stroke-width="4"/>
    <circle cx="24" cy="-5" r="7" fill="#000000"/>
    <path d="M 30 -40 C 55 -20, 55 20, 35 40" fill="none" stroke="#FF2A4B" stroke-width="8" stroke-linecap="round" filter="url(#neonRedGlowC)"/>
  </g>

  <g id="hero-clock" transform="translate(800, 260)" filter="url(#shadowHeavyC)">
    <rect x="0" y="0" width="1020" height="520" rx="28" fill="#0A0E17" stroke="#000000" stroke-width="10"/>
    <rect x="18" y="18" width="984" height="484" rx="20" fill="#030712" stroke="#1E293B" stroke-width="6"/>
    <rect x="36" y="36" width="948" height="448" rx="14" fill="#02040A" stroke="#000000" stroke-width="6"/>

    <g transform="translate(80, 110)" fill="#FF1E40" filter="url(#neonRedGlowC)">
      <polygon points="15,0 85,0 70,20 30,20"/>
      <polygon points="0,15 20,30 20,110 0,125"/>
      <polygon points="100,15 100,125 80,110 80,30"/>
      <polygon points="0,145 20,160 20,240 0,255"/>
      <polygon points="100,145 100,255 80,240 80,160"/>
      <polygon points="15,270 85,270 70,250 30,250"/>
    </g>
    <g transform="translate(240, 110)" fill="#FF1E40" filter="url(#neonRedGlowC)">
      <polygon points="15,0 85,0 70,20 30,20"/>
      <polygon points="100,15 100,125 80,110 80,30"/>
      <polygon points="15,135 85,135 70,145 30,145"/>
      <polygon points="0,145 20,160 20,240 0,255"/>
      <polygon points="15,270 85,270 70,250 30,250"/>
    </g>

    <g transform="translate(480, 250)" filter="url(#shadowHeavyC)">
      <circle cx="0" cy="0" r="140" fill="#0F172A" stroke="#000000" stroke-width="10"/>
      <circle cx="0" cy="0" r="115" fill="#020617" stroke="#000000" stroke-width="8"/>
      <circle cx="0" cy="0" r="95" fill="url(#lensGlass)" stroke="#000000" stroke-width="6"/>
      <circle cx="0" cy="0" r="55" fill="#090D16" stroke="#000000" stroke-width="5"/>
      <circle cx="0" cy="0" r="22" fill="#FF1E40" filter="url(#neonRedGlowC)"/>
      <circle cx="6" cy="-6" r="8" fill="#FFFFFF"/>
      <text x="0" y="-100" text-anchor="middle" class="mono-text" font-size="12" fill="#94A3B8">F/1.4 4K</text>
      <text x="0" y="112" text-anchor="middle" class="mono-text" font-size="12" fill="#FF2A4B">SPY CAM</text>
      <circle cx="0" cy="0" r="148" fill="none" stroke="#FF2A4B" stroke-width="4" stroke-dasharray="16 12" filter="url(#neonRedGlowC)"/>
    </g>

    <g transform="translate(680, 110)" fill="#FF1E40" filter="url(#neonRedGlowC)">
      <polygon points="0,15 20,30 20,110 0,125"/>
      <polygon points="100,15 100,125 80,110 80,30"/>
      <polygon points="15,135 85,135 70,145 30,145"/>
      <polygon points="100,145 100,255 80,240 80,160"/>
    </g>
    <g transform="translate(840, 110)" fill="#FF1E40" filter="url(#neonRedGlowC)">
      <polygon points="15,0 85,0 70,20 30,20"/>
      <polygon points="100,15 100,255 80,240 80,30"/>
    </g>
    <g transform="translate(80, 60)" filter="url(#neonRedGlowC)">
      <circle cx="15" cy="15" r="9" fill="#FF1E40"/>
      <text x="35" y="22" class="mono-text" font-size="18" fill="#FF1E40" font-weight="900" letter-spacing="2">● REC 1080P</text>
    </g>
    <text x="890" y="85" class="mono-text" font-size="24" fill="#FF1E40" font-weight="900">AM</text>
  </g>

  <g id="forensic-clipboard" transform="translate(140, 520) rotate(-6)" filter="url(#shadowHeavyC)">
    <rect x="0" y="0" width="460" height="520" rx="14" fill="#334155" stroke="#000000" stroke-width="8"/>
    <rect x="130" y="-20" width="200" height="45" rx="6" fill="#94A3B8" stroke="#000000" stroke-width="6"/>
    <rect x="25" y="35" width="410" height="460" fill="#F8FAFC" stroke="#000000" stroke-width="5"/>
    <text x="230" y="75" text-anchor="middle" class="title-text" font-size="18" fill="#0F172A" letter-spacing="1">POLICE EVIDENCE REPORT</text>
    <line x1="50" y1="90" x2="410" y2="90" stroke="#000000" stroke-width="3"/>
    <rect x="45" y="175" width="370" height="70" rx="6" fill="#FEF08A" stroke="#000000" stroke-width="3"/>
    <text x="60" y="210" class="title-text" font-size="20" fill="#B91C1C">HIDDEN CAMERAS FOUND: 4</text>
    <text x="60" y="235" class="mono-text" font-size="14" fill="#0F172A">HARDWARE: ALARM CLOCK / SHOWER</text>
    <text x="50" y="280" class="mono-text" font-size="14" fill="#1E293B">☒ BEDROOM CLOCK (WIRED TO CLOUD)</text>
    <text x="50" y="310" class="mono-text" font-size="14" fill="#1E293B">☒ SMOKE DETECTOR (PINHOLE LENS)</text>
    <g transform="translate(180, 390) rotate(-10)">
      <rect x="-120" y="-30" width="240" height="60" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#EF4444" stroke-width="6"/>
      <text x="0" y="10" text-anchor="middle" class="title-text" font-size="26" fill="#EF4444" letter-spacing="2">SEIZED EVIDENCE</text>
    </g>
  </g>

  <g transform="translate(960, 45)" filter="url(#shadowHeavyC)">
    <rect x="-160" y="0" width="320" height="40" rx="8" fill="#FFAA00" stroke="#000000" stroke-width="4"/>
    <text x="0" y="27" text-anchor="middle" class="title-text" font-size="20" fill="#000000" letter-spacing="3">PRIVACY SCANDAL</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="124" fill="#000000" stroke="#000000" stroke-width="26" stroke-linejoin="round">THEY'RE WATCHING</text>
    <text x="0" y="135" text-anchor="middle" class="title-text" font-size="124" fill="#FFFFFF" stroke="#000000" stroke-width="6" stroke-linejoin="round">THEY'RE WATCHING</text>
  </g>

  <rect x="0" y="0" width="1920" height="1080" fill="none" stroke="#FFAA00" stroke-width="8" opacity="0.9"/>
</svg>`;
