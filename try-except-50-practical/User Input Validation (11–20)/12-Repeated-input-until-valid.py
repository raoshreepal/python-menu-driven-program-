# Loop until a valid integer is entered using while True

while True:
    try:
        num = int(input("Enter a valid integer: "))
        print("You entered:", num)
        break  # Exit loop if input is valid
    except ValueError:
        print("That's not an integer. Try again.")
