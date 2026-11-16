# ThinkLate Franchise Spec v1: "The Fine Print"
Drafted 2026-11-06. Franchise = **consumer economics: how companies quietly take your money / ownership / control.**
Everything here is built for: AI voice, AI visuals, public footage, free DaVinci Resolve, ~6 h/week.

---

## 1. The promise (one sentence)
> "In under 45 seconds (or 6 minutes), I show you the hidden mechanism behind something that already annoys you, with receipts."

- **Viewer:** 20–45, US/UK/India, paying for subscriptions, fees and devices they don't really own.
- **Your edge:** you always show the mechanism and the document (a filing, a terms-of-service page, a docket), not just the outrage.
- **Never:** tell viewers what to buy or invest in. Say what happened and why.

## 2. Title formulas (reuse, don't template the content)
**Shorts (≤ 5 words):**
1. `[Brand] Charges You Rent`
2. `You Don't Own [Thing]`
3. `The [Fee] Nobody Mentions`
4. `Why [Thing] Costs More`
5. `[Brand]'s Hidden Switch`

**Long-form (≤ 50 characters):**
1. `How [Company] Turned [Thing] Into Rent`
2. `The Real Price of [Thing]`
3. `Why You Can't Cancel [Thing]`
4. `[Company] Knew. Here's the Document.`

Rules: no hashtags in titles, a concrete noun in the first 3 words, and the title must match the video's number. (S1 said "800%" in the title and "$22" in the thumbnail, and the video itself said "$20".)

## 3. Beat sheets

### Short, 40 s, ~105 words
| Time | Beat | Visual |
|---|---|---|
| 0–2 s | **Hook:** one number or conflict | Big caption + strongest image |
| 2–10 s | **Stakes:** who pays, who profits | Evidence screenshot |
| 10–30 s | **3 beats**, joined by "but"/"therefore" | Change every 3–4 s |
| 30–37 s | **Reveal:** the mechanism | Chart or document highlight |
| 37–40 s | **Loop line** echoing the hook | Returns to the first image |

### Long-form, ~6 min, ~900 words
| Time | Beat |
|---|---|
| 0:00–0:20 | Cold open: the conflict, with a number |
| 0:20–0:40 | Promise: what they'll know by the end |
| 0:40–4:30 | 4 beats; each ends with an open question the next beat answers |
| 4:30–5:30 | Payoff: the mechanism, in one sentence |
| 5:30–6:00 | Close: one line, no advice, no "like and subscribe" speech |

Banned: "Act 1", "Chapter", "do the math", "let me give you a picture first". Chapters (5–7 max) go in the description only.

## 4. Hook templates (pick one per video)
1. **The bait-and-switch:** "You paid \$[X] for [Thing]. [Company] still controls it."
2. **The switch you didn't know existed:** "There's a software flag inside your [Thing]."
3. **The fee that isn't on the price tag:** "The \$[X] listed isn't what you pay."
4. **The cancel maze:** "Signing up took 1 click. Cancelling takes [N]."
5. **The shrink:** "Same box, same price, [X]% less."
6. **The paper trail:** "It's in the terms. Page [N]."
7. **The lawsuit:** "[Agency] sued [Company] over this."
8. **The scale:** "[N] million people. One click."

## 5. Style bible (A/B test, then lock for 90 days)
Generate the same scene (a person looking at a bill, a locked car seat) in both styles. Choose in 30 minutes.

**Style A: Editorial ink-and-paper (closest to your V1)**
> Editorial ink-and-paper illustration, warm cream paper texture, bold black outlines, flat shading, limited palette: cream #F4EBD9, ink navy #14213D, signal red #D62828, mustard #F2A900, slight film grain, no text in the image, no real people's faces.

**Style B: 2D flat vector (matches your Rule 15 thumbnails)**
> Flat 2D vector illustration, clean bold outlines, saturated palette on deep navy, cel-shaded, single focal object, no text in the image, no real people's faces.

Locked rules (either style):
- Add all text in DaVinci (not in the AI image) so spelling is perfect.
- Never generate faces of real people. Use archival photos from Wikimedia Commons.
- Captions: bold sans-serif, 2–3 words, keyword highlighted in the accent color.
- Thumbnail: one prop, one emotion, 2–3 words in a top banner, same style as the video.

## 6. Shot-list template (copy per video)
| # | Script line | Visual type | Source / prompt | Length | License |
|---|---|---|---|---|---|
| 1 | | stock / evidence / AI still / chart | | 3–5 s | |

Mix target: ~40% stock or AI, ~30% evidence screenshots, ~30% charts and text.

## 7. Source ledger (one per video; paste a short form into the description)
| Claim | Primary source | URL | Date checked |
|---|---|---|---|

No claim goes in the script without a row. If you can't source it, cut it or soften it.

## 8. Audio spec
- One narrator voice, same on every upload.
- Generate per paragraph (3–5 sentences), 3 takes, keep the best.
- Trim gaps to ~0.15 s. Music at about -22 dB under the voice.
- **Export at about -14 LUFS.** Optional one-liner: `ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy out.mp4`.

## 9. Pre-publish checklist (the silent-Short rule)
- [ ] Play the **last 10 seconds on your phone with sound.** Audio must be present.
- [ ] Short is 9:16, 30–45 s; long-form is 16:9.
- [ ] Title number = thumbnail number = video number.
- [ ] Loudness about -14 LUFS (not -24).
- [ ] No game, TV or movie footage.
- [ ] Source ledger complete; description lists sources.
- [ ] Tags: only your own topic words (no other channels' names).
- [ ] Manual captions checked (no "morts" or other misrecognitions).
- [ ] Synthetic-media disclosure ticked where footage looks real.

## 10. First 10 topics (angles only; **verify every fact before scripting**)
| # | Topic | Format | Primary source to find | Note |
|---|---|---|---|---|
| 1 | Heated-seat subscriptions | Short | Press coverage + company statement | Already researched in V4 |
| 2 | Printer-ink cartridge lockouts | Short | Terms of service + consumer-agency filings | |
| 3 | Games you "buy" but don't own | Short | Store terms, studio announcement | Use stock/AI visuals, **no gameplay** |
| 4 | Resort and hotel fees | Short | Regulator rule or lawsuit docket | |
| 5 | Ticket fees revealed at checkout | Short | Regulator or court filings | |
| 6 | Subscription cancel mazes | Short → long | Regulator complaint | Tag from V4 |
| 7 | Tractor right-to-repair | Short | State bill text | Cite the exact bill |
| 8 | Shrinkflation | Short | Statistical agency data | Evergreen |
| 9 | Data-center power bills | Short | Grid-operator or utility-commission filing | **Re-check the "800%" and "\$22" figures** |
| 10 | The "Rent Economy" synthesis | 6-min long-form | Combine #1–#6 | Build from the best Short |

Before each: run the Day-1 demand check (3+ small channels with 10× views on the topic).

## 11. 90-day plan and review gate
- Weeks 1–3: 3 Shorts/week (9 Shorts, topics 1–9).
- Week 4: 1 long-form (#10).
- Weeks 5–12: same rhythm, double down on winning hooks.
- **Day 90 gate:** ≥ 20 Shorts and ≥ 6 long-form out. If no Short passed ~5,000 views and subs < 100, change the format or niche (not the tools).

Weekly hours: Day 1 (60 min) demand; Day 2 (75) scripts; Day 3 (90) audio and assets; Day 4 (90) edit; Day 5 (45) publish. About 6 h.
