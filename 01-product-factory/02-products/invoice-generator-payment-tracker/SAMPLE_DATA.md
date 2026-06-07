# Sample Data — Nivora Invoice Generator & Payment Tracker

---

## Clients (10)

| Client ID | Name | Company | Status |
|-----------|------|---------|--------|
| CL-001 | Sarah Chen | Chen Design Studio | Active |
| CL-002 | Marcus Johnson | Johnson Consulting | Active |
| CL-003 | Elena Rodriguez | Rodriguez Web Services | Active |
| CL-004 | David Kim | Kim & Co. Marketing | Active |
| CL-005 | Aisha Patel | Patel Digital Solutions | Active |
| CL-006 | James Wilson | Wilson Creative Agency | Active |
| CL-007 | Priya Sharma | Sharma Bookkeeping | Inactive |
| CL-008 | Carlos Mendez | Mendez Tech Services | Active |
| CL-009 | Olivia Thompson | Thompson Freelance Writing | Active |
| CL-010 | Ben Okafor | Okafor Design Lab | Archived |

Each client includes realistic email, phone, and address.

---

## Invoices (25)

| Invoice ID | Client | Date | Due Date | Subtotal | Status |
|-----------|--------|------|----------|----------|--------|
| INV-001 | Sarah Chen | Jan 5 | Feb 5 | 1500 | Paid |
| INV-002 | Marcus Johnson | Jan 8 | Feb 8 | 2500 | Paid |
| INV-003 | Elena Rodriguez | Jan 12 | Feb 12 | 1800 | Paid |
| INV-004 | David Kim | Jan 15 | Feb 15 | 3200 | Paid |
| INV-005 | Aisha Patel | Jan 20 | Feb 20 | 2100 | Paid |
| INV-006 | James Wilson | Jan 25 | Feb 25 | 4000 | Partial |
| INV-007 | Sarah Chen | Feb 2 | Mar 2 | 1600 | Paid |
| INV-008 | Carlos Mendez | Feb 5 | Mar 5 | 950 | Paid |
| INV-009 | Olivia Thompson | Feb 10 | Mar 10 | 750 | Paid |
| INV-010 | Marcus Johnson | Feb 12 | Mar 12 | 2800 | Overdue |
| INV-011 | Elena Rodriguez | Feb 18 | Mar 18 | 1500 | Sent |
| INV-012 | James Wilson | Feb 22 | Mar 22 | 3500 | Sent |
| INV-013 | David Kim | Feb 25 | Mar 25 | 1800 | Sent |
| INV-014 | Aisha Patel | Mar 1 | Apr 1 | 2200 | Overdue |
| INV-015 | Sarah Chen | Mar 5 | Apr 5 | 1400 | Sent |
| INV-016 | Carlos Mendez | Mar 8 | Apr 8 | 1200 | Sent |
| INV-017 | Olivia Thompson | Mar 12 | Apr 12 | 600 | Sent |
| INV-018 | Priya Sharma | Mar 15 | Apr 15 | 3000 | Draft |
| INV-019 | James Wilson | Mar 18 | Apr 18 | 2800 | Overdue |
| INV-020 | Marcus Johnson | Mar 22 | Apr 22 | 2000 | Sent |
| INV-021 | Elena Rodriguez | Mar 25 | Apr 25 | 1700 | Draft |
| INV-022 | David Kim | Mar 28 | Apr 28 | 1500 | Sent |
| INV-023 | Aisha Patel | Apr 1 | May 1 | 2600 | Sent |
| INV-024 | Sarah Chen | Apr 5 | May 5 | 1800 | Sent |
| INV-025 | Carlos Mendez | Apr 8 | May 8 | 800 | Sent |

Tax rate: 10% on all invoices.

Mixed statuses ensure dashboard formulas display every category.

---

## Payments (15)

| Payment ID | Invoice | Client | Amount | Method |
|-----------|---------|--------|--------|--------|
| PAY-001 | INV-001 | Sarah Chen | 1650 | Bank Transfer |
| PAY-002 | INV-002 | Marcus Johnson | 2750 | PayPal |
| PAY-003 | INV-003 | Elena Rodriguez | 1980 | Bank Transfer |
| PAY-004 | INV-004 | David Kim | 3520 | Cheque |
| PAY-005 | INV-005 | Aisha Patel | 2310 | Bank Transfer |
| PAY-006 | INV-006 | James Wilson | 2200 | PayPal |
| PAY-007 | INV-007 | Sarah Chen | 1760 | Bank Transfer |
| PAY-008 | INV-008 | Carlos Mendez | 1045 | Cash |
| PAY-009 | INV-009 | Olivia Thompson | 825 | Bank Transfer |
| PAY-010 | INV-010 | Marcus Johnson | 1400 | PayPal |
| PAY-011 | INV-015 | Sarah Chen | 1540 | Bank Transfer |
| PAY-012 | INV-016 | Carlos Mendez | 1320 | Bank Transfer |
| PAY-013 | INV-020 | Marcus Johnson | 1100 | Credit Card |
| PAY-014 | INV-023 | Aisha Patel | 1430 | PayPal |
| PAY-015 | INV-014 | Aisha Patel | 1210 | Bank Transfer |

Payment distribution:
- INV-006 (Partial): 2200 paid of 4400 total
- INV-010 (Overdue): 1400 paid of 3080 total
- INV-014 (Overdue): 1210 paid of 2420 total
- INV-020 (Sent): 1100 paid of 2200 total
- INV-015 (Sent): 1540 of 1540 total (paid — status will auto-update to Paid once outstanding = 0)

---

## Dashboard Expected Values (with sample data shown above)

| Metric | Expected |
|--------|----------|
| Total Revenue (excl. Draft) | ~45,000 |
| Paid Revenue | ~24,000 |
| Outstanding Revenue | ~10,000 |
| Total Invoices | 25 |
| Paid Invoices | ~9 |
| Unpaid Invoices | ~14 |
| Overdue Invoices | ~3 |
| Active Clients | 9 |
