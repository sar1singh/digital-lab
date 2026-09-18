# ThinkLate Template System

Reusable frame and chart templates. Built so 20–30 videos share one visual format with text swaps only.

**Status:** working, tested. Demo set rendered in `preview/`.

---

## Files

| File | What it is |
|---|---|
| `brand.py` | **Single source of truth** — palette, fonts, canvas, type scale. Change a value here and every template follows |
| `frames.py` | 10 frame types → editable SVG |
| `charts.py` | 4 chart types → on-brand SVG + PNG |
| `preview/` | Rendered demo set. `preview/_sheet_frames.png` and `preview/_sheet_charts.png` are contact sheets |
| `data/` | Put your CSVs here |
| `frames/`, `charts/` | Your real per-video output |

---

## Install the fonts first

The templates reference these by name. Without them installed locally you get fallbacks, which is why serif looks like sans in the rendered previews.

- **Instrument Serif** (or Playfair Display) — headlines
- **IBM Plex Sans** — body and labels
- **IBM Plex Mono** — numbers, sources

All free on Google Fonts. Install to the OS, not just to an app.

---

## Usage

### Frames

```python
from frames import (title_card, chapter_card, kicker, quote_card,
                    timeline, table, lower_third, source_overlay,
                    end_card, thumbnail)

title_card("Is AI a Bubble?", "Ask the Railways",
           out="frames/v01_00_title.svg")

chapter_card(2, "What the railways actually built",
             out="frames/v01_02_chapter.svg")

kicker("90%", "OF ADVANCED CHIPS", "made on one island",
       out="frames/v01_kicker_chips.svg")

quote_card("The traffic will be there.", "Railway prospectus", "1845",
           source="Source: [verified citation]",
           out="frames/v01_quote_1845.svg")

timeline([("1830", "First intercity line"),
          ("1845", "Mania peaks"),
          ("1847", "Credit tightens")],
         title="Railway mania, start to finish",
         source="Source: [citation]",
         out="frames/v01_timeline.svg")

table(["Bubble", "Peak", "Drawdown", "Asset survived?"],
      [["Railways", "1845", "~85%", "Yes"]],
      title="The asset being real has never prevented a bubble",
      source="Source: [citation]", highlight_col=3,
      out="frames/v01_table.svg")

thumbnail(["IS AI", "NEXT?"], out="frames/v01_thumb.svg")
```

`lower_third()` and `source_overlay()` render on **transparent** backgrounds — overlay them in Resolve.

### Charts

```python
import pandas as pd
from charts import line, bars, stacked_share, slope, from_csv

bars(["China", "United States", "Myanmar"], [69, 12, 11],
     title="Rare earth mine production, share of global output",
     source="Source: USGS Mineral Commodity Summaries 2026",
     highlight="China", pct=True, out="charts/v01_rare_earth")

df = pd.read_csv("data/bubbles.csv")
line(df, x="t", ys=["Railways", "Telecom", "Dot-com"],
     title="Three manias, indexed",
     source="Source: [citation]",
     highlight="Railways", out="charts/v01_manias")

slope("Before", "After",
      {"Suez (days)": (26, 26), "Cape route (days)": (26, 36)},
      title="What rerouting around Africa costs",
      source="Source: UNCTAD", highlight="Cape route (days)",
      out="charts/v01_reroute")
```

Every chart writes `.svg` **and** `.png`, with the source line and wordmark baked in.

---

## Rules the code enforces

Deliberately, so you can't drift:

- **One accent colour per chart** — only the series named in `highlight` gets amber
- **Max 5 series** — `line()` and `stacked_share()` raise an error above that
- **No dual axes, no pie charts** — not implemented
- **Source line is a required argument** on every chart. You cannot render an uncited chart
- **Wordmark on every frame and chart**

---

## Editing in Affinity

SVGs open with live, editable text. To change a design decision across all 30 videos, edit `brand.py` and re-render — don't hand-edit SVGs.

For the thumbnail, replace the placeholder rect in the left 60% with your real chart or archival image.

---

## Resolve workflow

1. Import the SVGs — they scale cleanly at 1920×1080
2. For repeated cards, rebuild `title_card` / `chapter_card` / `kicker` as **Fusion titles** once. Then it's text-field swaps in the timeline, no file regeneration
3. Add **film grain as one adjustment layer** over the whole timeline. `GRAIN` is off in `frames.py` because SVG `feTurbulence` renders inconsistently across Affinity, Resolve and ImageMagick
4. Save a render preset once

---

## Per-video routine

1. Lock the script
2. Mark asset cues in the margin
3. Write one `build_vNN.py` that calls the template functions with this video's text and data
4. Run it — all frames and charts appear in `frames/` and `charts/`
5. Import into Resolve

By video 3 this is roughly 30 minutes of asset work, replacing the several hours that stalled previous attempts.

---

## Known limitations

- `_wrapped()` wraps by character count, not measured text width. Long words in a narrow field can overrun — check the render
- `table()` is comfortable up to 4 columns and 6 rows. Beyond that, split into two frames
- `timeline()` is designed for 3–6 events
- Preview PNGs in `preview/` were rendered without the brand fonts installed, so serif appears as sans. Charts used an installed serif, which is why they look correct
- Figures in the demo set are **illustrative placeholders**. Replace every one with a verified source before publishing
