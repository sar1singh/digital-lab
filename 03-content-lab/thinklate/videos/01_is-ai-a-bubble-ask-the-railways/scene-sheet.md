# Video 1 — Scene Sheet

**FLOOR, 13 scenes, ~7 min.** Format per `RUNBOOK.md` → PART `14_SCENE-SHEET`. Built 2026-09-13.

**12 of 15 assets are already generated** and sitting in `assets/` as both SVG (editable in Affinity) and PNG at 1920 wide. **You need to source three archival images and nothing else.**

Surface alternation per `CRAFT.md` → PART `06_MOTION-AND-SURFACE`: **ink** for data and kickers, **paper** for quotes and archive.

---

## The sheet

| Scene | Script | Asset | Status | Motion |
|---|---|---|---|---|
| **S1** | `[TAKE 1]` "Your company announced an AI budget too" | **A1** — modern data-centre exterior, wide | ✅ `A1_datacenter_exterior.png` | Slow push 2% |
| **S2** | `[TAKE 2]` "Technology being real and a bubble aren't opposites" | `S04_title.png` *(holding frame: "REAL, BUT RUINED")* | ✅ | Static, 3s |
| **S3** | `[TAKE 3]` "Part of this game through your job" | **A2** — neutral modern office / desk | ✅ `A2_tech_workspace.png` | Slow pan |
| **S4** | `[TAKE 4]` "So // railways... greatest technology mania in history" | `S04_evidence_ssrn_mania.png` + `LT_S04_ssrn_mania.png` | ✅ | Cut on "railways", hold quote 4s |
| **S4b** | `[TAKE 4]` Odlyzko SSRN quote | `S04_evidence_ssrn_mania.png` | ✅ | Static — let it read |
| **S5** | `[TAKE 5]` "15 to 20% of GDP actual capital investment" | `evidence_gdp_odlyzko.png` + `LT_S05_odlyzko_gdp.png` | ✅ | **Hold 6s minimum.** The one number |
| **S6** | `[TAKE 6]` "Trustworthy quantitative measures existed" | `S06_evidence_ssrn_measures.png` + `LT_S06_ssrn_measures.png` | ✅ | Static |
| **S7** | `[TAKE 7]` Darwin, J.S. Mill, Brontës: "a collective hallucination" | `S07_evidence_historical_share.png` + `LT_S07_investors_darwin.png` | ✅ | Push on A3, lower-third in at 1s |
| **S8** | `[TAKE 8]` "Investment disaster, but provided nationwide network of great utility" | `S08_evidence_disaster_utility.png` + `LT_S08_disaster_utility.png` | ✅ | Static. Subscribe visual badge pops up |
| **S9** | `[TAKE 9]` "Tracks survived. Shareholders didn't." | `S09_lt_pattern.png` over tracks | ✅ | Lower-third only |
| **S10** | `[TAKE 10]` 1830s mania: "collapsed prematurely" | `S10_evidence_1830s_paradox.png` + `LT_S10_premature_bubble.png` | ✅ | Static |
| **S11** | `[TAKE 11]` "Today's AI boom: where does the risk actually sit?" | `S11_evidence_goldman_report.png` + `LT_S11_goldman_ai_spend.png` | ✅ | **Pinned inference disclaimer badge** |
| **S12** | `[TAKE 12]` "Shareholder vs Headcount" | `S12_evidence_sequoia_chart.png` + `LT_S12_sequoia_ai_depreciation.png` | ✅ | Split screen text |
| **S13** | `[TAKE 13]` "Which number will give it away?" | `S13_endcard.png` | ✅ | Hold to end. Both end zones clear |

**Thumbnail:** `S00_thumbnail.png` — layout frame with `IS AI / NEXT?`. Composite the archival image behind it in Affinity, 1280×720, under 2 MB.

---

## The only three things you must source

**Budget 20 minutes total. If one takes longer than ten, use the fallback.**

| ID | What | Where | Licence check |
|---|---|---|---|
| **A1** | Data centre exterior, wide, unbranded | Wikimedia Commons — search *data center* · or Unsplash | **Avoid recognisable company branding.** Check the rights statement on the individual file, not the category |
| **A2** | Neutral office or desk, no faces | Unsplash / Pexels | Free to use; still note the source in the description |
| **A3** | 1840s British railway engraving, share certificate, or prospectus | **Wikimedia Commons** — *Category:Rail transport in the United Kingdom in the 1840s* · **Library of Congress** Prints & Photographs · **British Library** Flickr Commons | Pre-1900 British engravings are generally public domain, **but verify each item's own statement** — `RUNBOOK.md` → PART `13_RUNBOOK` step 6 |

### Fallbacks — use these instead of losing an hour

- **A1 or A2 unavailable** → run the take over a **full-screen quote card** or plain ink field. A Floor video carried by type is fine; a Floor video that never gets recorded is not
- **A3 unavailable** → `S05_kicker_gdp.png` held longer, or the title card. **The video does not break without archival footage** — the quotes are doing the work
- **Nothing is working** → record audio anyway. Assets can be dropped onto a finished voice track tomorrow night. **Voice first, always** (`RUNBOOK.md` → PART `13_RUNBOOK` step 8)

---

## Asset count

**15 total: 12 generated, 3 sourced.** Runbook step 5 caps a 16-minute video at 20–28 and warns over 30 means over-illustrated. Fifteen for seven minutes is right at the top of comfortable — **if you're running short on time, cut S2 and S12 first.** Neither carries information.

---

## Editing order — `RUNBOOK.md` → PART `13_RUNBOOK` step 8

1. **Voice track first.** Assemble visuals to it, never the reverse
2. Three-layer composition — archive dimmed to 60–75%, content, then text
3. Slow push or pan on every archival still, 1–3% scale. **Static stills read as dead air**
4. `S05` kicker: hold 6s. Your instinct will be to cut early
5. Fairlight → Voice Isolation on the voice track
6. Film grain as **one** adjustment layer over the whole timeline
7. **No intro animation** — rule 12
8. **Subscribe pop-up at S8 only.** Visual, over continuing narration, no spoken mention — rule 13

---

## Regenerating or editing any frame

The SVGs are editable in Affinity and the text stays live. To re-render from the tokens instead:

```
cd templates
python3 -c "
import sys; sys.path.insert(0,'.')
from frames import kicker
kicker('15–20%','of GDP','your new subtitle', out='../videos/01_is-ai-a-bubble-ask-the-railways/assets/S05_kicker_gdp.svg')
"
```

Available: `title_card` · `chapter_card` · `kicker` · `quote_card` · `timeline` · `table` · `lower_third` · `source_overlay` · `end_card` · `thumbnail`. All pull colour and type from `templates/brand.py`, so they follow the unified `#1B2A4A`.

---

## Tomorrow, in order

| | Step | Budget |
|---|---|---|
| 1 | Read `script.md` aloud once, timed. **Rewrite the Hinglish into your register** | 45 min |
| 2 | Source A1, A2, A3 — or take the fallbacks | 20 min |
| 3 | Record take by take. Say the take number aloud. Room tone at the end | 60 min |
| 4 | Edit — voice first, then visuals | 150 min |
| 5 | Thumbnail from `S00`, then the feed test against three competitors | 30 min |
| 6 | Package: description, chapters, **Sources block**, subtitles | 45 min |
| 7 | `LOG.md` — **log the hours honestly**, or the cost ratchet is invisible | 10 min |

**≈ 6 hours.** Under the 8 you have. The slack is deliberate — first videos overrun.

**Stop-gate:** if step 1 shows the script isn't your voice, spend the time there. **A rewritten script with fallback visuals beats a perfect asset set read badly.**
