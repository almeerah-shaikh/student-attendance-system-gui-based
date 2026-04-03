# Student Attendance System GUI

A Python-based Student Attendance System with a GUI for teachers to log in, manage students, and mark attendance. It securely stores data in files, offers user authentication, and provides an intuitive interface for efficient classroom attendance tracking.

<img width="445" height="375" alt="image" src="https://github.com/user-attachments/assets/55165d07-a1f0-4cd0-8f56-85948242a28d" />
<img width="892" height="594" alt="image" src="https://github.com/user-attachments/assets/c092c387-94cd-4e65-9ff0-87bbab90d8de" />


# Student Attendance System GUI

## Project Overview

The Student Attendance System GUI is a comprehensive Python application designed to simplify and digitize the process of managing student attendance in educational institutions. With a user-friendly graphical interface, this system enables teachers and administrators to securely log in, manage student records, and efficiently record daily attendance. All data is stored in files for persistence and easy retrieval.

---

## Features

- **User Authentication:** Secure login system to ensure only authorized users can access and manage attendance data.
- **Student Management:** Add, edit, and view student records with ease.
- **Attendance Tracking:** Mark and view attendance for each student, with records saved for future reference.
- **File-Based Storage:** All user, student, and attendance data are stored in files for simplicity and portability.
- **Graphical User Interface:** Intuitive and easy-to-use interface for all operations.

---

## Project Structure and Description

```
student-attendance-system-gui/
│
├── attendance.py      # Handles attendance marking and retrieval logic
├── auth.py           # Manages user authentication and login functionality
├── file_handler.py   # Responsible for reading and writing data to files
├── gui.py            # Builds and manages the graphical user interface
├── login.py          # Contains the login window and related logic
├── main.py           # Entry point of the application; initializes and runs the system
├── student.py        # Manages student data and operations
├── __pycache__/      # Stores Python bytecode cache files
└── data.txt          # Stores persistent data (students, attendance, users, etc.)
```

### File Descriptions

- **attendance.py:**  
  Contains functions and classes for marking attendance, retrieving attendance records, and managing attendance-related operations.

- **auth.py:**  
  Implements user authentication, including login verification and password management, to ensure secure access to the system.

- **file_handler.py:**  
  Provides utility functions for reading from and writing to data files. Handles all file I/O operations for students, attendance, and user data.

- **gui.py:**  
  Defines the main graphical user interface, including windows, buttons, forms, and navigation between different parts of the application.

- **login.py:**  
  Contains the logic for the login window, handling user input, authentication checks, and error messages for failed logins.

- **main.py:**  
  The main entry point of the application. Initializes the GUI and coordinates the startup sequence of the system.

- **student.py:**  
  Manages student-related data and operations, such as adding new students, editing student information, and listing all students.

- **__pycache__/:**  
  Directory automatically created by Python to store compiled bytecode files for faster execution.

- **data.txt:**  
  The main data file where all persistent information (students, attendance records, user credentials) is stored.

---

## How to Run

1. Ensure you have Python installed (preferably Python 3.7+).
2. Clone or download this repository.
3. Navigate to the student-attendance-system-gui directory.
4. Run the application:
   ```
   python main.py
   ```
5. Follow the on-screen instructions to log in and use the system.

---

## Future Plans

- Convert the system into a web application using Flask or Django for broader accessibility.
- Add database support for more robust data management.
- Implement reporting and analytics features for attendance data.


---

Let me know if you want this saved to your README.md file or need further customization!
