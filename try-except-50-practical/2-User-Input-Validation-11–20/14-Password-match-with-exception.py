# Raise ValueError if passwords do not match

password1 = input("Enter password: ")
password2 = input("Confirm password: ")

try:
    if password1 != password2:
        raise ValueError("Passwords do not match.")
    print("Password matched successfully!")
except ValueError as e:
    print("Error:", e)
