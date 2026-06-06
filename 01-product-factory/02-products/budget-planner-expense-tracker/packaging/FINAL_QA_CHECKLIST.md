# Final QA Checklist — Budget Planner & Expense Tracker

## Pre-Publish Checks

### Spreadsheet
- [ ] XLSX opens without errors in Microsoft Excel
- [ ] All 7 tabs present in XLSX
- [ ] All formulas calculate (no #REF!, #DIV/0!, #NAME? errors with sample data)
- [ ] Dashboard summary values match source tabs
- [ ] Charts render correctly (pie chart, bar chart)
- [ ] Data validation dropdowns functional on Expense Tracker and Bills Tracker
- [ ] Conditional formatting visible (red for negative variance, red for unpaid bills)

### Google Sheets
- [ ] XLSX uploaded to Google Drive successfully
- [ ] Converted to Google Sheets without data loss
- [ ] All formulas converted correctly
- [ ] Charts recreated if needed
- [ ] Sharing permissions set to "Anyone with link → Viewer"
- [ ] /copy link created and tested in incognito browser
- [ ] Copied workbook opens with all tabs preserved

### PDF Quick-Start Guide
- [ ] PDF exports cleanly as 1 page
- [ ] All steps readable at 100% zoom
- [ ] Common mistakes section included
- [ ] Which cells to edit / not edit clearly explained
- [ ] Support/contact placeholder included

### Screenshots
- [ ] Screenshot 1: Dashboard overview captured
- [ ] Screenshot 2: Monthly Budget tab captured
- [ ] Screenshot 3: Expense Tracker tab captured
- [ ] Screenshot 4: Bills + Debt + Savings collage created
- [ ] Screenshot 5: Product bundle mockup created
- [ ] All screenshots cropped, clean, and readable
- [ ] No personal/financial info visible in screenshots

### Listing Copy
- [ ] Gumroad listing title matches product name
- [ ] Gumroad subtitle matches product value proposition
- [ ] Gumroad description complete with all sections
- [ ] Gumroad "What's included" matches actual deliverables
- [ ] Gumroad FAQ answers common questions
- [ ] Gumroad price set to $7
- [ ] Gumroad refund policy included
- [ ] Payhip listing copy adapted from Gumroad copy
- [ ] Payhip price set to $7
- [ ] Both listings free from typos

### Files Attached to Listings
- [ ] XLSX file attached to Gumroad listing
- [ ] Google Sheet /copy link included in Gumroad description
- [ ] PDF quick-start guide attached to Gumroad listing
- [ ] 5 screenshots uploaded to Gumroad listing
- [ ] Same files attached to Payhip listing

### Product Catalog
- [ ] Listing URLs recorded in PRODUCT_CATALOG.csv
- [ ] Date published recorded in PRODUCT_CATALOG.csv
- [ ] Status updated to Published in PRODUCT_CATALOG.csv
- [ ] Price confirmed as $7

## Publishing

- [ ] Gumroad listing published and accessible
- [ ] Payhip listing published and accessible
- [ ] Test purchase completed on at least one platform
- [ ] Download flow works after test purchase
- [ ] Buyer receives all expected files after purchase

## Post-Publish

- [ ] First week: track views daily
- [ ] First sale: track revenue in PRODUCT_CATALOG.csv
- [ ] Run retrospective after 1 week or first sale
