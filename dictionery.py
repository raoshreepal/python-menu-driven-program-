# Functions for dictionary operations
def add_entry(d):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
    print("Entry added.")

def find_entry(d):
    key = input("Enter key to find: ")
    if key in d:
        print(f"Value: {d[key]}")
    else:
        print("Key not found.")

def update_entry(d):
    key = input("Enter key to update: ")
    if key in d:
        value = input("Enter new value: ")
        d[key] = value
        print("Value updated.")
    else:
        print("Key not found.")

def delete_entry(d):
    key = input("Enter key to delete: ")
    if key in d:
        del d[key]
        print("Entry deleted.")
    else:
        print("Key not found.")

# Menu for dictionary

my_dict = {}
while True:
    print("\nDictionary Menu")
    print("1. Add Entry")
    print("2. Find Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Display Dictionary")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_entry(my_dict)
    elif choice == '2':
        find_entry(my_dict)
    elif choice == '3':
        update_entry(my_dict)
    elif choice == '4':
        delete_entry(my_dict)
    elif choice == '5':
        print("Current Dictionary:", my_dict)
    elif choice == '6':
        break
    else:
        print("Invalid choice!")
