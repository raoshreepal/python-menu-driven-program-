from datetime import datetime

dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d")
today = datetime.today()

age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print("Your age is:", age)
