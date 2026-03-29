from student import Student

students = {}

def add_student(roll_no, name):
    if roll_no in students:
        return "Student already exists."
    students[roll_no] = Student(roll_no, name)
    return "Student added successfully."

def mark_attendance(roll_no, status):
    if roll_no not in students:
        return "Student not found."

    status = status.upper()
    if status not in ["P", "A"]:
        return "Invalid status. Use P or A."

    students[roll_no].mark_attendance(status)
    return "Attendance marked successfully."

def view_all_students():
    return list(students.values())

def search_student(roll_no):
    return students.get(roll_no, None)

def delete_student(roll_no):
    if roll_no in students:
        del students[roll_no]
        return "Student deleted successfully."
    return "Student not found."

def get_students_data():
    return students

def load_students_data(data):
    global students
    students = data