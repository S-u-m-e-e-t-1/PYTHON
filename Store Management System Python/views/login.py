import tkinter as tk
from tkinter import messagebox
from admin_panel import AdminPage
from staff_panel import StaffPage
import sqlite3
from config.database import DB_CONFIG
from utils.helper import verify_credentials

class LoginDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Login")
        self.center_window(300, 380)
        self.dialog.grab_set()
        self.parent = parent

        self.dialog.configure(bg="#f3f4f6")

        tk.Label(self.dialog, text="Login", font=("Helvetica", 20, "bold"), bg="#f3f4f6", fg="#333333").pack(pady=20)

        self.role_var = tk.StringVar(value="Admin")
        role_label = tk.Label(self.dialog, text="Select Role:", font=("Helvetica", 12), bg="#f3f4f6", fg="#555555")
        role_label.pack(pady=(0, 10))
        role_menu = tk.OptionMenu(self.dialog, self.role_var, "Admin", "Staff")
        role_menu.config(font=("Helvetica", 12), width=20, relief="flat", bg="#ffffff", fg="#4682b4")
        role_menu.pack(pady=10)

        username_label = tk.Label(self.dialog, text="Username:", font=("Helvetica", 12), bg="#f3f4f6", fg="#555555")
        username_label.pack(pady=(0, 5))
        self.username_entry = tk.Entry(self.dialog, font=("Helvetica", 12), bg="#ffffff", fg="#333333")
        self.username_entry.pack(pady=(0, 10))

        password_label = tk.Label(self.dialog, text="Password:", font=("Helvetica", 12), bg="#f3f4f6", fg="#555555")
        password_label.pack(pady=(0, 5))
        self.password_entry = tk.Entry(self.dialog, show="*", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
        self.password_entry.pack(pady=(0, 10))

        submit_button = tk.Button(self.dialog, text="Submit", command=self.handle_login,
                                  bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"),
                                  activebackground="#45a049", relief="raised", bd=2, width=15)
        submit_button.pack(pady=20)

        footer_label = tk.Label(self.dialog, text="Powered by Your Company", font=("Helvetica", 8), bg="#f3f4f6", fg="#888888")
        footer_label.pack(side="bottom", pady=10)

    def handle_login(self):
        role = self.role_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        success, photo_path, user_details = verify_credentials(username, password, role)
        if success:
            self.open_dashboard(role, photo_path, user_details)
            if role == "Staff":
                self.mark_attendance(user_details)
        else:
            messagebox.showerror("Error", "Invalid login")

    def mark_attendance(self, user_details):
        staff_id = user_details.get('id')
        if staff_id:
            query = "INSERT INTO attendance (staff_id, date) VALUES (?, datetime('now'))"
            params = (staff_id,)
            try:
                self.execute_sql(query, params)
                messagebox.showinfo("Success", "Attendance marked successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error marking attendance: {e}")
        else:
            messagebox.showerror("Error", "Staff ID not found, cannot mark attendance.")

    def execute_sql(self, query, params):
        try:
            connection = sqlite3.connect(DB_CONFIG['database'])
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            connection.close()
            # messagebox.showinfo("Success", "Query executed successfully.")
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def open_dashboard(self, role, photo_path, user_details):
        self.dialog.destroy()
        if role == "Admin":
            AdminPage(self.parent, profile_image_path=photo_path, admin_details=user_details)
        elif role == "Staff":
            staff_id = user_details.get('id')
            staff_name = user_details.get('Username')
            if staff_id is not None:
                StaffPage(self.parent, profile_image_path=photo_path, staff_name=staff_name, staff_id=staff_id, staff_details=user_details)
            else:
                messagebox.showerror("Error", "Staff ID not found.")

    def center_window(self, width, height):
        x = (self.dialog.winfo_screenwidth() - width) // 2
        y = (self.dialog.winfo_screenheight() - height) // 2
        self.dialog.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    LoginDialog(root)

    root.mainloop()
