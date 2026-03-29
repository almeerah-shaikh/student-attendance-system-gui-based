from student import Student

def save_to_file(students, filename="data.txt"):
    with open(filename, "w") as file:
        for roll_no, student in students.items():
            attendance_str = ",".join(student.attendance)
            file.write(f"{roll_no}|{student.name}|{attendance_str}\n")

def load_from_file(filename="data.txt"):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    roll_no = parts[0]
                    name = parts[1]
                    attendance_list = parts[2].split(",") if len(parts) > 2 and parts[2] else []

                    student = Student(roll_no, name)
                    student.attendance = attendance_list
                    students[roll_no] = student
    except FileNotFoundError:
        pass

    return students