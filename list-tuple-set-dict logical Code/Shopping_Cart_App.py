cart = []

def add_item():
    item = input("Enter item to add to cart: ")
    cart.append(item)
    print("Item added to cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
    else:
        print("Your Cart Items:")
        for item in cart:
            print("-", item)

def remove_item():
    item = input("Enter item to remove: ")
    if item in cart:
        cart.remove(item)
        print("Item removed.")
    else:
        print("Item not found in cart.")


while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add_item()
    elif ch == '2':
        view_cart()
    elif ch == '3':
        remove_item()
    elif ch == '4':
        break
    else:
        print("Invalid choice!")

