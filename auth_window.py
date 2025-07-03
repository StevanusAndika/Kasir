import tkinter as tk
from tkinter import messagebox
from utils import hash_password

class AuthWindow:
    def __init__(self, master, db_manager):
        self.master = master
        self.db = db_manager
        self.launch_dashboard = None  # akan diisi dari main.py
        self.master.title("Login Kasir Minimarket IPWIJA")
        self.master.geometry("400x300")
        self.master.configure(bg="#F5F5F5")
        self.master.resizable(False, False)

        self.build_login()
        self.master.bind('<Control-r>', lambda event: self.build_register())

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def build_login(self):
        self.clear_widgets()

        frame = tk.Frame(self.master, bg="#F5F5F5")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(frame, text="Login", font=("Helvetica", 18, "bold"), bg="#F5F5F5").pack(pady=(0, 20))

        tk.Label(frame, text="Username", bg="#F5F5F5", anchor="w").pack(fill="x")
        self.username_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=(0, 10))

        tk.Label(frame, text="Password", bg="#F5F5F5", anchor="w").pack(fill="x")
        self.password_entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=(0, 15))

        login_btn = tk.Button(frame, text="Login", command=self.login, width=20, bg="#4CAF50", fg="white",
                              font=("Arial", 10, "bold"), relief="flat")
        login_btn.pack(pady=(0, 10))

        daftar_btn = tk.Button(frame, text="Daftar", command=self.build_register, width=20, bg="#2196F3", fg="white",
                               font=("Arial", 10, "bold"), relief="flat")
        daftar_btn.pack()

    def build_register(self):
        self.clear_widgets()

        frame = tk.Frame(self.master, bg="#F5F5F5")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(frame, text="Registrasi", font=("Helvetica", 18, "bold"), bg="#F5F5F5").pack(pady=(0, 20))

        tk.Label(frame, text="Username", bg="#F5F5F5", anchor="w").pack(fill="x")
        self.username_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=(0, 10))

        tk.Label(frame, text="Password", bg="#F5F5F5", anchor="w").pack(fill="x")
        self.password_entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=(0, 15))

        register_btn = tk.Button(frame, text="Daftar", command=self.register, width=20, bg="#4CAF50", fg="white",
                                 font=("Arial", 10, "bold"), relief="flat")
        register_btn.pack(pady=(0, 10))

        kembali_btn = tk.Button(frame, text="Kembali", command=self.build_login, width=20, bg="#9E9E9E", fg="white",
                                font=("Arial", 10, "bold"), relief="flat")
        kembali_btn.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi")
            return

        user = self.db.check_user(username, password)
        if user:
            self.master.withdraw()  # sembunyikan window login
            if self.launch_dashboard:
                self.launch_dashboard(user)
        else:
            messagebox.showerror("Error", "Username atau password salah")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi")
            return

        if len(username) < 4:
            messagebox.showerror("Error", "Username minimal 4 karakter")
            return

        if len(password) < 6:
            messagebox.showerror("Error", "Password minimal 6 karakter")
            return

        if self.db.register_user(username, password):
            messagebox.showinfo("Sukses", "Registrasi berhasil! Silakan login")
            self.build_login()
        else:
            messagebox.showerror("Error", "Username sudah digunakan")