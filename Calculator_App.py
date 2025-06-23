def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum =", a + b)

def subtract():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Difference =", a - b)

def multiply():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Product =", a * b)

def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Division by zero error!")

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add()
    elif ch == '2':
        subtract()
    elif ch == '3':
        multiply()
    elif ch == '4':
        divide()
    elif ch == '5':
        break
    else:
        print("Invalid choice!")

