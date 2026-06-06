# Session Continuation — Digital-Lab / Product Factory

> Copy this entire file into a new AI session to resume Product Factory execution without losing context.

---

## Current State

Digital-Lab is a personal digital products experiment. The active execution track is **Product Factory** (building and selling small spreadsheet/template products). Three other labs (SaaS Lab, Content Lab, Agency Lab) are **parked**.

**Primary goal:** First product built, listed, sold — first $50-$100 revenue.

**Current Product 1 status:** Packaging (delivery artifacts ready, listing pending).

---

## What Has Been Completed

- Repository restructured for Product Factory execution model
- Product workspace created for Budget Planner & Expense Tracker
- 7-tab XLSX workbook built with 91 formulas (SUMIF, COUNTIF, IFERROR, SUM, AVERAGE, TEXT)
- Formula audit completed — all cross-sheet references verified
- Navigation links fixed for Google Sheets (hyperlinks replaced with plain text)
- Automated QA: 55/55 PASS
- Manual Google Sheets QA: PASS
- v1.2 finalized as current recommended version
- Delivery folder created with buyer-facing files:
  - `budget-planner-expense-tracker.xlsx` (no version number)
  - `quick-start-guide.md`, `.html`, `.pdf`
  - `release-notes.txt`
  - `google-sheets-copy-link.txt` (placeholder)
  - `listing-assets/` — 5 demo images (product-cover, bundle-preview, feature-*)
  - `screenshots/README.md` — manual capture guide
  - `budget-planner-expense-tracker-delivery.zip` (all buyer files)

---

## What Must Not Be Changed

1. **Do not start Product 2** until Product 1 is listed or explicitly parked.
2. **Do not change workbook formulas** — 91 formulas are verified and tested.
3. **Do not modify v1.2.xlsx** — it is the approved source. Copy it for any new variants.
4. **Do not change product strategy** — Product Factory active, other labs parked.
5. **Do not do market research** — move directly to execution.
6. **Do not set up Etsy, website, logo, newsletter, or branding** before first sale or 5 products published.
7. **No buyer-facing filenames may include version numbers** (v1.2, v1.1, etc.).
8. **Internal QA files must not be included in buyer delivery.**

---

## Current Active Task

Create Google Sheets copy link, capture real screenshots, create Gumroad listing, and publish.

---

## Product Roadmap

| # | Product | Status | Price |
|---|---------|--------|-------|
| 1 | Budget Planner & Expense Tracker | **Packaging** — delivery artifacts ready | $7 |
| 2 | Invoice Template & Billing Calculator | Not started | $7 |
| 3 | Freelancer Pricing Calculator | Backlog | $5-$12 |
| 4 | Net Worth Tracker | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Backlog | $5-$12 |

---

## Founder Decisions

- **Email:** workbysar1@gmail.com
- **Temporary brand:** "Work by Sar1"
- **Platform (Phase 1):** Gumroad + Payhip
- **Pricing:** $7 launch price (Product 1)
- **Product naming:** Generic, descriptive names. No branding blocking.
- **Build rule:** Max 1-2 days per product before publishing.
- **Publishing rule:** All P0 and P1 tests must pass before listing goes live.
- **Decision rule:** Before any task, ask: "Will this increase probability of first $50-$100 revenue?" If no, park it.
- **Product type:** Spreadsheet/template/calculator formats. No code-heavy products.

---

## Immediate Next Actions

1. Upload v1.2 XLSX to Google Drive → File > Save as Google Sheets
2. Recreate charts in Google Sheets if needed
3. Create Google Sheets /copy link
4. Paste /copy link into `delivery/google-sheets-copy-link.txt`
5. Capture 5 real screenshots from Google Sheets (per `delivery/screenshots/README.md`)
6. Draft Gumroad listing from `LISTING_COPY_GUMROAD.md`
7. Draft Payhip listing from `LISTING_COPY_PAYHIP.md`
8. Upload XLSX, PDF guide, listing images, screenshots to both listings
9. Set price to $7 on both platforms
10. Test checkout preview
11. Publish both listings
12. Record listing URLs in `PRODUCT_CATALOG.csv`
13. Update `PRODUCT_CATALOG.csv` status to Published
14. **Then** start Product 2 (Invoice Template & Billing Calculator)

---

## Key File Paths

```
Repository root: digital-lab/
Active product:   01-product-factory/02-products/budget-planner-expense-tracker/
Source workbook:  .../artifacts/budget-planner-expense-tracker-v1.2.xlsx
Delivery folder:  .../delivery/
Buyer workbook:   .../delivery/budget-planner-expense-tracker.xlsx
QA test suite:    .../qa/ (71 manual test cases)
Listing copy:     .../LISTING_COPY_GUMROAD.md, LISTING_COPY_PAYHIP.md
Product catalog:  .../00-control/PRODUCT_CATALOG.csv
Build checklist:  .../BUILD_CHECKLIST.md
```

## Important URIs for Reference

- Product workspace: `01-product-factory/02-products/budget-planner-expense-tracker/`
- Approval flow: DIGITAL_LAB_CONTEXT.md → NOW.md → NEXT_ACTIONS.md → BUILD_CHECKLIST.md
- Decision log: `00-control/DIGITAL_LAB_CONTEXT.md` (Decision Log section)
