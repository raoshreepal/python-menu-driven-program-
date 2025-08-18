# 19_alarm_clock.py
from datetime import datetime
import time

def main():
    alarm_time = input("Set alarm for (HH:MM, 24-hour): ")
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("⏰ Alarm! Time's up!")
            break
        time.sleep(10)

if __name__ == "__main__":
    main()
# 19. Alarm Clock Program
# This script sets an alarm for a specified time in 24-hour format.
# It continuously checks the current time every 10 seconds and triggers the alarm when the set time is reached.
# The user inputs the alarm time in "HH:MM" format, and the program will print a message when the alarm goes off.
# Make sure to run this script in an environment where you can see the output, as it will wait until the alarm time is reached.