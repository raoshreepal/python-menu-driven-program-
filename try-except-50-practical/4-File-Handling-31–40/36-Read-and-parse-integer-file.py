# Handle ValueError if file content is not a valid integer

try:
    with open("number.txt", "r") as file:
        number = int(file.read())
        print("Parsed number:", number)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Error: File content is not a valid integer.")