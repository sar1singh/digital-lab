# Asset 4: Payment Tracker Screenshot (`04-secondary-feature.png`)

**Purpose:** Show payment tracking with VLOOKUP-linked client names and payment methods.
**Output file:** `listing-assets/04-payment-tracker.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** Payment Tracker tab + optional Client Name VLOOKUP inset

---

## Capture Instructions

**Source:** Google Sheets → Payment Tracker tab

**Crop area (primary):**
- **Top:** Row 1 (column headers)
- **Bottom:** Row 16 (last payment entry)
- **Left:** Column A
- **Right:** Column G

**Zoom level:** 100%

**Pre-capture steps:**
1. Open Payment Tracker tab in Google Sheets
2. Hide formula bar and gridlines
3. Deselect all cells
4. Optionally select cell C2 to show the VLOOKUP formula in the formula bar, THEN capture a secondary inset showing the formula

---

## Elements Must Be Visible

### Payment Tracker Table (all 15 payments)

| Column | Description | Sample Values |
|--------|-------------|---------------|
| A: Payment ID | Unique identifier | PAY-001 through PAY-015 |
| B: Invoice ID | Links to Invoice Register | INV-001, INV-002, etc. |
| C: Client Name | Auto-populated via VLOOKUP | Sarah Chen, James Wilson, etc. |
| D: Payment Date | Date of payment | Jan 20, 2025, etc. |
| E: Payment Method | Dropdown: Bank Transfer, PayPal, etc. | Bank Transfer, PayPal, Cash |
| F: Amount | Payment amount | Various |
| G: Notes | Optional notes | "Full payment", "Partial payment", etc. |

### VLOOKUP Formula (optional inset)
If creating a formula callout inset:
- **Inset box** top-right corner
- **Source cell:** C2
- **Formula displayed:** `=IFERROR(VLOOKUP(B2,'Invoice Register'!A:E,5,FALSE),"")`
- **Callout arrow** from inset to the Client Name column

---

## Annotations / Callouts

| Callout | Position | Text |
|---------|----------|------|
| 1 | Above C column | "Client names auto-linked from Invoice Register" |
| 2 | Right of Payment Method | "Payment method dropdown — customizable in Settings" |
| 3 | Right of Amount column | "Track every payment against invoices" |

---

## Title Overlay

```
Payment Tracking
Auto-linked payments, methods, and client names
```

---

## Acceptance Criteria

- [ ] All 15 payment entries visible
- [ ] Client Name column shows real names (not error values)
- [ ] Payment Method dropdown values visible (at least 2–3 methods shown)
- [ ] Amount values all positive numbers
- [ ] Gridlines hidden
- [ ] Formula bar hidden (unless showing VLOOKUP inset)
- [ ] No #REF!, #VALUE!, #DIV/0! errors in Client Name column
- [ ] Payment IDs sequentially numbered (PAY-001 through PAY-015)

---

## QA Checklist

- [ ] 15 payment rows visible (PAY-001 to PAY-015)
- [ ] Client Names match Invoice Register data
- [ ] At least 3 payment methods visible (Bank Transfer, PayPal, Cash, etc.)
- [ ] All payment amounts are positive
- [ ] Payment amounts match expected sample data
- [ ] VLOOKUP formula correctly shown as `=IFERROR(VLOOKUP(...), "")`
- [ ] No spelling errors in column headers
- [ ] Dropdown arrows visible on Payment Method column (E)
