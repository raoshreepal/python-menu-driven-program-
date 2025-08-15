# Ask user for integer input, retry on ValueError

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
