
import tkinter as tk
from login import LoginWindow
from gui import AttendanceGUI
from file_handler import load_from_file
from attendance import load_students_data


def open_dashboard():
    dashboard_root = tk.Tk()
    app = AttendanceGUI(dashboard_root)
    dashboard_root.mainloop()


def main():
    data = load_from_file()
    load_students_data(data)

    login_root = tk.Tk()
    login_app = LoginWindow(login_root, open_dashboard)
    login_root.mainloop()


if __name__ == "__main__":
    main()