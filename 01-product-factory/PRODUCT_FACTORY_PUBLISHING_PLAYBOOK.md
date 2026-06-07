# Product Factory Publishing Playbook

> End-to-end playbook for shipping a Product Factory product. Hardened from Product #1 (Nivora Budget Planner & Expense Tracker).

---

## Overview

Each product follows this 10-stage pipeline:

```
Idea → Build → Internal QA → Asset Generation → Packaging
→ Marketplace Listing → Publish → Distribution
→ Learnings Capture → Factory Standards Update
```

Total target: 1–2 days per product.

---

## Stage 1: Idea

**Gate:** Does this meet all selection criteria?
- [ ] Proven demand (similar products already selling)
- [ ] Buildable in 1–2 days
- [ ] Fits spreadsheet/template/calculator format
- [ ] Clear buyer ROI (saves time, saves money, reduces mistakes)
- [ ] Explainable in one sentence

If yes, create the product workspace and move to Build.

---

## Stage 2: Build

**Gate:** Workbook is functional with all required tabs.

**Rules:**
- Brand (Nivora), support email (workbysar1@gmail.com), and naming conventions already locked — never start without these
- No SaaS, no code-heavy product, no full brand system
- Spreadsheet/template/calculator first
- Smallest useful paid version only

**Output:** Draft workbook with sample data.

---

## Stage 3: Internal QA

**Gate:** All QA checks pass with no P0/P1 issues.

**Required checks:**
- [ ] All tabs created and named correctly
- [ ] All formulas return expected results — no #REF!, #VALUE!, #DIV/0!
- [ ] Cross-sheet SUMIF/COUNTIF references verified
- [ ] Dashboard summary values match source data (spot-check 3+)
- [ ] Data validation dropdowns work on all required columns
- [ ] Conditional formatting applied correctly
- [ ] Freeze panes set on data tabs
- [ ] Sample data populated and realistic
- [ ] Formula cells marked (gray background), input cells clear
- [ ] No hardcoded values where formulas should exist
- [ ] IFERROR wrappers present where division by zero is possible
- [ ] Charts render correctly (if applicable)
- [ ] Print layout acceptable
- [ ] Google Sheets upload: formulas survive conversion
- [ ] Google Sheets: conditional formatting survives
- [ ] Google Sheets: copy link works (test manually)

**Do not proceed if any P0/P1 issue remains.**

---

## Stage 4: Asset Generation

**Gate:** All 6 marketplace images created and QA'd.

**Timing:** Assets are generated only after the workbook is complete, QA'd, and branded. Never generate assets before the workbook is final.

**Required image set:**

| # | File | Content | Purpose |
|---|------|---------|---------|
| 1 | `01-cover.png` | Product cover with brand, preview, benefits | Thumbnail — drives click-through |
| 2 | `02-dashboard.png` | Dashboard with real sample data | First value impression |
| 3 | `03-primary-feature.png` | Main input sheet / core utility | Core utility demonstration |
| 4 | `04-secondary-feature.png` | Supporting feature or workflow | Shows product depth |
| 5 | `05-supporting-feature.png` | Less obvious features | Captures undecided buyers |
| 6 | `06-whats-included.png` | Deliverables checklist or feature grid | Answers "what do I get?" |

**Specifications:**
- PNG format, 1000–1920px wide
- Consistent aspect ratio across all 6 images
- Text legible at 280px thumbnail width
- No browser chrome, bookmarks, personal data
- Brand (Nivora) on cover and where appropriate
- Real sample data — never empty sheets

**Upload order on marketplace:** 1 (Cover) → 2 (Dashboard) → 3 (Primary Feature) → 4 (Secondary Feature) → 5 (Supporting Feature) → 6 (What's Included)

---

## Stage 5: Packaging

**Gate:** Delivery folder contains only buyer-facing assets. ZIP is built and verified.

**Sequence (order matters):**
1. Export final branded workbook → `{brand}-{product-slug}.xlsx`
2. Create Google Sheets copy → validate copy link works
3. Create copy link file → `google-sheets-copy-link.txt`
4. Generate PDF guide → `{brand}-{product-slug}-quick-start-guide.pdf` (second-to-last step)
5. Build delivery ZIP → `{brand}-{product-slug}-delivery.zip` (final step)

**ZIP contents (exactly 3 files, no subdirectories):**
```
{brand}-{product-slug}-delivery.zip
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
└── google-sheets-copy-link.txt
```

**Exclude from ZIP:**
- Screenshots (uploaded directly to marketplace)
- Source/planning files (.md, .html, .py)
- QA docs and checklists
- Listing assets (cover, feature images)
- Release notes
- Versioned artifact files
- Any internal or planning documents

**Delivery folder structure:**
```
delivery/
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
├── google-sheets-copy-link.txt
├── {brand}-{product-slug}-delivery.zip
├── listing-assets/           # 6 gallery images
└── screenshots/              # Raw screenshot sources
```

---

## Stage 6: Marketplace Listing

**Gate:** Listing is drafted but not yet published.

### Gumroad

- Product-first platform
- No traditional storefront requirement
- Thumbnail required (cover image)
- Cover image required (16:9 recommended)
- PayPal required for India-based sellers
- CTA options limited (buy now / pre-order)
- Upload ZIP + 6 gallery images
- Set price
- Test checkout before publishing

### Payhip

- Storefront-first platform
- Brand/store name required
- PayPal integration required
- Create store before first listing
- Upload same ZIP + images
- Set same price

### Listing Copy Requirements

- **Title:** SEO-friendly, discoverable. Format: `{Product Name} — Google Sheets + Excel`
- **Publisher line:** `by Nivora`
- **What's Included:** Specific deliverables listed (not generic descriptions)
- **Who It's For:** Target audience description
- **Benefits:** Address buyer pain points, not just features
- **FAQ:** Address common hesitations (e.g., "Do I need spreadsheet skills?")
- **Support contact:** workbysar1@gmail.com

---

## Stage 7: Publish

**Gate:** Pre-publish review passes all sections. Test purchase completes.

**Pre-flight checks:**
- [ ] ZIP opens and contains exactly 3 files
- [ ] Excel file opens without errors
- [ ] Google Sheets copy link works (test manually)
- [ ] PDF guide opens and has correct brand/title
- [ ] Dashboard formulas return correct values
- [ ] Screenshots match final product version
- [ ] Brand is consistent across all buyer-facing content
- [ ] Marketplace copy is complete and accurate
- [ ] Test checkout/purchase works end-to-end
- [ ] All 6 images uploaded in correct order
- [ ] Cover set as thumbnail
- [ ] ZIP uploaded as product file
- [ ] Price set

**Publish on Gumroad first, then Payhip.**

---

## Stage 8: Distribution

**Gate:** Listing URLs recorded. Product is available for purchase.

- [ ] Record Gumroad URL in PRODUCT_CATALOG.csv
- [ ] Record Payhip URL in PRODUCT_CATALOG.csv
- [ ] Update product status to Published in PRODUCT_CATALOG.csv
- [ ] Verify listing is visible in marketplace search
- [ ] Verify purchase flow works (incognito test)

---

## Stage 9: Learnings Capture

**Gate:** RETROSPECTIVE.md created in product workspace.

Create `RETROSPECTIVE.md` documenting:
- What worked
- What caused friction
- Buyer friction (observed or suspected)
- Asset/screenshot improvements
- Listing/copy improvements
- Packaging/delivery improvements
- Lessons learned (numbered)
- Standard updates required (checklist)

---

## Stage 10: Factory Standards Update

**Gate:** Lessons from retrospective are applied to factory standards.

For each lesson captured:
1. Does a standard already cover this? If yes, is it adequate?
2. If not, create or update the relevant standard document
3. Update continuation/context files if needed
4. Document the change in the decision log

**Then:** Move to next product.

---

## Brand & Naming Reference (Locked)

| Property | Value |
|----------|-------|
| Brand name | Nivora |
| Support email | workbysar1@gmail.com |
| Platform accounts | Gumroad, Payhip (under workbysar1@gmail.com) |
| File naming | `nivora-{product-slug}.{ext}` |
| Marketplace publisher | "by Nivora" |
| Internal operator label | "Work by Sar1" — never customer-facing |

---

## Timeline Summary

| Stage | Target Duration |
|-------|----------------|
| Idea | < 1 hour |
| Build | 2–6 hours |
| Internal QA | 1–2 hours |
| Asset Generation | 1–2 hours |
| Packaging | 1 hour |
| Marketplace Listing | 1 hour |
| Publish | 30 min |
| Distribution | 15 min |
| Learnings Capture | 30 min |
| Factory Standards Update | 30 min |
| **Total** | **8–14 hours (~1–2 days)** |
