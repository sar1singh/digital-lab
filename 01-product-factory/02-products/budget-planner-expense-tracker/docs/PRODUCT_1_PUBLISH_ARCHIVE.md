# Product 1 Publish Archive

> Internal documents moved from `delivery/` to `docs/` during pre-publish cleanup.

---

## Why Files Were Moved

The `delivery/` folder is reserved for **customer-facing assets only**. Internal planning, QA, and reference documents belong in `docs/` to prevent accidental inclusion in buyer delivery and to keep the delivery folder clean for marketplace upload.

---

## Moved Files

| File | Origin | Destination |
|------|--------|-------------|
| BRAND_QA_CHECKLIST.md | `delivery/` | `docs/` |
| FINAL_PUBLISH_STATUS.md | `delivery/` | `docs/` |
| FINAL_ZIP_QA.md | `delivery/` | `docs/` |
| GUMROAD_IMAGE_ORDER.md | `delivery/` | `docs/` |
| PUBLISHING_READINESS_CHECKLIST.md | `delivery/` | `docs/` |
| SCREENSHOT_RETAKE_GUIDE.md | `delivery/` | `docs/` |
| WHATS_INCLUDED_CARD_TEXT.md | `delivery/` | `docs/` |
| quick-start-guide.md | `delivery/` | `docs/` |
| quick-start-guide.html | `delivery/` | `docs/` |
| release-notes.txt | `delivery/` | `docs/` |

---

## Final Delivery Structure

```
delivery/
├── nivora-budget-planner-expense-tracker.xlsx        # Buyer workbook
├── nivora-budget-planner-expense-tracker-quick-start-guide.pdf  # Buyer PDF guide
├── google-sheets-copy-link.txt                       # Google Sheets copy instructions
├── nivora-budget-planner-expense-tracker-delivery.zip # Buyer ZIP (contains above 3 files)
├── listing-assets/                                    # Marketplace gallery images
│   ├── 01-cover.png
│   ├── 02-dashboard.png
│   ├── 03-monthly-budget.png
│   ├── 04-expense-tracker.png
│   └── 05-bills-debt-savings.png
└── screenshots/                                       # Raw screenshot sources
```

Only customer-facing assets remain in delivery.

---

## Delivery Rule

From DELIVERY_STANDARD.md:

> **Delivery folder contains only buyer-facing assets and final ZIP.** Internal planning, QA, and reference documents belong in `docs/` or product workspace root.
