import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from db_manager import DatabaseManager

class DashboardKasir:
    def __init__(self, master, user_data=None):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.master = master
        self.master.title("Dashboard Kasir")
        self.master.geometry("1100x700")
        self.db = DatabaseManager()
        self.cart = []
        self.user_data = user_data

        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self.master, text="SISTEM KASIR - MINIMARKET IPWIJA", 
                     font=ctk.CTkFont(size=22, weight="bold"), text_color="red").pack(pady=10)

        # Frame atas
        frame_top = ctk.CTkFrame(self.master)
        frame_top.pack(padx=20, fill="x", pady=5)

        self.entry_tanggal = ctk.CTkEntry(frame_top, width=120)
        self.entry_tanggal.insert(0, datetime.now().strftime("%d/%m/%Y"))

        ctk.CTkLabel(frame_top, text="TANGGAL").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_tanggal.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_top, text="PELANGGAN").grid(row=0, column=2, padx=5, pady=5)
        self.entry_pelanggan = ctk.CTkEntry(frame_top, width=200)
        self.entry_pelanggan.grid(row=0, column=3, padx=5, pady=5)

        ctk.CTkLabel(frame_top, text="TUNAI/KREDIT").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_pembayaran = ctk.CTkComboBox(frame_top, values=["TUNAI", "KREDIT"], width=100)
        self.combo_pembayaran.set("TUNAI")
        self.combo_pembayaran.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_top, text="SALES").grid(row=1, column=2, padx=5, pady=5)
        self.entry_sales = ctk.CTkEntry(frame_top, width=200)
        self.entry_sales.grid(row=1, column=3, padx=5, pady=5)
        if self.user_data:
            self.entry_sales.insert(0, self.user_data.get("username", ""))
            self.entry_sales.configure(state="disabled")

        # Frame input
        frame_input = ctk.CTkFrame(self.master)
        frame_input.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(frame_input, text="Kode Barang").grid(row=0, column=0, sticky="w")
        self.entry_kode = ctk.CTkEntry(frame_input)
        self.entry_kode.grid(row=0, column=1, sticky="ew", padx=5)
        self.entry_kode.bind("<KeyRelease>", self.show_suggestions)

        ctk.CTkLabel(frame_input, text="Jumlah").grid(row=0, column=2, padx=10, sticky="w")
        self.entry_jumlah = ctk.CTkEntry(frame_input, width=50)
        self.entry_jumlah.insert(0, "1")
        self.entry_jumlah.grid(row=0, column=3)

        self.listbox_suggest = tk.Listbox(frame_input, height=4)
        self.listbox_suggest.grid(row=1, column=1, columnspan=3, sticky="ew")
        self.listbox_suggest.bind("<Double-Button-1>", self.select_suggestion)

        ctk.CTkButton(frame_input, text="Tambah", command=self.tambah_barang).grid(row=0, column=4, padx=10)

        # Tabel transaksi
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=28)

        columns = ("Kode", "Nama", "Jumlah", "Satuan", "Harga", "Diskon", "Netto", "Total")
        self.tree = ttk.Treeview(self.master, columns=columns, show="headings", height=10)
        self.tree.pack(padx=20, fill="x", pady=5)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        # Frame bawah
        frame_bottom = ctk.CTkFrame(self.master)
        frame_bottom.pack(padx=20, pady=10, fill="x")

        self.label_subtotal = ctk.CTkLabel(frame_bottom, text="Subtotal: Rp 0", font=ctk.CTkFont(size=14))
        self.label_subtotal.pack(anchor="w")

        self.label_grandtotal = ctk.CTkLabel(frame_bottom, text="Grand Total: Rp 0", font=ctk.CTkFont(size=14))
        self.label_grandtotal.pack(anchor="w")

        ctk.CTkLabel(frame_bottom, text="Tunai (F7):").pack(anchor="w", pady=(10, 0))
        self.entry_bayar = ctk.CTkEntry(frame_bottom, width=150)
        self.entry_bayar.pack(anchor="w")
        self.entry_bayar.bind("<KeyRelease>", self.hitung_kembalian)
        self.entry_bayar.bind("<Return>", self.hitung_kembalian)
        self.entry_bayar.bind("<KeyPress>", self.hanya_angka)

        self.label_kembali = ctk.CTkLabel(frame_bottom, text="Kembali: Rp 0")
        self.label_kembali.pack(anchor="w", pady=(10, 0))

        # Tombol aksi
        frame_button = ctk.CTkFrame(self.master)
        frame_button.pack(pady=10)

        ctk.CTkButton(frame_button, text="Simpan [F9]", command=self.simpan_transaksi, width=150).pack(side="left", padx=10)
        ctk.CTkButton(frame_button, text="Baru [F5]", command=self.reset_transaksi, width=150).pack(side="left", padx=10)

    def format_rupiah(self, angka):
        return f"Rp {angka:,.0f}".replace(",", ".")

    def show_suggestions(self, event=None):
        keyword = self.entry_kode.get().strip()
        self.listbox_suggest.delete(0, tk.END)
        if keyword:
            results = self.db.search_barang(keyword)
            for row in results:
                self.listbox_suggest.insert(tk.END, f"{row[0]} - {row[1]}")

    def select_suggestion(self, event=None):
        selection = self.listbox_suggest.get(self.listbox_suggest.curselection())
        kode = selection.split(" - ")[0]
        self.entry_kode.delete(0, tk.END)
        self.entry_kode.insert(0, kode)
        self.listbox_suggest.delete(0, tk.END)

    def tambah_barang(self):
        kode = self.entry_kode.get().strip()
        try:
            jumlah = int(self.entry_jumlah.get())
        except:
            jumlah = 1

        barang = self.db.get_barang_by_kode(kode)
        if not barang:
            messagebox.showerror("Tidak ditemukan", f"Barang dengan kode {kode} tidak ditemukan.")
            return

        kode, nama, satuan, harga = barang
        total = harga * jumlah
        self.tree.insert("", tk.END, values=(kode, nama, jumlah, satuan, harga, 0, harga, total))
        self.cart.append((kode, nama, jumlah, satuan, harga, total))

        self.update_total()
        self.entry_kode.delete(0, tk.END)
        self.entry_jumlah.delete(0, tk.END)
        self.entry_jumlah.insert(0, "1")
        self.hitung_kembalian()

    def update_total(self):
        total = sum(item[-1] for item in self.cart)
        self.label_subtotal.configure(text=f"Subtotal: {self.format_rupiah(total)}")
        self.label_grandtotal.configure(text=f"Grand Total: {self.format_rupiah(total)}")

    def hitung_kembalian(self, event=None):
        try:
            bayar = int(self.entry_bayar.get())
        except ValueError:
            bayar = 0

        total = sum(item[-1] for item in self.cart)
        kembali = max(bayar - total, 0)
        self.label_kembali.configure(text=f"Kembali: {self.format_rupiah(kembali)}")

    def hanya_angka(self, event):
        if not event.char.isdigit() and event.keysym not in ("BackSpace", "Delete", "Left", "Right"):
            return "break"

    def simpan_transaksi(self):
        if not self.cart:
            messagebox.showwarning("Kosong", "Tidak ada item untuk disimpan.")
            return

        try:
            bayar = int(self.entry_bayar.get())
        except:
            messagebox.showerror("Error", "Masukkan jumlah bayar yang valid.")
            return

        total = sum(item[-1] for item in self.cart)
        kembali = bayar - total

        data_penjualan = (
            datetime.now(),
            self.entry_pelanggan.get(),
            self.entry_sales.get(),
            self.combo_pembayaran.get(),
            total,
            bayar,
            kembali
        )

        data_detail = [
            (kode, nama, jumlah, satuan, harga, total)
            for (kode, nama, jumlah, satuan, harga, total) in self.cart
        ]

        self.db.simpan_transaksi(data_penjualan, data_detail)
        messagebox.showinfo("Berhasil", "Transaksi berhasil disimpan.")
        self.label_kembali.configure(text=f"Kembali: {self.format_rupiah(kembali)}")
        self.reset_transaksi(clear_form=False)

    def reset_transaksi(self, clear_form=True):
        self.tree.delete(*self.tree.get_children())
        self.cart = []
        self.update_total()
        self.entry_kode.delete(0, tk.END)
        self.entry_jumlah.delete(0, tk.END)
        self.entry_jumlah.insert(0, "1")
        if clear_form:
            self.entry_bayar.delete(0, tk.END)
            self.label_kembali.configure(text="Kembali: Rp 0")