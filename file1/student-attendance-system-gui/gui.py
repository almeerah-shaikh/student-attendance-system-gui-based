
import tkinter as tk
from tkinter import messagebox, ttk
from attendance import (
    add_student,
    mark_attendance,
    view_all_students,
    search_student,
    delete_student,
    get_students_data
)
from file_handler import save_to_file

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Dashboard")
        self.root.geometry("900x620")
        self.root.configure(bg="#f4f6f8")

        title = tk.Label(
            root,
            text="Student Attendance Dashboard",
            font=("Arial", 20, "bold"),
            bg="#f4f6f8",
            fg="#1f3b73"
        )
        title.pack(pady=15)

        form_frame = tk.Frame(root, bg="#f4f6f8")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Roll No:", font=("Arial", 11), bg="#f4f6f8").grid(row=0, column=0, padx=10, pady=5)
        self.roll_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
        self.roll_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Student Name:", font=("Arial", 11), bg="#f4f6f8").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Attendance (P/A):", font=("Arial", 11), bg="#f4f6f8").grid(row=2, column=0, padx=10, pady=5)
        self.status_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
        self.status_entry.grid(row=2, column=1, padx=10, pady=5)

        button_frame = tk.Frame(root, bg="#f4f6f8")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Add Student", width=18, command=self.add_student_gui, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=8, pady=8)
        tk.Button(button_frame, text="Mark Attendance", width=18, command=self.mark_attendance_gui, bg="#2196F3", fg="white").grid(row=0, column=1, padx=8, pady=8)
        tk.Button(button_frame, text="Search Student", width=18, command=self.search_student_gui, bg="#FF9800", fg="white").grid(row=0, column=2, padx=8, pady=8)
        tk.Button(button_frame, text="Delete Student", width=18, command=self.delete_student_gui, bg="#f44336", fg="white").grid(row=0, column=3, padx=8, pady=8)

        tk.Button(button_frame, text="View All Students", width=18, command=self.display_students, bg="#673AB7", fg="white").grid(row=1, column=0, padx=8, pady=8)
        tk.Button(button_frame, text="Save Data", width=18, command=self.save_data_gui, bg="#009688", fg="white").grid(row=1, column=1, padx=8, pady=8)
        tk.Button(button_frame, text="Clear Fields", width=18, command=self.clear_fields, bg="#607D8B", fg="white").grid(row=1, column=2, padx=8, pady=8)
        tk.Button(button_frame, text="Exit", width=18, command=self.exit_app, bg="#795548", fg="white").grid(row=1, column=3, padx=8, pady=8)

        self.tree = ttk.Treeview(root, columns=("Roll No", "Name", "Present", "Absent", "Percentage"), show="headings", height=15)
        self.tree.heading("Roll No", text="Roll No")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Present", text="Present")
        self.tree.heading("Absent", text="Absent")
        self.tree.heading("Percentage", text="Attendance %")

        self.tree.column("Roll No", width=100)
        self.tree.column("Name", width=180)
        self.tree.column("Present", width=100)
        self.tree.column("Absent", width=100)
        self.tree.column("Percentage", width=120)

        self.tree.pack(pady=20)

        self.display_students()

    def add_student_gui(self):
        roll_no = self.roll_entry.get().strip()
        name = self.name_entry.get().strip()

        if not roll_no or not name:
            messagebox.showwarning("Input Error", "Please enter both Roll No and Name.")
            return

        result = add_student(roll_no, name)
        messagebox.showinfo("Result", result)
        self.display_students()
        self.clear_fields()

    def mark_attendance_gui(self):
        roll_no = self.roll_entry.get().strip()
        status = self.status_entry.get().strip()

        if not roll_no or not status:
            messagebox.showwarning("Input Error", "Please enter Roll No and Attendance status.")
            return

        result = mark_attendance(roll_no, status)
        messagebox.showinfo("Result", result)
        self.display_students()
        self.clear_fields()

    def search_student_gui(self):
        roll_no = self.roll_entry.get().strip()

        if not roll_no:
            messagebox.showwarning("Input Error", "Please enter Roll No.")
            return

        student = search_student(roll_no)
        if student:
            present, absent = student.get_attendance_count()
            percentage = student.get_attendance_percentage()
            messagebox.showinfo(
                "Student Found",
                f"Roll No: {student.roll_no}\n"
                f"Name: {student.name}\n"
                f"Present: {present}\n"
                f"Absent: {absent}\n"
                f"Attendance: {percentage:.2f}%"
            )
        else:
            messagebox.showerror("Not Found", "Student not found.")

    def delete_student_gui(self):
        roll_no = self.roll_entry.get().strip()

        if not roll_no:
            messagebox.showwarning("Input Error", "Please enter Roll No.")
            return

        result = delete_student(roll_no)
        messagebox.showinfo("Result", result)
        self.display_students()
        self.clear_fields()

    def display_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = view_all_students()
        for student in students:
            present, absent = student.get_attendance_count()
            percentage = student.get_attendance_percentage()
            self.tree.insert("", tk.END, values=(
                student.roll_no,
                student.name,
                present,
                absent,
                f"{percentage:.2f}%"
            ))

    def save_data_gui(self):
        save_to_file(get_students_data())
        messagebox.showinfo("Saved", "Data saved successfully.")

    def clear_fields(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

    def exit_app(self):
        save_to_file(get_students_data())
        self.root.destroy()