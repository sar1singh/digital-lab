# ThinkLate Video 05 — Master DaVinci Resolve Timeline & SFX Editing Guide

> **Episode:** *"The $2 Trillion AI IPO Scam?"* (`05_the-ai-ipo-bubble`)  
> **Channel:** ThinkLate (`@wethinklate`) | **Target Runtime:** 5m 34s  
> **Aesthetic Standard:** Cinematic Graphic Noir / Bloomberg Originals / Vox Borders  
> **Master Spoken Audio:** `assets/audio/voiceover_mastered.mp3` (5m 34s | 93 Whisper Segments)  
> **Governing Standards:** Rule 7 (Timeline Integrity), Rule 10 (Gameplay Canvas), Rule 13 (Blindfold Test).  

---

## 🛠️ 1. Project Setup & 4-Track Layout Protocol

### DaVinci Resolve Track Architecture:

```
┌────────────────────────────────────────────────────────────────────────┐
│ VIDEO TRACK 4 (V4): Kinetic Typography Slams (DaVinci Text+) & Badges  │
├────────────────────────────────────────────────────────────────────────┤
│ VIDEO TRACK 3 (V3): Full-Screen Graphic Plates & Animated Chart MP4    │
├────────────────────────────────────────────────────────────────────────┤
│ VIDEO TRACK 2 (V2): Scoped Blur Adjustment Clip (Gaussian Blur 0.15)    │
│                     *ACTIVE ONLY under V4 text slams over gameplay*    │
├────────────────────────────────────────────────────────────────────────┤
│ VIDEO TRACK 1 (V1): Continuous 1080p60 Gameplay Canvas (Zoom 1.15x)    │
└────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ AUDIO TRACK 1 (A1): Master Dialogue Voiceover [FADER: -5.0 dB]         │
├────────────────────────────────────────────────────────────────────────┤
│ AUDIO TRACK 2 (A2): Cinematic Ambient BGM Bed [FADER: -23.0 dB]        │
├────────────────────────────────────────────────────────────────────────┤
│ AUDIO TRACK 3 (A3): Sub-Bass Impact Booms & Slams [FADER: -12.0 dB]    │
├────────────────────────────────────────────────────────────────────────┤
│ AUDIO TRACK 4 (A4): Diegetic Foley & UI Clicks [FADER: -16.0 dB]       │
└────────────────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **Fairlight Headroom Rule:** Set **Track A1 Dialogue Fader strictly to `-5.0 dB`**. When Guy's voiceover sums with A2 BGM and A3 Sub-Bass impacts, the master bus delivers a broadcast-compliant **-16.0 to -18.0 LUFS** with zero clipping.

---

## 🎬 2. Master Spoken Timeline Schedule (Whisper Ground Truth)

| # | Timecode (MM:SS) | V1 Canvas | V2 Blur | V3 Full-Screen Asset | V4 DaVinci Text+ (Exact On-Screen Copy) | Audio Track & Exact SFX Cue |
| :-: | :--- | :--- | :---: | :--- | :--- | :--- |
| **01** | `00:00 – 00:09` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `SUMMER 2026`<br>Headline: `ANTHROPIC S-1 REGISTRATION` | **A4:** Wall Street opening bell (-16 dB) at `00:01` |
| **02** | `00:10 – 00:20` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `NASDAQ: ANT`<br>Headline: `$2,000,000,000,000 VALUATION`<br>Subtext: `TWO TRILLION WITH A "T"` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `00:15` |
| **03** | `00:20 – 00:31` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE IDEALISTIC NON-PROFIT`<br>Subtext: `AI WAS TOO DANGEROUS TO COMMERCIALIZE` | **A2:** Ambient BGM bed enters at -23 dB |
| **04** | `00:32 – 00:42` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `SELLING SHARES TO YOUR DENTIST`<br>Subtext: `BEFORE THE POWER BILL ARRIVES` | **A4:** Soft digital terminal blip (-16 dB) |
| **05** | `00:43 – 00:52` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_01_sec_filing_terminal.jpg` *(3% Push)* | Headline: `PAGE 48: CONSOLIDATED STATEMENT`<br>Badge: `H1 2026 REVENUE: $16.3 BILLION` | **A4:** Paper rustle / terminal key click (-18 dB) |
| **06** | `00:53 – 01:07` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `NET LOSS`<br>Headline: `-$80,700,000,000`<br>Subtext: `EIGHTY BILLION LOST TYPING TEXT` | **A3:** Heavy impact boom (-12 dB) at `00:56`<br>**A2:** Dead-air drop (Silence 1.5s) at `01:00` |
| **07** | `01:08 – 01:19` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `FOLLOW THE MONEY`<br>Subtext: `IT IS NOT A BUSINESS. IT IS A CAROUSEL.` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `01:16` |
| **08** | `01:20 – 01:30` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_02_boardroom_carousel.jpg` *(3% Push)* | Headline: `THE $10B CHECK`<br>Body: `AMAZON ➔ ANTHROPIC • MICROSOFT ➔ OPENAI` | **A4:** Server fan whirls up into high whine (-16 dB) |
| **09** | `01:31 – 01:40` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `WIRED BACK IN 72 HOURS`<br>Headline: `RENTING AWS & AZURE SERVER RACKS` | **A4:** Data blip (-16 dB) at `01:35` |
| **10** | `01:41 – 01:50` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `WIRED TO SANTA CLARA`<br>Headline: `BUYING HUNDREDS OF THOUSANDS OF GPUS` | **A4:** Cash register chime (-16 dB) at `01:46` |
| **11** | `01:51 – 02:05` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `RECORD EARNINGS • RECORD VALUATIONS`<br>Subtext: `THE EXACT SAME $10B IN A CIRCLE` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `01:58` |
| **12** | `02:05 – 02:20` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `WHERE IS THE PAYING CUSTOMER?`<br>Subtext: `A $20/MO COVER LETTER BOT CANNOT PAY FOR A REACTOR` | **A2:** Dead-air drop (Silence 2.0s) at `02:14` |
| **13** | `02:21 – 02:35` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_03_sequoia_math_chart.jpg` *(3% Push)* | Headline: `SEQUOIA CAPITAL: DAVID CAHN`<br>Subtext: `THE $600 BILLION QUESTION` | **A4:** Calculator mechanical click (-16 dB) |
| **14** | `02:36 – 02:50` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `CHIP OBSOLESCENCE`<br>Headline: `GPUS BURN OUT IN 4–5 YEARS`<br>Subtext: `$300B CAPEX REQUIRES $600B/YEAR REVENUE` | **A4:** High-voltage transformer hum (-18 dB) |
| **15** | `02:51 – 03:08` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `REALITY CHECK`<br>Headline: `ENTIRE GLOBAL SOFTWARE MARKET = $350B`<br>Subtext: `AI MUST REPLACE ALL SOFTWARE TWICE OVER` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `02:58`<br>**A2:** Dead-air drop (Silence 2.0s) at `03:02` |
| **16** | `03:09 – 03:22` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THAT IS NOT A FORECAST`<br>Subtext: `THAT IS MATHEMATICAL FICTION` | **A3:** Sub-bass hit (-12 dB) at `03:15` |
| **17** | `03:23 – 03:40` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_04_telecom_1999_split.jpg` *(3% Push)* | Headline: `1999: TELECOM MANIA`<br>Body: `WORLDCOM • GLOBAL CROSSING • MILLIONS OF MILES OF FIBER` | **A4:** Vintage typewriter clatter & switchboard crackle (-16 dB) |
| **18** | `03:41 – 03:55` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `THE CRASH`<br>Headline: `90% OF STARTUPS WENT BANKRUPT`<br>Subtext: `TRILLIONS IN PAPER WEALTH EVAPORATED` | **A4:** Distant thunder rumble (-18 dB) |
| **19** | `03:56 – 04:15` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE GLASS FIBER STAYED IN THE GROUND`<br>Subtext: `BOUGHT FOR PENNIES ON THE DOLLAR` | **A3:** Low sub-bass drone (-14 dB) |
| **20** | `04:16 – 04:30` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `THE REBIRTH`<br>Headline: `BANKRUPT FIBER POWERED NETFLIX, YOUTUBE & AWS` | **A4:** Data blip (-16 dB) at `04:22` |
| **21** | `04:31 – 04:45` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE BUBBLE POPPED`<br>Subtext: `THE PLUMBING STAYED` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `04:38` |
| **22** | `04:46 – 05:05` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_01_sec_filing_terminal.jpg` *(3% Push)* | Headline: `TRAINING COSTS ARE COMPOUNDING`<br>Subtext: `INFERENCE MARGINS ARE COLLAPSING TO ZERO` | **A4:** Heavy safe door closes with heavy metallic thud (-14 dB) |
| **23** | `05:06 – 05:22` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `THE SURVIVOR PLAYBOOK`<br>Headline: `FOLLOW THE PHYSICAL ASSETS`<br>Body: `POWER GRIDS • NUCLEAR PLANTS • PROPRIETARY LOCAL DATA` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `05:14` |
| **24** | `05:23 – 05:34` | Gameplay (Zoom 1.15x) | **OFF** | — *(Gameplay fade to black)* | Quote: `"WHEN THE CAROUSEL STOPS..."`<br>Quote: `"MAKE SURE YOU ARE NOT HOLDING THE BILL"` | **A4:** Final trading bell chime fades into silence (-16 dB) |

---

## 3. DaVinci Resolve Master Export Settings
* **Timeline Resolution:** `2560 x 1440 QHD` (forces YouTube to assign the premium **`av01` / `vp09`** codec).
* **Frame Rate:** `60 fps` (matches source gameplay canvas).
* **Audio Format:** `Linear PCM 24-bit` or `AAC 320 kbps`.
* **Master Bus Limiter:** True Peak ceiling at **`-1.0 dBFS`**.

