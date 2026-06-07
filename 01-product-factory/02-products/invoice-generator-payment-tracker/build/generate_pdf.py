import os
from fpdf import FPDF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS = os.path.join(ROOT, "screenshots")
OUTPUT_DIR = os.path.join(ROOT, "delivery")

PDF_FILENAME = "nivora-invoice-generator-payment-tracker-quick-start-guide.pdf"


class GuidePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(13, 27, 42)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(13, 27, 42)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(13, 27, 42)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(51, 51, 51)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text, indent=10):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(51, 51, 51)
        x = self.get_x()
        self.cell(indent, 5.5, "")
        self.set_font("Helvetica", "", 10)
        bullet_char =         "-"
        self.cell(5, 5.5, bullet_char)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def table_row(self, cells, bold=False, fill=False):
        self.set_font("Helvetica", "B" if bold else "", 9)
        if fill:
            self.set_fill_color(240, 240, 240)
        col_widths = [30, 0]
        for i, cell_text in enumerate(cells):
            if i == 0:
                self.cell(30, 6, cell_text, border=1, fill=fill)
            else:
                self.cell(0, 6, cell_text, border=1, fill=fill, new_x="LMARGIN", new_y="NEXT")
        self.ln(0)


def build_pdf():
    pdf = GuidePDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # --- Page 1: Cover ---
    cover_path = os.path.join(SCREENSHOTS, "01-cover.png")
    if os.path.exists(cover_path):
        pdf.add_page()
        w, h = 210, 297
        pdf.image(cover_path, x=0, y=0, w=w, h=h * 0.85)
        pdf.set_font("Helvetica", "I", 10)
        pdf.set_text_color(128, 128, 128)
        pdf.set_y(h * 0.88)
        pdf.cell(0, 10, "Nivora Invoice Generator & Payment Tracker - Quick-Start Guide", align="C")

    # --- Welcome ---
    pdf.add_page()
    pdf.section_title("Welcome")
    pdf.body_text(
        "Thank you for purchasing Nivora Invoice Generator & Payment Tracker. "
        "This spreadsheet helps freelancers, consultants, and independent professionals "
        "create invoices, track payments, manage clients, and monitor revenue - all in one file.\n\n"
        "No special skills needed. Just fill in the highlighted input cells - "
        "everything else calculates automatically."
    )

    # --- Workbook Overview ---
    pdf.section_title("Workbook Overview")
    pdf.body_text("The workbook contains 7 tabs:")
    pdf.ln(2)

    tabs = [
        ("Start Here", "Setup instructions and navigation"),
        ("Dashboard", "Revenue KPIs, invoice status, monthly trends, top clients"),
        ("Clients", "Client directory with contact details and status tracking"),
        ("Invoice Register", "All invoices with auto-calculated status"),
        ("Payment Tracker", "All payments received, linked to invoices automatically"),
        ("Invoice Generator", "Printable invoice with auto-calculated totals"),
        ("Settings", "Currency, tax rate, dropdown values"),
    ]
    for tab, desc in tabs:
        pdf.table_row([tab, desc])
    pdf.ln(4)

    pdf.body_text(
        "Important: Cells with gray background contain formulas - do not edit them. "
        "Cells with white or green background are for your input."
    )

    # --- Quick Start ---
    pdf.section_title("Quick Start")
    steps = [
        "Open the file - Use the Google Sheets copy link, or open the XLSX in Excel",
        "Go to Settings first - Set your currency symbol and default tax rate",
        "Add your clients - Enter client details in the Clients tab",
        "Create invoices - Use the Invoice Generator or enter invoices in the Invoice Register",
        "Track payments - Log payments in the Payment Tracker tab",
        "View your Dashboard - All metrics update automatically",
    ]
    for step in steps:
        pdf.bullet(step)

    # --- Dashboard ---
    pdf.add_page()
    pdf.section_title("Dashboard")
    pdf.body_text(
        "The Dashboard tab shows your business at a glance with real-time KPI cards, "
        "monthly revenue breakdown, invoice status breakdown, and your top clients."
    )
    pdf.sub_title("KPI Cards")
    pdf.body_text(
        "Total Revenue, Paid Revenue, Outstanding Revenue, Total Invoices, "
        "Paid/Unpaid/Overdue counts, Active Clients, and Average Invoice Value."
    )
    pdf.sub_title("Revenue by Month")
    pdf.body_text("Monthly revenue breakdown showing trends over time.")
    pdf.sub_title("Invoice Status Breakdown")
    pdf.body_text("Paid, Sent, Partial, Overdue, and Draft counts at a glance.")
    pdf.sub_title("Top Clients by Revenue")
    pdf.body_text("Your highest-value clients ranked by revenue.")

    # Dashboard screenshot
    dash_path = os.path.join(SCREENSHOTS, "02-dashboard.png")
    if os.path.exists(dash_path):
        pdf.ln(4)
        try:
            pdf.image(dash_path, x=10, w=190)
            pdf.ln(2)
        except Exception:
            pass

    # --- Clients ---
    pdf.add_page()
    pdf.section_title("Clients")
    pdf.body_text(
        "The Clients tab stores your client directory. Each client record includes: "
        "Client ID, Name, Company, Email, Phone, Address, Status (Active/Inactive/Archived), and Notes."
    )
    pdf.sub_title("Adding Clients")
    pdf.body_text(
        "Enter client details in the next available row. All new clients are automatically "
        "picked up by formulas across the workbook. Use the Status dropdown to mark "
        "clients as Active, Inactive, or Archived."
    )

    # Clients screenshot
    clients_path = os.path.join(SCREENSHOTS, "05-advanced-features.png")
    if os.path.exists(clients_path):
        pdf.ln(4)
        try:
            pdf.image(clients_path, x=10, w=190)
            pdf.ln(2)
        except Exception:
            pass

    # --- Invoice Register ---
    pdf.add_page()
    pdf.section_title("Invoice Register")
    pdf.body_text(
        "The Invoice Register is your master log of all invoices. Each entry includes "
        "Invoice ID, Date, Due Date, Client, Description, Subtotal, Tax Rate, "
        "Tax Amount, Total, Amount Paid, Outstanding Balance, and Status."
    )
    pdf.sub_title("Auto-Calculated Status")
    pdf.body_text(
        "Status is calculated automatically:\n"
        "- Paid: Amount Paid equals Total\n"
        "- Overdue: Past due date and not fully paid\n"
        "- Partial: Amount Paid is between $0 and Total\n"
        "- Sent: Not overdue, no payment received\n"
        "- Draft: Manual override only (set via Settings)"
    )

    # --- Payment Tracker ---
    pdf.section_title("Payment Tracker")
    pdf.body_text(
        "The Payment Tracker logs all payments received. Each entry includes "
        "Payment ID, Invoice ID, Client Name (auto-populated via VLOOKUP), "
        "Payment Date, Payment Method, Amount, and Notes."
    )
    pdf.body_text(
        "Simply enter the Invoice ID and the client name fills in automatically. "
        "Payment methods are customizable in the Settings tab."
    )

    payment_path = os.path.join(SCREENSHOTS, "04-secondary-feature.png")
    if os.path.exists(payment_path):
        pdf.ln(4)
        try:
            pdf.image(payment_path, x=10, w=190)
            pdf.ln(2)
        except Exception:
            pass

    # --- Invoice Generator ---
    pdf.add_page()
    pdf.section_title("Invoice Generator")
    pdf.body_text(
        "The Invoice Generator creates a professional, printable invoice with "
        "INVOICE title, invoice number, date, due date, from/bill-to sections, "
        "line items, and auto-calculated totals."
    )
    pdf.sub_title("To Create an Invoice")
    steps = [
        "Enter the client name in the Bill To section",
        "Add line items (description, quantity, rate)",
        "Amount, Subtotal, Tax, and Total calculate automatically",
        "Print or save as PDF directly from Google Sheets or Excel",
    ]
    for step in steps:
        pdf.bullet(step)

    invoice_path = os.path.join(SCREENSHOTS, "03-primary-feature.png")
    if os.path.exists(invoice_path):
        pdf.ln(4)
        try:
            pdf.image(invoice_path, x=10, w=190)
            pdf.ln(2)
        except Exception:
            pass

    # --- Settings ---
    pdf.section_title("Settings")
    pdf.body_text(
        "The Settings tab lets you customize:\n"
        "- Currency Symbol ($, pound, euro, etc.)\n"
        "- Default Tax Rate (e.g., 10%)\n"
        "- Invoice Status Values\n"
        "- Payment Method Values (Bank Transfer, PayPal, Cash, etc.)\n"
        "- Client Status Values (Active, Inactive, Archived)"
    )
    pdf.body_text(
        "Important: Set your currency and tax rate before entering any data."
    )

    # --- Google Sheets Import ---
    pdf.add_page()
    pdf.section_title("Google Sheets Import Instructions")
    pdf.sub_title("To Use in Google Sheets (Recommended)")
    steps = [
        "Click the Google Sheets copy link you received after purchase",
        "Google Sheets will prompt: 'Make a copy' - click it",
        "The file opens in your Google Drive as an editable copy",
        "Start using immediately - no setup required",
    ]
    for step in steps:
        pdf.bullet(step)
    pdf.ln(4)

    pdf.sub_title("To Use in Microsoft Excel")
    steps = [
        "Open the XLSX file directly in Excel",
        "Enable editing if prompted",
        "Works in Excel for desktop and Excel for web",
        "Note: Some formatting may differ between Excel and Google Sheets",
    ]
    for step in steps:
        pdf.bullet(step)

    # --- FAQ ---
    pdf.add_page()
    pdf.section_title("FAQ")

    faqs = [
        ("Do I need spreadsheet skills?",
         "No. Fill in the highlighted input cells - everything else calculates automatically."),
        ("Does this work in Google Sheets?",
         "Yes. Make a copy to Google Drive and start using immediately. Also works in Excel."),
        ("Is this a one-time purchase?",
         "Yes. No subscription, no recurring fees. Download and use forever."),
        ("Can I customize tax rate and currency?",
         "Yes. The Settings tab lets you set currency symbol, default tax rate, and dropdown values."),
        ("How do I add more clients?",
         "Go to the Clients tab and enter data in the next available row. Formulas pick them up automatically."),
        ("What if I need help?",
         "Email workbysar1@gmail.com. We respond within 24 hours."),
    ]
    for q, a in faqs:
        pdf.sub_title(f"Q: {q}")
        pdf.body_text(f"A: {a}")

    # --- Troubleshooting ---
    pdf.add_page()
    pdf.section_title("Troubleshooting")

    issues = [
        ("#REF! error in formulas",
         "You may have deleted a referenced cell or sheet. Check that all 7 tabs are present."),
        ("#VALUE! error in formulas",
         "Check that you entered numbers in cells expecting numeric values (Quantity, Rate, Amount)."),
        ("Dashboard not updating",
         "Make sure you entered invoices in the Invoice Register tab."),
        ("Dropdown not showing options",
         "Check the Settings tab - dropdown values are configured there."),
        ("Invoice Generator total wrong",
         "Verify Subtotal, Tax Rate, and Amount Paid. Total = Subtotal + Tax."),
        ("Client Name not in Payment Tracker",
         "Check that the Invoice ID exists in the Invoice Register with a valid Client Name."),
        ("Google Sheets shows #REF! errors",
         "Use the Google Sheets copy link for best results."),
    ]
    for issue, solution in issues:
        pdf.sub_title(issue)
        pdf.body_text(f"Solution: {solution}")

    # --- Support ---
    pdf.section_title("Support")
    pdf.body_text(
        "Email: workbysar1@gmail.com\n"
        "Response time: Within 24 hours\n\n"
        "(c) Nivora - Simple tools for independent professionals."
    )

    # Save
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, PDF_FILENAME)
    pdf.output(output_path)
    print(f"PDF generated: {output_path}")
    print(f"Pages: {pdf.page_no()}")
    return output_path


if __name__ == "__main__":
    build_pdf()
