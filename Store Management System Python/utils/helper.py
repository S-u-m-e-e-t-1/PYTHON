from tkinter import messagebox

import sqlite3
from config.database import DB_CONFIG
from datetime import date
import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageDraw

def verify_credentials(username, password, role):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()

        if role == 'Admin':
            table = 'admin'
        elif role == 'Staff':
            table = 'staff'
        else:
            return False, None, None

        query = f"SELECT id, username, password, photo, phone, email FROM {table} WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            photo_path = result[3]
            user_details = {
                "id": result[0],
                "Username": result[1],
                "Password": result[2],
                "Phone": result[4],
                "Email": result[5],
            }
            return True, photo_path, user_details
        else:
            return False, None, None
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return False, None, None
    finally:
        cursor.close()
        connection.close()

def fetch_all_products():
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        
        return products
    except sqlite3.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def fetch_all_staff():
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        
        query = "SELECT * FROM staff"
        cursor.execute(query)
        staff = cursor.fetchall()
        
        return staff
    except sqlite3.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def fetch_all_dealers():
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        query = "SELECT id, name, address, phone, email, outstanding, photo FROM dealers"
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def create_window(parent, title, geometry, open_windows):
    window = tk.Toplevel(parent)
    window.title(title)
    window.geometry(geometry)
    open_windows.append(window)
    return window

def create_side_nav(parent, commands):
    side_nav = tk.Frame(parent, width=150, bg='lightgrey')
    side_nav.pack(side='left', fill='y')
    for text, cmd in commands:
        tk.Button(side_nav, text=text, command=cmd, font=("Arial", 12)).pack(pady=5, fill='x')

def create_entry(parent, field, value):
    row = tk.Frame(parent)
    tk.Label(row, text=field, width=15, anchor='w', font=("Arial", 12)).pack(side='left')
    entry = tk.Entry(row, font=("Arial", 12))
    entry.insert(0, value)
    entry.pack(side='right', expand=True, fill='x')
    row.pack(side='top', fill='x', padx=5, pady=5)
    return entry

def display_image(file_path, image_label):
    if file_path:
        image = Image.open(file_path).resize((100, 100), Image.ANTIALIAS)
        mask = Image.new('L', (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)
        rounded_image = ImageOps.fit(image, (100, 100), centering=(0.5, 0.5))
        rounded_image.putalpha(mask)
        photo = ImageTk.PhotoImage(rounded_image)
        image_label.config(image=photo)
        image_label.image = photo

def upload_photo(photo_path, image_label):
    file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        photo_path.set(file_path)
        display_image(file_path, image_label)

def fetch_bills_by_staff_id(staff_id):
    try:
        connection = sqlite3.connect(DB_CONFIG['database'])
        cursor = connection.cursor()
        
        query = """
            SELECT bill_no, customer_name, contact, date, total_price, mode_of_payment, transaction_id 
            FROM bill 
            WHERE staff_id = ? LIMIT 50
        """
        cursor.execute(query, (staff_id,))
        bills = cursor.fetchall()
        
        return bills
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()