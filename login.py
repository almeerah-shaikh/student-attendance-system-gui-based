
import tkinter as tk
from tkinter import messagebox
from auth import authenticate

class LoginWindow:
    def __init__(self, master, on_success):
        self.master = master
        self.master.title("Login")
        self.on_success = on_success

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate(username, password):
            self.master.destroy()
            self.on_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

import tkinter as tk
from tkinter import messagebox
from auth import authenticate


class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Login - Student Attendance System")
        self.root.geometry("450x350")
        self.root.configure(bg="#f4f6f8")
        self.root.resizable(False, False)

        self.on_login_success = on_login_success

        title = tk.Label(
            root,
            text="Student Attendance System",
            font=("Arial", 18, "bold"),
            bg="#f4f6f8",
            fg="#1f3b73"
        )
        title.pack(pady=25)

        subtitle = tk.Label(
            root,
            text="Login to Continue",
            font=("Arial", 12),
            bg="#f4f6f8",
            fg="#555555"
        )
        subtitle.pack(pady=5)

        form_frame = tk.Frame(root, bg="#f4f6f8")
        form_frame.pack(pady=25)

        tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#f4f6f8").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.username_entry = tk.Entry(form_frame, font=("Arial", 12), width=22)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#f4f6f8").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.password_entry = tk.Entry(form_frame, font=("Arial", 12), width=22, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(
            root,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="#1f78d1",
            fg="white",
            width=15,
            command=self.login
        )
        login_button.pack(pady=20)

        hint = tk.Label(
            root,
            text="Demo Login → Username: admin | Password: 1234",
            font=("Arial", 9),
            bg="#f4f6f8",
            fg="#777777"
        )
        hint.pack(pady=10)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if authenticate(username, password):
            messagebox.showinfo("Login Successful", "Welcome to the Student Attendance System!")
            self.root.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")