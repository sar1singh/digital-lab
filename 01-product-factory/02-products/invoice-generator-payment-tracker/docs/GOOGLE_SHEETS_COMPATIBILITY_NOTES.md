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

### Charts
- Excel charts may not render identically in GS
- Dashboard charts should be recreated in GS during QA phase if needed

### Print Layout
- Invoice Generator tab print layout must be tested in both Excel and GS
- Set print area, page breaks, and scaling explicitly

## GS-Specific Actions During QA

1. Upload XLSX to Google Drive and open in Sheets
2. Verify all formulas show correct values (no #REF!, #VALUE!, #DIV/0!)
3. Verify dropdowns work
4. Verify conditional formatting preserved
5. Create copy link and test from incognito
6. Test print layout of Invoice Generator tab
7. Verify charts render (if included)
8. Check that navigation instructions are clear (hyperlinks won't work)
