from datetime import datetime, timedelta, date
import calendar
import time
import pytz

# 1. Current Date and Time
def current_datetime():
    """Returns the current date and time."""
    return datetime.now()

# 2. Age Calculator
def calculate_age(birthdate: str):
    """Calculates age from birthdate (format: YYYY-MM-DD)."""
    birth = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

# 3. Days Until Your Next Birthday
def days_until_birthday(birthdate: str):
    """Returns days remaining until next birthday."""
    today = datetime.today()
    bday = datetime.strptime(birthdate, "%Y-%m-%d").replace(year=today.year)
    if bday < today:
        bday = bday.replace(year=today.year + 1)
    return (bday - today).days

# 4. Countdown Timer
def countdown(seconds: int):
    """Countdown timer in seconds."""
    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining")
        time.sleep(1)
    print("Time's up!")

# 5. Difference Between Two Dates
def date_difference(date1: str, date2: str):
    """Returns difference in days between two dates (format: YYYY-MM-DD)."""
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# 6. Convert 12-hour to 24-hour Time Format
def convert_to_24_hour(time_str: str):
    """Converts 12-hour format (e.g., 02:30 PM) to 24-hour format."""
    return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")

# 7. Get Day of the Week from a Date
def day_of_week(date_str: str):
    """Returns the day of the week from date."""
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")

# 8. Is a Given Year a Leap Year?
def is_leap_year(year: int):
    """Checks if a given year is a leap year."""
    return calendar.isleap(year)

# 9. Add/Subtract Days from a Given Date
def modify_date(start_date: str, days: int):
    """Adds or subtracts days from a date."""
    d = datetime.strptime(start_date, "%Y-%m-%d")
    return d + timedelta(days=days)

# 10. Generate a Calendar for a Month
def generate_month_calendar(year: int, month: int):
    """Generates a calendar for a specific month."""
    return calendar.month(year, month)

# 11. Get Number of Days in a Month
def days_in_month(year: int, month: int):
    """Returns the number of days in a month."""
    return calendar.monthrange(year, month)[1]

# 12. Time Until New Year
def time_until_new_year():
    """Returns time remaining until New Year."""
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    return new_year - now

# 13. Calculate Total Seconds Between Two Times
def seconds_between_times(time1: str, time2: str):
    """Returns total seconds between two times (HH:MM:SS)."""
    t1 = datetime.strptime(time1, "%H:%M:%S")
    t2 = datetime.strptime(time2, "%H:%M:%S")
    return abs((t2 - t1).total_seconds())

# 14. Check if a Date is in the Past or Future
def check_date_past_future(date_str: str):
    """Checks if a given date is in the past, future, or today."""
    d = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = date.today()
    if d < today:
        return "Past"
    elif d > today:
        return "Future"
    else:
        return "Today"

# 15. Meeting Scheduler (Check if Time Overlaps)
def check_meeting_overlap(start1, end1, start2, end2):
    """Checks if two meeting times overlap."""
    s1 = datetime.strptime(start1, "%H:%M")
    e1 = datetime.strptime(end1, "%H:%M")
    s2 = datetime.strptime(start2, "%H:%M")
    e2 = datetime.strptime(end2, "%H:%M")
    return s1 < e2 and s2 < e1

# 16. Get ISO Week Number from Date
def get_iso_week_number(date_str: str):
    """Returns the ISO week number for a given date."""
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return d.isocalendar()[1]

# 17. Convert String to Date and Vice Versa
def str_to_date(date_str: str):
    """Converts a string to a date object."""
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def date_to_str(date_obj: date):
    """Converts a date object to a string."""
    return date_obj.strftime("%Y-%m-%d")

# 18. Time Difference Between Two Time Zones
def time_diff_between_timezones(tz1: str, tz2: str):
    """Returns the time difference between two time zones."""
    now = datetime.now()
    tz1_time = pytz.timezone(tz1).localize(now)
    tz2_time = tz1_time.astimezone(pytz.timezone(tz2))
    return tz2_time - tz1_time

# 19. Alarm Clock Program
def alarm_clock(alarm_time: str):
    """Triggers an alarm at the specified time (format: HH:MM)."""
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("⏰ Alarm! Time's up!")
            break
        time.sleep(10)

# 20. Working Days Between Two Dates (Exclude Weekends)
def working_days_between(start_date: str, end_date: str):
    """Returns number of working days between two dates (excluding weekends)."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    days = 0
    for i in range((end - start).days + 1):
        day = start + timedelta(days=i)
        if day.weekday() < 5:  # Mon–Fri are 0–4
            days += 1
    return days

# -----------------------------
# Example usage (Uncomment to test)
# -----------------------------
if __name__ == "__main__":
    print("1. Current DateTime:", current_datetime())
    print("2. Age from DOB:", calculate_age("1990-08-18"))
    print("3. Days till birthday:", days_until_birthday("1990-08-18"))
    # countdown(5)  # Uncomment to test
    print("5. Date difference:", date_difference("2025-08-01", "2025-08-18"))
    print("6. 24-hour time:", convert_to_24_hour("02:30 PM"))
    print("7. Day of week:", day_of_week("2025-08-18"))
    print("8. Leap year?:", is_leap_year(2024))
    print("9. Add days:", modify_date("2025-08-18", 10))
    print("10. Calendar:\n", generate_month_calendar(2025, 8))
    print("11. Days in month:", days_in_month(2025, 2))
    print("12. Time until New Year:", time_until_new_year())
    print("13. Seconds between:", seconds_between_times("10:00:00", "12:30:00"))
    print("14. Date check:", check_date_past_future("2025-08-18"))
    print("15. Meeting overlap:", check_meeting_overlap("10:00", "11:00", "10:30", "11:30"))
    print("16. ISO week:", get_iso_week_number("2025-08-18"))
    print("17. String to date:", str_to_date("2025-08-18"))
    print("18. Timezone difference:", time_diff_between_timezones("Asia/Kolkata", "UTC"))
    # alarm_clock("13:00")  # Uncomment to test
    print("20. Working days:", working_days_between("2025-08-01", "2025-08-18"))
