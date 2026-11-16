# ThinkLate Video 05 — Generative Video Prompt Bible (Google Veo & Kling AI)

> **Episode:** *"How An $80 Airbed Stole An Entire Industry"* (`05_how-airbnb-stole-100b`)  
> **Aesthetic Standard:** Cinematic 35mm Film Grain $\times$ Gritty Documentary Infotainment $\times$ High-Contrast Noir.  
> **Format:** 16:9 Aspect Ratio | 1080p / 4K Photorealism | Audio Muted for Timeline Compositing.

---

## 🎬 Master 15-Scene Generative Prompt Table

| Scene # | Narrative Beat & Timecode | Optimized Generative Prompt (Veo / Kling / MiniMax) | Visual Action & Camera Movement |
| :---: | :--- | :--- | :--- |
| **01** | **The Hook: Eviction Notice (0:00)** | `Cinematic photorealistic 35mm film shot of a weathered wooden apartment door in San Francisco, October 2007. An eviction notice with red overdue text is taped to the wood. Soft natural dusk window light, dust motes in air, shallow depth of field, high contrast, cinematic drama --ar 16:9` | Slow macro push-in on the overdue rent notice. |
| **02** | **Broke Designers on Floor (0:08)** | `Cinematic wide shot of two exhausted young industrial designers in their 20s sitting on the bare wooden floor of an unfurnished San Francisco loft apartment in 2007. Scattered tracing paper, sketches, markers, and an empty pizza box on the floor. Moody low-key cinematic lighting, 4k photorealism --ar 16:9` | Gentle 24fps camera drift revealing bare loft. |
| **03** | **Hotels 100% Sold Out (0:24)** | `Cinematic medium shot of an overcrowded 2007 grand hotel lobby during a major convention. Weary international travelers standing near luggage looking frustrated. In the foreground, a prominent brass counter sign reads 'NO VACANCY'. Warm interior tungsten lighting, subtle handheld camera drift, documentary realism --ar 16:9` | Handheld documentary drift across crowded lobby. |
| **04** | **The Airbed & Pop-Tarts Hustle (0:34)** | `Macro cinematic shot of two hands furiously pumping air into a blue inflatable camping air mattress on a scuffed apartment hardwood floor. Warm morning sunbeams cutting through Venetian blinds, authentic gritty 2007 indie film atmosphere, tactile details --ar 16:9` | Rapid rhythmic pumping motion, airbed expanding. |
| **05** | **VC Laughs in Their Face (1:33)** | `Cinematic eye-level shot inside a sunny Silicon Valley coffee shop in 2008. A wealthy venture capitalist in a fleece vest stands up with a dismissive smirk, leaving a coffee mug on the table. Across from him, two stunned young founders look down at their handwritten pitch deck. Natural morning backlighting, photorealistic cinematic documentary --ar 16:9` | VC walks out of frame, leaving founders frozen. |
| **06** | **$20,000 Card Debt Binder (2:44)** | `Cinematic close-up top-down view of hands opening a black three-ring binder filled with clear plastic trading card sleeves, each slot filled with different colorful maxed-out credit cards from 2008. Dramatic moody desk lamp lighting, cinematic noir style --ar 16:9` | Slow flip of plastic binder pages revealing maxed cards. |
| **07** | **The Cereal Box Factory (3:30)** | `Cinematic atmospheric medium shot of a cluttered late-night kitchen table turned into a makeshift factory. Cardboard cereal boxes being assembled with hot glue guns, bulk cereal grains, and cardboard shavings under an overhead incandescent lightbulb. Gritty entrepreneurial grit, high texture, 35mm film grain --ar 16:9` | Hot glue gun steaming, hands folding cardboard. |
| **08** | **Paul Graham YC Crucible (4:19)** | `Cinematic medium shot inside a minimalist Silicon Valley startup accelerator office in 2009. A thoughtful senior investor in glasses examines a colorful novelty cereal box with a wry, impressed smile. Modern studio lighting, soft orange and slate color palette, cinematic 4k --ar 16:9` | Senior mentor nods slowly, smiling with respect. |
| **09** | **March 2009: Airbnb Rebrand (4:45)** | `Extreme macro cinematic shot of fingers typing on a 2009 laptop keyboard, transitioning to an old web browser address bar where the text 'airbedandbreakfast.com' is backspaced and replaced with 'airbnb.com'. Soft screen glow illuminating the hands, cinematic depth of field --ar 16:9` | Rapid backspace and typing of new short domain. |
| **10** | **Brooklyn Ground War (6:07)** | `Cinematic low-angle tracking shot of a young determined founder holding a professional DSLR camera, walking down a classic Brooklyn brownstone street under an overcast autumn sky. Wet asphalt, yellow leaves, tactile documentary realism, filmic color grading --ar 16:9` | Dynamic forward tracking shot alongside walking founder. |
| **11** | **Craigslist Form Hijack (7:25)** | `Cinematic dark-room shot focusing on a glowing laptop screen displaying green command-line terminal code rapidly scraping web forms. Dark moody tech-thriller lighting, blue and green reflections on the keyboard, cinematic noir --ar 16:9` | Terminal code scrolling rapidly, green phosphor glow. |
| **12** | **March 2020 Travel Collapse (9:27)** | `Cinematic wide static shot of a colossal, completely deserted international airport terminal in March 2020. Towering flight departure boards all displaying flashing red 'CANCELLED' text. Sterile cold blue fluorescent lighting, reflections on polished marble floors, cinematic solitude --ar 16:9` | Static haunting wide frame of empty terminal. |
| **13** | **$100B NASDAQ IPO (10:29)** | `Cinematic wide night shot of Times Square in winter, focusing on the massive cylindrical electronic NASDAQ billboard screen displaying a soaring stock chart and ticker 'ABNB'. City lights, yellow cabs moving, falling light snow, crisp ultra-photorealistic broadcast news aesthetic --ar 16:9` | Slow tilt up from traffic to glowing NASDAQ tower. |
| **14** | **The $180 Chore List (11:11)** | `Cinematic eye-level shot inside a luxury minimalist high-rise rental kitchen. A traveler holding a glossy laminated sheet titled 'GUEST CHECKOUT CHORES'. In the background, a digital tablet displays an invoice with a highlighted '$180 Cleaning Fee'. Satirical, sharp high-contrast modern cinematography --ar 16:9` | Subtle rack focus from chore sheet to tablet invoice. |
| **15** | **Barcelona City Ban Protests (12:45)** | `Cinematic documentary shot of a passionate urban street protest in Barcelona. Demonstrators holding painted signs and banners reading 'HOUSING IS A RIGHT'. Historic Mediterranean architecture in background, afternoon sun, handheld documentary realism --ar 16:9` | Handheld camera moving through protest crowd. |

---

## 🛠️ Usage Instructions

- **Via Google Veo / Gemini API:** Use `tools/generate_veo_scene.py` passing the Scene ID.
- **Via Kling / MiniMax (Fal.ai API):** Pass the exact prompt text to the Fal.ai endpoint (`fal-ai/kling-video/v1/standard/text-to-video` or `fal-ai/minimax/video-01`).
- **Via Web Portals:** Copy and paste the prompt directly into [klingai.com](https://klingai.com) or [aistudio.google.com](https://aistudio.google.com), select **16:9** aspect ratio, 5 seconds duration, and download the resulting MP4 into `assets/generative_broll/`.

