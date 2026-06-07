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
| 1 | Budget Planner & Expense Tracker | Spreadsheet (7 tabs) | **Ready to Publish** — Gumroad listing pending | $7 |
| 2 | Invoice Generator & Payment Tracker | Spreadsheet (7 tabs) | **Ready to Publish** — all 10 QA layers complete, delivery ZIP ready | $7 |
| 3 | Project Budget Tracker | Spreadsheet (7 tabs) | **Specification Phase** — all planning docs complete | $7 |
| 4 | Net Worth Tracker | Spreadsheet | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Spreadsheet | Backlog | $5-$12 |

Do not start Product N+1 until Product N is either published or explicitly parked. Products 1-2 are frozen — no further development unless customer reports issue.

## Product Statuses

| Status | Description |
|--------|-------------|
| **Planned** | Idea selected, not started |
| **In Build** | Workspace created, actively building |
| **Packaging** | Workbook complete, delivery artifacts in progress |
| **Ready to Publish** | All 5 reviews passed (Content, Branding, Packaging, Marketplace, Delivery). Gate cleared. |
| **Listed** | Gumroad/Payhip listing created, not yet published |
| **Published** | Listed AND available for purchase |
| **Sold** | At least one purchase recorded |

---

## Publishing Process (10-Stage Pipeline)

| Stage | Phase | Key Action | Duration |
|-------|-------|------------|----------|
| 1 | Idea | Validate product meets selection criteria | < 1 hr |
| 2 | Build | Create workbook with sample data | 2–6 hrs |
| 3 | Internal QA | Formula audit, Google Sheets test | 1–2 hrs |
| 4 | Asset Generation | Create 6 marketplace images (after workbook final) | 1–2 hrs |
| 5 | Packaging | Branded files, PDF guide (2nd-last), ZIP (last) | 1 hr |
| 6 | Marketplace Listing | Create Gumroad + Payhip listings | 1 hr |
| 7 | Publish | All 5 reviews pass → publish | 30 min |
| 8 | Distribution | Record URLs, verify live | 15 min |
| 9 | Learnings Capture | Create RETROSPECTIVE.md | 30 min |
| 10 | Factory Standards Update | Apply lessons to standards | 30 min |
| | **Total** | | **8–14 hrs** |

**Gate:** Stage 7 (Publish) requires ALL 5 reviews to pass (Content, Branding, Packaging, Marketplace, Delivery).

## Brand & Founder Identity

- **Customer-facing publisher brand:** Nivora
- **Support email:** workbysar1@gmail.com
- **Founder/operations email:** workbysar1@gmail.com
- **Never use "Work by Sar1" as customer-facing branding again.**

## Key Files

### Core Factory Documents
- `PRODUCT_FACTORY_STRATEGY.md` — strategy and operating thesis
- `PRODUCT_FACTORY_WORKFLOW.md` — 10-stage pipeline (Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update)
- `PRODUCT_FACTORY_CONTEXT.md` — this file (mission, rules, statuses, processes)
- `PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md` — end-to-end playbook with all stages, gates, timelines
- `FIRST_10_PRODUCTS_ROADMAP.md` — full 10-product pipeline

### Standards & Specifications
- `PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md` — platform-specific requirements (Gumroad, Payhip, future)
- `PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md` — image specs, gallery order, naming, quality requirements
- `PRODUCT_FACTORY_PRE_PUBLISH_QA.md` — 5-review process (Content, Branding, Packaging, Marketplace, Delivery)
- `PRODUCT_FACTORY_DELIVERY_STANDARD.md` — ZIP contents, naming, exclusions, packaging sequence
- `PRODUCT_FACTORY_PRODUCT_STRUCTURE.md` — workspace folder layout and lifecycle

### Systems (active)
- `07-systems/QA_COVERAGE_STANDARD.md` — 10-layer QA standard for all products
- `07-systems/BRAND_STANDARD.md` — brand usage rules (Nivora, naming, email)
- `07-systems/DELIVERY_STANDARD.md` — delivery format and QA gate
- `07-systems/MARKETPLACE_ASSET_STANDARD.md` — image requirements
- `07-systems/PRE_PUBLISH_REVIEW_CHECKLIST.md` — gated checklist (Layer 10)
- `07-systems/templates/` — reusable QA plan and checklist templates

### Legacy Systems (compatible, superseded by PRODUCT_FACTORY_*)
- `07-systems/` — older documents; new products should reference PRODUCT_FACTORY_* documents

### Templates
- `templates/PRE_PUBLISH_CHECKLIST.md` — pre-publish gate checklist
- `templates/DELIVERY_STRUCTURE_STANDARD.md` — folder structure reference
- `templates/LISTING_ASSET_STANDARD.md` — image set reference
- `templates/PRODUCT_RETROSPECTIVE_TEMPLATE.md` — post-publish review template

### Context & Control
- `00-control/DIGITAL_LAB_CONTEXT.md` — full decision log and strategic context
- `00-control/SESSION_CONTINUATION.md` — copy-paste resume for new AI session
- `00-control/PRODUCT_FACTORY_CONTINUATION_CONTEXT.md` — optimized copy-paste resume
- `00-control/NOW.md` — current active task
- `00-control/PRODUCT_CATALOG.csv` — ranked pipeline with status, price, URLs
- `NEXT_ACTIONS.md` — detailed phased action list (repo root)

## Mandatory Factory Standards

The following rules apply to ALL products (hardened from Product #1 lessons):

| # | Rule | Detail | Source Document |
|---|------|--------|-----------------|
| 1 | **Brand-first** | Brand (Nivora), support email, naming conventions locked before any asset or build work | `PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md`, `BRAND_STANDARD.md` |
| 2 | **Standard folder structure** | artifacts/, build/, qa/, listing-assets/, screenshots/, docs/, delivery/ | `PRODUCT_FACTORY_PRODUCT_STRUCTURE.md` |
| 3 | **Delivery folder rule** | Buyer-facing assets only — no QA, drafts, or internal files | `PRODUCT_FACTORY_DELIVERY_STANDARD.md` |
| 4 | **6-screenshot standard** | Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included | `PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md` |
| 5 | **5-review exit criteria** | Pass all: Content, Branding, Packaging, Marketplace, Delivery reviews | `PRODUCT_FACTORY_PRE_PUBLISH_QA.md` |
| 6 | **Retrospective required** | RETROSPECTIVE.md for every shipped product; lessons update factory standards | `PRODUCT_FACTORY_WORKFLOW.md` (Stage 9–10) |
| 7 | **Assets after QA** | Generate marketplace images only after workbook is final and QA'd | `PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md` |
| 8 | **ZIP as final step** | Build ZIP last, exactly 3 files (workbook, PDF, copy link), no subdirectories | `PRODUCT_FACTORY_DELIVERY_STANDARD.md` |
| 9 | **Gumroad first** | List on Gumroad first, then Payhip. Add platforms only after consistent sales | `PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md` |
| 10 | **10-stage pipeline** | Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update | `PRODUCT_FACTORY_WORKFLOW.md` |
| 11 | **QA coverage gate** | All 10 QA layers from `QA_COVERAGE_STANDARD.md` must pass before "Delivery Ready" status | `QA_COVERAGE_STANDARD.md` |
| 12 | **Automated QA before manual** | Implement Layers 1–4 (automated) before Layers 5–9 (manual). Manual QA only for platform/visual behavior | `QA_COVERAGE_STANDARD.md` |
| 13 | **COUNTIFS finite range** | Negative-match COUNTIFS/SUMIFS must use finite range (not whole-column) and include non-empty criterion `"<>"` | `QA_COVERAGE_STANDARD.md` |
| 14 | **DV inline lists for GS** | Data validations use inline comma-separated lists (`"A,B,C"`) instead of sheet cell references. Range refs break during GS conversion | `QA_COVERAGE_STANDARD.md` |
| 15 | **Formula expected values** | Every formula in FORMULAS.md needs at least one test-row expected value, not just structural description | `FORMULAS.md` template |
