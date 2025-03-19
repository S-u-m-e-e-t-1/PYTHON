from tkinter import messagebox
from tkinter import ttk
from utils.helper import fetch_bills_by_staff_id
from utils.bill_pdf_generator import generate_bill_pdf  
from tkinter import Toplevel, Label, Entry, Button
from datetime import datetime
import random
import sqlite3  # Import sqlite3 for SQLite database connection
from decimal import Decimal, ROUND_DOWN
from num2words import num2words
from config.database import DB_CONFIG

class StaffController:
    def __init__(self, root, staff_id, staff_name, bills_tree, search_var):
        self.root = root
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.bills_tree = bills_tree
        self.search_var = search_var
        self.bills = []

    

    def generate_bill(self):
        # Create a new window for bill generation
        bill_window = Toplevel(self.root)
        bill_window.title("Generate Bill")

        # Prefilled fields
        Label(bill_window, text="Staff Name:").grid(row=0, column=0)
        Label(bill_window, text=self.staff_name).grid(row=0, column=1)  # Use staff_name instead of staff_id

        Label(bill_window, text="Date:").grid(row=1, column=0)
        Label(bill_window, text=datetime.now().strftime("%Y-%m-%d")).grid(row=1, column=1)

        Label(bill_window, text="Shop Name:").grid(row=2, column=0)
        Label(bill_window, text="Your Shop Name").grid(row=2, column=1)

        Label(bill_window, text="Bill No:").grid(row=3, column=0)
        Label(bill_window, text=str(random.randint(1000, 9999))).grid(row=3, column=1)

        # Customer details
        Label(bill_window, text="Customer Name:").grid(row=4, column=0)
        customer_name_entry = Entry(bill_window)
        customer_name_entry.grid(row=4, column=1)

        Label(bill_window, text="Phone:").grid(row=5, column=0)
        phone_entry = Entry(bill_window)
        phone_entry.grid(row=5, column=1)

        Label(bill_window, text="Address:").grid(row=6, column=0)
        address_entry = Entry(bill_window)
        address_entry.grid(row=6, column=1)

        # Table for items
        items_tree = ttk.Treeview(bill_window, columns=("Serial No", "Item", "Price", "Quantity", "Total"))
        items_tree.heading("#0", text="")
        items_tree.heading("Serial No", text="Serial No")
        items_tree.heading("Item", text="Item")
        items_tree.heading("Price", text="Price")
        items_tree.heading("Quantity", text="Quantity")
        items_tree.heading("Total", text="Total")
        items_tree.grid(row=7, column=0, columnspan=2)

        # Grand total
        Label(bill_window, text="Grand Total:").grid(row=8, column=0)
        grand_total_label = Label(bill_window, text="0")
        grand_total_label.grid(row=8, column=1)

        # Product details
        Label(bill_window, text="Product Name:").grid(row=10, column=0)
        product_name_entry = Entry(bill_window)
        product_name_entry.grid(row=10, column=1)

        Label(bill_window, text="Quantity:").grid(row=11, column=0)
        quantity_entry = Entry(bill_window)
        quantity_entry.grid(row=11, column=1)

        def add_product_to_list():
            product_name = product_name_entry.get()
            quantity = int(quantity_entry.get())
            product = self.fetch_product_details(product_name)

            if product:
                serial_no = len(items_tree.get_children()) + 1
                total_price = product['price'] * quantity
                items_tree.insert("", "end", values=(serial_no, product['name'], product['price'], quantity, total_price))
                self.update_grand_total(items_tree, grand_total_label)

        Button(bill_window, text="Add Product", command=add_product_to_list).grid(row=12, column=0, columnspan=2)

        # Payment options
        def show_payment_popup():
            payment_window = Toplevel(bill_window)
            payment_window.title("Payment")

            Label(payment_window, text="Transaction ID:").grid(row=0, column=0)
            transaction_id_entry = Entry(payment_window)
            transaction_id_entry.grid(row=0, column=1)

            Button(payment_window, text="Submit", command=lambda: self.create_pdf(
                customer_name_entry.get(),
                phone_entry.get(),
                address_entry.get(),
                items_tree,
                grand_total_label.cget("text"),
                transaction_id_entry.get()
            )).grid(row=1, column=0, columnspan=2)

        Button(bill_window, text="Proceed to Payment", command=show_payment_popup).grid(row=9, column=0, columnspan=2)

    def create_pdf(self, customer_name, phone, address, items_tree, grand_total, transaction_id):
        # Collect item details
        items = []
        for item in items_tree.get_children():
            items.append(items_tree.item(item)["values"])

        # Generate a random bill number
        bill_no = str(random.randint(1000, 9999))

        # Call the PDF generation function
        generate_bill_pdf(
            staff_name=self.staff_name,
            date=datetime.now().strftime("%Y-%m-%d"),
            shop_name="Your Shop Name",
            bill_no=bill_no,
            customer_name=customer_name,
            phone=phone,
            address=address,
            items=items,
            grand_total=grand_total,
            transaction_id=transaction_id
        )

        # Insert bill details into the database
        self.insert_bill_details(bill_no, customer_name, phone, grand_total, transaction_id)

        # Insert product details into the database
        self.insert_bill_products(bill_no, items)

        messagebox.showinfo("Success", "Bill generated and saved as PDF.")

    def insert_bill_details(self, bill_no, customer_name, contact, total_price, transaction_id):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])  # Connect to SQLite database
            cursor = connection.cursor()
            query = """
                INSERT INTO bill (bill_no, customer_name, contact, date, total_price, mode_of_payment, staff_id, transaction_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                bill_no,
                customer_name,
                contact,
                datetime.now().strftime("%Y-%m-%d"),
                total_price,
                "Cash",  # Assuming mode of payment is cash; adjust as needed
                self.staff_id,
                transaction_id
            ))
            connection.commit()
            cursor.close()
            connection.close()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def insert_bill_products(self, bill_no, items):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])  # Connect to SQLite database
            cursor = connection.cursor()
            query = """
                INSERT INTO bill_products (bill_no, product_id, quantity)
                VALUES (?, ?, ?)
            """
            for item in items:
                product_id = self.get_product_id(item[1])  # Assuming item[1] is the product name
                cursor.execute(query, (bill_no, product_id, item[3]))  # Assuming item[3] is the quantity
            connection.commit()
            cursor.close()
            connection.close()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def get_product_id(self, product_name):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])  # Connect to SQLite database
            cursor = connection.cursor()
            query = "SELECT id FROM products WHERE name = ?"
            cursor.execute(query, (product_name,))
            product_id = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return product_id
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return None

    def logout(self):
        self.root.destroy()

    def load_bills(self):
        self.bills = fetch_bills_by_staff_id(self.staff_id)
        self.display_bills()

    def display_bills(self):
        for bill in self.bills:
            self.bills_tree.insert("", "end", values=bill)

    def filter_bills(self, event=None):
        query = self.search_var.get().lower()
        for item in self.bills_tree.get_children():
            self.bills_tree.delete(item)
        for bill in self.bills:
            if any(query in str(value).lower() for value in bill):
                self.bills_tree.insert("", "end", values=bill)

    def fetch_product_details(self, product_name):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])  # Connect to SQLite database
            cursor = connection.cursor()
            query = "SELECT * FROM products WHERE name = ?"
            cursor.execute(query, (product_name,))
            product = cursor.fetchone()
            cursor.close()
            connection.close()
            return product
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return None

    def update_grand_total(self, items_tree, grand_total_label):
        total = Decimal(0)
        for item in items_tree.get_children():
            total += Decimal(items_tree.item(item)["values"][4])
        
        # Truncate to two decimal places
        total = total.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        
        # Convert total to words in Indian Rupees
        total_in_words = num2words(total, to='currency', lang='en_IN').replace('euro', 'Rupees').replace('cents', 'Paise')

        # Update the label with ₹ symbol and formatted words
        grand_total_label.config(text=f"₹{total} ({total_in_words})")
