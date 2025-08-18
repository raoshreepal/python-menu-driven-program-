# 18_time_zone_difference.py
from datetime import datetime
import pytz

def main():
    tz1 = input("Enter first timezone (e.g., Asia/Kolkata): ")
    tz2 = input("Enter second timezone (e.g., UTC): ")
    now = datetime.now(pytz.timezone(tz1))
    other = now.astimezone(pytz.timezone(tz2))
    diff = other.utcoffset() - now.utcoffset()
    print(f"Time difference between {tz1} and {tz2} is: {diff}")

if __name__ == "__main__":
    main()
