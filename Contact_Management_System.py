contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Phone Number: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add_contact()
    elif ch == '2':
        view_contacts()
    elif ch == '3':
        search_contact()
    elif ch == '4':
        delete_contact()
    elif ch == '5':
        break
    else:
        print("Invalid choice!")

