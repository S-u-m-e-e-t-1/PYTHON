import tkinter as tk
from tkinter import Frame, Label, Button
from utils.chart_generator import create_bar_chart
from controllers.admin_controller import AdminController  
from PIL import Image, ImageTk  

class AdminPage:
    def __init__(self, parent, profile_image_path=None, admin_details=None):
        self.root = tk.Toplevel(parent)
        self.root.title("Admin Dashboard")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f8ff")
        self.controller = AdminController(self.root)
        self.nav_visible = True

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)

        self.side_nav = Frame(self.root, bg="#4682b4", width=250)
        self.side_nav.grid(row=0, column=0, sticky="ns")
        self.side_nav.grid_propagate(False)

        nav_title = Label(self.side_nav, text="Admin Panel", font=("Arial", 18), bg="#4682b4", fg="white")
        nav_title.pack(pady=20)

        if profile_image_path:
            try:
                image = Image.open(f"assets/profile/{profile_image_path}")
                image = image.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                image_label = Label(self.side_nav, image=photo, bg="#4682b4")
                image_label.image = photo
                image_label.pack(pady=10)
            except Exception as e:
                print(f"Error loading image: {e}")

        if admin_details:
            for key, value in admin_details.items():
                Label(
                    self.side_nav,
                    text=f"{key}: {value}",
                    font=("Arial", 12),
                    bg="#4682b4",
                    fg="white",
                    anchor="w",
                ).pack(fill="x", padx=20, pady=5)

        nav_buttons = [
            ("Product Dashboard", self.controller.product_dashboard),
            ("Dealer Dashboard", self.controller.dealer_dashboard),
            ("Staff Dashboard", self.controller.staff_dashboard),
            ("Salary", self.controller.view_salary),
            ("Bills", self.controller.view_bills),
           
            ("Logout", self.controller.logout)
        ]
        for button_text, command in nav_buttons:
            Button(
                self.side_nav,
                text=button_text,
                font=("Arial", 14),
                bg="white",
                fg="#4682b4",
                height=2,
                relief="groove",
                command=command,
            ).pack(fill="x", pady=10, padx=10)

        self.toggle_btn = Button(
            self.root,
            text="✖",
            font=("Arial", 16),
            bg="#4682b4",
            fg="white",
            command=self.toggle_nav,
            bd=0,
        )
        self.toggle_btn.place(x=10, y=10)

        content_frame = Frame(self.root, bg="#f0f8ff")
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        header_frame = Frame(content_frame, bg="white", relief="ridge", borderwidth=2)
        header_frame.pack(side="top", fill="x", pady=10)

        shop_name = Label(header_frame, text="Amazing Shop", font=("Arial", 24, "bold"), bg="white", fg="#4682b4")
        shop_name.pack(pady=5)

        shop_motto = Label(
            header_frame,
            text="Your satisfaction, our priority!",
            font=("Arial", 14, "italic"),
            bg="white",
            fg="#6c757d",
        )
        shop_motto.pack()

        charts_container = Frame(content_frame, bg="#f0f8ff")
        charts_container.pack(fill="both", expand=True, pady=10)

        charts_container.rowconfigure([0, 1], weight=1, minsize=200)
        charts_container.columnconfigure([0, 1], weight=1, minsize=300)

        chart_titles = ["Sales Overview", "Profit Analysis", "Customer Growth", "Market Trends"]
        chart_data = [[10, 25, 30, 15], [5, 15, 20, 10], [50, 60, 70, 80], [100, 80, 60, 40]]
        categories = ["Q1", "Q2", "Q3", "Q4"]

        for i in range(2):
            for j in range(2):
                chart_frame = Frame(charts_container, bg="white", relief="ridge", borderwidth=2)
                chart_frame.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                create_bar_chart(chart_frame, chart_titles[i * 2 + j], chart_data[i * 2 + j], categories)

    def toggle_nav(self):
        if self.nav_visible:
            self.side_nav.grid_remove()
            self.toggle_btn.config(text="☰")
        else:
            self.side_nav.grid()
            self.toggle_btn.config(text="✖")
        self.nav_visible = not self.nav_visible
