# Use context manager with try-except for safe file handling

try:
    with open("info.txt", "r") as file:
        data = file.read()
        print("File content:", data)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("I/O error occurred.")