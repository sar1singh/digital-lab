# Test Cases: Screenshots — Invoice Generator & Payment Tracker

**QA Layer:** 7 (Marketplace Asset QA)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

---

## Common Requirements (All 6 Images)

| ID | Check | Method |
|----|-------|--------|
| SS-C-001 | Width ≥ 1200px | Open in image editor, check dimensions |
| SS-C-002 | Aspect ratio consistent across all 6 images | Compare width/height ratios |
| SS-C-003 | PNG format (not JPEG, not GIF) | Check file extension + format properties |
| SS-C-004 | No browser chrome, bookmarks, tabs, or personal data | Visual inspection |
| SS-C-005 | Text legible at 280px thumbnail width | Scale image to 280px wide, read all text |
| SS-C-006 | Brand name "Nivora" appears on cover + at least 2 other images | Visual inspection |
| SS-C-007 | No spelling errors in any visible text | Read all text |
| SS-C-008 | No old brand names or internal identifiers | Scan for old names |
| SS-C-009 | File naming matches convention: `NN-feature-description.png` | Verify filenames |
| SS-C-010 | Images ordered correctly for marketplace upload (1–6) | Confirm sequence |

---

## Image-Specific Checks

### 01-cover.png

| ID | Check | Expected |
|----|-------|----------|
| SS-001-01 | Headline present | "Nivora Invoice Generator & Payment Tracker" |
| SS-001-02 | Subheadline present | "Create, track, and manage invoices — all in one spreadsheet." |
| SS-001-03 | Feature bullets count | 5 bullets with checkmark icons |
| SS-001-04 | Excel + Google Sheets badge visible | Top-right corner |
| SS-001-05 | Instant Download badge visible | Below Excel badge |
| SS-001-06 | Dashboard inset shows KPI data | Real values ($54,560, etc.) |
| SS-001-07 | Background uses dark navy gradient | #0D1B2A → #1B2838 |
| SS-001-08 | No browser chrome or personal data | Clean composition |
| SS-001-09 | Dimensions: 1200 × 800 px | 3:2 aspect ratio |
| SS-001-10 | Text legible at thumbnail size | 280px width test |

### 02-dashboard.png

| ID | Check | Expected |
|----|-------|----------|
| SS-002-01 | All 9 KPI cards visible | Revenue, Paid, Outstanding, Invoices, etc. |
| SS-002-02 | KPI values match sample data | Total Revenue: $54,560.00, etc. |
| SS-002-03 | Revenue by Month visible | 4 months with values |
| SS-002-04 | Month values sum to $54,560.00 | Jan+Feb+Mar+Apr = total |
| SS-002-05 | Invoice Status Breakdown visible | Paid 10, Sent 6, Partial 2, Overdue 7, Draft 0 |
| SS-002-06 | Top Clients section visible | At least 3 client names |
| SS-002-07 | Gridlines hidden | Visual inspection |
| SS-002-08 | Formula bar hidden | Visual inspection |
| SS-002-09 | No cell selected | No highlighted cell border |
| SS-002-10 | No formula errors visible | No #REF!, #VALUE!, #DIV/0! |

### 03-primary-feature.png

| ID | Check | Expected |
|----|-------|----------|
| SS-003-01 | "INVOICE" title visible | Bold, prominent |
| SS-003-02 | All 3 line items visible | Items with Qty × Rate = Amount |
| SS-003-03 | Line item calculations correct | 40×75=3,000, 10×150=1,500, 5×100=500 |
| SS-003-04 | Subtotal = $5,000.00 | Sum of 3 line item amounts |
| SS-003-05 | Tax Amount = $500.00 | 10% of subtotal |
| SS-003-06 | Total = $5,500.00 | Subtotal + Tax |
| SS-003-07 | Payment Instructions visible | Bottom section |
| SS-003-08 | Client details visible | Sarah Chen shown |
| SS-003-09 | Gridlines hidden | Visual inspection |
| SS-003-10 | Formula text not visible | Only calculated values shown |

### 04-secondary-feature.png

| ID | Check | Expected |
|----|-------|----------|
| SS-004-01 | All 15 payment entries visible | PAY-001 to PAY-015 |
| SS-004-02 | Client Name column shows real names | No errors/blank |
| SS-004-03 | Payment Method column shown | At least 2–3 methods visible |
| SS-004-04 | Amount column values positive | All > 0 |
| SS-004-05 | VLOOKUP formula (if inset) correct | `=IFERROR(VLOOKUP(...), "")` |
| SS-004-06 | Gridlines hidden | Visual inspection |
| SS-004-07 | No formula errors | No #REF!, #VALUE! |
| SS-004-08 | Payment IDs sequential | PAY-001 through PAY-015 |

### 05-advanced-features.png

| ID | Check | Expected |
|----|-------|----------|
| SS-005-01 | All 10 client entries visible | CL-001 to CL-010 |
| SS-005-02 | All 8 column headers present | Client ID, Name, Company, Email, Phone, Address, Status, Notes |
| SS-005-03 | Status column shows multiple statuses | Active, Inactive, Archived |
| SS-005-04 | Active count visible | 8 Active clients |
| SS-005-05 | Gridlines hidden | Visual inspection |
| SS-005-06 | No cell selected | Visual inspection |
| SS-005-07 | Contact info readable | Names, companies, emails visible |

### 06-whats-included.png

| ID | Check | Expected |
|----|-------|----------|
| SS-006-01 | "What's Included" header | Prominent title |
| SS-006-02 | 8 deliverable items | 2-column × 4-row grid |
| SS-006-03 | Invoice Generator listed first | Primary feature position |
| SS-006-04 | Excel + Google Sheets listed | Cross-platform note |
| SS-006-05 | Quick-Start PDF Guide listed | PDF deliverable |
| SS-006-06 | Each item has icon, title, description | Visual inspection |
| SS-006-07 | Bottom bar with "Instant Download · Nivora" | Dark bar at bottom |
| SS-006-08 | All features from workbook represented | No missing features |
| SS-006-09 | No features not in workbook | No false claims |

---

## Branding Checks

| ID | Check | Applies To |
|----|-------|------------|
| SS-B-001 | "Nivora" appears on cover image | 01-cover.png |
| SS-B-002 | "Nivora" appears on dashboard image | 02-dashboard.png (via Start Here reference or overlay) |
| SS-B-003 | "Nivora" appears on What's Included | 06-whats-included.png |
| SS-B-004 | No competing brand names visible | All images |
| SS-B-005 | Font styling consistent across set | All images |

---

## Consistency Checks

| ID | Check | Method |
|----|-------|--------|
| SS-X-001 | Same aspect ratio on all 6 images | Compare dimensions |
| SS-X-002 | Same color temperature across non-cover images | Visual comparison |
| SS-X-003 | Callout style consistent (font, size, color) | Compare callout annotations |
| SS-X-004 | Overlay title style consistent | Compare title overlays |
| SS-X-005 | All images use real sample data (no empty sheets) | Visual inspection |

---

## Readability Checks

| ID | Check | Method |
|----|-------|--------|
| SS-R-001 | All text readable at 100% zoom | Visual inspection |
| SS-R-002 | All text readable at 280px thumbnail width | Scale down test |
| SS-R-003 | No text cut off at crop boundaries | Check margins |
| SS-R-004 | Sufficient contrast between text and background | Contrast ratio check |
| SS-R-005 | No overlapping text or callouts | Visual inspection |

---

## Summary

| Area | Total Tests |
|------|-------------|
| Common requirements | 10 |
| Cover image (01) | 10 |
| Dashboard (02) | 10 |
| Invoice Generator (03) | 10 |
| Payment Tracker (04) | 8 |
| Client Management (05) | 7 |
| What's Included (06) | 9 |
| Branding | 5 |
| Consistency | 5 |
| Readability | 5 |
| **Total** | **79** |
