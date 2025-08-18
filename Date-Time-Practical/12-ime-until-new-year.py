# 12_time_until_new_year.py
from datetime import datetime

def main():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    diff = new_year - now
    print("Time until New Year:", diff)

if __name__ == "__main__":
    main()
# This script calculates the time remaining until the next New Year.
# It uses the datetime module to get the current date and time, then creates a datetime object for the next New Year.
# The difference is calculated and printed, showing how much time is left until January 1st of the next year.
# The output will be in the format of days, hours, minutes, and seconds remaining until New Year.