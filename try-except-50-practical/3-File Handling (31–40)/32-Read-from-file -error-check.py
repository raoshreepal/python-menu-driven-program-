# Handle IOError during file reading

try:
    with open("data.txt", "r") as file:
        print(file.read())
except IOError:
    print("Error: An I/O error occurred while reading the file.")