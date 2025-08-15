# Catch FileNotFoundError and create the file

file_name = "newfile.txt"

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Creating a new file...")
    with open(file_name, "w") as file:
        file.write("This is a new file.")
    print("File created and written to.")