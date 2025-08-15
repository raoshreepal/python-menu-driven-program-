# Handle invalid float inputs with try-except

try:
    value = float(input("Enter a float number: "))
    print("You entered:", value)
except ValueError:
    print("Invalid input! Please enter a float.")
