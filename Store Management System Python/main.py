import tkinter as tk
import subprocess
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Page")
        self.geometry("800x600")

        header_frame = tk.Frame(self, bg="lightblue", height=50)
        header_frame.pack(fill="x", side="top")

        tk.Label(header_frame, text="My App", font=("Arial", 16), bg="lightblue").pack(side="left", padx=10)
        tk.Button(header_frame, text="About Us", command=self.about_us, bg="lightblue", relief="flat").pack(side="right", padx=10)

        self.image_slider_frame = tk.Frame(self, bg="white", height=400)
        self.image_slider_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.setup_image_slider()

        tk.Button(self, text="Log In", command=self.open_login_popup, font=("Arial", 12)).pack(pady=20)

    def setup_image_slider(self):
        images = [f"assets/slider/i{i}.png" for i in range(1, 11)]
        self.current_image_index = 0
        self.images = []

        for image_path in images:
            try:
                img = Image.open(image_path).resize((600,400), Image.ANTIALIAS)
                self.images.append(ImageTk.PhotoImage(img))
            except Exception:
                pass

        self.image_label = tk.Label(self.image_slider_frame, bg="white")
        self.image_label.pack(expand=True)
        if self.images:
            self.image_label.config(image=self.images[0])
            self.after(2000, self.next_image)

    def next_image(self):
        if not self.images:
            return
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.image_label.config(image=self.images[self.current_image_index])
        self.after(2000, self.next_image)

    def open_login_popup(self):
        self.withdraw()
        try:
            subprocess.run(["python", "views/login.py"], check=True)
        except FileNotFoundError:
            messagebox.showerror("Error", "The login.py file was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.deiconify()

    def login_action(self, popup):
        messagebox.showinfo("Login", "Login action performed!")
        popup.destroy()

    def about_us(self):
        messagebox.showinfo("About Us", "This is the About Us page!")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
