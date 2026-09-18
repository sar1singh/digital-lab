"""
ThinkLate brand tokens — single source of truth.
Every template and chart imports from here. Change a value once, everything follows.
"""

# ---------------------------------------------------------------- palette
# UNIFIED 2026-09-13: INK was #111827. The brand now owns ONE dark, #1B2A4A,
# shared with the character art. #111827 was functionally greyscale, which meant
# the brand owned no colour at all. Do not reintroduce a second dark.
INK     = "#1B2A4A"   # base / background — same navy as the avatar field
PAPER   = "#F4F1EA"   # text on dark, chart surface
AMBER   = "#D99A2B"   # THE accent. One per frame. Never two.
# SLATE lightened 2026-09-13 from #6B7280, which scored 3.67:1 on the old INK and
# 2.94:1 on the new one — failing WCAG AA (4.5:1) either way. It carries captions and
# the source lines, which is the one place ThinkLate cannot afford to be unreadable.
SLATE   = "#98A2B3"   # secondary lines, captions, sources — 5.52:1 on INK
BRICK   = "#9B3A2F"   # negative values only. Never for emphasis.

# derived — re-derived from the new INK
INK_SOFT   = "#24365C"  # panel fill, one step up from base
PAPER_DIM  = "#A8A29A"  # de-emphasised text on dark
GRID       = "#2E4270"  # chart gridlines on dark

# ---------------------------------------------------------------- type
# Install locally: Instrument Serif (or Playfair Display), IBM Plex Sans, IBM Plex Mono.
# Fallbacks keep SVGs legible on machines without them.
SERIF = "Instrument Serif, Playfair Display, Libre Baskerville, DejaVu Serif, Georgia, serif"
SANS  = "IBM Plex Sans, Inter, DejaVu Sans, Helvetica, Arial, sans-serif"
MONO  = "IBM Plex Mono, DejaVu Sans Mono, Menlo, monospace"

# matplotlib needs bare family names, not CSS stacks
MPL_SERIF = ["Instrument Serif", "Playfair Display", "DejaVu Serif"]
MPL_SANS  = ["IBM Plex Sans", "Inter", "DejaVu Sans"]
MPL_MONO  = ["IBM Plex Mono", "DejaVu Sans Mono"]

# ---------------------------------------------------------------- canvas
W, H = 1920, 1080          # video frame
TW, TH = 1280, 720         # thumbnail

# Title-safe margin. Nothing important outside this.
MARGIN = 120

# ---------------------------------------------------------------- type scale
# Sized for legibility on a TV at ~10 feet. Do not shrink these.
SIZE = {
    "hero":     136,   # video title card
    "h1":        92,   # chapter card
    "h2":        64,   # chart title
    "kicker":   240,   # the one big number
    "quote":     58,
    "body":      40,
    "label":     32,   # chart axis labels
    "caption":   28,   # sources, attribution
}

CHANNEL = "ThinkLate"
TAGLINE = "Master of none, expert of after"
HANDLE  = "@wethinklate"


# ---------------------------------------------------------------- surfaces
# Two surfaces, not one. Dark for data, paper for archive and documents.
# Alternating them across a 20-minute video is what stops it reading as
# one long gloomy slide deck.
SURFACES = {
    "ink": {                      # charts, data, kickers
        "bg":      INK,
        "fg":      PAPER,
        "dim":     PAPER_DIM,
        "rule":    GRID,
        "panel":   INK_SOFT,
        "accent":  AMBER,
    },
    "paper": {                    # quotes, documents, archival, timelines
        "bg":      PAPER,
        "fg":      "#1A1A17",     # warm near-black, not pure black
        "dim":     "#6E6A61",
        "rule":    "#D6D0C4",
        "panel":   "#EAE5DA",
        "accent":  "#A8741A",     # darker amber — #D99A2B fails contrast on paper
    },
}
