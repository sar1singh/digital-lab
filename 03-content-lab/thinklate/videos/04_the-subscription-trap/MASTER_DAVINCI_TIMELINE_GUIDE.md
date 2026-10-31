# ThinkLate Video 04 — Master DaVinci Resolve Timeline & SFX Editing Guide

> **Episode:** *"Why You Will Never Own Anything Again"* (`04_the-subscription-trap`)  
> **Channel:** ThinkLate (`@wethinklate`) | **Target Runtime:** 8m 09s  
> **Aesthetic Standard:** Cinematic Graphic Noir / Bloomberg Originals / Vox Borders  
> **Master Spoken Audio:** `assets/audio/voiceover_mastered.mp3` (8m 09s | 68 Whisper Segments)  
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
> **The Fairlight -5.0 dB Headroom Rule:**
> Leave the Master Bus at `0.0 dB`, but set the **A1 Dialogue Fader strictly to `-5.0 dB`**. When Guy's master audio sums with A2 BGM and A3 Sub-Bass impacts, the master output will sit at a broadcast-clean **-16.0 to -18.5 LUFS** with zero red-meter clipping.

---

## 🎬 2. Master Spoken Timeline Schedule (Whisper Ground Truth)

Every timecode below is derived directly from Whisper speech recognition (`transcription_timestamps.json`).

| # | Timecode (MM:SS) | V1 Canvas | V2 Blur | V3 Full-Screen Asset | V4 DaVinci Text+ (Exact On-Screen Copy) | Audio Track & Exact SFX Cue |
| :-: | :--- | :--- | :---: | :--- | :--- | :--- |
| **01** | `00:00 – 00:08` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE $60,000 CAR`<br>Subtext: `FROZEN AT DAWN` | **A4:** `sfx_car_door_thud.wav` (-16 dB) at `00:01` |
| **02** | `00:08 – 00:18` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `GLOBAL ROLLOUT`<br>Body: `UK • GERMANY • SOUTH AFRICA` | **A2:** Ambient bed enters at -23 dB |
| **03** | `00:18 – 00:26` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_01_frosted_dashboard.jpg` *(3% Push)* | — | **A4:** `sfx_error_buzz.wav` (-16 dB) at `00:24` |
| **04** | `00:26 – 00:37` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `BOLTED AT THE FACTORY`<br>Body: `COPPER • RELAYS • SWITCHES` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `00:26` |
| **05** | `00:37 – 00:44` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `CLOUD LOCK`<br>Quote: `"NOT UNLESS YOUR CARD BILLS"` | **A4:** `sfx_data_blip.wav` (-16 dB) at `00:41` |
| **06** | `00:44 – 00:51` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `A HOSTAGE IN YOUR SEAT` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `00:44` |
| **07** | `00:51 – 00:59` | Gameplay (Zoom 1.15x) | **OFF** | — | — *(Clean gameplay canvas breath)* | **A2:** BGM swells to -16 dB during breath |
| **08** | `01:00 – 01:06` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `IT WAS NOT A PRANK`<br>Subtext: `IT WAS A TEST` | **A3:** Sub-bass hit (-12 dB) at `01:00` |
| **09** | `01:06 – 01:14` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_02_hp_printer_kill.jpg` *(3% Push)* | Headline: `2016: DYNAMIC SECURITY` | **A4:** `sfx_printer_head_grind.wav` (-16 dB) at `01:07` |
| **10** | `01:15 – 01:22` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `OVERNIGHT BRICK`<br>Body: `THIRD-PARTY INK DETECTED` | **A4:** `sfx_error_buzz.wav` (-16 dB) at `01:16` |
| **11** | `01:23 – 01:33` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `YOU BOUGHT A PRINTER`<br>Subtext: `THAT AUDITS YOUR INK` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `01:28` |
| **12** | `01:34 – 01:40` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `REGULATORY FINE`<br>Headline: `€10,000,000 PENALTY` | **A4:** Cash register / gavel thud (-16 dB) |
| **13** | `01:41 – 01:48` | Gameplay (Zoom 1.15x) | **OFF** | `evidence_hp_ceo_quote.jpg` | Yellow highlight sweep across quote | **A4:** Highlight sweep whoosh (-18 dB) |
| **14** | `01:49 – 01:57` | Gameplay (Zoom 1.15x) | **BLUR** | — | Quote: `"BUYING A PRINTER IS AN INVESTMENT FOR HP"` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `01:50` |
| **15** | `01:58 – 02:09` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `CHEAP INK = BAD INVESTMENT`<br>Subtext: `YOU ARE THE TARGET` | **A2:** Dead-air drop (Silence 1.5s) at `02:03` |
| **16** | `02:10 – 02:21` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `A COLD SEAT IS AN INSULT`<br>Subtext: `A TRACTOR FEEDS A FAMILY` | **A3:** Dramatic impact hit (-12 dB) at `02:16` |
| **17** | `02:22 – 02:37` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_03_nebraska_combine.jpg` *(3% Push)* | Headline: `NEBRASKA 2017`<br>Subtext: `DANNY KLUTHE TESTIMONY` | **A4:** Diesel engine coughs & dies (-16 dB) |
| **18** | `02:38 – 02:53` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `JOHN DEERE TRIP CHARGE`<br>Headline: `$230 TO ARRIVE + $130/HOUR`<br>Subtext: `JUST TO PLUG IN A LAPTOP` | **A4:** Data blip (-16 dB) at `02:48` |
| **19** | `02:54 – 03:04` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `WHOSE TRACTOR WAS IT?` | **A2:** Dead-air drop (Silence 2.0s) at `02:59` |
| **20** | `03:04 – 03:24` | Gameplay (Zoom 1.15x) | **OFF** | `hacker_noir_plate.jpg` *(3% Push)* | Headline: `THE UKRAINIAN UNDERGROUND`<br>Subtext: `PIRATE FIRMWARE ON FARMS` | **A4:** Keyboard clatter & solder hiss (-16 dB) |
| **21** | `03:24 – 03:38` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `COPYRIGHT AS A WEAPON`<br>Subtext: `PIRATES RESPECT OWNERSHIP MORE` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `03:31` |
| **22** | `03:38 – 03:49` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `NOT A VILLAIN IN A CAPE`<br>Subtext: `A SPREADSHEET` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `03:44` |
| **23** | `03:50 – 04:03` | Gameplay (Zoom 1.15x) | **OFF** | `CHART_VALUATION_MULTIPLIER_animated.mp4` | Animated bar rises: `HARDWARE 1.5x` | **A4:** Ticker tape rattle (-16 dB) |
| **24** | `04:04 – 04:20` | Gameplay (Zoom 1.15x) | **OFF** | `CHART_VALUATION_MULTIPLIER_animated.mp4` | Animated bar explodes: `RECURRING SAAS 6.7x` | **A3:** Sub-bass impact & cash register (-12 dB) |
| **25** | `04:21 – 04:32` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `FOR A CUSTOMER WHO CANNOT LEAVE` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `04:27` |
| **26** | `04:33 – 04:47` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `VALUATION SURGE`<br>Headline: `$1.5B ➔ $6.7B OVERNIGHT`<br>Subtext: `ZERO NEW INVENTION` | **A4:** Data blip (-16 dB) at `04:41` |
| **27** | `04:48 – 05:02` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE CEO STOCK SCOREBOARD`<br>Subtext: `PAID TO TAKE YOUR OWNERSHIP` | **A2:** Dead-air drop (Silence 1.5s) at `04:55` |
| **28** | `05:02 – 05:17` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_05_geneva_cartel_1924.jpg` *(3% Push)* | Headline: `GENEVA • CHRISTMAS EVE 1924` | **A4:** Match strike & clock ticking (-16 dB) |
| **29** | `05:18 – 05:33` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `THE SECRET PACT`<br>Body: `OSRAM • PHILIPS • GENERAL ELECTRIC` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `05:25` |
| **30** | `05:34 – 05:49` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `LIVERMORE FIRE STATION`<br>Headline: `GLOWING NON-STOP SINCE 1901`<br>Subtext: `GREAT PRODUCT • TERRIBLE BUSINESS` | **A4:** Electrical hum (-18 dB) |
| **31** | `05:50 – 06:02` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `THE PHOEBUS CARTEL`<br>Badge: `1,000-HOUR LIMIT`<br>Subtext: `FINED FOR MAKING IT LAST` | **A4:** Glass filament snaps (-16 dB) at `06:00` |
| **32** | `06:03 – 06:19` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `SAME INCENTIVE`<br>Subtext: `BETTER PAPERWORK` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `06:10` |
| **33** | `06:19 – 06:33` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_06_phone_lock_delivery.jpg` *(3% Push)* | Headline: `SMALL TOWN INDIA`<br>Subtext: `THE SMARTPHONE PADLOCK` | **A4:** Scooter engine in night traffic (-18 dB) |
| **34** | `06:34 – 06:53` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `ONE LATE PAYMENT`<br>Body: `HIS MAP • HIS ORDERS • HIS INCOME`<br>Subtext: `JOB HELD HOSTAGE` | **A4:** Heavy padlock clunk (-14 dB) at `06:45` |
| **35** | `06:54 – 07:10` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `FEDERAL FTC LAWSUIT`<br>Headline: `ADOBE ANNUAL PLAN TRAP`<br>Subtext: `EARLY TERMINATION PENALTY` | **A4:** Data blip (-16 dB) at `07:05` |
| **36** | `07:11 – 07:28` | Gameplay (Zoom 1.15x) | **OFF** | `anchor_07_seat_warm_glow.jpg` *(3% Push)* | Headline: `SEPTEMBER 2023`<br>Headline: `BMW DROPS THE SEAT RENT` | **A4:** Soft seat-warmer relay click (-16 dB) |
| **37** | `07:29 – 07:44` | Gameplay (Zoom 1.15x) | **BLUR** | — | Badge: `RIGHT TO REPAIR WINS`<br>Body: `COLORADO (TRACTORS) • MN & CA (PHONES)` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `07:34` |
| **38** | `07:45 – 08:00` | Gameplay (Zoom 1.15x) | **BLUR** | — | Headline: `A SEAT • A PRINTER • A TRACTOR`<br>Subtext: `ONE UPDATE FROM A LEASE` | **A3:** `sfx_sub_boom.wav` (-12 dB) at `07:50` |
| **39** | `08:01 – 08:08` | Gameplay (Zoom 1.15x) | **OFF** | — *(Gameplay fade to black)* | Quote: `"REMEMBER WHO IS HOLDING THE KEY"` | **A2:** Ambient bed fades to complete silence |

---

## 3. DaVinci Resolve Master Export Settings
* **Timeline Resolution:** `2560 x 1440 QHD` (forces YouTube to assign the premium **`av01` / `vp09`** codec).
* **Frame Rate:** `60 fps` (matches source gameplay).
* **Video Format:** `QuickTime` / `H.265 (HEVC)` or `MP4` / `H.264`.
* **Audio Format:** `Linear PCM 24-bit` or `AAC 320 kbps`.
* **Master Bus Limiter:** True Peak ceiling at **`-1.0 dBFS`**.

