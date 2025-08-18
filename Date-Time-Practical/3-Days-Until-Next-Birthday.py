from datetime import datetime

dob_str = input("Enter your birth date (MM-DD): ")
today = datetime.today()
birthday = datetime.strptime(f"{today.year}-{dob_str}", "%Y-%m-%d")

if birthday < today:
    birthday = birthday.replace(year=today.year + 1)

days_left = (birthday - today).days
print("Days until your next birthday:", days_left)
