# Allow only 3 attempts to enter a valid integer

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break
    except ValueError:
        attempts += 1
        print(f"Invalid input. Attempts left: {max_attempts - attempts}")
else:
    print("Too many invalid attempts. Exiting.")
