# 13_seconds_between_times.py
from datetime import datetime

def main():
    t1 = input("Enter first time (HH:MM:SS): ")
    t2 = input("Enter second time (HH:MM:SS): ")
    time1 = datetime.strptime(t1, "%H:%M:%S")
    time2 = datetime.strptime(t2, "%H:%M:%S")
    print("Seconds between times:", abs((time2 - time1).total_seconds()))

if __name__ == "__main__":
    main()
