# Validate date format using datetime.strptime

from datetime import datetime

date_str = input("Enter date (YYYY-MM-DD): ")

try:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print("Valid date:", date_obj.date())
except ValueError:
    print("Invalid date format! Please use YYYY-MM-DD.")
