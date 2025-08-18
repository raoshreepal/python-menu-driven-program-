# 10_month_calendar.py
import calendar

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))

if __name__ == "__main__":
    main()
# This script displays the calendar for a specific month of a given year.
# It uses the calendar module to generate the month view.
# The user inputs the year and month, and the script prints the calendar for that month.
# The output will show the days of the week and the dates arranged in a grid format.