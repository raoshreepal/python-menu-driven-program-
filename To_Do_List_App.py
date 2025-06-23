tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    task = input("Enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print("Task deleted.")
    else:
        print("Task not found.")


while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add_task()
    elif ch == '2':
        view_tasks()
    elif ch == '3':
        delete_task()
    elif ch == '4':
        break
    else:
        print("Invalid choice!")

