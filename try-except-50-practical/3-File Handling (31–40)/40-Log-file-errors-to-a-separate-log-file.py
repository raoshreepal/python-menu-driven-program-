# Log exceptions during file access to a separate log file

try:
    with open("maybe_missing.txt", "r") as file:
        print(file.read())
except Exception as e:
    with open("file_error_log.txt", "a") as log:
        log.write(f"Error: {str(e)}\n")
    print("An error occurred. Check 'file_error_log.txt' for details.")