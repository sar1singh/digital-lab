# Google Sheets Compatibility Notes — Invoice Generator & Payment Tracker

## Known Compatibility Issues (from Product #1)

### Hyperlinks
- openpyxl hyperlinks break in Google Sheets import
- Fix: Replace hyperlinks with plain text navigation instructions on Start Here tab

### Formulas
All formulas in FORMULAS.md are designed for Excel + Google Sheets compatibility.

**Verified compatible:**
- SUM, SUMIF, SUMIFS — work identically
- COUNTIF, COUNTIFS — work identically
- IF, IFERROR — work identically
- TODAY — works in both (note: GS may recalculate on open)
- TEXT — works identically
- VLOOKUP — works identically

**Avoid:**
- INDIRECT — fragile in GS when sheets are renamed
- OFFSET — volatile, can cause performance issues in GS
- XLOOKUP — not available in all Excel versions; VLOOKUP is safer for this product
- Array formulas (CSE) — not needed; use SUMIFS/COUNTIFS instead

### Data Validation
- Excel data validation references to ranges on other sheets may need named ranges for GS compatibility
- Plan: define named ranges in Settings tab for dropdown source values

### Conditional Formatting
- Excel conditional formatting generally survives GS import
- Avoid overly complex CF rules
- Use simple color scales and highlight rules

### VLOOKUP (Payment Tracker — new in QA)
- `=IFERROR(VLOOKUP(B2,'Invoice Register'!A:E,5,FALSE),"")` is GS-compatible
- Single-quoted sheet names (`'Invoice Register'`) are required in both Excel and GS
- Test by uploading and verifying Client Name column resolves correctly

### Draft Status (manual-only — new in QA)
- Auto-status formula never produces "Draft" — GS import maintains this behavior
- "Draft" is available as a manual dropdown/entry option in Settings
- Dashboard formulas exclude Draft via `"<>Draft"` — this pattern is GS-compatible

### Charts
- Excel charts may not render identically in GS
- Dashboard charts should be recreated in GS during QA phase if needed

### Print Layout
- Invoice Generator tab print layout must be tested in both Excel and GS
- Set print area, page breaks, and scaling explicitly

## GS Manual QA Runbook

Detailed step-by-step instructions available in:
`docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md`

Includes: upload, formula verification, VLOOKUP check, dropdown test, dashboard values,
print layout, copy link creation, and troubleshooting.

## QA Results Tracker

Results logging available in:
`qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`

32 test cases covering: tab presence (8), formula integrity (12), dropdowns (2),
dashboard values (7), visual formatting (3). All default to "Pending Manual Test".
