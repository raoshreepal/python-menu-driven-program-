def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found!")
        return None

def process_file(filename):
    content = read_file(filename)
    if content:
        try:
            # Example processing: convert to int (raises ValueError if fails)
            number = int(content)
            return number * 2
        except ValueError:
            print("File content is not a valid number!")
            return None
    return None

# Example usage
print(process_file("data.txt"))
