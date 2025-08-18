# 7_day_of_week.py
from datetime import datetime

def main():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print("Day of the week:", date_obj.strftime("%A"))

if __name__ == "__main__":
    main()
# This script takes a date input from the user in the format YYYY-MM-DD
# and outputs the day of the week for that date.
# It uses the datetime module to parse the input date and format it to display the full name of the day.
# The output will be one of the days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.