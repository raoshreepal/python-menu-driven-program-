# 6_convert_12_to_24.py
from datetime import datetime

def main():
    time_12hr = input("Enter time in 12-hour format (HH:MM AM/PM): ")
    time_24hr = datetime.strptime(time_12hr, "%I:%M %p").strftime("%H:%M")
    print("24-hour format:", time_24hr)

if __name__ == "__main__":
    main()
# This script converts a time from 12-hour format to 24-hour format.
# It uses the datetime module to parse the input time and format it accordingly.
# The input should be in the format "HH:MM AM/PM", and the output will be in "HH:MM" 24-hour format.