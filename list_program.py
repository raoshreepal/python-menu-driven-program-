# Functions for list operations
def append_item(lst):
    item = input("Enter item to append: ")
    lst.append(item)
    print("Item appended.")

def find_item(lst):
    item = input("Enter item to find: ")
    if item in lst:
        print("Item found at index:", lst.index(item))
    else:
        print("Item not found.")

def replace_item(lst):
    old = input("Enter item to replace: ")
    if old in lst:
        new = input("Enter new item: ")
        idx = lst.index(old)
        lst[idx] = new
        print("Item replaced.")
    else:
        print("Item not found.")

def delete_item(lst):
    item = input("Enter item to delete: ")
    if item in lst:
        lst.remove(item)
        print("Item deleted.")
    else:
        print("Item not found.")

# Menu for list

my_list = []
while True:
    print("\nList Menu")
    print("1. Append")
    print("2. Find")
    print("3. Replace")
    print("4. Delete")
    print("5. Display List")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        append_item(my_list)
    elif choice == '2':
        find_item(my_list)
    elif choice == '3':
        replace_item(my_list)
    elif choice == '4':
        delete_item(my_list)
    elif choice == '5':
        print("Current List:", my_list)
    elif choice == '6':
        break
    else:
        print("Invalid choice!")
