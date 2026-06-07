# Session Continuation — Digital-Lab / Product Factory

> Copy this entire file into a new AI session to resume Product Factory execution without losing context.

---

## Current State

Digital-Lab is a personal digital products experiment. The active execution track is **Product Factory** (building and selling small spreadsheet/template products). Three other labs (SaaS Lab, Content Lab, Agency Lab) are **parked**.

**Primary goal:** First product built, listed, sold — first $50-$100 revenue.

**Current Product 1 status:** Ready to Publish — workbook fixed, final ZIP built with 3 clean buyer files, Gumroad listing is the next manual action.

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
- Brand updated to Nivora across all files, images, PDF, and listing copy
- Dashboard bottom summary fixed: B40 (=B4->=B5 Expenses), B41 (=B5->=B7 Net Savings)
- Final clean ZIP rebuilt with only 3 buyer files (no internal files)
- FINAL_ZIP_QA.md created
- Google Sheets copy link finalized and pasted into `delivery/google-sheets-copy-link.txt`
- Delivery folder contains buyer-ready files:
  - `nivora-budget-planner-expense-tracker.xlsx` (Nivora-branded name, no version number)
  - `nivora-budget-planner-expense-tracker-quick-start-guide.pdf` (Nivora-branded PDF guide)
  - `google-sheets-copy-link.txt` (Nivora-branded copy link)
  - `listing-assets/` — 5 demo images (product-cover, bundle-preview, feature-*)
  - `nivora-budget-planner-expense-tracker-delivery.zip` (buyer ZIP: xlsx + pdf + copy link)

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
9. **Nivora is the sole customer-facing brand.** Never use "Work by Sar1" for buyer-facing content.
10. **workbysar1@gmail.com is support/operations only** — not a brand name.

---

## Current Active Task

Create Gumroad listing for Nivora Budget Planner & Expense Tracker.

---

## Product Roadmap

| # | Product | Format | Status | Price |
|---|---------|--------|--------|-------|
| 1 | Budget Planner & Expense Tracker | Spreadsheet (7 tabs) | **Ready to Publish** | $7 |
| 2 | Invoice Generator & Payment Tracker | Spreadsheet | **Planning — workspace created** | $7 |
| 3 | Freelancer Pricing Calculator | Spreadsheet | Backlog | $5-$12 |
| 4 | Net Worth Tracker | Spreadsheet | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Spreadsheet | Backlog | $5-$12 |

---

## Founder / Brand Decisions

- **Customer-facing brand:** Nivora
- **Founder/operator email:** workbysar1@gmail.com (support, billing, platform signup)
- **Platform (Phase 1):** Gumroad + Payhip
- **Pricing:** $7 launch price (Product 1)
- **Product naming:** Generic, descriptive names. No branding blocking.
- **Build rule:** Max 1-2 days per product before publishing.
- **Publishing rule:** All P0 and P1 tests must pass before listing goes live.
- **Decision rule:** Before any task, ask: "Will this increase probability of first $50-$100 revenue?" If no, park it.
- **Product type:** Spreadsheet/template/calculator formats. No code-heavy products.
- **Never use "Work by Sar1" as customer-facing branding again.**

---

## Immediate Next Actions

1. Create Gumroad listing from `LISTING_COPY_GUMROAD.md` (use Nivora brand)
2. Create Payhip listing from `LISTING_COPY_PAYHIP.md`
3. Upload final ZIP + listing images to both listings
4. Set price to $7 on both platforms
5. Test checkout preview
6. Publish both listings
7. Record listing URLs in `PRODUCT_CATALOG.csv`
8. Update `PRODUCT_CATALOG.csv` status to Published
9. **Then** start Product 2 (Invoice Generator & Payment Tracker)

---

## Key File Paths

```
Repository root: digital-lab/
Active product:   01-product-factory/02-products/budget-planner-expense-tracker/
Source workbook:  .../artifacts/budget-planner-expense-tracker-v1.2.xlsx
Delivery folder:  .../delivery/
Buyer workbook:   .../delivery/nivora-budget-planner-expense-tracker.xlsx
QA test suite:    .../qa/ (71 manual test cases)
Listing copy:     .../LISTING_COPY_GUMROAD.md, LISTING_COPY_PAYHIP.md
Product catalog:  .../00-control/PRODUCT_CATALOG.csv
Build checklist:  .../BUILD_CHECKLIST.md
Brand QA:         .../docs/BRAND_QA_CHECKLIST.md
```

## Continuation Files

- `00-control/DIGITAL_LAB_CONTEXT.md` — full decision log and strategic context
- `00-control/SESSION_CONTINUATION.md` — this file
- `00-control/PRODUCT_FACTORY_CONTINUATION_CONTEXT.md` — optimized copy-paste resume
- `00-control/NOW.md` — current active task
- `01-product-factory/PRODUCT_FACTORY_CONTEXT.md` — factory-specific context

## Product Factory Standards (from Product #1 Lessons)

| Standard | Location |
|----------|----------|
| Publishing Playbook | `01-product-factory/PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md` |
| Marketplace Checklist | `01-product-factory/PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md` |
| Asset Specifications | `01-product-factory/PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md` |
| Pre-Publish QA | `01-product-factory/PRODUCT_FACTORY_PRE_PUBLISH_QA.md` |
| Delivery Standard | `01-product-factory/PRODUCT_FACTORY_DELIVERY_STANDARD.md` |
| Product Structure | `01-product-factory/PRODUCT_FACTORY_PRODUCT_STRUCTURE.md` |
| Brand Standard | `01-product-factory/07-systems/BRAND_STANDARD.md` |
| Delivery Structure Standard | `01-product-factory/templates/DELIVERY_STRUCTURE_STANDARD.md` |
| Listing Asset Standard | `01-product-factory/templates/LISTING_ASSET_STANDARD.md` |
| Pre-Publish Checklist | `01-product-factory/templates/PRE_PUBLISH_CHECKLIST.md` |
| Delivery Standard (legacy) | `01-product-factory/07-systems/DELIVERY_STANDARD.md` |
| Marketplace Asset Standard (legacy) | `01-product-factory/07-systems/MARKETPLACE_ASSET_STANDARD.md` |
| Retrospective Template | `01-product-factory/templates/PRODUCT_RETROSPECTIVE_TEMPLATE.md` |
| Workflow | `01-product-factory/PRODUCT_FACTORY_WORKFLOW.md` |
| Context | `01-product-factory/PRODUCT_FACTORY_CONTEXT.md` |

## Mandatory Rules for All Products

1. **Brand-first:** Brand (Nivora), support email, naming conventions locked before any asset or workbook work
2. **Standard folder structure:** artifacts/, build/, qa/, listing-assets/, screenshots/, docs/, delivery/
3. **Delivery folder:** buyer-facing assets only — no QA, drafts, or internal files
4. **6-screenshot standard:** Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included
5. **5-review exit criteria:** Pass all reviews — Content, Branding, Packaging, Marketplace, Delivery
6. **Retrospective required:** RETROSPECTIVE.md for every shipped product; lessons become factory standards
7. **Assets after QA:** Generate marketplace images only after workbook is final and QA'd
8. **ZIP as final step:** Build ZIP last, exactly 3 files (workbook, PDF, copy link), no subdirectories
9. **Gumroad first:** List on Gumroad first, then Payhip. Add platforms only after consistent sales
10. **10-stage pipeline:** Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update
