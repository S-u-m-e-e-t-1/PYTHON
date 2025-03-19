import tkinter as tk
from tkinter import Frame, Label, Button, Toplevel, messagebox, ttk
from PIL import Image, ImageTk
from controllers.staff_controller import StaffController

class StaffPage:
    def __init__(self, parent, profile_image_path=None,staff_name=None, staff_id=None, staff_details=None):
        self.root = Toplevel(parent)
        self.root.title("Staff Panel")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f8f9fa")

        self.search_var = tk.StringVar()

        self.content_frame = Frame(self.root, bg="#f8f9fa")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.bills_tree = ttk.Treeview(self.content_frame, columns=("Bill No", "Customer Name", "Contact", "Date", "Total Price", "Payment Mode", "Transaction ID"), show='headings')
        
        self.controller = StaffController(self.root, staff_id,staff_name, self.bills_tree, self.search_var)
        self.nav_visible = True
        self.staff_details = staff_details
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)

        self.side_nav = Frame(self.root, bg="#6c757d", width=250)
        self.side_nav.grid(row=0, column=0, sticky="ns")
        self.side_nav.grid_propagate(False)

        Label(
            self.side_nav,
            text="Staff Panel",
            font=("Arial", 18, "bold"),
            bg="#6c757d",
            fg="white",
        ).pack(pady=30)

        if self.staff_details:
            if profile_image_path:
                try:
                    image_path = f"assets/staff/{profile_image_path}"
                    image = Image.open(image_path)
                    image = image.resize((100, 100), Image.ANTIALIAS)
                    photo = ImageTk.PhotoImage(image)
                    image_label = Label(self.side_nav, image=photo, bg="#6c757d")
                    image_label.image = photo
                    image_label.pack(pady=10)
                except Exception as e:
                    print(f"Error loading image: {e}")

            details = [
                f"Username: {self.staff_details.get('Username', 'Unknown')}",
                f"Phone: {self.staff_details.get('Phone', 'N/A')}",
                f"Email: {self.staff_details.get('Email', 'N/A')}",
                f"ID: {self.staff_details.get('id', 'N/A')}"
            ]

            for detail in details:
                Label(
                    self.side_nav,
                    text=detail,
                    font=("Arial", 12),
                    bg="#6c757d",
                    fg="white",
                    anchor="w",
                ).pack(fill="x", padx=20, pady=5)

        # Define button configurations
        nav_buttons = [
            
            ("Generate Bill", self.controller.generate_bill, "#28a745", "white"),
            ("Logout", self.controller.logout, "#dc3545", "white")
        ]

        # Create buttons using a loop
        for text, command, bg, fg in nav_buttons:
            Button(
                self.side_nav,
                text=text,
                command=command,
                font=("Arial", 12),
                bg=bg,
                fg=fg
            ).pack(fill="x", padx=20, pady=10)

        self.toggle_btn = Button(self.root, text="✖", command=self.toggle_nav, font=("Arial", 12), bg="#6c757d", fg="white")
        self.toggle_btn.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

        # Create a frame for the search bar and button
        search_frame = Frame(self.content_frame, bg="#f8f9fa")
        search_frame.pack(pady=10, padx=10, fill='x')

        search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 12))
        search_entry.pack(side='left', fill='x', expand=True)

        search_button = Button(search_frame, text="Search", command=self.controller.filter_bills, font=("Arial", 12), bg="#007bff", fg="white")
        search_button.pack(side='left', padx=5)

        self.bills_tree.pack(expand=True, fill='both', padx=10, pady=10)

        self.controller.load_bills()

    def toggle_nav(self):
        if self.nav_visible:
            self.side_nav.grid_remove()
            self.toggle_btn.config(text="☰")
        else:
            self.side_nav.grid()
            self.toggle_btn.config(text="✖")
        self.nav_visible = not self.nav_visible

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Application")
    root.geometry("1200x800")

    def open_staff_page():
        StaffPage(root)

    btn = Button(root, text="Open Staff Page", command=open_staff_page, font=("Arial", 16), bg="#6c757d", fg="white")
    btn.pack(pady=20)

    root.mainloop()
