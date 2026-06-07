# Product Factory Lessons Learned — V1

> Captured from Product #1: Nivora Budget Planner & Expense Tracker

---

## A. Branding Lessons

| Lesson | Impact |
|--------|--------|
| Product needs brand before publishing | Starting without a brand causes rework: all files, images, listing copy, and PDFs need renaming mid-pipeline |
| Personal email is not a brand | `workbysar1@gmail.com` is a contact method, not a publisher identity. Marketplace buyers buy from brands, not email addresses |
| Brand name must be decided before listing assets | Listing covers, preview images, and screenshots must show the brand consistently from day one |
| Product filenames should use brand naming convention | Renaming `budget-planner-expense-tracker.xlsx` → `nivora-budget-planner-expense-tracker.xlsx` touched 10+ files mid-pipeline |
| Marketplace assets should show brand consistently | All 5 listing images had to be regenerated when brand changed from "Work by Sar1" to "Nivora" |

**Decision:** Brand = Nivora (locked for all future products)

---

## B. Screenshot Lessons

**Screenshots must show actual product data.** Do not submit empty templates or generic mockups.

**Required for every product:**
- Dashboard or summary view with real sample data
- Primary feature view (formulas visible where possible)
- Secondary feature view (dropdowns, filters, data validation)
- Advanced view (less obvious tabs that add value)
- "What's Included" overview

**Avoid:**
- Empty sheets with no sample data
- Generic mockups only (no actual product screenshots)
- Cropped UI that hides key features
- Unreadable text at marketplace thumbnail sizes

---

## C. Cover Image Lessons

**The cover image must communicate value in 3 seconds.**

Requirements:
- Shows a workbook preview (not just a logo)
- Indicates both Google Sheets + Excel support
- Shows the brand name
- Lists key benefits at a glance
- Is legible at thumbnail size (Gumroad displays ~280px wide)

---

## D. Packaging Lessons

**Buyer ZIP must contain only what the buyer needs:**

```
product-name.zip
├── product-name.xlsx
├── product-name-quick-start-guide.pdf
└── google-sheets-copy-link.txt
```

**Exclude:**
- Screenshots (uploaded directly to marketplace)
- Source/planning files (MD, HTML, release notes)
- QA docs (FINAL_ZIP_QA.md, BRAND_QA_CHECKLIST.md, etc.)
- Listing assets (cover, feature images)
- Internal notes or versioned artifact names
- No subdirectories inside ZIP unless unavoidable

---

## E. Listing Lessons

**Required marketplace images (order matters):**

| Order | Image | Purpose |
|-------|-------|---------|
| 1 | Cover | Thumbnail — value in 3 seconds |
| 2 | Dashboard | Full overview showing real data |
| 3 | Primary feature | Main utility in action |
| 4 | Secondary feature | Supporting workflow |
| 5 | Advanced features | Less obvious value |
| 6 | What's Included | Checklist of deliverables |

**Listing copy must include:**
- What's Included section with specific deliverables
- Who it's for
- Benefits (not just features)
- FAQ addressing common hesitations
- Support contact

---

## F. Product Evaluation Lessons

**Every product must pass a pre-publish review before listing creation begins.**

Checklist dimensions:
- **Trust:** Does the product look legitimate? No broken formulas, clean layout, professional styling
- **Perceived value:** Would a buyer feel they got their money's worth? At $7, the product must clearly deliver more than $7 of value
- **Clarity:** Can a buyer understand what they're getting in 10 seconds? Title, cover, and first screenshot must answer "what is this and do I need it?"
- **Professionalism:** No typos, no version numbers in buyer files, consistent branding, proper file naming
- **Delivery quality:** ZIP is clean, PDF is readable, copy link works, no broken references

---

## Action Items for Future Products

1. Decide brand before any build work begins
2. Create brand-standard file naming early
3. Generate marketplace assets as part of packaging (not after)
4. Include pre-publish review as a mandatory workflow stage
5. Use the same asset naming convention across all products
6. Never include internal files in buyer delivery
7. Validate Google Sheets copy link before listing
8. Run brand consistency scan before finalizing delivery
