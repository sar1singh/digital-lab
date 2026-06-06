# QA Signoff Checklist — Budget Planner & Expense Tracker v1.0

## Pre-Publish Gates

All items must be checked before product can be published.

### XLSX QA

- [ ] All P0 test cases pass (TC-F-01 through TC-F-05, TC-F-07, TC-F-09, TC-F-10, TC-F-13, TC-F-14, TC-F-17 through TC-F-23, TC-UI-01, TC-UI-02, TC-UI-11, TC-DD-01, TC-DD-03, TC-DD-05, TC-DD-10, TC-DD-12)
- [ ] All P1 test cases pass (TC-UI-03, TC-UI-04, TC-UI-06, TC-UI-07, TC-UI-08, TC-UI-09, TC-UI-13, TC-UI-14, TC-F-06, TC-F-08, TC-F-11, TC-F-12, TC-F-15, TC-F-16, TC-DD-02, TC-DD-04, TC-DD-06, TC-DD-07, TC-DD-08, TC-DD-09, TC-DD-11)
- [ ] No P0 bugs open
- [ ] No P1 bugs open (unless documented exception)

### Google Sheets Import QA

- [ ] TC-GS-01: Upload successful
- [ ] TC-GS-02: Opens in Google Sheets
- [ ] TC-GS-03: All 7 tabs preserved
- [ ] TC-GS-04: Formulas preserved
- [ ] TC-GS-05: Dropdowns preserved
- [ ] TC-GS-06: Conditional formatting preserved
- [ ] TC-GS-07: Charts documented for recreation
- [ ] TC-GS-09: /copy link created
- [ ] TC-GS-10: /copy link works in incognito
- [ ] TC-GS-11: Copied sheet is independent
- [ ] TC-GS-12: Buyer can edit their copy

### Dashboard QA

- [ ] TC-DB-01: Summary cards show values
- [ ] TC-DB-02: Income changes propagate
- [ ] TC-DB-05: Bills Due count changes
- [ ] TC-DB-06: Debt Remaining changes
- [ ] TC-DB-07: Savings Progress changes
- [ ] TC-DB-09: No error values
- [ ] TC-DB-10: Charts render

### Packaging

- [ ] PDF quick-start guide exported
- [ ] 5 screenshots captured per SCREENSHOT_CAPTURE_GUIDE.md
- [ ] Gumroad listing draft reviewed
- [ ] Payhip listing draft reviewed
- [ ] Screenshots attached to both listing drafts
- [ ] XLSX attached to both listing drafts
- [ ] PDF guide attached to both listing drafts
- [ ] Price set to $7 on both platforms
- [ ] Google Sheet /copy link included in listings
- [ ] Refund/digital product policy included
- [ ] Test checkout preview reviewed

### Final Status

| Gate | Status |
|------|--------|
| XLSX QA | Pass / Fail |
| Google Sheets QA | Pass / Fail |
| Dashboard QA | Pass / Fail |
| Packaging Complete | Yes / No |
| Ready to Publish | Yes / No |

---

## QA Signoff

**Tester Name:** ______________________

**Date:** ______________________

**Signature:** ______________________

---

## Post-Publish Tracking

- [ ] Listing URLs recorded in PRODUCT_CATALOG.csv
- [ ] Date published recorded
- [ ] Status updated to Published
- [ ] Views tracked after 24 hours
