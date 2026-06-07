# Test Cases: Delivery Package — Invoice Generator & Payment Tracker

**QA Layer:** 6 (Delivery Package QA)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

## File Naming

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-001 | Workbook filename uses brand prefix | nivora-invoice-generator-payment-tracker.xlsx | P0 |
| D-002 | PDF guide filename uses brand prefix | nivora-invoice-generator-payment-tracker-quick-start-guide.pdf | P0 |
| D-003 | ZIP filename uses brand prefix | nivora-invoice-generator-payment-tracker-delivery.zip | P0 |
| D-004 | Copy link filename is standard | google-sheets-copy-link.txt | P1 |
| D-005 | No version numbers in any buyer filename | None present | P0 |

## ZIP Contents

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-006 | ZIP contains exactly 3 files | xlsx, pdf, txt | P0 |
| D-007 | ZIP contains no subdirectories | Flat structure only | P1 |
| D-008 | ZIP contains no internal docs | No .md, .html, QA files | P0 |
| D-009 | ZIP contains no listing assets | No PNG files | P1 |
| D-010 | ZIP contains no screenshots | No image files | P1 |
| D-011 | ZIP opens without errors | Standard ZIP extraction works | P0 |

## Delivery Folder

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-012 | Delivery folder has no internal docs | No QA checklists, build notes, planning files | P0 |
| D-013 | Delivery folder contains listing-assets/ (6 PNGs) | 6 files with correct naming | P1 |
| D-014 | Delivery folder contains screenshots/ (optional) | May be empty or contain sources | P2 |

## Google Sheets Copy Link

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-015 | Copy link file exists | google-sheets-copy-link.txt present | P0 |
| D-016 | Copy link URL works (tested manually) | Opens Google Sheets copy dialog | P0 |
| D-017 | Copy link file contains brand and instructions | Nivora named, usage instructions included | P1 |

## Branding

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| D-018 | Workbook title includes "Nivora" | Check workbook properties or Start Here tab | P0 |
| D-019 | PDF title includes "Nivora" | "Nivora Invoice Generator & Payment Tracker" | P0 |
| D-020 | No "Work by Sar1" in any delivery file | grep returns 0 matches | P0 |
| D-021 | Support email present in PDF guide | workbysar1@gmail.com | P1 |
| D-022 | Support email present in copy link file | workbysar1@gmail.com | P1 |

## Verification Commands (run before delivery finalization)

```powershell
# Brand consistency scan
Get-ChildItem -Recurse -LiteralPath "delivery\" | Select-String -Pattern "Work by Sar1" -CaseSensitive
# Expected: 0 matches

# ZIP content verification
$zip = "delivery\nivora-invoice-generator-payment-tracker-delivery.zip"
if (Test-Path $zip) { Expand-Archive -Path $zip -DestinationPath "$env:TEMP\zipcheck" -Force; Get-ChildItem "$env:TEMP\zipcheck" }

# Version number scan
Get-ChildItem -Recurse -LiteralPath "delivery\" -File | Where-Object { $_.Name -match "v\d+" }
# Expected: 0 matches
```
