import tkinter as tk
from tkinter import ttk
from utils.helper import fetch_all_products, create_window, create_side_nav, create_entry, display_image, upload_photo
import sqlite3
import os
from config.database import DB_CONFIG
from PIL import Image, ImageTk
import shutil 

class InventoryModel:
    def __init__(self):
        self.open_windows = []

    def open_product_dashboard(self, parent):
        new_window = create_window(parent, "Product Dashboard", "1000x600", self.open_windows)
        create_side_nav(new_window, [
            ("Add", self.add_product),
            ("Remove", self.remove_product),
            ("Edit", self.edit_product),
            ("Close", self.close_all_windows)
        ])
        self.show_products(new_window)

    def show_products(self, parent):
        main_content = tk.Frame(parent, bg='white')
        main_content.pack(side='right', expand=True, fill='both')
        for widget in main_content.winfo_children():
            widget.destroy()

        products = fetch_all_products()
        if products:
            columns = ("ID", "Name", "Brand", "Price", "Quantity", "Dealer ID", "Photo")
            tree = ttk.Treeview(main_content, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center')

            for product in products:
                tree.insert("", "end", values=product)

            tree.pack(expand=True, fill='both')

            image_frame = tk.Frame(main_content, bg='white')
            image_frame.pack(side='bottom', fill='x')

            def on_select(event):
                selected_item = tree.selection()
                if selected_item:
                    item = tree.item(selected_item)
                    product = item['values']
                    photo_filename = product[6]
                    photo_path = os.path.join("assets/products", photo_filename)
                    if os.path.exists(photo_path):
                        image = Image.open(photo_path).resize((100, 100), Image.ANTIALIAS)
                        photo = ImageTk.PhotoImage(image)
                        image_label.config(image=photo)
                        image_label.image = photo

            tree.bind("<<TreeviewSelect>>", on_select)

            image_label = tk.Label(image_frame, bg='white')
            image_label.pack(pady=10)
        else:
            tk.Label(main_content, text="No products found.", font=("Arial", 12), bg='white').pack(pady=10, padx=10)

    def add_product(self):
        self._product_form("Add Product", self._save_product)

    def remove_product(self):
        self._product_search("Remove Product", self._confirm_remove_product)

    def edit_product(self):
        self._product_search("Edit Product", self._edit_product_form)

    def _product_form(self, title, save_cmd, product=None):
        popup = create_window(None, title, "400x400", self.open_windows)
        fields = ["ID", "Name", "Brand", "Price", "Quantity", "Dealer ID"]
        entries = {field: create_entry(popup, field, product[i] if product else "") for i, field in enumerate(fields)}

        photo_path = tk.StringVar(value=product[6] if product else "")
        image_label = tk.Label(popup)
        image_label.pack(pady=5)
        display_image(photo_path.get(), image_label)

        tk.Button(popup, text="Upload Photo", command=lambda: upload_photo(photo_path, image_label), font=("Arial", 12)).pack(pady=5)
        tk.Button(popup, text="Save", command=lambda: save_cmd(entries, photo_path, popup), font=("Arial", 12)).pack(pady=5)

    def _save_product(self, entries, photo_path, popup):
        product_data = {field: entry.get() for field, entry in entries.items()}
        if photo_path.get():
            photo_filename = os.path.basename(photo_path.get())
            destination = os.path.join("assets/products", photo_filename)
            shutil.copy(photo_path.get(), destination)
            product_data["Photo"] = photo_filename

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            dealer_id = product_data["Dealer ID"]
            cursor.execute("SELECT id FROM dealers WHERE id = ?", (dealer_id,))
            dealer_exists = cursor.fetchone()

            if not dealer_exists:
                tk.messagebox.showerror("Error", "Invalid Dealer ID. Please enter a valid Dealer ID.")
                return

            insert_query = """
            INSERT INTO products (id, name, brand, price, quantity, dealer_id, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
                product_data["ID"],
                product_data["Name"],
                product_data["Brand"],
                product_data["Price"],
                product_data["Quantity"],
                product_data["Dealer ID"],
                product_data["Photo"]
            ))
            connection.commit()
        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_products(popup.master)

    def _product_search(self, title, action_cmd):
        popup = create_window(None, title, "400x200", self.open_windows)
        search_frame = tk.Frame(popup)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Enter ID:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        id_entry = tk.Entry(search_frame, font=("Arial", 12))
        id_entry.grid(row=0, column=1, padx=5)

        tk.Label(search_frame, text="Enter Name:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
        name_entry = tk.Entry(search_frame, font=("Arial", 12))
        name_entry.grid(row=1, column=1, padx=5)

        def search_product():
            product_id = id_entry.get()
            product_name = name_entry.get()

            try:
                connection = sqlite3.connect(DB_CONFIG['database'])
                cursor = connection.cursor()

                search_query = """
                SELECT id, name, brand, price, quantity, dealer_id, photo FROM products
                WHERE id = ? AND name = ?
                """
                cursor.execute(search_query, (product_id, product_name))
                product = cursor.fetchone()

                for widget in popup.winfo_children():
                    if isinstance(widget, tk.Frame) and widget != search_frame:
                        widget.destroy()

                if product:
                    action_cmd(product, popup)
                else:
                    tk.Label(popup, text="No matching product found.", font=("Arial", 12)).pack(pady=10)

            except sqlite3.Error as err:
                print(f"Error: {err}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()

        search_button = tk.Button(search_frame, text="Search", command=search_product, font=("Arial", 12))
        search_button.grid(row=2, columnspan=2, pady=5)

    def _confirm_remove_product(self, product, popup):
        confirm_popup = create_window(None, "Confirm Remove", "300x150", self.open_windows)
        tk.Label(confirm_popup, text=f"Are you sure you want to remove product ID: {product[0]}?", font=("Arial", 12)).pack(pady=10)
        tk.Button(confirm_popup, text="Yes", command=lambda: self._remove_product_from_db(product[0], confirm_popup, popup), font=("Arial", 12)).pack(side='left', padx=5)
        tk.Button(confirm_popup, text="No", command=confirm_popup.destroy, font=("Arial", 12)).pack(side='right', padx=5)

    def _remove_product_from_db(self, product_id, confirm_popup, search_popup):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            delete_query = "DELETE FROM products WHERE id = ?"
            cursor.execute(delete_query, (product_id,))
            connection.commit()
            print("Product removed successfully.")

        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        confirm_popup.destroy()
        search_popup.destroy()
        self.show_products(search_popup.master)

    def _edit_product_form(self, product, popup):
        self._product_form("Edit Product", self._update_product, product)

    def _update_product(self, entries, photo_path, popup):
        updated_data = {field: entry.get() for field, entry in entries.items()}
        if photo_path.get() != updated_data["Photo"]:
            photo_filename = os.path.basename(photo_path.get())
            destination = os.path.join("assets/products", photo_filename)
            shutil.copy(photo_path.get(), destination)
            updated_data["Photo"] = photo_filename

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            update_query = """
            UPDATE products
            SET name = ?, brand = ?, price = ?, quantity = ?, dealer_id = ?, photo = ?
            WHERE id = ?
            """
            cursor.execute(update_query, (
                updated_data["Name"],
                updated_data["Brand"],
                updated_data["Price"],
                updated_data["Quantity"],
                updated_data["Dealer ID"],
                updated_data["Photo"],
                updated_data["ID"]
            ))
            connection.commit()
            print("Product updated successfully.")
        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_products(popup.master)

    def close_all_windows(self):
        for window in self.open_windows:
            window.destroy()
        self.open_windows.clear()