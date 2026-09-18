# Video 1 — Sources

Format per `RUNBOOK.md` → PART `15_SCRIPT-FORMAT` §2b. **Every factual claim in `script.md` traces to an ID here.**

`Opened` is the date the document was actually read. `Read` says how much — **"abstract only" is honest and must be stated**, because a claim resting on an abstract is weaker than one resting on a page.

---

## R1

```
Author / publisher:  Andrew Odlyzko, University of Minnesota
Title:               Collective Hallucinations and Inefficient Markets:
                     The British Railway Mania of the 1840s
Date:                15 January 2010
URL:                 https://ssrn.com/abstract=1537338
Opened:              2026-09-13
Read:                ABSTRACT ONLY — the 322-page PDF is not read
On-screen credit:    Odlyzko, 2010
```

**Claims it supports — all verbatim from the abstract:**

| Script | Quoted text |
|---|---|
| `[TAKE 4]` | "the greatest technology mania in history" |
| `[TAKE 6]` | "trustworthy quantitative measures" existed showing "there would not be enough demand for railway transport to provide the expected revenues and profits" |
| `[TAKE 6b]` | investors ignored them "for several years… until the lines were placed in service" |
| `[TAKE 7]` | investors "included Charles Darwin, John Stuart Mill, and the Bronte sisters" |
| `[TAKE 7]` | "a collective hallucination" |
| `[TAKE 10]` | the 1830s mania "collapsed prematurely… as projects started during its exuberant phase became successful" |
| `[TAKE 10]` | it "demonstrates the difficulty in identifying bubbles that are truly irrational" |

⚠️ **Limitation to respect:** abstract only. **Do not add any figure, date or detail attributed to R1 beyond the rows above** without opening the full PDF and updating `Read:`.

---

## R2

```
Author / publisher:  Andrew Odlyzko, University of Minnesota
Title:               The railway mania of the 1860s and financial innovation
Date:                Revised 3 March 2024 / 16 April 2024
URL:                 https://www-users.cse.umn.edu/~odlyzko/doc/mania18.pdf
Opened:              2026-09-13
Read:                FULL TEXT
On-screen credit:    Odlyzko, 2024
```

**Claims it supports:**

| Script | Quoted text |
|---|---|
| `[TAKE 5]` | "The two railway manias of the 1840s and 1860s involved capital investments of 15 to 20% of GDP, comparable to £300 to 400 billion for UK or $3 to 4 trillion for USA today. (These were not stock market valuations, but actual funds provided by investors.)" |
| `[TAKE 8]` | the 1840s mania "turned out to be an investment disaster, but provided the country with a nationwide communication network of great utility" |
| — | "The outcome was ruin to many individuals and businesses, and a large, but inefficient, expansion of the rail network" |
| not in script | §10: railway legislation "automatically offered limited liability to investors" — **the correction in `RESEARCH.md` §2.** Keeps "unlimited liability" out of the script |

**Say the GDP figure as he frames it** — actual funds provided by investors, *not* market valuation. Dropping that clause changes the claim.

---

## NOT SOURCED — claims deliberately absent from the script

These were considered and **cut rather than marked `[VERIFY]`**, because an unsourced claim in a recorded script becomes a published one.

| Claim | Why cut |
|---|---|
| ~8,590 miles of track authorised 1845–47 | Search-result summary only. Never opened |
| Paid-up capital £30m → £100m+ by 1849 | Same |
| Average ordinary dividend 1.83% in 1850 | Same |
| 10% deposit on subscription | Same. `[TAKE 11]` says "part-paid shares" and "calls" qualitatively instead — no percentage |
| **How AI capex is actually financed** | **Nothing opened.** This is why `[TAKE 11]` is labelled on screen as inference rather than stated as fact |

---

## Description Sources block — paste this

```
Sources:
- Andrew Odlyzko, "Collective Hallucinations and Inefficient Markets:
  The British Railway Mania of the 1840s", University of Minnesota, 2010
  — https://ssrn.com/abstract=1537338
- Andrew Odlyzko, "The railway mania of the 1860s and financial innovation",
  University of Minnesota, revised 2024
  — https://www-users.cse.umn.edu/~odlyzko/doc/mania18.pdf

The claim about how today's AI buildout is financed is labelled on screen as
inference. It is not documented here, and I have not verified it.
```

**Pre-publish check:** every `⟨src:⟩` ID in `script.md` appears above, and every ID above appears in the block. Mismatch either way is a bug.

**Archival image credits get added here too** once A1, A2 and A3 are chosen — with each item's own rights statement, not the collection's.
