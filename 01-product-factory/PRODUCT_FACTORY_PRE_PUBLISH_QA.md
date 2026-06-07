# Product Factory Pre-Publish QA

> Consolidated QA process that every product must pass before publishing. All items must be verified before the listing goes live.

---

## QA Process Overview

```
Content Review → Branding Review → Packaging Review
→ Marketplace Review → Delivery Review → Gate Decision
```

Each review is a standalone pass. All must pass. No partial gate passes.

---

## 1. Content Review

Verify the product itself is correct and complete.

### Workbook
- [ ] All tabs created and named correctly
- [ ] All formulas return expected results — no #REF!, #VALUE!, #DIV/0! errors
- [ ] Cross-sheet SUMIF/COUNTIF references verified against correct columns
- [ ] Dashboard summary values match source data (spot-check 3+ values)
- [ ] Data validation dropdowns work on all required columns
- [ ] Conditional formatting applied and correct
- [ ] Freeze panes set on data tabs
- [ ] Formula cells marked (gray background), input cells clear
- [ ] Sample data populated and realistic
- [ ] No hardcoded values where formulas should exist
- [ ] IFERROR wrappers present where division by zero is possible
- [ ] Charts render correctly (if applicable)
- [ ] Print layout acceptable — no cutoff content

### Google Sheets
- [ ] Workbook uploads to Google Drive without errors
- [ ] All formulas survive conversion
- [ ] Conditional formatting survives conversion
- [ ] Data validation dropdowns work in Google Sheets
- [ ] Charts render in Google Sheets (if applicable)
- [ ] Copy link works (test manually)
- [ ] Navigation instructions are clear (hyperlinks likely broken — use plain text)

### PDF Guide
- [ ] Title includes brand: "Nivora {Product Name}"
- [ ] Support email included (workbysar1@gmail.com)
- [ ] Basic usage instructions present and accurate
- [ ] File naming uses brand prefix
- [ ] PDF opens without errors
- [ ] Content matches the final workbook version

---

## 2. Branding Review

Verify brand consistency across all buyer-facing content.

- [ ] Brand name (Nivora) appears consistently on all buyer-facing content
- [ ] No personal email used as brand name
- [ ] Support email (workbysar1@gmail.com) is contact-only, not brand
- [ ] No "Work by Sar1" anywhere in buyer-facing content
- [ ] All delivery filenames start with `nivora-`
- [ ] PDF title includes "Nivora"
- [ ] Marketplace publisher line is "by Nivora"
- [ ] Listing title uses consistent brand format
- [ ] Brand appears on cover image and where appropriate on other assets
- [ ] Brand consistency scan passed (automated grep for old names = 0 matches in delivery/)

**Grep command:**
```powershell
Get-ChildItem -Recurse -LiteralPath "delivery\" | Select-String -Pattern "Work by Sar1" -CaseSensitive
```
Expected: 0 matches.

---

## 3. Packaging Review

Verify the delivery package is clean and professional.

- [ ] ZIP contains exactly 3 files: workbook, PDF guide, copy link
- [ ] No subdirectories inside ZIP
- [ ] All filenames in ZIP use brand prefix (`nivora-*`)
- [ ] No version numbers in buyer-facing filenames
- [ ] No internal files in ZIP (QA docs, source files, screenshots, listing assets)
- [ ] No duplicate files in ZIP
- [ ] ZIP opens without errors
- [ ] ZIP contents verified programmatically against expected file list
- [ ] Delivery folder contains only buyer-facing assets
- [ ] No internal/planning/QA documents in delivery/ folder
- [ ] No temporary screenshots in delivery/ folder
- [ ] No release notes in delivery/ folder

---

## 4. Marketplace Review

Verify the listing is complete and accurate.

### Listing Copy
- [ ] Title is clear and searchable: `{Product Name} — Google Sheets + Excel`
- [ ] Publisher line: "by Nivora"
- [ ] What's Included section lists specific deliverables (not generic descriptions)
- [ ] Who It's For section targets the right buyer
- [ ] Benefits address buyer pain points (not just features)
- [ ] FAQ answers common hesitations
- [ ] Support contact included (workbysar1@gmail.com)
- [ ] Price set

### Images
- [ ] All 6 gallery images uploaded in correct order:
  1. Cover
  2. Dashboard
  3. Primary Feature
  4. Secondary Feature
  5. Supporting Feature
  6. What's Included
- [ ] Cover image set as thumbnail
- [ ] Images match the final workbook (not an earlier version)
- [ ] Text is legible at marketplace display sizes
- [ ] No browser chrome or personal info in screenshots

### Product File
- [ ] ZIP uploaded as product file on marketplace
- [ ] ZIP is the final branded version (no old versions)

### Checkout
- [ ] Test purchase / preview mode works end-to-end
- [ ] Buyer receives download instructions
- [ ] Download links work

---

## 5. Delivery Review

Verify the buyer experience from purchase through first use.

- [ ] Buyer can understand the product in 10 seconds from title + cover
- [ ] After purchase, buyer receives clear download/access instructions
- [ ] Google Sheets copy link works immediately (test from incognito)
- [ ] Excel file opens without errors
- [ ] PDF guide is included and complete
- [ ] No broken references or missing files in delivery
- [ ] First-time user can start using the product without external help
- [ ] Dashboard formulas show correct values on first open
- [ ] Branding is consistent across all delivered files
- [ ] Marketplace copy accurately describes what the buyer receives

---

## Review Results Tracking

For each product, record review results:

```
Product: {Name}
Date: {date}
Content Review: [PASS/FAIL]
Branding Review: [PASS/FAIL]
Packaging Review: [PASS/FAIL]
Marketplace Review: [PASS/FAIL]
Delivery Review: [PASS/FAIL]
Overall: [PASS/FAIL]
Gate Decision: [READY TO PUBLISH / BLOCKED]
Notes: {any issues found and resolved}
```

---

## Failed Review Protocol

If any review fails:
1. Note which section(s) failed
2. Fix the issue(s)
3. Re-run the affected review(s)
4. Do not proceed until ALL sections pass

**Single fail = full block.** No exceptions.
