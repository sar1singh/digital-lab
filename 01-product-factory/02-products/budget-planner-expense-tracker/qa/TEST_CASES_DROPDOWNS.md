# Test Cases — Dropdowns / Data Validation — Budget Planner & Expense Tracker

## Expense Tracker

### TC-DD-01: Category Dropdown Exists

| Field | Value |
|-------|-------|
| Test ID | TC-DD-01 |
| Priority | P0 |
| Area | Expense Tracker |
| Steps | 1. Go to Expense Tracker tab. 2. Click an empty cell in the Category column (column C). 3. Look for a dropdown arrow. |
| Expected result | Dropdown arrow appears when cell is selected. Clicking it shows a list of valid categories. |

### TC-DD-02: Category Dropdown Contains Expected Values

| Field | Value |
|-------|-------|
| Test ID | TC-DD-02 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. Open the Category dropdown. 2. Read all values in the list. |
| Expected result | Dropdown includes: Housing, Utilities, Groceries, Transport, Insurance, Health, Entertainment, Dining, Subscriptions, Shopping, Education, Debt Payments, Savings, Other. |

### TC-DD-03: Payment Method Dropdown Exists

| Field | Value |
|-------|-------|
| Test ID | TC-DD-03 |
| Priority | P0 |
| Area | Expense Tracker |
| Steps | 1. Click an empty cell in the Payment Method column (column E). 2. Look for a dropdown arrow. |
| Expected result | Dropdown arrow appears with valid payment method options. |

### TC-DD-04: Payment Method Dropdown Contains Expected Values

| Field | Value |
|-------|-------|
| Test ID | TC-DD-04 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. Open the Payment Method dropdown. 2. Read all values. |
| Expected result | Dropdown includes: Cash, Credit Card, Debit Card, Bank Transfer, PayPal, Other. |

### TC-DD-05: Planned/Unplanned Dropdown Exists

| Field | Value |
|-------|-------|
| Test ID | TC-DD-05 |
| Priority | P0 |
| Area | Expense Tracker |
| Steps | 1. Click an empty cell in the Planned/Unplanned column (column F). 2. Look for a dropdown arrow. |
| Expected result | Dropdown arrow appears with Planned and Unplanned options. |

### TC-DD-06: Valid Values Accepted

| Field | Value |
|-------|-------|
| Test ID | TC-DD-06 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. Select "Housing" from the Category dropdown. 2. Select "Credit Card" from Payment Method. 3. Select "Planned" from Planned/Unplanned. |
| Expected result | All three values accepted without error. |

### TC-DD-07: Invalid Values Rejected (If Validation Set to Reject)

| Field | Value |
|-------|-------|
| Test ID | TC-DD-07 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. In Category column, type "InvalidCategory999" manually. 2. Press Enter. 3. Note the response. |
| Expected result | Excel/Google Sheets either rejects the value with an error message or allows it depending on validation settings. Document actual behavior. |

---

## Bills Tracker

### TC-DD-08: Frequency Dropdown Exists

| Field | Value |
|-------|-------|
| Test ID | TC-DD-08 |
| Priority | P1 |
| Area | Bills Tracker |
| Steps | 1. Go to Bills Tracker tab. 2. Click an empty cell in the Frequency column (column D). 3. Look for a dropdown arrow. |
| Expected result | Dropdown arrow appears with valid frequency options. |

### TC-DD-09: Frequency Dropdown Contains Expected Values

| Field | Value |
|-------|-------|
| Test ID | TC-DD-09 |
| Priority | P1 |
| Area | Bills Tracker |
| Steps | 1. Open the Frequency dropdown. 2. Read all values. |
| Expected result | Dropdown includes: Monthly, Quarterly, Yearly, One-Time. |

### TC-DD-10: Paid Status Dropdown Exists

| Field | Value |
|-------|-------|
| Test ID | TC-DD-10 |
| Priority | P0 |
| Area | Bills Tracker |
| Steps | 1. Click an empty cell in the Paid Status column (column E). 2. Look for a dropdown arrow. |
| Expected result | Dropdown arrow appears. |

### TC-DD-11: Paid Status Dropdown Contains Expected Values

| Field | Value |
|-------|-------|
| Test ID | TC-DD-11 |
| Priority | P1 |
| Area | Bills Tracker |
| Steps | 1. Open the Paid Status dropdown. 2. Read all values. |
| Expected result | Dropdown includes: Paid, Unpaid, Upcoming. |

### TC-DD-12: Paid/Unpaid Values Work With Conditional Formatting

| Field | Value |
|-------|-------|
| Test ID | TC-DD-12 |
| Priority | P0 |
| Area | Bills Tracker |
| Steps | 1. Set a bill's Paid Status to "Unpaid" (if it wasn't already). 2. Observe the row background. 3. Change it to "Paid". 4. Observe again. |
| Expected result | Unpaid rows have a red/pink background fill. Paid rows return to normal (no fill or white). |
