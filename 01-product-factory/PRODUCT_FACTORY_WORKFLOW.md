# Product Factory Workflow

> Standard 10-stage pipeline for every Product Factory product. Updated from Product #1 (Nivora Budget Planner & Expense Tracker) learnings.

---

## Pipeline

```
Idea → Build → Internal QA → Asset Generation → Packaging
→ Marketplace Listing → Publish → Distribution
→ Learnings Capture → Factory Standards Update
```

---

## Stage 1: Idea

**Gate:** Does this product meet ALL selection criteria?

**Checks:**
- [ ] Proven demand (similar products already selling)
- [ ] Buildable in 1–2 days
- [ ] Fits spreadsheet/template/calculator format
- [ ] Clear buyer ROI (saves time, saves money, reduces mistakes)
- [ ] Explainable in one sentence

**Output:** Decision: build now, defer, or reject.

**References:**
- [Selection Rules](PRODUCT_FACTORY_CONTEXT.md#selection-rules)
- [Strategy](PRODUCT_FACTORY_STRATEGY.md)

---

## Stage 2: Build

**Gate:** Workbook is functional with all required tabs. Brand is locked before any file is created.

**Rules:**
- Brand (Nivora), support email (workbysar1@gmail.com), and naming conventions locked before first file
- No SaaS, no code-heavy product, no full brand system
- Spreadsheet/template/calculator first
- Smallest useful paid version only

**Output:** Draft workbook with realistic sample data.

**References:**
- [Product Structure](PRODUCT_FACTORY_PRODUCT_STRUCTURE.md) — workspace folders
- [Brand Standard](07-systems/BRAND_STANDARD.md)

---

## Stage 3: Internal QA

**Gate:** All QA checks pass. No P0/P1 issues.

**Required:**
- Formula audit — all cross-sheet references correct
- Google Sheets compatibility test
- All tabs, formulas, dropdowns, formatting verified
- Dashboard values spot-checked against source data

**Output:** QA report and list of any fixes applied.

**References:**
- [Pre-Publish QA](PRODUCT_FACTORY_PRE_PUBLISH_QA.md) — Content Review section
- [Delivery Standard](PRODUCT_FACTORY_DELIVERY_STANDARD.md)

---

## Stage 4: Asset Generation

**Gate:** All 6 marketplace images created and verified. Assets generated AFTER workbook is final.

**Required images:**
1. `01-cover.png` — Cover with brand, preview, benefits
2. `02-dashboard.png` — Dashboard with real data
3. `03-primary-feature.png` — Main input workflow
4. `04-secondary-feature.png` — Secondary workflow
5. `05-supporting-feature.png` — Less obvious features
6. `06-whats-included.png` — Deliverables overview

**Timing:** Generate assets only after workbook is complete and QA'd. Generating early causes rework.

**References:**
- [Asset Specifications](PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md)
- [Listing Asset Standard](templates/LISTING_ASSET_STANDARD.md)

---

## Stage 5: Packaging

**Gate:** Delivery folder contains only buyer-facing assets. ZIP is built and verified.

**Sequence (order matters):**
1. Export final branded workbook
2. Create Google Sheets copy and validate copy link
3. Create copy link file
4. Generate PDF guide (2nd-to-last step)
5. Build delivery ZIP (final step — exactly 3 files)

**ZIP contents:**
```
{brand}-{product-slug}-delivery.zip
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
└── google-sheets-copy-link.txt
```

**References:**
- [Delivery Standard](PRODUCT_FACTORY_DELIVERY_STANDARD.md)
- [Product Structure](PRODUCT_FACTORY_PRODUCT_STRUCTURE.md)

---

## Stage 6: Marketplace Listing

**Gate:** Listing is drafted but not yet published.

**Platforms (current):**
- Gumroad (product-first, no storefront required)
- Payhip (storefront-first, brand/store required)

**Required for both:**
- All 6 gallery images uploaded in correct order
- Cover image set as thumbnail
- ZIP uploaded as product file
- Complete listing copy (What's Included, Who It's For, Benefits, FAQ)
- Price set
- Test purchase completed

**References:**
- [Marketplace Checklist](PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md)
- [Asset Specifications](PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md)

---

## Stage 7: Publish

**Gate:** Pre-publish review passes ALL sections. Test purchase works.

**Reviews required:**
1. Content Review — product correctness and completeness
2. Branding Review — brand consistency across all buyer-facing content
3. Packaging Review — delivery package clean and professional
4. Marketplace Review — listing complete and accurate
5. Delivery Review — buyer experience from purchase through first use

**All 5 must pass. No partial gates.**

**References:**
- [Pre-Publish QA](PRODUCT_FACTORY_PRE_PUBLISH_QA.md)
- [Pre-Publish Checklist](templates/PRE_PUBLISH_CHECKLIST.md)

---

## Stage 8: Distribution

**Gate:** Listing is live. Product is available for purchase.

**Actions:**
- Record Gumroad URL in PRODUCT_CATALOG.csv
- Record Payhip URL in PRODUCT_CATALOG.csv
- Update product status to Published
- Verify listing visible in marketplace search
- Verify purchase flow works (incognito test)

**References:**
- [Product Catalog](../00-control/PRODUCT_CATALOG.csv)

---

## Stage 9: Learnings Capture

**Gate:** RETROSPECTIVE.md created in product workspace.

**Document:**
- What worked
- What caused friction
- Buyer friction (observed or suspected)
- Asset/screenshot improvements
- Listing/copy improvements
- Packaging/delivery improvements
- Lessons learned (numbered)
- Standard updates required (checklist)

**References:**
- [Retrospective Template](templates/PRODUCT_RETROSPECTIVE_TEMPLATE.md)

---

## Stage 10: Factory Standards Update

**Gate:** Lessons from retrospective are applied to factory standards.

**Process:**
1. Review each lesson against existing standards
2. If standard covers it — is it adequate?
3. If not — create or update the relevant document
4. Update continuation/context files
5. Log the decision

**Then:** Start the next product.

**References:**
- [Publishing Playbook](PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md) (end-to-end process)

---

## Workflow Rules Summary

| # | Rule | Source |
|---|------|--------|
| 1 | Brand locked before any build work | Product #1 branding rework lesson |
| 2 | Assets generated only after workbook is final | Product #1 screenshot retake lesson |
| 3 | ZIP is the final step (exactly 3 files) | Product #1 delivery cleanup lesson |
| 4 | PDF is second-to-last step | Product #1 PDF regeneration lesson |
| 5 | All 5 reviews must pass before publishing | Product #1 formula bug in late stage |
| 6 | Retrospective required for every product | Product #1 process hardening |
| 7 | Lessons update factory standards | Continuous improvement loop |
