# Asset 2: Dashboard Screenshot (`02-dashboard.png`)

**Purpose:** First impression of product value — shows the real-time business overview.
**Output file:** `listing-assets/02-dashboard.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** Dashboard tab in Google Sheets (columns A–F, rows 1–30)

---

## Capture Instructions

**Source:** Google Sheets → Dashboard tab

**Crop area:**
- **Top:** Row 1 (start of tab — no title bar)
- **Bottom:** Row 30 (after last Top Clients entry)
- **Left:** Column A
- **Right:** Column F (enough to capture Revenue by Month)

**Zoom level:** 100% (default Google Sheets view)

**Pre-capture steps:**
1. Open Dashboard tab in Google Sheets
2. Hide the formula bar (View → Show → Formula bar)
3. Hide gridlines (View → Show → Gridlines)
4. Ensure no cell is selected (click an empty area)
5. Wait for all formulas to finish calculating

---

## Elements Must Be Visible

### 1. KPI Cards (rows 1–10)
All 9 KPI labels and values:

| Label | Expected Value |
|-------|---------------|
| Total Revenue | $54,560.00 |
| Paid Revenue | $18,700.00 |
| Outstanding Revenue | $28,520.00 |
| Total Invoices | 25 |
| Paid Invoices | 10 |
| Unpaid Invoices | 15 |
| Overdue Invoices | 7 |
| Active Clients | 8 |
| Average Invoice Value | $2,182.40 |

### 2. Revenue by Month (rows 13–16)
| Month | Value |
|-------|-------|
| Jan 2025 | $16,610.00 |
| Feb 2025 | $14,190.00 |
| Mar 2025 | $18,040.00 |
| Apr 2025 | $5,720.00 |

### 3. Invoice Status Breakdown (rows 18–22)
| Status | Count |
|--------|-------|
| Paid | 10 |
| Sent | 6 |
| Partial | 2 |
| Overdue | 7 |
| Draft | 0 |

### 4. Top Clients by Revenue (rows 24–29)
Show at least the top 3 client names and their revenue values.

---

## Annotations / Callouts

Apply numbered callout circles (red #C62828, white text, 28px diameter) positioned at:

| Callout | Position | Text |
|---------|----------|------|
| 1 | Upper-left of KPI area | "Real-time revenue KPIs — auto-calculated from your invoices" |
| 2 | Right of Revenue by Month | "Monthly revenue breakdown — track trends over time" |
| 3 | Below Status Breakdown | "Invoice status at a glance — Paid, Sent, Overdue & more" |
| 4 | Right of Top Clients | "Top clients by revenue — see your best customers" |

**Callout line style:** 2px red stroke, 45° angle from circle to described area.

**Annotation note placement:** Callout text appears outside the image border (or as overlaid semi-transparent bar at bottom).

---

## Title Overlay

If adding text overlay on the image:

```
Dashboard Overview
Real-time metrics, revenue breakdown, and client insights
```

**Font:** Calibri Bold/Regular, white text with dark semi-transparent bar below

---

## Acceptance Criteria

- [ ] All 9 KPI cards visible with correct values
- [ ] Revenue by Month section shows 4 months of data
- [ ] Invoice Status Breakdown shows all 5 statuses
- [ ] Top Clients section shows at least 3 clients
- [ ] Gridlines hidden
- [ ] Formula bar hidden
- [ ] No cell selection active
- [ ] No #REF!, #VALUE!, #DIV/0! errors visible
- [ ] Callouts clearly point to described features
- [ ] Brand name "Nivora" appears (on Start Here tab reference or overlay)

---

## QA Checklist

- [ ] All KPI values match workbook expected values
- [ ] Month values sum to $54,560.00
- [ ] Status counts sum to 25
- [ ] No errors or warnings displayed
- [ ] Gridlines + formula bar both hidden
- [ ] Crop includes all 4 sections without clipping
- [ ] Callouts legible and correctly positioned
