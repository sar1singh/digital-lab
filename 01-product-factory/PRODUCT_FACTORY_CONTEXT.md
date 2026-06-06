# Product Factory Context

## Mission

Build small proven-format digital products (spreadsheets, templates, calculators) and sell them on Gumroad and Payhip. Goal: first $50-$100 revenue as fast as realistically possible. Then scale to 5 products live.

## Operating Principles

- Build → Publish → Learn → Repeat
- Max 1-2 days per product before publishing
- Compete in existing proven markets; copy successful formats legally
- Improve packaging and execution, not product novelty
- First revenue is more important than innovation

## Selection Rules

A product must:
1. Have proven demand (similar products already selling)
2. Be buildable in 1-2 days
3. Fit spreadsheet/template/calculator format
4. Have obvious buyer ROI (saves time, saves money, reduces mistakes)
5. Be easy to explain in one sentence

## Anti-Drift Rules

Before any task, ask: "Will this increase probability of first $50-$100 revenue?"

If no, park it.

**Do not do:**
- SaaS
- Website building
- Logo/branding projects
- Newsletter setup
- Audience building
- Social media growth
- Infrastructure building
- Automation platforms
- Product factory app
- Broad research loops
- Etsy setup (before first sale or 5 products published)

## Current Roadmap

| # | Product | Format | Status | Price |
|---|---------|--------|--------|-------|
| 1 | Budget Planner & Expense Tracker | Spreadsheet (7 tabs) | **Packaging** — delivery artifacts ready | $7 |
| 2 | Invoice Template & Billing Calculator | Spreadsheet | Not started | $7 |
| 3 | Freelancer Pricing Calculator | Spreadsheet | Backlog | $5-$12 |
| 4 | Net Worth Tracker | Spreadsheet | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Spreadsheet | Backlog | $5-$12 |

Do not start Product 2 until Product 1 is listed or explicitly parked.

## Product Statuses

- **Planned** — idea selected, not started
- **In Build** — workspace created, actively building
- **Packaging** — workbook complete, delivery artifacts created, listing pending
- **Listed** — Gumroad/Payhip listing live
- **Published** — listed AND available for purchase
- **Sold** — at least one purchase recorded

## Publishing Process

### For each product:
1. Build workbook (Python/openpyxl generation)
2. Run automated QA (formulas, dropdowns, dashboard, navigation)
3. Run manual QA in Excel and Google Sheets
4. Fix all P0/P1 issues
5. Create buyer-facing delivery files:
   - `product-name.xlsx` (no version numbers)
   - `google-sheets-copy-link.txt`
   - `release-notes.txt`
   - `quick-start-guide.md` + `.html` + `.pdf`
   - Listing images (5 assets)
   - Screenshots (captured from real Google Sheets)
6. Create delivery zip (exclude QA files, planning docs, versioned workbooks)
7. Create Gumroad listing
8. Create Payhip listing
9. Publish both
10. Record URLs in PRODUCT_CATALOG.csv

## Brand & Founder Identity

- **Customer-facing publisher brand:** Nivora
- **Support email:** workbysar1@gmail.com
- **Founder/operations email:** workbysar1@gmail.com
- **Never use "Work by Sar1" as customer-facing branding again.**

## Key Files

- `00-control/DIGITAL_LAB_CONTEXT.md` — full decision log and strategic context
- `00-control/SESSION_CONTINUATION.md` — copy-paste resume for new AI session
- `00-control/PRODUCT_FACTORY_CONTINUATION_CONTEXT.md` — optimized copy-paste resume
- `00-control/NOW.md` — current active task
- `00-control/PRODUCT_CATALOG.csv` — ranked pipeline with status, price, URLs
- `PRODUCT_FACTORY_STRATEGY.md` — strategy and operating thesis
- `FIRST_10_PRODUCTS_ROADMAP.md` — full 10-product pipeline
- `NEXT_ACTIONS.md` — detailed phased action list
- `PRODUCT_FACTORY_WORKFLOW.md` — Research→Validate→Build→Package→List→Publish→Track
