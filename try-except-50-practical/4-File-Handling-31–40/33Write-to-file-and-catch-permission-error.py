# Handle PermissionError when trying to write to a restricted file

try:
    with open("/restricted_file.txt", "w") as file:
        file.write("Trying to write to a protected file.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")