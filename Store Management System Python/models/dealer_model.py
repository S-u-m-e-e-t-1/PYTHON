import tkinter as tk
from tkinter import ttk
from utils.helper import fetch_all_dealers, create_window, create_side_nav, create_entry, display_image, upload_photo
import sqlite3
import os
import shutil
from config.database import DB_CONFIG
from PIL import Image, ImageTk

class DealerModel:
    def __init__(self):
        self.open_windows = []
        self.image_cache = {}

    def open_dealer_dashboard(self, parent):
        new_window = create_window(parent, "Dealer Dashboard", "1000x600", self.open_windows)
        create_side_nav(new_window, [
            ("Add", self.add_dealer),
            ("Remove", self.remove_dealer),
            ("Edit", self.edit_dealer),
            ("Close", self.close_all_windows)
        ])
        self.show_dealers(new_window)

    def show_dealers(self, parent):
        main_content = tk.Frame(parent, bg='white')
        main_content.pack(side='right', expand=True, fill='both')
        for widget in main_content.winfo_children():
            widget.destroy()

        dealers = fetch_all_dealers()
        if dealers:
            columns = ("ID", "Name", "Address", "Phone", "Email", "Outstanding", "Photo")
            tree = ttk.Treeview(main_content, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center')

            for dealer in dealers:
                tree.insert("", "end", values=dealer)

            tree.pack(expand=True, fill='both')

            image_frame = tk.Frame(main_content, bg='white')
            image_frame.pack(side='bottom', fill='x')

            def on_select(event):
                selected_item = tree.selection()
                if selected_item:
                    item = tree.item(selected_item)
                    dealer = item['values']
                    photo_filename = dealer[6]
                    photo_path = os.path.join("assets/dealers", photo_filename)
                    if os.path.exists(photo_path):
                        image = Image.open(photo_path).resize((100, 100), Image.ANTIALIAS)
                        photo = ImageTk.PhotoImage(image)
                        image_label.config(image=photo)
                        image_label.image = photo

            tree.bind("<<TreeviewSelect>>", on_select)

            image_label = tk.Label(image_frame, bg='white')
            image_label.pack(pady=10)
        else:
            tk.Label(main_content, text="No dealers found.", font=("Arial", 12), bg='white').pack(pady=10, padx=10)

    def add_dealer(self):
        self._dealer_form("Add Dealer", self._save_dealer)

    def _dealer_form(self, title, save_cmd, dealer=None):
        popup = create_window(None, title, "400x400", self.open_windows)
        fields = ["ID", "Name", "Address", "Phone", "Email", "Outstanding"]
        entries = {field: create_entry(popup, field, dealer[i] if dealer else "") for i, field in enumerate(fields)}

        photo_path = tk.StringVar(value=dealer[6] if dealer else "")
        image_label = tk.Label(popup)
        image_label.pack(pady=5)
        display_image(photo_path.get(), image_label)

        tk.Button(popup, text="Upload Photo", command=lambda: upload_photo(photo_path, image_label), font=("Arial", 12)).pack(pady=5)
        tk.Button(popup, text="Save", command=lambda: save_cmd(entries, photo_path, popup), font=("Arial", 12)).pack(pady=5)

    def _save_dealer(self, entries, photo_path, popup):
        dealer_data = {field: entry.get() for field, entry in entries.items()}
        if photo_path.get():
            photo_filename = os.path.basename(photo_path.get())
            destination = os.path.join("assets/dealers", photo_filename)
            shutil.copy(photo_path.get(), destination)
            dealer_data["Photo"] = photo_filename

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO dealers (id, name, address, phone, email, outstanding, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
                dealer_data["ID"],
                dealer_data["Name"],
                dealer_data["Address"],
                dealer_data["Phone"],
                dealer_data["Email"],
                dealer_data["Outstanding"],
                dealer_data["Photo"]
            ))
            connection.commit()
            print("Dealer added successfully.")
        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_dealers(popup.master)

    def remove_dealer(self):
        self._dealer_search("Remove Dealer", self._confirm_remove_dealer)

    def edit_dealer(self):
        self._dealer_search("Edit Dealer", self._edit_dealer_form)

    def _dealer_search(self, title, action_cmd):
        popup = create_window(None, title, "400x200", self.open_windows)
        search_frame = tk.Frame(popup)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Enter ID:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        id_entry = tk.Entry(search_frame, font=("Arial", 12))
        id_entry.grid(row=0, column=1, padx=5)

        tk.Label(search_frame, text="Enter Name:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
        name_entry = tk.Entry(search_frame, font=("Arial", 12))
        name_entry.grid(row=1, column=1, padx=5)

        def search_dealer():
            dealer_id = id_entry.get()
            dealer_name = name_entry.get()

            try:
                connection = sqlite3.connect(DB_CONFIG['database'])
                cursor = connection.cursor()

                search_query = """
                SELECT id, name, address, phone, email, outstanding, photo FROM dealers
                WHERE id = ? AND name = ?
                """
                cursor.execute(search_query, (dealer_id, dealer_name))
                dealer = cursor.fetchone()

                for widget in popup.winfo_children():
                    if isinstance(widget, tk.Frame) and widget != search_frame:
                        widget.destroy()

                if dealer:
                    action_cmd(dealer, popup)
                else:
                    tk.Label(popup, text="No matching dealer found.", font=("Arial", 12)).pack(pady=10)

            except sqlite3.Error as err:
                print(f"Error: {err}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()

        search_button = tk.Button(search_frame, text="Search", command=search_dealer, font=("Arial", 12))
        search_button.grid(row=2, columnspan=2, pady=5)

    def _confirm_remove_dealer(self, dealer, popup):
        confirm_popup = create_window(None, "Confirm Remove", "300x150", self.open_windows)
        tk.Label(confirm_popup, text=f"Are you sure you want to remove dealer ID: {dealer[0]}?", font=("Arial", 12)).pack(pady=10)
        tk.Button(confirm_popup, text="Yes", command=lambda: self._remove_dealer_from_db(dealer[0], confirm_popup, popup), font=("Arial", 12)).pack(side='left', padx=5)
        tk.Button(confirm_popup, text="No", command=confirm_popup.destroy, font=("Arial", 12)).pack(side='right', padx=5)

    def _remove_dealer_from_db(self, dealer_id, confirm_popup, search_popup):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            delete_query = "DELETE FROM dealers WHERE id = ?"
            cursor.execute(delete_query, (dealer_id,))
            connection.commit()
            print("Dealer removed successfully.")

        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        confirm_popup.destroy()
        search_popup.destroy()
        self.show_dealers(search_popup.master)

    def _edit_dealer_form(self, dealer, popup):
        self._dealer_form("Edit Dealer", self._update_dealer, dealer)

    def _update_dealer(self, entries, photo_path, popup):
        updated_data = {field: entry.get() for field, entry in entries.items()}
        if photo_path.get() != updated_data["Photo"]:
            photo_filename = os.path.basename(photo_path.get())
            destination = os.path.join("assets/dealers", photo_filename)
            shutil.copy(photo_path.get(), destination)
            updated_data["Photo"] = photo_filename

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            update_query = """
            UPDATE dealers
            SET name = ?, address = ?, phone = ?, email = ?, outstanding = ?, photo = ?
            WHERE id = ?
            """
            cursor.execute(update_query, (
                updated_data["Name"],
                updated_data["Address"],
                updated_data["Phone"],
                updated_data["Email"],
                updated_data["Outstanding"],
                updated_data["Photo"],
                updated_data["ID"]
            ))
            connection.commit()
            print("Dealer updated successfully.")
        except sqlite3.Error as err:
            print(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_dealers(popup.master)

    def close_all_windows(self):
        for window in self.open_windows:
            window.destroy()
        self.open_windows.clear()
