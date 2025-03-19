import tkinter as tk
from tkinter import ttk
import sqlite3
from config.database import DB_CONFIG

class SalaryModel:
    def __init__(self):
        pass

    def open_salary_dashboard(self, parent):
        window = tk.Toplevel(parent)
        window.title("Salary Dashboard")
        window.geometry("600x400")

        search_frame = tk.Frame(window)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Search:").pack(side="left", padx=5)
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side="left", fill="x", expand=True, padx=5)

        search_button = tk.Button(search_frame, text="Search", command=lambda: self.search_salaries(search_entry.get()))
        search_button.pack(side="left", padx=5)

        sort_button = tk.Button(search_frame, text="Sort", command=self.sort_salaries_popup)
        sort_button.pack(side="left", padx=5)

        pay_salary_button = tk.Button(search_frame, text="Pay Salary", command=self.pay_salary_popup)
        pay_salary_button.pack(side="left", padx=5)

        columns = ("transaction_id", "staff_id", "amount", "date", "mode")
        self.salaries_table = ttk.Treeview(window, columns=columns, show="headings")
        self.salaries_table.pack(fill="both", expand=True, padx=10, pady=10)

        for col in columns:
            self.salaries_table.heading(col, text=col.replace("_", " ").title())

        self.load_all_salaries()

    def load_all_salaries(self):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        query = "SELECT transaction_id, staff_id, amount, date, mode FROM salary ORDER BY date DESC"
        cursor.execute(query)
        salaries = cursor.fetchall()

        for salary in salaries:
            self.salaries_table.insert("", "end", values=salary)

        cursor.close()
        connection.close()

    def search_salaries(self, query):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        search_query = """
        SELECT transaction_id, staff_id, amount, date, mode
        FROM salary
        WHERE transaction_id LIKE ? OR staff_id LIKE ?
        """
        cursor.execute(search_query, (f"%{query}%", f"%{query}%"))
        salaries = cursor.fetchall()

        for item in self.salaries_table.get_children():
            self.salaries_table.delete(item)

        for salary in salaries:
            self.salaries_table.insert("", "end", values=salary)

        cursor.close()
        connection.close()

    def sort_salaries_popup(self):
        popup = tk.Toplevel()
        popup.title("Sort Salaries")
        popup.geometry("300x150")

        tk.Label(popup, text="Sort by:").pack(pady=10)

        sort_options = ["Date", "Staff ID"]
        sort_var = tk.StringVar(value=sort_options[0])

        for option in sort_options:
            tk.Radiobutton(popup, text=option, variable=sort_var, value=option).pack(anchor="w")

        sort_button = tk.Button(popup, text="Sort", command=lambda: self.sort_salaries(sort_var.get()))
        sort_button.pack(pady=10)

    def sort_salaries(self, criteria):
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        if criteria == "Date":
            order_by = "date"
        elif criteria == "Staff ID":
            order_by = "staff_id"
        else:
            order_by = "date"

        sort_query = f"""
        SELECT transaction_id, staff_id, amount, date, mode
        FROM salary
        ORDER BY {order_by} ASC
        """
        cursor.execute(sort_query)
        salaries = cursor.fetchall()

        for item in self.salaries_table.get_children():
            self.salaries_table.delete(item)

        for salary in salaries:
            self.salaries_table.insert("", "end", values=salary)

        cursor.close()
        connection.close()

    def pay_salary_popup(self):
        popup = tk.Toplevel()
        popup.title("Pay Salary")
        popup.geometry("300x400")

        tk.Label(popup, text="Transaction ID:").pack(pady=5)
        transaction_id_entry = tk.Entry(popup)
        transaction_id_entry.pack(pady=5)

        tk.Label(popup, text="Staff ID:").pack(pady=5)
        staff_id_entry = tk.Entry(popup)
        staff_id_entry.pack(pady=5)

        tk.Label(popup, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(popup)
        amount_entry.pack(pady=5)
        tk.Label(popup, text="Date:").pack(pady=5)
        date_entry = tk.Entry(popup)
        date_entry.pack(pady=5)

        tk.Label(popup, text="Mode:").pack(pady=5)
        mode_entry = tk.Entry(popup)
        mode_entry.pack(pady=5)

        pay_button = tk.Button(popup, text="Pay", command=lambda: self.pay_salary(
            transaction_id_entry.get(), staff_id_entry.get(), amount_entry.get(),
           date_entry.get(), mode_entry.get()))
        pay_button.pack(pady=10)

    def pay_salary(self, transaction_id, staff_id, amount, date, mode):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            pay_query = """
            INSERT INTO salary (transaction_id, staff_id, amount, date, mode)
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(pay_query, (transaction_id, staff_id, amount, date, mode))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_all_salaries()

        except sqlite3.Error as err:
            print(f"Error: {err}")
