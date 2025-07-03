import mysql.connector
from utils import hash_password

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # kosongkan jika tidak ada password
            database="kasir_db"
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.create_user_table()

    def create_user_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def register_user(self, username, password):
        try:
            hashed = hash_password(password)
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed)
            )
            self.conn.commit()
            return True
        except mysql.connector.IntegrityError:
            return False  # username sudah ada
        except Exception as e:
            print(f"Error registering user: {e}")
            return False

    def check_user(self, username, password):
        try:
            self.cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )
            user = self.cursor.fetchone()
            if user and user['password'] == hash_password(password):
                return user
            return None
        except Exception as e:
            print(f"Error checking user: {e}")
            return None

    def get_barang_by_kode(self, kode):
        # Implementasi pencarian barang
        pass

    def simpan_transaksi(self, data_penjualan, data_detail):
        # Implementasi simpan transaksi
        pass
    
    def search_barang(self, keyword):
        # Implementasi pencarian barang
        pass