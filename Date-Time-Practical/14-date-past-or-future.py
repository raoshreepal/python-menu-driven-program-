# 14_date_past_or_future.py
from datetime import datetime, date

def main():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    d = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = date.today()
    if d < today:
        print("The date is in the past.")
    elif d > today:
        print("The date is in the future.")
    else:
        print("The date is today.")

if __name__ == "__main__":
    main()
