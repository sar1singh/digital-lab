# Sheet Structure — Nivora Invoice Generator & Payment Tracker

## Tab 1: Start Here

Purpose: Setup instructions, warnings, quick navigation guide.

Contents:
- Welcome and product overview
- How to use (setup steps)
- Do not edit formula cells warning
- Google Sheets usage instructions
- Tab navigation guide

---

## Tab 2: Dashboard

Purpose: Key metrics and visual summaries.

Layout (top to bottom, left to right):

**Summary Cards Row:**
- Total Revenue (formula from Invoice Register)
- Paid Revenue (formula — SUMIFS)
- Outstanding Revenue (formula — SUMIFS)
- Total Invoices (formula — COUNTA)

**Summary Cards Row 2:**
- Paid Invoices (COUNTIFS)
- Unpaid Invoices (COUNTIFS)
- Overdue Invoices (COUNTIFS)
- Active Clients (COUNTIF)

**Summary Cards Row 3:**
- Average Invoice Value (formula — AVERAGEIF)
- Revenue by Month summary section
- Invoice Status Breakdown section
- Top Clients by Revenue section

---

## Tab 3: Clients

Purpose: Store and manage client information.

Columns:

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Client ID | Text | Auto-generated or manual entry |
| B | Client Name | Text | Required |
| C | Company | Text | Optional |
| D | Email | Text | Contact email |
| E | Phone | Text | Contact phone |
| F | Address | Text | Full address |
| G | Status | Dropdown | Active / Inactive / Archived |
| H | Notes | Text | Optional notes |

---

## Tab 4: Invoice Register

Purpose: All invoices with status tracking.

Columns:

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Invoice ID | Text | Manual or structured ID (e.g., INV-001) |
| B | Invoice Date | Date | Date invoice issued |
| C | Due Date | Date | Payment due date |
| D | Client ID | Text | Links to Clients tab |
| E | Client Name | Text | VLOOKUP from Clients |
| F | Description | Text | Brief invoice description |
| G | Subtotal | Currency | Sum of line items |
| H | Tax Rate | Percentage | From Settings or manual |
| I | Tax Amount | Currency | Formula: Subtotal * Tax Rate |
| J | Total | Currency | Formula: Subtotal + Tax Amount |
| K | Amount Paid | Currency | Manual entry as payments arrive |
| L | Outstanding | Currency | Formula: Total - Amount Paid |
| M | Status | Formula | Paid / Overdue / Partial / Sent / Draft |

---

## Tab 5: Payment Tracker

Purpose: Track individual payments received.

Columns:

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Payment ID | Text | Structured ID (e.g., PAY-001) |
| B | Invoice ID | Text | Links to Invoice Register |
| C | Client Name | Text | VLOOKUP via Invoice ID |
| D | Payment Date | Date | Date payment received |
| E | Payment Method | Dropdown | From Settings |
| F | Amount | Currency | Payment amount |
| G | Notes | Text | Optional |

---

## Tab 6: Invoice Generator

Purpose: Printable invoice layout with auto-calculations.

Layout:

**Header Section:**
- Invoice title
- Invoice number (manual or pre-filled)
- Invoice date (TODAY or manual)
- Due date (manual)

**From Section:**
- Your name / company (manual entry)
- Your address (manual entry)

**Bill To Section:**
- Client Name (manual or dropdown)
- Client Company (auto-filled)
- Client Address (auto-filled)

**Line Items Table:**
| # | Description | Quantity | Rate | Amount |
|---|-------------|----------|------|--------|
| 1 | (manual) | (number) | (currency) | =Quantity*Rate |
| 2 | ... | ... | ... | ... |

**Summary Section:**
- Subtotal (=SUM of Amount column)
- Tax Rate (from Settings or manual)
- Tax Amount (=Subtotal * Tax Rate)
- Total (=Subtotal + Tax Amount)

**Payment Instructions Section:**
- Payment methods accepted (manual text)
- Payment terms (manual text)

---

## Tab 7: Settings

Purpose: Configure dropdown values, currency, and defaults.

Layout (key-value pairs):

| Setting | Value |
|---------|-------|
| Currency Symbol | $ |
| Default Tax Rate | 10% |
| Invoice Status Values | Sent, Partial, Paid, Overdue, Draft |
| Payment Method Values | Bank Transfer, PayPal, Cash, Cheque, Credit Card, Other |
| Client Status Values | Active, Inactive, Archived |
