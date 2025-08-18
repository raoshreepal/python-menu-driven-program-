# 16_iso_week_number.py
from datetime import datetime

def main():
    date_str = input("Enter date (YYYY-MM-DD): ")
    d = datetime.strptime(date_str, "%Y-%m-%d")
    print("ISO week number:", d.isocalendar()[1])

if __name__ == "__main__":
    main()
