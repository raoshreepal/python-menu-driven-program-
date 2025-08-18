# 9_add_subtract_days.py
from datetime import datetime, timedelta

def main():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    days = int(input("Enter number of days to add/subtract (use negative for subtract): "))
    new_date = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=days)
    print("New date:", new_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
# output
# Enter the date (YYYY-MM-DD): 2023-09-01
# Enter number of days to add/subtract (use negative for subtract): 5
# New date: 2023-09-06