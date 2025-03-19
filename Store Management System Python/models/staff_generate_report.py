from tkinter import Toplevel, Text, Scrollbar, Button, messagebox
import sqlite3
from config.database import DB_CONFIG
import os
from fpdf import FPDF

def generate_staff_report(root, staff_id):
    # Create a new window for the report
    report_window = Toplevel(root)
    report_window.title("Staff Report")

    # Create a text widget with a scrollbar
    text_area = Text(report_window, wrap='none')  # Disable word wrap for table-like format
    scrollbar = Scrollbar(report_window, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)

    # Set tab stops for table-like alignment
    text_area.tag_configure('center', justify='center')
    text_area.tag_configure('right', justify='right')
    text_area.insert('end', "Staff Report\n", 'center')
    text_area.insert('end', "\n")

    # Pack the widgets
    text_area.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    # Fetch and display staff details
    staff_details = fetch_staff_details(staff_id)
    text_area.insert('end', "Staff Details:\n", 'center')
    for key, value in staff_details.items():
        text_area.insert('end', f"{key}\t{value}\n")

    # Fetch and display bill details
    bill_details = fetch_bill_details(staff_id)
    text_area.insert('end', "\nBill Details:\n", 'center')
    for bill in bill_details:
        for key, value in bill.items():
            text_area.insert('end', f"{key}\t{value}\n")

    # Fetch and display attendance details
    attendance_details = fetch_attendance_details(staff_id)
    text_area.insert('end', "\nAttendance Details:\n", 'center')
    for attendance in attendance_details:
        for key, value in attendance.items():
            text_area.insert('end', f"{key}\t{value}\n")

    # Fetch and display salary details
    salary_details = fetch_salary_details(staff_id)
    text_area.insert('end', "\nSalary Details:\n", 'center')
    for salary in salary_details:
        for key, value in salary.items():
            text_area.insert('end', f"{key}\t{value}\n")

    # Add a Print button
    print_button = Button(report_window, text="Print", command=lambda: print_report(text_area.get("1.0", "end"),staff_id))
    print_button.pack(side='bottom')

def print_report(report_content, staff_id):
    try:
        # Create a PDF document
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Define column widths
        column_widths = [40, 40, 40, 40]  # Adjust as needed for your data

        # Add content to the PDF in a table-like format
        for line in report_content.split('\n'):
            columns = line.split('\t')  # Assuming tab-separated values
            for i, column in enumerate(columns):
                pdf.cell(column_widths[i], 10, txt=column, border=1, ln=0, align='C')
            pdf.ln(10)  # Move to the next line

        # Save the PDF to a file
        pdf_file_path = f"assets/staff_reports/temp_report_{staff_id}.pdf"
        pdf.output(pdf_file_path)

        # Use the system's print command to print the PDF
        os.startfile(pdf_file_path, "print")
    except Exception as e:
        messagebox.showerror("Print Error", f"Error: {e}")

def fetch_staff_details(staff_id):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        query = "SELECT * FROM staff WHERE id = ?"
        cursor.execute(query, (staff_id,))
        staff = cursor.fetchone()
        cursor.close()
        connection.close()
        return staff
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

def fetch_bill_details(staff_id):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        query = "SELECT * FROM bill WHERE staff_id = ?"
        cursor.execute(query, (staff_id,))
        bills = cursor.fetchall()
        cursor.close()
        connection.close()
        return bills
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

def fetch_attendance_details(staff_id):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        query = "SELECT * FROM attendance WHERE staff_id = ?"
        cursor.execute(query, (staff_id,))
        attendance = cursor.fetchall()
        cursor.close()
        connection.close()
        return attendance
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

def fetch_salary_details(staff_id):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        query = "SELECT * FROM salary WHERE staff_id = ?"
        cursor.execute(query, (staff_id,))
        salary = cursor.fetchall()
        cursor.close()
        connection.close()
        return salary
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None
