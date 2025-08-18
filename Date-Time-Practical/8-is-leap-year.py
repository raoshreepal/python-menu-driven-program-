# 8_is_leap_year.py
import calendar

def main():
    year = int(input("Enter a year: "))
    print(f"{year} is a leap year?" , calendar.isleap(year))

if __name__ == "__main__":
    main()
# This script checks if a given year is a leap year.
# It uses the calendar module's isleap function to determine if the year is a leap year.
# A leap year is defined as a year that is divisible by 4, except for end-of-century years, which must be divisible by 400.
# The output will be True if it is a leap year, otherwise False.