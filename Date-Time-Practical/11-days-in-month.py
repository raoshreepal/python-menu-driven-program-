# 11_days_in_month.py
import calendar

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    days = calendar.monthrange(year, month)[1]
    print(f"Number of days: {days}")

if __name__ == "__main__":
    main()
