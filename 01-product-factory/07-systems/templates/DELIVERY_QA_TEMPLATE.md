# Delivery QA Template

> Copy into product workspace as `qa/TEST_CASES_DELIVERY_PACKAGE.md`.
> Replace `[brand]`, `[product-slug]`, `[Product Name]` with actual values.

---

## Product: [Product Name]

Delivery filenames reference: `[brand]-[product-slug]-delivery.zip`

---

## File Naming

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-001 | Workbook filename uses brand prefix | `[brand]-[product-slug].xlsx` | P0 |
| D-002 | PDF guide filename uses brand prefix | `[brand]-[product-slug]-quick-start-guide.pdf` | P0 |
| D-003 | ZIP filename uses brand prefix | `[brand]-[product-slug]-delivery.zip` | P0 |
| D-004 | Copy link filename is standard | `google-sheets-copy-link.txt` | P1 |
| D-005 | No version numbers in buyer-facing filenames | None present | P0 |

## ZIP Contents

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-006 | ZIP contains exactly 3 files | xlsx, pdf, txt | P0 |
| D-007 | ZIP has flat structure (no subdirectories) | Flat | P1 |
| D-008 | ZIP contains no internal docs | No .md, .html, QA files | P0 |
| D-009 | ZIP contains no listing assets | No image files | P1 |
| D-010 | ZIP opens without errors | Standard extraction works | P0 |

## Delivery Folder

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-011 | No internal docs in delivery folder | No QA checklists, build notes | P0 |
| D-012 | `listing-assets/` has 6 screenshots (if applicable) | Correct naming | P1 |

## Google Sheets Copy Link

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-013 | Copy link file exists | `google-sheets-copy-link.txt` | P0 |
| D-014 | Copy link URL works (tested) | Opens GS copy dialog | P0 |
| D-015 | Link file contains brand + instructions | Brand named, usage included | P1 |

## Branding

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-016 | Workbook title includes brand | On Start Here tab | P0 |
| D-017 | PDF title includes brand | In PDF metadata/title | P0 |
| D-018 | No old brand names in delivery | Grep returns 0 matches | P0 |
| D-019 | Support email in PDF | Present | P1 |
| D-020 | Support email in copy link file | Present | P1 |

---

## Verification Commands

```powershell
# Brand consistency scan
Get-ChildItem -Recurse -LiteralPath "delivery\" | Select-String -Pattern "OldBrand" -CaseSensitive

# ZIP content verification
$zip = "delivery\[brand]-[product-slug]-delivery.zip"
if (Test-Path $zip) { Expand-Archive -Path $zip -DestinationPath "$env:TEMP\zipcheck" -Force; Get-ChildItem "$env:TEMP\zipcheck" }

# Version number scan
Get-ChildItem -Recurse -LiteralPath "delivery\" -File | Where-Object { $_.Name -match "v\d+" }
```
