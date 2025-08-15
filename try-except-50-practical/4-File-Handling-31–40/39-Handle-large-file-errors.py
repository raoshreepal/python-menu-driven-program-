# Read large file in chunks, handle MemoryError

try:
    with open("largefile.txt", "r") as file:
        while True:
            chunk = file.read(1024)  # Read in 1KB chunks
            if not chunk:
                break
            print(chunk)
except MemoryError:
    print("Error: Not enough memory to read the file.")
except FileNotFoundError:
    print("Error: File not found.")