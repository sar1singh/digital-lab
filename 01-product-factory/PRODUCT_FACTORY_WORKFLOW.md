# Product Factory Workflow

## Loop

Research -> Validate -> Build -> QA -> Package -> Pre-Publish Review -> List -> Publish -> Track -> Retrospective

## Stage 1: Research

Goal: confirm that buyers already pay for this type of product.

Outputs:
- Competitor examples
- Price range
- Common features
- Common listing language
- Buyer pain points
- Differentiation angle

Use: [Product Research Template](03-templates/PRODUCT_RESEARCH_TEMPLATE.md)

## Stage 2: Validate

Goal: decide whether to build now, defer, or reject.

Build only if:
- There are existing paid products in the category.
- The product can be explained in one sentence.
- A first version can be built in 1-2 days.
- The buyer has a money, time, or mistake-reduction reason to pay.

Use: [Product Validation Template](03-templates/PRODUCT_VALIDATION_TEMPLATE.md)

## Stage 3: Build

Goal: create the smallest useful paid version.

Rules:
- No SaaS.
- No code-heavy product.
- No full brand system.
- No website.
- Spreadsheet/template/calculator first.

Use: [Product Build Checklist](03-templates/PRODUCT_BUILD_CHECKLIST.md), [Delivery Structure Standard](templates/DELIVERY_STRUCTURE_STANDARD.md) (Brand-First Workflow section)

## Stage 4: QA

Goal: verify the product works correctly before packaging.

Required:
- Formula audit — all cross-sheet references correct
- Automated checks where possible
- Manual spot-check of key values
- Navigation test (all tabs, all links)
- Google Sheets compatibility test (if applicable)

Use: Product-specific QA checklists

## Stage 5: Package

Goal: make the product easy to understand, buy, and use.

Required:
- Clear product title with brand prefix
- Plain promise
- Screenshot or preview
- What's included
- Who it is for
- Simple usage instructions
- Refund/support note
- Delivery ZIP with exactly 3 files (workbook, PDF, copy link)
- All filenames use brand naming convention

Use: [Delivery Standard](07-systems/DELIVERY_STANDARD.md), [Brand Standard](07-systems/BRAND_STANDARD.md)

## Stage 6: Pre-Publish Review

Goal: catch all quality, branding, delivery, and listing issues before going live.

Gate: all sections of the Pre-Publish Checklist must pass before listing creation begins.

Use: [Pre-Publish Checklist](templates/PRE_PUBLISH_CHECKLIST.md), [Delivery Structure Standard](templates/DELIVERY_STRUCTURE_STANDARD.md), [Listing Asset Standard](templates/LISTING_ASSET_STANDARD.md)

## Stage 7: List

Goal: create the marketplace listing.

Platforms:
- Gumroad first
- Payhip second if easy

Required:
- All 6 gallery images uploaded in correct order
- Cover image set as thumbnail
- What's Included section in description
- Clear pricing
- ZIP file uploaded
- Test purchase before publishing

Use: [Product Listing Template](03-templates/PRODUCT_LISTING_TEMPLATE.md), [Listing Asset Standard](templates/LISTING_ASSET_STANDARD.md)

## Stage 8: Publish

Goal: get the listing live.

Use: Product Launch Checklist

## Stage 9: Track

Goal: monitor performance and identify improvements.

Track:
- Product status
- Listing URL
- Price
- Views
- Sales
- Revenue
- Notes

Use: [Product Catalog](00-control/PRODUCT_CATALOG.csv)

## Stage 10: Retrospective

Goal: capture lessons learned before starting the next product.

Complete after publishing or after one week live. Create `RETROSPECTIVE.md` in the product workspace.

Use: [Product Retrospective Template](templates/PRODUCT_RETROSPECTIVE_TEMPLATE.md)

Every retrospective's lessons become Product Factory standards. Update templates and context files accordingly.
