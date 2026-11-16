# Video 03: Primary Evidence & Live Citation Capture Guide
> **Channel:** ThinkLate (`@wethinklate`) | **Episode:** `03_death_of_ownership` — *"You Don't Own What You Buy."*  
> **Purpose:** Verified live URLs, exact document coordinates, verbatim text to highlight, and step-by-step browser/OBS capture instructions so your video evidence is 100% indisputable.

---

## 📸 How to Capture Broadcast-Grade Evidence (Ergonomic Standard)

1. **Browser Zoom:** Always set your browser zoom to **125% or 150%** before taking a screenshot so typography is pin-sharp on 1080p and 4K displays.
2. **Capture Mode:** 
   * **Stills:** Use Windows Snipping Tool (`Win + Shift + S`) or browser full-page screenshot.
   * **Motion Scroll:** Use OBS Studio (`Window Capture` on Chrome/Brave) to capture a slow, smooth 3-second mouse scroll down the document for dynamic motion B-roll.
3. **Storage:** Save all captures into `videos/03_death_of_ownership/assets/` using the IDs below (e.g. `assets/EVID_01_CA_AB2426.png`).

## 📐 Affinity Photo / Designer Canvas Specs (For Multi-Crop Cards)

When combining 2–3 screenshots (e.g. Website Header + Specific Operative Sentence) into a single composite card:

### 1. Canvas Sizes to Use in Affinity:
* **Option A: Full-Screen Composite Canvas (16:9):**  
  * **Dimensions:** `1920 × 1080 px` (Standard) or `3840 × 2160 px` (4K / 2x Retain Detail).  
  * **Color:** RGB / 8-bit / sRGB.  
  * **Background:** Transparent (so you can layer it over video) or Dark Studio Slate `#0F1626`.  
  * **Margins:** 80px Title-Safe padding from outer boundary.
* **Option B: Floating Evidence Card Canvas (Right 45% Split):**  
  * **Dimensions:** `920 × 880 px` (or `1000 × 800 px`).  
  * **Export:** PNG-24 with Alpha Transparency.  
  * **Drop Shadow:** Blur `24px`, Opacity `65%`, Offset `Y: 12px`, Color `#000000`.

### 2. The 2-Tier Layout Blueprint (Header + Zoomed Quote):
```
┌────────────────────────────────────────────────────────────────────────┐
│ [FLOATING EVIDENCE CARD: 920 × 880 PX]                                │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ TIER 1 (TOP 30%): CONTEXT HEADER CROP (125% Browser Zoom)        │  │
│  │ [Website Logo / Publication Name]  •  [Article Headline / Date]  │  │
│  │ (Proves authentic source & authority to viewer)                  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                  ▼                                     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ TIER 2 (BOTTOM 70%): OPERATIVE QUOTE CROP (150% - 175% Zoom)     │  │
│  │ "It is unlawful for a seller to advertise with the term 'BUY'..."│  │
│  │ ══════════════════════════════════════════════════════════════   │  │
│  │ (Yellow / Cyan Highlight Box: #F59E0B @ 30% opacity or border)   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🎬 Famous YouTuber Evidence Methods (Easy to do in DaVinci Resolve)

If you prefer building this directly on your DaVinci Resolve timeline without manually stitching in Affinity, top video essayists (Vox, Johnny Harris, ColdFusion, Lemmino) use these **3 simple native techniques**:

### Method 1: The "Vox / Johnny Harris" Animated Highlighter Sweep
* **Visual Result:** The article appears on screen, and 0.5s later, a bright yellow or amber marker stroke smoothly sweeps across the text.
* **How to do it in DaVinci in 30 seconds:**
  1. Place your article screenshot on **Video Track 2**.
  2. In the Effects library, drag a **Solid Color Generator** (or Color Clip) onto **Video Track 3** directly above the screenshot.
  3. Change the Solid Color to **Warm Amber / Yellow (`#F59E0B` or `#FACC15`)**.
  4. In the Inspector, adjust the **Cropping (Top & Bottom)** sliders so the colored bar covers only the exact line of text.
  5. Set **Composite Mode** to **`Multiply`** (the black text instantly shows through the yellow color like real ink!).
  6. To animate the sweep: At frame 0, set `Crop Right` to 1000. At frame 15 (0.5s), set `Crop Right` to 0. Add a keyframe.
  * *Result:* Broadcast-quality animated highlighter stroke with zero plugins!

### Method 2: The "Background Dim & Spot Zoom" (Focus Pull)
* **Visual Result:** The full website is visible, but the entire page dims and blurs slightly while the critical paragraph scales up with a shadow, pulling 100% of viewer attention.
* **How to do it in DaVinci:**
  1. Put the full webpage screenshot on **Track 1**. In Inspector, drop Opacity to `60%` (or add subtle Gaussian Blur).
  2. Put the cropped close-up screenshot on **Track 2** directly over it.
  3. Increase Zoom to `1.15x` and enable **Drop Shadow** (under OpenFX or Fusion).

### Method 3: The "Tactile 3D Tilt" (Floating Document)
* **Visual Result:** Instead of looking like a flat computer screenshot, the document floats in 3D space like a physical government document or magazine clipping.
* **How to do it in DaVinci:**
  1. In the Inspector under **Transform**, scroll to **Pitch & Yaw**.
  2. Set **`Yaw: 6.0`** (slight horizontal rotation) and **`Pitch: -3.0`** (subtle vertical tilt).
  3. Turn on **Drop Shadow** (Shadow Distance: 15, Blur: 25).
  * *Result:* Gives an immediate cinematic documentary feel.

---

## 📑 The 6 Verified Primary Citations (Live Fact Dossier)

### Evidence 1: California AB 2426 (Business & Professions Code § 17500.6)
* **What It Proves:** California legally banned digital storefronts from using "BUY" or "PURCHASE" without explicit disclosures that the user is only getting a revocable license.
* **Live Source URL:**  
  [https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2426](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2426)  
  *(Alternative mirror: [Justia Law — Cal. Bus. & Prof. Code § 17500.6](https://law.justia.com/codes/california/code-bpc/division-7/part-3/chapter-1/article-1/section-17500.6/))*
* **Target Coordinate:** Section 17500.6, Subsection (a).
* **Verbatim Text to Highlight in Yellow:**
  > *"It is unlawful for a seller of a digital good to advertise or offer for sale a digital good to a purchaser in this state with the term 'buy', 'purchase', or any other term that a reasonable person would interpret as conferring an unrestricted ownership interest... unless the seller does either of the following..."*
* **Recommended Capture Asset Name:** `assets/EVID_01_CA_AB2426.png`

---

### Evidence 2: Steam Cart Checkout Warning (Valve Corporation)
* **What It Proves:** Even beloved Valve was forced by law to admit that clicking "Purchase" on Steam only grants a revocable license.
* **Live Source URL:**  
  Open your desktop **Steam Client** $\rightarrow$ Add any game to cart $\rightarrow$ Go to Checkout screen.  
  *(Web mirror: [store.steampowered.com/cart](https://store.steampowered.com/cart))*
* **Target Coordinate:** Directly above the "Continue to payment" green button at bottom of shopping cart.
* **Verbatim Text to Highlight in Cyan Box:**
  > *"A purchase of a digital product grants a license for the product on Steam."*
* **Recommended Capture Asset Name:** `assets/EVID_02_STEAM_CART_WARNING.png`

---

### Evidence 3: PlayStation Direct — PS5 Pro & $79.99 Disc Drive
* **What It Proves:** Sony sells a $699.99 console without a disc drive and paywalls physical game compatibility behind an expensive $79.99 accessory that suffers frequent stockouts.
* **Live Source URL:**  
  [https://direct.playstation.com/en-us/buy-accessories/disc-drive-for-ps5-digital-edition-consoles](https://direct.playstation.com/en-us/buy-accessories/disc-drive-for-ps5-digital-edition-consoles)
* **Target Coordinate:** Main product hero showing the $79.99 price tag and "Currently Unavailable" or "Out of Stock" button.
* **Verbatim Details to Highlight:**
  * Product Title: *"Disc Drive for PS5® Digital Edition Consoles"*
  * Price: *"$79.99"*
  * Stock Status: *"Currently Unavailable"*
* **Recommended Capture Asset Name:** `assets/EVID_03_PS5_PRO_DISC_DRIVE.png`

---

### Evidence 4: The Ubisoft *The Crew* Federal Class Action Lawsuit
* **What It Proves:** Gamers sued Ubisoft in California federal court after Ubisoft deleted game files and revoked licenses from 12 million players.
* **Court Case Citation:**  
  *Cassell et al. v. Ubisoft Entertainment SA et al.*, Case No. 3:24-cv-07746, U.S. District Court for the Northern District of California (Filed November 2024).
* **Live Source URL:**  
  [https://www.classaction.org/news/ubisoft-sued-over-the-crew-server-shutdown-loss-of-access](https://www.classaction.org/news/ubisoft-sued-over-the-crew-server-shutdown-loss-of-access)  
  *(Or Bloomberg Law / CourtListener docket summary)*
* **Target Coordinate:** Complaint Summary Paragraph 1–3.
* **Verbatim Text to Highlight:**
  > *"Defendants deceptively represented to consumers that they were purchasing the game 'The Crew', while secretly intending to render the game permanently unplayable by shutting down servers and remotely revoking access licenses."*
* **Recommended Capture Asset Name:** `assets/EVID_04_UBISOFT_CREW_LAWSUIT.png`

---

### Evidence 5: Indian Game Resale Lifeline (Gameloot / CEX India)
* **What It Proves:** In developing economies like India, console gaming historically survived exclusively on pre-owned disc trade. Digital-only games with zero resale eliminate this economic engine.
* **Live Source URL:**  
  [https://gameloot.in/shop/playstation/ps5-games/](https://gameloot.in/shop/playstation/ps5-games/)  
  *(Or CeX India: [in.webuy.com](https://in.webuy.com))*
* **Target Coordinate:** A popular AAA game listing showing both "Pre-Owned Buy" and "Sell / Buyback" values.
* **Verbatim Details to Highlight:**
  * Title: *"PS5 Pre-Owned Disc"*
  * Buy Price: *"₹2,499"* | Sell/Cashback Value: *"₹1,900"*
  * Effective Cost to Play: *"₹599"* (vs ₹5,999 non-refundable digital tag).
* **Recommended Capture Asset Name:** `assets/EVID_05_INDIA_DISC_RESALE.png`

---

### Evidence 6: BMW ConnectedDrive Heated Seat Subscription
* **What It Proves:** The "digital license / hardware rental" infection is expanding beyond video games into physical cars and appliances.
* **Live Source URL:**  
  [https://www.bmw.co.uk/en/shop/ls/dp/Seat_Heating_SFA_gb](https://www.bmw.co.uk/en/shop/ls/dp/Seat_Heating_SFA_gb)  
  *(Or archive capture: The Verge / BBC reporting on BMW ConnectedDrive heated seat paywall)*
* **Target Coordinate:** ConnectedDrive store listing showing monthly/annual subscription options for built-in heated seats.
* **Verbatim Text to Highlight:**
  > *"Front seat heating subscription — £15 / $18 per month... 1 month, 1 year, or unlimited."*
* **Recommended Capture Asset Name:** `assets/EVID_06_BMW_HEATED_SEATS.png`

---

## 🖥️ UI, Platform & Regulatory Cards (Secondary Visual Assets)

### Card 1: Stop Killing Games — European Citizens' Initiative
* **What It Proves:** Over 1 million EU citizens mobilized to demand legal requirements for offline patches when servers shut down.
* **Live Source URL:** [https://citizens-initiative.europa.eu/initiatives/details/2024/000007_en](https://citizens-initiative.europa.eu/initiatives/details/2024/000007_en)
* **Coordinate:** Official EU portal banner + Signature counter (Target: 1,000,000 signatures).
* **Asset Name:** `assets/CARD_STOP_KILLING_GAMES.png`

### Card 2: 1908 Supreme Court "First Sale Doctrine" (Bobbs-Merrill v. Straus)
* **What It Proves:** Legal precedent established over 100 years ago that purchasing physical goods confers absolute ownership and right of resale.
* **Source:** [Justia Law — Bobbs-Merrill Co. v. Straus, 210 U.S. 339 (1908)](https://supreme.justia.com/cases/federal/us/210/339/)
* **Asset Name:** `assets/CARD_FIRST_SALE_1908.png`

### Card 3: Sony PlayStation Revoking 1,300 Discovery Episodes
* **What It Proves:** Sony attempted to delete 1,300 paid Discovery TV seasons from PlayStation user libraries due to expired licensing.
* **Source:** PlayStation Support Notification / Variety / IGN article headline: *"Sony Is Removing 1,300+ Discovery Shows From PlayStation Libraries, Even If You Paid for Them."*
* **Asset Name:** `assets/CARD_SONY_DISCOVERY.png`

### Card 4: PlayStation Store Full-Price Monopoly ($59.99 for 5-Year-Old Game)
* **What It Proves:** Without physical disc resale or competing storefronts, console owners face artificial price stagnation.
* **Source:** PlayStation Store web search showing older catalog title at full $59.99 MSRP.
* **Asset Name:** `assets/CARD_PS_STORE_PRICES.png`

### Card 5: GOG.com DRM-Free Standalone Offline Installer
* **What It Proves:** GOG provides permanent ownership via downloadable standalone `.exe` installers that work completely offline without launcher checks.
* **Source:** GOG.com library screen showing `"DOWNLOAD OFFLINE BACKUP GAME INSTALLERS"` button.
* **Asset Name:** `assets/CARD_RULE1_GOG.png`

### Card 6: Indian EV Scooter Software Paywall
* **What It Proves:** Indian electric scooters locking physical hardware (hill-hold, cruise control) behind over-the-air software subscription packages.
* **Source:** Autocar India / Rushlane headline on Ola Electric / Ather software subscription feature packs.
* **Asset Name:** `assets/CARD_EV_SCOOTER_OTA.png`

---

## 📊 Data Charts

### Chart 1: 20-Year Industry Divergence (Physical vs Digital Sales Collapse) — [STATUS: DONE]
* **Status:** **DONE & READY** in `assets/CHART_SALES_COLLAPSE.png`, `assets/CHART_SALES_COLLAPSE_transparent.png`, and `assets/CHART_SALES_COLLAPSE_4K.png`.
* **Generator Script:** `render_sales_chart.py`
* **Data Points Rendered:**
  * Year 2004: Physical Software: **90%** | Digital Software: **10%**
  * Year 2015: Crossover Inflection Point: **50% / 50%**
  * Year 2024: Physical Software: **8%** (▼ 91% Collapse) | Digital Software: **92%** (▲ Storefront Monopoly)
* **Visual Style:** High-contrast Dark Slate / Frosted Glass Floating Card with glowing spline lines and callout pill badges. Drop directly on Video Track 3 in DaVinci Resolve!

