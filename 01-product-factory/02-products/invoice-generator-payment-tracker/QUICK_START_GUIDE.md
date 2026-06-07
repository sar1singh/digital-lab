# Nivora Invoice Generator & Payment Tracker — Quick-Start Guide

## Welcome

Thank you for purchasing **Nivora Invoice Generator & Payment Tracker**. This spreadsheet helps freelancers, consultants, and independent professionals create invoices, track payments, manage clients, and monitor revenue — all in one file.

No special skills needed. Just fill in the highlighted input cells — everything else calculates automatically.

---

## Workbook Overview

The workbook contains **7 tabs**:

| Tab | Purpose |
|-----|---------|
| **Start Here** | Setup instructions and navigation |
| **Dashboard** | Revenue KPIs, invoice status, monthly trends, top clients |
| **Clients** | Client directory with contact details and status tracking |
| **Invoice Register** | All invoices with auto-calculated status (Paid, Sent, Overdue, Partial, Draft) |
| **Payment Tracker** | All payments received, linked to invoices automatically |
| **Invoice Generator** | Printable invoice with auto-calculated subtotal, tax, and total |
| **Settings** | Currency, tax rate, dropdown values (statuses, payment methods) |

**Important:** Cells with **gray background** contain formulas — do not edit them. Cells with **white or green background** are for your input.

---

## Quick Start

1. **Open the file** — Use the Google Sheets copy link, or open the XLSX in Excel
2. **Go to Settings first** — Set your currency symbol and default tax rate
3. **Add your clients** — Enter client details in the Clients tab
4. **Create invoices** — Use the Invoice Generator or enter invoices in the Invoice Register
5. **Track payments** — Log payments in the Payment Tracker tab
6. **View your Dashboard** — All metrics update automatically

---

## Dashboard

The Dashboard tab shows your business at a glance with these sections:

- **KPI Cards** — Total Revenue, Paid Revenue, Outstanding Revenue, Total Invoices, Paid/Unpaid/Overdue counts, Active Clients, Average Invoice Value
- **Revenue by Month** — Monthly revenue breakdown
- **Invoice Status Breakdown** — Paid, Sent, Partial, Overdue, Draft counts
- **Top Clients by Revenue** — Your highest-value clients

All values update automatically as you add invoices and payments.

---

## Clients

The Clients tab stores your client directory. Each client record includes:

- Client ID (auto-numbered CL-001, CL-002, etc.)
- Client Name
- Company
- Email
- Phone
- Address
- Status (Active, Inactive, or Archived — select from dropdown)
- Notes

**Status tracking:** Use the Status column to mark clients as Active, Inactive, or Archived. The dropdown menu shows all available options.

---

## Invoice Register

The Invoice Register is your master log of all invoices. Each invoice includes:

- Invoice ID (auto-numbered INV-001, INV-002, etc.)
- Invoice Date and Due Date
- Client (linked to Clients tab)
- Description
- Subtotal, Tax Rate, Tax Amount (auto-calculated)
- Total (auto-calculated)
- Amount Paid (enter manually)
- Outstanding Balance (auto-calculated)
- **Status** (auto-calculated — Paid, Sent, Overdue, Partial, or Draft)

**Status logic:**
- **Paid** — Amount Paid equals Total
- **Overdue** — Past due date and not fully paid
- **Partial** — Amount Paid is between $0 and Total
- **Sent** — Not overdue, no payment received
- **Draft** — Manual override only (set via dropdown in Settings)

---

## Payment Tracker

The Payment Tracker logs all payments received. Each entry includes:

- Payment ID (auto-numbered PAY-001, PAY-002, etc.)
- Invoice ID (links to Invoice Register)
- **Client Name** (auto-populated via VLOOKUP — no manual entry needed)
- Payment Date
- Payment Method (select from dropdown: Bank Transfer, PayPal, Cash, Credit Card, Check)
- Amount
- Notes

Simply enter the Invoice ID and the client name fills in automatically.

---

## Invoice Generator

The Invoice Generator creates a professional, printable invoice. It includes:

- **Header** — INVOICE title, invoice number, date, due date
- **From Section** — Your name/company and address
- **Bill To Section** — Client name and address
- **Line Items** — Up to 10 items with Description, Quantity, Rate, and auto-calculated Amount
- **Summary** — Subtotal, Tax Rate, Tax Amount, and Total (all auto-calculated)
- **Payment Instructions** — Default payment instructions and contact info

**To create an invoice:**
1. Enter the client name
2. Add line items (description, quantity, rate)
3. The Amount, Subtotal, Tax, and Total calculate automatically
4. Print or save as PDF

---

## Settings

The Settings tab lets you customize:

- **Currency Symbol** — Set your preferred currency ($, £, €, etc.)
- **Default Tax Rate** — Set your default tax rate (e.g., 10%)
- **Invoice Status Values** — Available statuses (Paid, Sent, Overdue, Partial, Draft)
- **Payment Method Values** — Available payment methods (Bank Transfer, PayPal, Cash, Credit Card, Check)
- **Client Status Values** — Available client statuses (Active, Inactive, Archived)

**Important:** Set your currency and tax rate before entering any data.

---

## Google Sheets Import Instructions

**To use in Google Sheets (recommended):**

1. Click the Google Sheets copy link you received after purchase
2. Google Sheets will prompt: "Make a copy" — click it
3. The file opens in your Google Drive as an editable copy
4. Start using immediately — no setup required

**To use in Microsoft Excel:**

1. Open the XLSX file directly in Excel
2. Enable editing if prompted
3. The file works in Excel for desktop and Excel for web
4. Note: Some Google Sheets-specific formatting may differ in Excel

---

## FAQ

**Q: Do I need spreadsheet skills to use this?**
A: No. Fill in the highlighted input cells — everything else calculates automatically.

**Q: Does this work in Google Sheets?**
A: Yes. Make a copy to Google Drive and start using immediately. Also works in Excel.

**Q: Is this a one-time purchase?**
A: Yes. No subscription, no recurring fees. Download and use forever.

**Q: Can I customize the tax rate and currency?**
A: Yes. The Settings tab lets you set currency symbol, default tax rate, and dropdown values.

**Q: How do I add more clients?**
A: Go to the Clients tab and enter data in the next available row. The formulas will pick them up automatically.

**Q: What if I need help?**
A: Email workbysar1@gmail.com. We respond within 24 hours.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Formulas show #REF! error | You may have deleted a referenced cell or sheet. Check that all 7 tabs are present. |
| Formulas show #VALUE! error | Check that you entered numbers in cells expecting numeric values (especially Quantity, Rate, Amount). |
| Dashboard not updating | Make sure you entered invoices in the Invoice Register tab. Dashboard reads from this tab. |
| Dropdown not showing options | Check the Settings tab — dropdown values are configured there. |
| Invoice Generator total wrong | Verify the Subtotal, Tax Rate, and Amount Paid values are correct. Total = Subtotal + Tax. |
| Client Name not appearing in Payment Tracker | Check that the Invoice ID you entered exists in the Invoice Register and that the Invoice Register has a valid Client Name. |
| Google Sheets shows #REF! | When uploading XLSX to Google Sheets, some range references may break. Use the Google Sheets copy link for best results. |

---

## Support

**Email:** workbysar1@gmail.com

**Response time:** Within 24 hours

---

&copy; Nivora — Simple tools for independent professionals.
