# Pre-Publish Review Checklist

> Must pass all sections before any product listing goes live.
>
> **Gate rule:** No product can become "Delivery Ready" unless all 10 QA layers
> from `QA_COVERAGE_STANDARD.md` are complete. Review this checklist as the
> final Layer 10 verification.

---

## Section A: Workbook Quality

- [ ] All tabs created and named correctly
- [ ] All formulas return expected results (no #REF!, #VALUE!, #DIV/0! errors)
- [ ] Formula cells marked with gray background
- [ ] Input cells clearly marked
- [ ] Data validation dropdowns working on all required columns
- [ ] Conditional formatting applied correctly
- [ ] Freeze panes set on data tabs
- [ ] Sample data populated and realistic
- [ ] Charts render correctly (if applicable)
- [ ] Print layout acceptable (no cutoff content)

## Section B: Formula Validation

- [ ] All cross-sheet SUMIF/COUNTIF references point to correct columns
- [ ] SUM totals include correct ranges
- [ ] IFERROR wrappers present where division by zero is possible
- [ ] Dashboard summary values match source data (spot-check 3+ values)
- [ ] No hardcoded values where formulas should exist
- [ ] No circular references

## Section C: Branding Validation

- [ ] Customer-facing brand name is set (Nivora)
- [ ] Brand appears consistently in: workbook title, PDF guide, copy link file, listing copy
- [ ] No personal email used as brand name
- [ ] Support email is present only as contact method (not as brand)
- [ ] All delivery filenames use brand naming convention
- [ ] Brand name does not appear in internal/QA files that could leak into delivery
- [ ] Brand consistency scan passed (automated grep for old brand names)

## Section D: Delivery Validation

- [ ] Buyer workbook filename uses brand prefix (e.g., `nivora-*.xlsx`)
- [ ] PDF guide filename uses brand prefix
- [ ] ZIP filename uses brand prefix
- [ ] ZIP contains exactly: workbook, PDF guide, copy link file
- [ ] No internal files in ZIP (QA docs, source MD/HTML, release notes, screenshots, listing assets)
- [ ] No version numbers in buyer-facing filenames
- [ ] Google Sheets copy link works (tested manually)
- [ ] PDF guide is readable and contains correct brand/title
- [ ] Buyer ZIP verified programmatically — contents match expected list

## Section E: Screenshot Validation

- [ ] Cover image communicates value in 3 seconds at thumbnail size
- [ ] Dashboard screenshot shows real data (not empty)
- [ ] Primary feature screenshot shows core utility
- [ ] Secondary feature screenshot shows supporting workflow
- [ ] Advanced features screenshot captures less obvious value
- [ ] All screenshots show actual product (no generic mockups)
- [ ] Text is legible at marketplace display sizes
- [ ] Brand appears in screenshots where appropriate
- [ ] No UI chrome, bookmarks, or personal information visible
- [ ] All screenshots use consistent dimensions and styling

## Section F: Marketplace Listing Validation

- [ ] Product title is clear and searchable
- [ ] Subtitle/one-liner explains value proposition
- [ ] What's Included section lists specific deliverables
- [ ] Who It's For section targets the right buyer
- [ ] Benefits section addresses buyer pain points
- [ ] FAQ answers common hesitations
- [ ] Support contact is included
- [ ] Price is set (Product 1 baseline: $7)
- [ ] All 6 gallery images uploaded in correct order
- [ ] ZIP file uploaded as product file
- [ ] Cover image set as thumbnail
- [ ] Preview/test purchase works end-to-end

## Section G: Buyer Experience Validation

- [ ] Buyer can understand the product in 10 seconds from title + cover
- [ ] After purchase, buyer receives clear instructions
- [ ] Google Sheets copy link works immediately
- [ ] Excel file opens without errors
- [ ] PDF guide is included and complete
- [ ] No broken references or missing files in delivery
- [ ] First-time user can start using the product without external help

---

## Publishing Gate

**All items in Sections A–G must be checked before publishing.**

Additionally, all 10 QA layers from `QA_COVERAGE_STANDARD.md` must be complete:
1. Automated workbook validation — must pass 100%
2. Formula/business logic tests — must pass 100%
3. Google Sheets compatibility lint — must pass 100%
4. UI/layout checks — must pass 100%
5. Manual smoke QA — all 9 steps documented as PASS
6. Delivery package QA — all tests pass
7. Marketplace asset QA — all 6 images meet spec
8. Listing copy QA — all sections complete
9. Link/copy-link QA — link tested and verified
10. Final pre-publish gate — this checklist, all sections A–G pass

If any item fails:
1. Fix the issue
2. Re-verify
3. Do not proceed until all sections pass

Gate keeper: AI agent or human reviewer

**No product can become "Delivery Ready" unless all 10 QA layers are complete.**

---

## Post-Publish Requirement

After publishing, create `RETROSPECTIVE.md` in the product workspace documenting what worked, what failed, and lessons learned. Every retrospective's lessons must be reviewed and potentially added to Product Factory standards. See [Retrospective Template](../templates/PRODUCT_RETROSPECTIVE_TEMPLATE.md).
