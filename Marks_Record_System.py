marks = {}

def add_marks():
    name = input("Enter student name: ")
    score = float(input("Enter marks: "))
    marks[name] = score
    print("Marks recorded.")

def view_all():
    if not marks:
        print("No marks available.")
    for name, score in marks.items():
        print(f"{name}: {score}")

def find_marks():
    name = input("Enter student name to search: ")
    if name in marks:
        print(f"{name}'s Marks: {marks[name]}")
    else:
        print("Student not found.")


while True:
    print("\n--- Marks Record ---")
    print("1. Add Marks")
    print("2. View All Marks")
    print("3. Search by Name")
    print("4. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add_marks()
    elif ch == '2':
        view_all()
    elif ch == '3':
        find_marks()
    elif ch == '4':
        break
    else:
        print("Invalid choice!")

