
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from config.database import DB_CONFIG

class BillModel:
    def __init__(self):
        pass

    def open_bills_dashboard(self, parent):
        window = tk.Toplevel(parent)
        window.title("Bills Dashboard")
        window.geometry("600x400")

        search_frame = tk.Frame(window)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Search:").pack(side="left", padx=5)
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side="left", fill="x", expand=True, padx=5)

        search_button = tk.Button(search_frame, text="Search", command=lambda: self.search_bills(search_entry.get()))
        search_button.pack(side="left", padx=5)

        sort_button = tk.Button(search_frame, text="Sort", command=self.sort_bills_popup)
        sort_button.pack(side="left", padx=5)

        columns = ("bill_no", "transaction_id", "customer_name", "contact", "date", "total_price", "mode_of_payment", "staff_id")
        self.bills_table = ttk.Treeview(window, columns=columns, show="headings")
        self.bills_table.pack(fill="both", expand=True, padx=10, pady=10)

        for col in columns:
            self.bills_table.heading(col, text=col.replace("_", " ").title())

        self.bills_table.bind("<Double-1>", self.on_item_click)
        self.load_last_30_bills()

    def load_last_30_bills(self):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        query = "SELECT bill_no, transaction_id, customer_name, contact, date, total_price, mode_of_payment, staff_id FROM bill ORDER BY date DESC LIMIT 30"
        cursor.execute(query)
        bills = cursor.fetchall()

        for bill in bills:
            self.bills_table.insert("", "end", values=bill)

        cursor.close()
        connection.close()

    def on_item_click(self, event):
        selected_item = self.bills_table.selection()
        if not selected_item:
            return

        bill_no = self.bills_table.item(selected_item, "values")[0]
        self.show_bill_details(bill_no)

    def show_bill_details(self, bill_no):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        bill_query = """
        SELECT bill_no, transaction_id, customer_name, contact, date, total_price, mode_of_payment, staff_id
        FROM bill
        WHERE bill_no = ?
        """
        cursor.execute(bill_query, (bill_no,))
        bill_details = cursor.fetchone()

        product_query = """
        SELECT p.name, bp.quantity, p.price, (bp.quantity * p.price) as total
        FROM bill_products bp
        JOIN products p ON bp.product_id = p.id
        WHERE bp.bill_no = ?
        """
        cursor.execute(product_query, (bill_no,))
        products = cursor.fetchall()

        cursor.close()
        connection.close()

        popup = tk.Toplevel()
        popup.title(f"Bill Details - {bill_no}")
        popup.geometry("500x400")

        bill_info = f"""
        Bill No: {bill_details[0]}
        Transaction ID: {bill_details[1]}
        Customer Name: {bill_details[2]}
        Contact: {bill_details[3]}
        Date: {bill_details[4]}
        Total Price: {bill_details[5]}
        Mode of Payment: {bill_details[6]}
        Staff ID: {bill_details[7]}
        """
        tk.Label(popup, text=bill_info, justify="left").pack(pady=10)

        product_frame = tk.Frame(popup)
        product_frame.pack(fill="both", expand=True)

        product_columns = ("Product Name", "Quantity", "Price", "Total")
        product_table = ttk.Treeview(product_frame, columns=product_columns, show="headings")
        product_table.pack(fill="both", expand=True)

        for col in product_columns:
            product_table.heading(col, text=col)

        for product in products:
            product_table.insert("", "end", values=product)

    def search_bills(self, query):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        search_query = """
        SELECT bill_no, transaction_id, customer_name, contact, date, total_price, mode_of_payment, staff_id
        FROM bill
        WHERE bill_no LIKE ? OR transaction_id LIKE ? OR customer_name LIKE ?
        """
        cursor.execute(search_query, (f"%{query}%", f"%{query}%", f"%{query}%"))
        bills = cursor.fetchall()

        for item in self.bills_table.get_children():
            self.bills_table.delete(item)

        for bill in bills:
            self.bills_table.insert("", "end", values=bill)

        cursor.close()
        connection.close()

    def sort_bills_popup(self):
        popup = tk.Toplevel()
        popup.title("Sort Bills")
        popup.geometry("300x150")

        tk.Label(popup, text="Sort by:").pack(pady=10)

        sort_options = ["Date", "Customer Name"]
        sort_var = tk.StringVar(value=sort_options[0])

        for option in sort_options:
            tk.Radiobutton(popup, text=option, variable=sort_var, value=option).pack(anchor="w")

        sort_button = tk.Button(popup, text="Sort", command=lambda: self.sort_bills(sort_var.get()))
        sort_button.pack(pady=10)

    def sort_bills(self, criteria):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        if criteria == "Date":
            order_by = "date"
        elif criteria == "Customer Name":
            order_by = "customer_name"
        else:
            order_by = "date"

        sort_query = f"""
        SELECT bill_no, transaction_id, customer_name, contact, date, total_price, mode_of_payment, staff_id
        FROM bill
        ORDER BY {order_by} ASC
        """
        cursor.execute(sort_query)
        bills = cursor.fetchall()

        for item in self.bills_table.get_children():
            self.bills_table.delete(item)

        for bill in bills:
            self.bills_table.insert("", "end", values=bill)

        cursor.close()
        connection.close()

    def get_last_50_bills():
        pass