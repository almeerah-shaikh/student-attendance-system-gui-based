class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.attendance = []

    def mark_attendance(self, status):
        self.attendance.append(status)

    def get_attendance_count(self):
        present = self.attendance.count("P")
        absent = self.attendance.count("A")
        return present, absent

    def get_attendance_percentage(self):
        total = len(self.attendance)
        if total == 0:
            return 0
        present = self.attendance.count("P")
        return (present / total) * 100

    def __str__(self):
        present, absent = self.get_attendance_count()
        percentage = self.get_attendance_percentage()
        return (
            f"Roll No: {self.roll_no}, Name: {self.name}, "
            f"Present: {present}, Absent: {absent}, "
            f"Attendance: {percentage:.2f}%"
        )