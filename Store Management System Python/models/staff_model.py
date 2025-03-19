import tkinter as tk
from tkinter import ttk, messagebox
from utils.helper import fetch_all_staff, create_window, create_side_nav, create_entry, display_image, upload_photo
import sqlite3
import os
import shutil
from config.database import DB_CONFIG
from models.staff_generate_report import generate_staff_report
from PIL import Image, ImageTk

class StaffModel:
    def __init__(self):
        self.open_windows = []

    def open_staff_dashboard(self, parent):
        new_window = create_window(parent, "Staff Dashboard", "1000x600", self.open_windows)
        create_side_nav(new_window, [
            ("Add", self.add_staff),
            ("Remove", self.remove_staff),
            ("Edit", self.edit_staff),
            ("Close", self.close_all_windows)
        ])
        self.show_staff(new_window)

    def show_staff(self, parent):
        main_content = tk.Frame(parent, bg='white')
        main_content.pack(side='right', expand=True, fill='both')
        for widget in main_content.winfo_children():
            widget.destroy()

        staff = fetch_all_staff()
        if staff:
            columns = ("ID", "Username", "Password", "Photo", "Phone", "Email")
            tree = ttk.Treeview(main_content, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center')

            for member in staff:
                tree.insert("", "end", values=member)

            tree.pack(expand=True, fill='both')

            image_frame = tk.Frame(main_content, bg='white')
            image_frame.pack(side='bottom', fill='x')

            self.image_label = tk.Label(image_frame, bg='white')
            self.image_label.pack(pady=10)

            def on_select(event):
                selected_item = tree.selection()
                if selected_item:
                    item = tree.item(selected_item)
                    staff_member = item['values']
                    photo_filename = staff_member[3]
                    photo_path = os.path.join("assets/staff", photo_filename)
                    if os.path.exists(photo_path):
                        image = Image.open(photo_path).resize((100, 100), Image.ANTIALIAS)
                        photo = ImageTk.PhotoImage(image)
                        self.image_label.config(image=photo)
                        self.image_label.image = photo

            tree.bind("<<TreeviewSelect>>", on_select)

            # Add a "Generate Report" button
            def generate_report():
                selected_item = tree.selection()
                if selected_item:
                    item = tree.item(selected_item)
                    staff_id = item['values'][0]  # Assuming ID is the first column
                    generate_staff_report(parent, staff_id)
                else:
                    messagebox.showwarning("Selection Error", "Please select a staff member to generate a report.")

            report_button = tk.Button(main_content, text="Generate Report", command=generate_report)
            report_button.pack(pady=10)

        else:
            tk.Label(main_content, text="No staff found.", font=("Arial", 12), bg='white').pack(pady=10, padx=10)
    def add_staff(self):
        self._staff_form("Add Staff", self._save_staff)

    def _staff_form(self, title, save_cmd, staff=None):
        popup = create_window(None, title, "400x400", self.open_windows)
        fields = ["ID", "Username", "Password", "Phone", "Email"]
        entries = {
            field: create_entry(popup, field, staff[i] if staff and i < len(staff) else "")
            for i, field in enumerate(fields)
        }
# entries = {field: create_entry(popup, field, staff[i] if staff else "") for i, field in enumerate(fields)}
        print(staff)
        photo = tk.StringVar(value=staff[5] if staff and len(staff) > 5 else "")
        photo_path = os.path.join("assets/staff", photo.get()) if photo.get() else ""
        image_label = tk.Label(popup)
        image_label.pack(pady=5)
        display_image(photo_path, image_label)

        tk.Button(popup, text="Upload Photo", command=lambda: upload_photo(photo_path, image_label), font=("Arial", 12)).pack(pady=5)
        tk.Button(popup, text="Save", command=lambda: save_cmd(entries, photo_path, popup), font=("Arial", 12)).pack(pady=5)

    def _save_staff(self, entries, photo_path, popup):
        staff_data = {field: entry.get() for field, entry in entries.items()}
        if photo_path.get():
            photo_filename = os.path.basename(photo_path.get())
            destination = os.path.join("assets/staff", photo_filename)
            shutil.copy(photo_path.get(), destination)
            staff_data["Photo"] = photo_filename

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO staff (id, username,password, photo, phone, email)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
                staff_data["ID"],
                staff_data["Username"],
                staff_data["Password"],
                staff_data["Photo"],
                staff_data["Phone"],
                staff_data["Email"]
            ))
            connection.commit()
            messagebox.showerror("Success!","Staff added Successfully")
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_staff(popup.master)

    def remove_staff(self):
        self._staff_search("Remove Staff", self._confirm_remove_staff)

    def edit_staff(self):
        self._staff_search("Edit Staff", self._edit_staff_form)

    def _staff_search(self, title, action_cmd):
        popup = create_window(None, title, "400x200", self.open_windows)
        search_frame = tk.Frame(popup)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Enter ID:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        id_entry = tk.Entry(search_frame, font=("Arial", 12))
        id_entry.grid(row=0, column=1, padx=5)

        tk.Label(search_frame, text="Enter Name:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
        name_entry = tk.Entry(search_frame, font=("Arial", 12))
        name_entry.grid(row=1, column=1, padx=5)

        def search_staff():
            staff_id = id_entry.get()
            staff_name = name_entry.get()

            try:
                connection = sqlite3.connect(DB_CONFIG['database'])
                cursor = connection.cursor()

                search_query = """
                SELECT id, username,password,  phone, email ,photo FROM staff
                WHERE id = ? AND username = ?
                """
                cursor.execute(search_query, (staff_id, staff_name))
                staff = cursor.fetchone()

                for widget in popup.winfo_children():
                    if isinstance(widget, tk.Frame) and widget != search_frame:
                        widget.destroy()

                if staff:
                    action_cmd(staff, popup)
                else:
                    tk.Label(popup, text="No matching staff found.", font=("Arial", 12)).pack(pady=10)

            except sqlite3.Error as err:
                messagebox.showerror("Database Error", f"An error occurred: {err}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()

        search_button = tk.Button(search_frame, text="Search", command=search_staff, font=("Arial", 12))
        search_button.grid(row=2, columnspan=2, pady=5)

    def _confirm_remove_staff(self, staff, popup):
        confirm_popup = create_window(None, "Confirm Remove", "300x150", self.open_windows)
        tk.Label(confirm_popup, text=f"Are you sure you want to remove staff ID: {staff[0]}?", font=("Arial", 12)).pack(pady=10)
        tk.Button(confirm_popup, text="Yes", command=lambda: self._remove_staff_from_db(staff[0], confirm_popup, popup), font=("Arial", 12)).pack(side='left', padx=5)
        tk.Button(confirm_popup, text="No", command=confirm_popup.destroy, font=("Arial", 12)).pack(side='right', padx=5)

    def _remove_staff_from_db(self, staff_id, confirm_popup, search_popup):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            # Fetch the photo filename before deleting the staff record
            select_query = "SELECT photo FROM staff WHERE id = ?"
            cursor.execute(select_query, (staff_id,))
            photo_filename = cursor.fetchone()[0]

            # Delete the staff record
            delete_query = "DELETE FROM staff WHERE id = ?"
            cursor.execute(delete_query, (staff_id,))
            connection.commit()
            messagebox.showinfo("Success", "Staff removed successfully.")


            # Delete the photo file if it exists
            if photo_filename:
                photo_path = os.path.join("assets/staff", photo_filename)
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                    messagebox.showinfo("Success", "Staff deatails removed successfully.")


        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        confirm_popup.destroy()
        search_popup.destroy()
        self.show_staff(search_popup.master)

    def _edit_staff_form(self, staff, popup):
        self._staff_form("Edit Staff", self._update_staff, staff)

    def _update_staff(self, entries, popup):
        updated_data = {field: entry.get() for field, entry in entries.items()}

        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()

            update_query = """
            UPDATE staff
            SET username = ?, email = ?, phone = ?
            WHERE id = ?
            """
            cursor.execute(update_query, (
                updated_data["Name"],
                updated_data["Email"],
                updated_data["Phone"],
                updated_data["ID"]
            ))
            connection.commit()
            messagebox.showinfo("Success", "Staff updated successfully.")
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

        popup.destroy()
        self.show_staff(popup.master)

    def close_all_windows(self):
        for window in self.open_windows:
            window.destroy()
        self.open_windows.clear()
   