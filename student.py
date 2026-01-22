import sqlite3

# ---------------- DATABASE SETUP ----------------
def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT UNIQUE,
            department TEXT,
            year INTEGER,
            marks REAL
        )
    """)
    conn.commit()
    conn.close()


# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")
    year = int(input("Enter year: "))
    marks = float(input("Enter marks: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, roll, department, year, marks) VALUES (?, ?, ?, ?, ?)",
            (name, roll, dept, year, marks)
        )
        conn.commit()
        print("✅ Student added successfully")
    except:
        print("❌ Roll number already exists")

    conn.close()


# ---------------- VIEW STUDENTS ----------------
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n------ Student Records ------")
    for row in records:
        print(row)

    conn.close()


# ---------------- SEARCH STUDENT ----------------
def search_student():
    roll = input("Enter roll number to search: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    record = cursor.fetchone()

    if record:
        print("Student Found:", record)
    else:
        print("❌ Student not found")

    conn.close()


# ---------------- UPDATE STUDENT ----------------
def update_student():
    roll = input("Enter roll number to update: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    record = cursor.fetchone()

    if not record:
        print("❌ Student not found")
        conn.close()
        return

    name = input("Enter new name: ")
    dept = input("Enter new department: ")
    year = int(input("Enter new year: "))
    marks = float(input("Enter new marks: "))

    cursor.execute("""
        UPDATE students
        SET name=?, department=?, year=?, marks=?
        WHERE roll=?
    """, (name, dept, year, marks, roll))

    conn.commit()
    conn.close()
    print("✅ Student updated successfully")


# ---------------- DELETE STUDENT ----------------
def delete_student():
    roll = input("Enter roll number to delete: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Student not found")
    else:
        print("✅ Student deleted successfully")

    conn.close()


# ---------------- MAIN MENU ----------------
def main():
    connect_db()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you! 👋")
            break
        else:
            print("❌ Invalid choice")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()