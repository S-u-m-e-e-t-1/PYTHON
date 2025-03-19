from fpdf import FPDF
import os

def generate_bill_pdf(staff_name, date, shop_name, bill_no, customer_name, phone, address, items, grand_total, transaction_id):
    pdf = FPDF()
    pdf.add_page()

    # Add a Unicode font
    font_path = os.path.join('assets', 'font', 'DejaVuSans.ttf')
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', '', 12)

    # Add title and basic info
    pdf.cell(200, 10, txt=f"Bill No: {bill_no}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Shop Name: {shop_name}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Staff Name: {staff_name}", ln=True, align='C')

    # Customer details
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True, align='L')

    # Table header
    pdf.cell(40, 10, txt="Serial No", border=1)
    pdf.cell(40, 10, txt="Item", border=1)
    pdf.cell(40, 10, txt="Price", border=1)
    pdf.cell(40, 10, txt="Quantity", border=1)
    pdf.cell(40, 10, txt="Total", border=1)
    pdf.ln()

    # Table content
    for item in items:
        pdf.cell(40, 10, txt=str(item[0]), border=1)
        pdf.cell(40, 10, txt=str(item[1]), border=1)
        pdf.cell(40, 10, txt=str(item[2]), border=1)
        pdf.cell(40, 10, txt=str(item[3]), border=1)
        pdf.cell(40, 10, txt=str(item[4]), border=1)
        pdf.ln()

    # Grand total
    pdf.cell(200, 10, txt=f"Grand Total: ₹{grand_total}", ln=True, align='R')
    pdf.cell(200, 10, txt=f"Transaction ID: {transaction_id}", ln=True, align='R')

    # Save the PDF in the assets/bills directory
    pdf.output(f"assets/bills/bill_{bill_no}.pdf")
