# Catch an exception and log error to a text file

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except Exception as e:
    print("An error occurred:", e)
    with open("error_log.txt", "a") as f:
        f.write(str(e) + "\n")
