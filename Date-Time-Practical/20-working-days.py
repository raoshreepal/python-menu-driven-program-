# 20_working_days.py
from datetime import datetime, timedelta

def main():
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    workdays = 0
    for i in range((end_date - start_date).days + 1):
        day = start_date + timedelta(days=i)
        if day.weekday() < 5:
            workdays += 1
    print(f"Working days (Mon–Fri): {workdays}")

if __name__ == "__main__":
    main()
