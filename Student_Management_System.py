# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    students[roll] = {"name": name, "grade": grade}
    print("Student added.")

def view_students():
    if not students:
        print("No student records.")
        return
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['name']}, Grade: {details['grade']}")

def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        print(f"Found: {students[roll]}")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")


while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll")
    print("4. Delete Student by Roll")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")


