# Product #1 Retrospective — Nivora Budget Planner & Expense Tracker

> Completed pre-publish, before listing goes live. Lessons captured as Product Factory standards.

---

## Product Info

| Field | Value |
|-------|-------|
| Product name | Nivora Budget Planner & Expense Tracker |
| Brand | Nivora |
| Platform(s) | Gumroad + Payhip |
| Price | $7 |
| Status | Ready to Publish |
| Format | Google Sheets + Excel spreadsheet (7 tabs) |

---

## What Worked

- **Automated QA:** 55/55 checks caught formula bugs early (17 SUMIF column refs fixed)
- **Google Sheets navigation note:** Replacing hyperlinks with plain text instructions was the right call — avoids broken links on GS
- **Final ZIP cleanup:** Moving from 6 files to 3 files in the ZIP made the delivery feel professional
- **Delivery folder separation:** Moving internal docs to `docs/` cleaned up the buyer-facing folder
- **Brand finalization:** Locking "Nivora" mid-pipeline was painful but correct — starting without a brand caused rework

## What Caused Friction

- **Brand started as "Work by Sar1":** Had to rename all files, images, PDFs, listing copy mid-pipeline. Brand should be decided before build starts.
- **Screenshots generated too early:** Cover and feature images had to be regenerated twice (brand change + workbook fixes). Screenshots should be final-phase only.
- **No pre-publish gate:** Dashboard formula bug (B40/B41 wrong cell refs) was caught during polish, not during QA. A formal gate would have caught it earlier.
- **PDF generated before final workbook:** PDF had old titles, had to be regenerated. PDF should be the last thing before ZIP.
- **No standard image set:** 5 images were created ad-hoc. Should be 6 standardized images (cover, dashboard, main input, core feature, secondary features, what's included).
- **Copy link URL changed mid-pipeline:** Had to update link 3 times. Copy link should be validated once and locked.

## Buyer Friction (observed or suspected)

- **Navigation in Google Sheets:** Hyperlinks don't work after GS import. The plain text instruction fix addresses this, but users may still expect clickable navigation.
- **File naming confusion:** Early files had `budget-planner-expense-tracker.xlsx` without brand prefix. Late rename to `nivora-*.xlsx` is better but could confuse early testers.

## Asset / Screenshot Improvements

- Need a standard 6-image set for every product
- Cover image must communicate value at thumbnail size
- Screenshots must show real data, not empty templates
- Dashboard screenshot is the most important — should be the second image
- "What's Included" image is worth creating — answers the main buyer question

## Listing / Copy Improvements

- "What's Included" section needs specific deliverables, not generic descriptions
- Benefits section needs to address pain points, not list features
- FAQ is important for conversion — address "do I need spreadsheet skills?"
- Support contact builds trust

## Packaging / Delivery Improvements

- ZIP should contain exactly 3 files: workbook, PDF, copy link
- No internal files in delivery folder
- No version numbers in buyer filenames
- Brand prefix on all delivery files
- Delivery folder = buyer-facing only; docs/ = internal

## Lessons Learned

1. **Brand first.** Finalize brand name, support email, and naming conventions before any build or asset work.
2. **Screenshots last.** Take screenshots and generate listing assets only after the workbook is complete, QA'd, and branded.
3. **Pre-publish gate required.** A formal checklist must be completed before listing goes live.
4. **Standard image set.** 6 images minimum (cover, dashboard, main input, core feature, secondary features, what's included).
5. **ZIP as final step.** Build the ZIP only after all files are finalized and QA'd.
6. **PDF is second-to-last.** Generate PDF after workbook is final, before ZIP creation.
7. **Copy link is fragile.** Lock the GS copy link early and only change if absolutely necessary.
8. **Retrospectives create standards.** Every product's lessons should update the factory templates.

## Standard Updates Required

- [x] Brand Standard — created (BRAND_STANDARD.md)
- [x] Delivery Standard — created (DELIVERY_STANDARD.md)
- [x] Asset Standard — created (MARKETPLACE_ASSET_STANDARD.md)
- [x] Pre-Publish Checklist — created (PRE_PUBLISH_REVIEW_CHECKLIST.md)
- [x] Retrospective Template — created (PRODUCT_RELEASE_RETROSPECTIVE_TEMPLATE.md)
- [x] Delivery folder structure rule — added to DELIVERY_STANDARD.md
- [x] Brand-first workflow — added to DELIVERY_STRUCTURE_STANDARD.md

## Verdict

- [x] Move on (improvements captured as standards for Product #2+)
