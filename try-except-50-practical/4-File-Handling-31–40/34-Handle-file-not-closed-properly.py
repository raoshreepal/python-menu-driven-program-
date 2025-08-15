# Use finally block to ensure file is closed properly

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except Exception as e:
    print("Error reading file:", e)
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened.")