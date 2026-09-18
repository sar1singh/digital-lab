# ThinkLate — Free-Tier Tool Stack, Asset by Asset

**Date:** 2026-09-13
**Researched:** free-tier limits verified against vendor and aggregator sources on this date.

**Warning on every number here:** free-tier limits change constantly and most of these figures come from comparison blogs and vendor pages, not from the products' own docs. **Check the actual signup page before relying on a limit.** Treat everything below as a starting point, not a contract.

---

## 1. The finding that matters most

**Only 2 of your 11 asset types should use generative AI at all.**

Everything else is layout, data visualisation, or real archival material. That isn't a limitation — it's the whole point. Your credibility moat is that a viewer can check your sources, and YouTube's July 2026 inauthentic-content policy penalises exactly the generated-imagery workflow that most "faceless channel" tooling is built around.

So most of the tools you named — Veo, Google Flow, Higgsfield, Grok Imagine — are **the wrong tools for this channel**, not tools you can't afford. Good to know before spending time on them.

| Asset | Generative AI? |
|---|---|
| Logo / avatar concept | ✅ Yes |
| Abstract background textures | ✅ Yes |
| Banner | ❌ Layout job |
| Thumbnails | ❌ Layout job |
| Charts | ❌ Data viz |
| Maps | ❌ Data viz |
| Archival images | ❌ **Real archive only** |
| Document excerpts | ❌ Real documents |
| Title/chapter/quote frames | ❌ Template |
| Subtitles | ❌ Transcription |
| Voice cleanup | ❌ Audio processing |

---

## 2. Logo and avatar

The one place you genuinely want generative AI.

| Tool | Free tier | Verdict |
|---|---|---|
| **Ideogram** | **Commercial use allowed, no watermark.** ~95% accuracy rendering specific words vs 30–50% for competitors | **Superseded.** The text-rendering advantage no longer matters — the mark contains no text and the wordmark is set in vector. See `08` §6.5 for the current verdict: **Bing Image Creator first, Leonardo for volume, never Recraft or OpenArt (watermark / no commercial licence)** |
| **Recraft** | 30 credits/day. **The only mainstream model producing true editable SVG paths** — real curves and nodes, not a traced raster | **Explore only. Free tier watermarks output and prohibits commercial use.** Excellent for testing whether a concept vectorises; you cannot ship from it |
| Gemini / Nano Banana | ~20 images/day free; Nano Banana Pro capped at ~2/day | Fine for concept sketches. Weaker on text |
| Canva free | Not generative for logos, but a solid editor with vector shapes and free fonts | **Where you assemble the final lockup** |

**Recommended path, all free:**

1. **Ideogram** → generate 20–30 owl-mark concepts using the prompt in `08_DESIGN-SPEC-FOR-GENAI.md` §6a. Commercial-cleared, no watermark
2. Pick one direction
3. **Vectorise it** — free options: **Inkscape** (Path → Trace Bitmap), or **SVGcode** (svgco.de, browser-based). Both free, no signup
4. **Clean up and build the lockup in Canva or Affinity** — you already have Affinity
5. Derive the avatar (owl head only) and the 150×150 watermark from the same file

**The honest caveat:** traced vectors are messier than drawn ones — extra nodes, slightly wrong curves. Good enough for YouTube at 98×98. If you later want it clean for merch or a sponsor deck, ₹1,500–3,000 to a designer to redraw it properly.

---

## 3. Banner, thumbnails, frames

**Not a generation problem. A layout problem.** Free tools do this fully.

| Tool | Free tier | Use |
|---|---|---|
| **Canva free** | Unlimited designs, custom dimensions, free fonts incl. Playfair Display and IBM Plex | **Banner (2560×1440), thumbnail template, all frame types.** Set up as reusable templates with locked layers |
| **Figma free** | 3 files, unlimited personal drafts | Better if you want proper component systems and auto-layout. Steeper learning curve |
| **Affinity** | You already have it | Best precision. No template/cloud convenience |

**Recommendation: Canva for the banner and thumbnail template.** Custom dimensions work on free, the fonts you need are there, and the template-duplicate workflow suits 20+ videos. Affinity for anything needing precision.

Do **not** use Canva's AI image generation for thumbnail subjects. Use a real chart, map, or archival image.

---

## 4. Charts and maps — free, and better than AI

| Tool | Free tier | Use |
|---|---|---|
| **Flourish** | Free tier, public projects | **Animated charts.** Best-looking output for least effort |
| **Datawrapper** | Free tier | Publication-quality static charts and choropleth maps |
| **MapChart.net** | Free | Fast country-highlight maps |
| **Natural Earth** | Public domain data | Custom base maps |
| `templates/charts.py` + `templates/animate.py` | Free, already built | On-brand, scriptable, MP4 output |

No generative AI here at all. Real data in, real chart out.

---

## 5. Archival images and documents — never generated

Full list in `05_ASSETS-AND-PROMPTS.md` §3. All free: **Wikimedia Commons · Library of Congress · US National Archives · NYPL Digital Collections · Europeana · Internet Archive · Getty Open Content · David Rumsey Maps · NASA**.

**Check the rights statement on each individual item.** "Public domain archive" doesn't mean every item in it is public domain.

**Free upscaling/restoration for low-res archive scans:** Upscayl (open source, runs locally, no limits) or Real-ESRGAN. This is a legitimate AI use — you're improving a real image, not inventing one.

---

## 6. The one legitimate generative-video use

Abstract, non-representational background textures and transitions. Nothing depicting anything real.

| Tool | Free tier | Notes |
|---|---|---|
| **Google Flow** | ~50 daily credits on Veo 3.1 and Nano Banana Pro. A "Fast" video ≈20 credits, "Quality" ≈100 | Roughly 2 fast generations/day. Enough for abstract loops |
| **Higgsfield** | ~10 credits/day, **watermarked**, flagship models locked | Watermark rules it out for anything on screen |
| **Grok Imagine** | Credit system, ~5 credits/day, refilling at midnight UTC | Thin |
| Banana Flow | ~20 credits/month | Very thin |

**Honest assessment: you need about three abstract background loops, total, reused across every video.** That's one afternoon on Google Flow's free tier and then you never touch it again. Don't build a workflow around AI video — you need almost none of it.

Free generation typically caps at 5–8 seconds at 720p/1080p, which is fine for a loop.

---

## 7. Audio and subtitles — all free

| Need | Tool | Notes |
|---|---|---|
| Record | Audacity, or Resolve Fairlight | Both free, both owned |
| Noise removal | **Resolve Fairlight → Voice Isolation** | First choice |
| Heavier cleanup | Adobe Podcast Enhance free tier | Genuinely good |
| Transcription / subtitles | **Whisper**, run locally | Free, unlimited, no upload. You're a dev — run it yourself |
| Music / SFX | YouTube Audio Library | Free, monetisation-cleared |

**No AI voice.** Use your own — `00_CONTEXT.md`.

---

## 8. The complete free stack

| # | Asset | Tool | Cost |
|---|---|---|---|
| 1 | Logo concepts | Ideogram | Free, commercial-cleared |
| 2 | Vectorise | Inkscape or SVGcode | Free |
| 3 | Logo lockup, avatar, watermark | Canva or Affinity | Free / owned |
| 4 | Banner 2560×1440 | Canva | Free |
| 5 | Thumbnail template | Canva or Affinity | Free |
| 6 | Frame templates | Canva, or `templates/` | Free |
| 7 | Static charts, maps | Datawrapper, MapChart | Free |
| 8 | Animated charts | Flourish, or `templates/animate.py` | Free |
| 9 | Archival images | The nine archives | Free |
| 10 | Upscale old scans | Upscayl | Free, local |
| 11 | Abstract loops (×3, once) | Google Flow | Free tier |
| 12 | Record + edit + colour | DaVinci Resolve | Owned |
| 13 | Audio cleanup | Fairlight, Adobe Podcast | Free |
| 14 | Subtitles | Whisper, local | Free |
| 15 | Music | YouTube Audio Library | Free |
| 16 | Keyword research | vidIQ free, Google Trends | Free |
| 17 | Research synthesis | NotebookLM | Free |

**Total: ₹0.** The only spends remain thinklate.com (~₹1,500/yr) and optionally a designer for clean logo vectors.

---

## 9. Traps

- **Recraft free tier prohibits commercial use and watermarks output.** It's the best SVG generator and you still can't ship from its free tier. Explore only
- **Higgsfield free tier watermarks everything.** Unusable for on-screen assets
- **Canva's AI image generation** — don't use it for thumbnail subjects. Real chart or real archive
- **Nano Banana Pro at ~2 images/day free** will feel unusable fast. Use Ideogram instead
- **Free video tiers cap at 5–8 seconds.** Fine for loops, useless for anything else — which is fine, because you need almost no generated video
- **Don't chase free-tier credits.** If a workflow needs daily credit farming across three tools, it's the wrong workflow. Your bottleneck is hours, not rupees

---

## Sources

[rangy.ai — Ideogram vs Recraft for logos](https://rangy.ai/blog/ideogram-vs-recraft-for-logos/) · [rangy.ai — best AI logo generators 2026](https://rangy.ai/blog/best-ai-logo-generator-2026/) · [Recraft AI vector generator](https://www.recraft.ai/ai-vector-generator) · [vectosolve — AI SVG generators tested](https://vectosolve.com/blog/best-ai-svg-generators-text-to-vector-2026) · [costgoat — Google Flow pricing](https://costgoat.com/pricing/google-flow) · [whiskailabs — Google Flow pricing](https://whiskailabs.net/google-flow-ai-pricing/) · [creetr — Higgsfield free tier](https://creetr.com/blog/is-higgsfield-ai-free) · [costbench — Higgsfield free plan](https://costbench.com/software/ai-video-generators/higgsfield/free-plan/) · [ximagineai — Grok Imagine limits](https://ximagineai.com/grok-imagine-limit-faq) · [datastudios — Gemini free tier 2026](https://www.datastudios.org/post/google-gemini-free-in-march-2026-plans-complete-feature-set-limits-workflows-availability-and) · [evolink — free AI video generators, verified plans](https://evolink.ai/blog/free-ai-video-generator-2026-what-is-actually-free) · [nanobanana pricing](https://nanobanana.im/pricing)
