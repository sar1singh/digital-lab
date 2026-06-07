# Asset 3: Invoice Generator Screenshot (`03-primary-feature.png`)

**Purpose:** Demonstrate the core invoice generator — the main reason someone buys.
**Output file:** `listing-assets/03-primary-feature.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** Invoice Generator tab in Google Sheets (columns A–E, rows 1–40)

---

## Capture Instructions

**Source:** Google Sheets → Invoice Generator tab

**Crop area:**
- **Top:** Row 1 (top of invoice)
- **Bottom:** Row 36 (end of Payment Instructions)
- **Left:** Column A
- **Right:** Column E

**Zoom level:** 100%

**Pre-capture steps:**
1. Open Invoice Generator tab in Google Sheets
2. Hide formula bar (View → Show → Formula bar)
3. Hide gridlines (View → Show → Gridlines)
4. Deselect all cells (click empty area)
5. Ensure the invoice preview looks complete and professional

---

## Elements Must Be Visible

### Header Section
- "INVOICE" title (large, bold)
- Invoice Number: INV-001
- Invoice Date: Jan 5, 2025
- Due Date: Feb 5, 2025

### From Section
- Your Name/Company field (can show default or sample)
- Address field

### Bill To Section
- Client Name: Sarah Chen
- Address field

### Line Items (3 items)
| Description | Quantity | Rate | Amount |
|------------|----------|------|--------|
| Brand identity design | 40 | $75.00 | $3,000.00 |
| Website development | 10 | $150.00 | $1,500.00 |
| Social media graphics | 5 | $100.00 | $500.00 |

### Summary Section
| Line | Value |
|------|-------|
| Subtotal | $5,000.00 |
| Tax Rate | 10% |
| Tax Amount | $500.00 |
| Total | $5,500.00 |

### Payment Instructions Section
- Payment instructions text visible
- Bank transfer details (sample)
- Contact email visible

---

## Annotations / Callouts

| Callout | Position | Text |
|---------|----------|------|
| 1 | Near Total value | "Auto-calculated total — subtotal + tax" |
| 2 | Near Line Items area | "Add items with quantity, rate, and auto-amount" |
| 3 | Near Subtotal/Tax | "Tax auto-calculated from your default rate" |

---

## Title Overlay

```
Professional Invoice Generator
Printable, auto-calculating, and ready to send to clients
```

---

## Acceptance Criteria

- [ ] "INVOICE" title visible at top
- [ ] All 3 line items visible with correct values
- [ ] Subtotal shows $5,000.00
- [ ] Tax Amount shows $500.00
- [ ] Total shows $5,500.00
- [ ] Payment Instructions section visible
- [ ] Gridlines hidden
- [ ] Formula bar hidden
- [ ] No cell selected
- [ ] Invoice fits within a single printable area
- [ ] No formula text visible (only calculated values)

---

## QA Checklist

- [ ] Line item values: 40×75=3,000, 10×150=1,500, 5×100=500
- [ ] Subtotal = 3,000 + 1,500 + 500 = $5,000.00
- [ ] Tax = 10% of $5,000 = $500.00
- [ ] Total = $5,000 + $500 = $5,500.00
- [ ] Client name "Sarah Chen" matches sample data
- [ ] Invoice Number INV-001 visible
- [ ] All text readable at full resolution
- [ ] No debug text, TODO, or internal notes visible
