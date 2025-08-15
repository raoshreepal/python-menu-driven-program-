# Use os.path.exists() to verify file existence

import os

file_path = "checkfile.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read())
else:
    print("Error: File does not exist.")
