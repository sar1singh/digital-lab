# Session Continuation — Digital-Lab / Product Factory

> Copy this entire file into a new AI session to resume Product Factory execution without losing context.

---

## Current State

Digital-Lab is a personal digital products experiment. The active execution track is **Product Factory** (building and selling small spreadsheet/template products). Three other labs (SaaS Lab, Content Lab, Agency Lab) are **parked**.

**Primary goal:** First product built, listed, sold — first $50-$100 revenue.

**Products 1-2 are Ready to Publish.** Both are blocked only by manual marketplace listing creation (Gumroad + Payhip).

**Product 3 (Project Budget Tracker) is in Specification Phase** — all planning docs complete. Do not start workbook build until directed.

---

## What Has Been Completed

### Product 1: Budget Planner & Expense Tracker
- 7-tab XLSX workbook with 91 formulas built and audited
- Automated QA: 55/55 PASS + Manual GS QA: PASS
- Brand updated to Nivora across all assets
- Google Sheets copy link finalized
- Delivery: workbook + PDF + copy link + ZIP + 5 listing images
- Status: **Ready to Publish**

### Product 2: Invoice Generator & Payment Tracker
- 7-tab XLSX workbook built via Python/openpyxl generator
- 4 automated QA suites (85 structural + 19 formula + 11 GS lint + 10 layout)
- All 10 QA layers PASSED — 3 bugs found and fixed before delivery
- Pre-publish review (Sections A-G): all PASS
- 6 PNG screenshots generated (01-cover.png through 06-whats-included.png)
- 10-page PDF quick-start guide generated (fpdf2)
- Delivery ZIP built and verified: 3 files (workbook + PDF + copy link)
- Full retrospective documented with QA/asset/PDF/delivery/listing learnings
- 3 new factory anti-drift rules added (Rules 23-25)
- Status: **Ready to Publish**

### Product 3: Project Budget Tracker
- Product workspace created with 7 subdirectories
- All 10 planning docs complete (PRODUCT_SPEC.md through LISTING_COPY_PAYHIP.md)
- Status: **Specification Phase** — do not build workbook yet

---

## What Must Not Be Changed

1. **Products 1-2 are frozen** — no further development unless customer reports issue.
2. **Do not start Product 4** until Product 3 is published or explicitly parked.
3. **Do not change workbook formulas** — verified and tested for both products.
4. **Do not change product strategy** — Product Factory active, other labs parked.
5. **Do not do market research** — move directly to execution.
6. **Do not set up Etsy, website, logo, newsletter, or branding** before first sale or 5 products published.
7. **No buyer-facing filenames may include version numbers.**
8. **Internal QA files must not be included in buyer delivery.**
9. **Nivora is the sole customer-facing brand.** Never use "Work by Sar1" for buyer-facing content.
10. **workbysar1@gmail.com is support/operations only** — not a brand name.

---

## Current Active Task

Create marketplace listings for Products 1-2 (manual founder action). Then build Product 3 (Project Budget Tracker) workbook.

---

## Product Roadmap

| # | Product | Format | Status | Price |
|---|---------|--------|--------|-------|
| 1 | Budget Planner & Expense Tracker | Spreadsheet (7 tabs) | **Ready to Publish** | $7 |
| 2 | Invoice Generator & Payment Tracker | Spreadsheet (7 tabs) | **Ready to Publish** | $7 |
| 3 | Project Budget Tracker | Spreadsheet (7 tabs) | **Specification Phase** | $7 |
| 4 | Net Worth Tracker | Spreadsheet | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Spreadsheet | Backlog | $5-$12 |

---

## Founder / Brand Decisions

- **Customer-facing brand:** Nivora
- **Founder/operator email:** workbysar1@gmail.com (support, billing, platform signup)
- **Platform (Phase 1):** Gumroad + Payhip
- **Pricing:** $7 launch price
- **Product naming:** Generic, descriptive names. No branding blocking.
- **Build rule:** Max 1-2 days per product before publishing.
- **Publishing rule:** All P0 and P1 tests must pass before listing goes live.
- **Decision rule:** Before any task, ask: "Will this increase probability of first $50-$100 revenue?" If no, park it.
- **Product type:** Spreadsheet/template/calculator formats. No code-heavy products.
- **Never use "Work by Sar1" as customer-facing branding again.**

---

## Immediate Next Actions

1. (Manual) Create Gumroad and Payhip listings for Product 1
2. (Manual) Create Gumroad and Payhip listings for Product 2
3. Upload delivery ZIPs + screenshots to both listings
4. Set price to $7 on both platforms for both products
5. Test checkout preview
6. Publish both listings
7. Record listing URLs in PRODUCT_CATALOG.csv
8. Update PRODUCT_CATALOG.csv status to Published
9. **Then** start Product 3 workbook build phase

---

## Key File Paths

```
Repository root:                         digital-lab/

Product 1 (Budget Planner):              01-product-factory/02-products/budget-planner-expense-tracker/
Product 2 (Invoice Generator):           01-product-factory/02-products/invoice-generator-payment-tracker/
Product 3 (Project Budget Tracker):      01-product-factory/02-products/project-budget-tracker/

Factory docs:                            01-product-factory/
Context/control:                         00-control/
  Session continuation:                  SESSION_CONTINUATION.md
  Factory continuation:                  PRODUCT_FACTORY_CONTINUATION_CONTEXT.md
  Product catalog:                       PRODUCT_CATALOG.csv
Handoff for Product 3:                   docs/AI_CONTINUATION_CONTEXT_PRODUCT_3.md
Progress dashboard:                      docs/PRODUCT_FACTORY_PROGRESS_DASHBOARD.md
Next actions:                            NEXT_ACTIONS.md
```

---

## Mandatory Rules for All Products

1. **Brand-first** — Brand (Nivora), support email, naming conventions locked before any work
2. **Standard folder structure** — artifacts/, build/, qa/, listing-assets/, screenshots/, docs/, delivery/
3. **Delivery folder rule** — buyer-facing assets only, no QA or internal files
4. **6-screenshot standard** — Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included
5. **5-review exit criteria** — Pass all: Content, Branding, Packaging, Marketplace, Delivery
6. **Retrospective required** — Every shipped product; lessons update factory standards
7. **Assets after QA** — Generate images only after workbook is final and QA'd
8. **ZIP as final step** — Exactly 3 files (workbook, PDF, copy link)
9. **Gumroad first** — List on Gumroad first, then Payhip
10. **10-stage pipeline** — Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update
11. **QA coverage gate** — All 10 QA layers must pass before Delivery Ready
12. **Automated QA before manual** — Layers 1-4 before Layers 5-9
13. **COUNTIFS finite range** — Negative-match must use finite range + non-empty criterion
14. **DV inline lists for GS** — Use comma-separated lists, not sheet cell references
15. **Formula expected values** — Every formula in spec needs test-row expected value

---

## Continuation Files

- `docs/AI_CONTINUATION_CONTEXT_PRODUCT_3.md` — primary handoff for Product #3 sessions
- `docs/PRODUCT_FACTORY_PROGRESS_DASHBOARD.md` — high-level dashboard
- `00-control/PRODUCT_FACTORY_CONTINUATION_CONTEXT.md` — optimized copy-paste resume
- `00-control/DIGITAL_LAB_CONTEXT.md` — full decision log and strategic context
- `00-control/NOW.md` — current active task
- `01-product-factory/PRODUCT_FACTORY_CONTEXT.md` — factory-specific context
