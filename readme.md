Berikut adalah file `README.md` untuk proyek Sistem Kasir Minimarket IPWIJA:

```markdown
# Sistem Kasir Minimarket IPWIJA



## 📝 Deskripsi Proyek
Aplikasi kasir berbasis GUI Python dengan fitur:
- Autentikasi pengguna (login/register)
- Manajemen transaksi penjualan
- Pencarian barang otomatis
- Perhitungan otomatis (subtotal, grandtotal, kembalian)
- Penyimpanan data ke database MySQL

## 🛠 Teknologi Digunakan
- Python 3.x
- Tkinter (GUI)
- CustomTkinter (Modern UI)
- MySQL Connector
- MySQL Database

## ⚙️ Persyaratan Sistem
1. Python 3.7+
2. MySQL Server
3. Database `kasir_db` (akan dibuat otomatis)

## 🚀 Panduan Instalasi
1. Clone repository ini:
   ```bash
   git clone https://github.com/username/sistem-kasir-ipwija.git
   cd sistem-kasir-ipwija
   ```

2. Install dependencies:
   ```bash
   python -m pip install mysql-connector-python
   python -m pip install customtkinter
   ```

3. Konfigurasi database:
   - Pastikan MySQL server berjalan
   - Buat database bernama `kasir_db` atau sesuaikan di `db_manager.py`

4. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## 📋 Struktur File
```
sistem-kasir/
├── main.py            # Entry point aplikasi
├── auth_window.py     # Modul autentikasi (login/register)
├── dashboard.py       # Modul dashboard kasir
├── db_manager.py      # Modul manajemen database
├── utils.py           # Fungsi utilitas
└── README.md          # Dokumentasi proyek
```

## 🧑‍💻 Penggunaan
1. **Login/Register**:
   - Gunakan tombol "Daftar" untuk membuat akun baru
   - Tekan "Login" setelah mengisi username/password

2. **Dashboard Kasir**:
   - Input kode barang atau cari menggunakan fitur autocomplete
   - Atur jumlah barang dan tekan "Tambah"
   - Sistem akan menghitung total otomatis
   - Masukkan jumlah bayar untuk melihat kembalian
   - Tekan "Simpan" untuk menyimpan transaksi

## 🎨 Tampilan Aplikasi
### Login Window


## 📌 Shortcut Keyboard
- `F5` - Reset transaksi
- `F7` - Fokus ke input pembayaran
- `F9` - Simpan transaksi
- `Ctrl+R` - Buka form registrasi (di halaman login)

## 🤝 Kontribusi
Kontribusi terbuka melalui:
1. Fork proyek ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Tambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📜 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE)

---
🛒 Dibuat untuk kebutuhan contoh belajar - © 2025
```


