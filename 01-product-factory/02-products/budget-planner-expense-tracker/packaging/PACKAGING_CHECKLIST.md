# Packaging Checklist — Budget Planner & Expense Tracker

## Pre-Packaging QA

- [ ] Open XLSX in Excel locally
- [ ] Verify all 7 tabs present
- [ ] Verify formulas calculate correctly (Monthly Budget SUMIFs, Dashboard summary)
- [ ] Verify Dashboard values match source tabs
- [ ] Verify charts render
- [ ] Verify sample data is populated and flagged as example
- [ ] Verify data validation dropdowns work on Expense Tracker and Bills Tracker
- [ ] Verify conditional formatting on negative variance (red) and unpaid bills (red)

## Google Sheets Upload

- [ ] Upload XLSX to Google Drive
- [ ] Open with Google Sheets
- [ ] Convert to Google Sheets format (File → Save as Google Sheets)
- [ ] Verify all formulas converted correctly
- [ ] Fix column widths if needed
- [ ] Recreate charts if they did not survive conversion
- [ ] Set sharing permissions (Anyone with link → Viewer)
- [ ] Create buyer copy link using /copy suffix
- [ ] Test copy link in incognito/private browser window
- [ ] Confirm copied workbook opens cleanly

## PDF Quick-Start Guide

- [ ] Export PDF_QUICK_START_GUIDE.md as 1-page PDF
- [ ] Verify all steps readable
- [ ] Verify common mistakes section included
- [ ] Verify support/contact placeholder present

## Screenshots

- [ ] Screenshot 1: Dashboard overview captured
- [ ] Screenshot 2: Monthly Budget tab captured
- [ ] Screenshot 3: Expense Tracker tab captured
- [ ] Screenshot 4: Bills + Debt + Savings tracker collage captured
- [ ] Screenshot 5: Product bundle mockup created
- [ ] All screenshots cropped and clearly readable
- [ ] File names match SCREENSHOT_CAPTURE_GUIDE.md

## Listing Preparation

- [ ] Gumroad listing drafted from LISTING_COPY_GUMROAD.md
- [ ] Payhip listing drafted from LISTING_COPY_PAYHIP.md
- [ ] Screenshots uploaded to both listing drafts
- [ ] PDF guide uploaded to both listing drafts
- [ ] XLSX file uploaded to both listing drafts
- [ ] Price set to $7 on both platforms
- [ ] Test checkout preview reviewed on both platforms

## Final Publishing

- [ ] Gumroad listing published
- [ ] Payhip listing published
- [ ] Listing URLs recorded in PRODUCT_CATALOG.csv
- [ ] Date published recorded in PRODUCT_CATALOG.csv
- [ ] Status updated to Published in PRODUCT_CATALOG.csv
