import tkinter as tk
from db_manager import DatabaseManager
from auth_window import AuthWindow
from dashboard import DashboardKasir

def launch_dashboard(user_data):
    dashboard_window = tk.Toplevel()
    DashboardKasir(dashboard_window, user_data=user_data)

if __name__ == "__main__":
    root = tk.Tk()
    db = DatabaseManager()
    app = AuthWindow(root, db)
    app.launch_dashboard = launch_dashboard  # inject fungsi agar bisa dipanggil dari AuthWindow
    root.mainloop()
