# 17_string_date_conversion.py
from datetime import datetime

def main():
    choice = input("Convert (1) String to Date or (2) Date to String? ")
    if choice == "1":
        date_str = input("Enter date string (YYYY-MM-DD): ")
        print("Date object:", datetime.strptime(date_str, "%Y-%m-%d").date())
    elif choice == "2":
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        d = datetime(year, month, day).date()
        print("Date string:", d.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
