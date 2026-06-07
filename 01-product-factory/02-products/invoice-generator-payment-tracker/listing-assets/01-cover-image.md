# Asset 1: Cover Image (`01-cover.png`)

**Purpose:** Primary marketplace thumbnail — drives click-through from search results.
**Output file:** `listing-assets/01-cover.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** N/A — composed graphic

---

## Headline

```
Nivora Invoice Generator & Payment Tracker
```

**Font:** Calibri Bold, 48pt, white (#FFFFFF)
**Position:** Top third of image, left-aligned or centered

---

## Subheadline

```
Create, track, and manage invoices — all in one spreadsheet.
```

**Font:** Calibri Regular, 22pt, light gray (#CCCCCC)
**Position:** Below headline, 10px padding

---

## Feature Bullets

Display as a vertical list with checkmark icons (✅ or green checkmark graphic):

```
• Professional invoice generator with auto-calculations
• Payment tracking with VLOOKUP-linked client names
• Revenue dashboard with real-time KPIs
• Client management with status tracking
• Works in Excel + Google Sheets
```

**Font:** Calibri Regular, 16pt, white (#FFFFFF)
**Position:** Bottom-left or right column depending on layout
**Icon:** Green checkmark (#2E7D32) before each bullet

---

## Badges

**"Excel + Google Sheets" badge:**
- Position: Top-right corner
- Background: Rounded rectangle, dark blue (#1A237E)
- Text: "Excel + Google Sheets" in white, 14pt
- Width: ~200px, Height: ~36px

**"Instant Download" badge:**
- Position: Below Excel/GS badge
- Background: Rounded rectangle, green (#2E7D32)
- Text: "Instant Download" in white, 12pt
- Width: ~160px, Height: ~30px

---

## Background

- Gradient: Dark navy (#0D1B2A) at top, slightly lighter (#1B2838) at bottom
- Subtle grid/pattern overlay for visual depth

---

## Screenshot Inset

- **Source:** Dashboard tab — cropped to show KPI cards row
- **Position:** Center of image, below headline
- **Border:** 2px white stroke, 8px border radius
- **Drop shadow:** 4px offset, 8px blur
- **Scale:** ~80% of original width, positioned to show top KPI area
- **Example values visible:**
  - Total Revenue: $54,560.00
  - Paid Revenue: $18,700.00
  - Outstanding Revenue: $28,520.00
  - Total Invoices: 25

---

## Layout Wireframe

```
┌──────────────────────────────────────────────────┐
│  [Badge: Excel+GS]  [Badge: Instant Download]    │
│                                                   │
│          Nivora Invoice Generator                 │
│                & Payment Tracker                  │
│                                                   │
│     Create, track, and manage invoices —           │
│            all in one spreadsheet.                │
│                                                   │
│     ┌──────────────────────────────────────┐     │
│     │   [Dashboard KPI screenshot inset]   │     │
│     │   Revenue: $54,560 | Paid: $18,700   │     │
│     └──────────────────────────────────────┘     │
│                                                   │
│  ✅ Professional invoice generator               │
│  ✅ Payment tracking with auto-linking           │
│  ✅ Revenue dashboard with real-time KPIs        │
│  ✅ Client management with status tracking        │
│  ✅ Works in Excel + Google Sheets                │
│                                                   │
└──────────────────────────────────────────────────┘
```

---

## Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Background gradient top | Dark navy | #0D1B2A |
| Background gradient bottom | Navy | #1B2838 |
| Headline | White | #FFFFFF |
| Subheadline | Light gray | #CCCCCC |
| Feature bullets | White | #FFFFFF |
| Checkmark icon | Green | #2E7D32 |
| Badge Excel | Dark blue | #1A237E |
| Badge Instant Download | Green | #2E7D32 |
| Inset border | White | #FFFFFF |

---

## Acceptance Criteria

- [ ] Headline reads: "Nivora Invoice Generator & Payment Tracker"
- [ ] Subheadline reads: "Create, track, and manage invoices — all in one spreadsheet."
- [ ] All 5 feature bullets present with checkmarks
- [ ] Excel + Google Sheets badge visible
- [ ] Instant Download badge visible
- [ ] Dashboard screenshot inset shows real KPI data
- [ ] Text is legible at 280px thumbnail width
- [ ] No browser chrome, bookmarks, or personal data
- [ ] Brand name "Nivora" appears prominently
- [ ] Dimensions: 1200 × 800 px (3:2 ratio)

---

## QA Checklist

- [ ] Spelling: all text checked for typos
- [ ] Branding: Nivora name used correctly (not misspelled)
- [ ] Data: values match workbook sample data
- [ ] Legibility: all text readable at thumbnail size
- [ ] Contrast: text/background contrast sufficient
- [ ] Consistency: matches style of other 5 assets
