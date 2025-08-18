
# 🕒 Python Date & Time Utilities (20 Script Collection)

This project is a collection of **20 standalone Python shell scripts**, each solving a practical date or time-related task. These scripts are designed for easy use and direct execution from the terminal.

---

## ✅ Features

- Get current date and time
- Calculate age and birthday countdowns
- Work with calendars, leap years, and time formats
- Compute differences between times, dates, and time zones
- Schedule meetings, set alarms, and more

---

## 📁 Script List

| S.No | Script File Name              | Description |
|------|-------------------------------|-------------|
| 1    | `1_current_datetime.py`       | Displays the current date and time |
| 2    | `2_age_calculator.py`         | Calculates your age from a given birthdate |
| 3    | `3_days_until_birthday.py`    | Shows how many days are left until your next birthday |
| 4    | `4_countdown_timer.py`        | Countdown timer in seconds |
| 5    | `5_date_difference.py`        | Calculates the number of days between two dates |
| 6    | `6_convert_12_to_24.py`       | Converts time from 12-hour to 24-hour format |
| 7    | `7_day_of_week.py`            | Returns the day of the week for a given date |
| 8    | `8_is_leap_year.py`           | Checks if a given year is a leap year |
| 9    | `9_add_subtract_days.py`      | Adds or subtracts days from a date |
| 10   | `10_month_calendar.py`        | Displays the calendar for a given month and year |
| 11   | `11_days_in_month.py`         | Returns number of days in a specified month |
| 12   | `12_time_until_new_year.py`   | Displays time remaining until New Year |
| 13   | `13_seconds_between_times.py` | Calculates seconds between two times |
| 14   | `14_date_past_or_future.py`   | Checks if a date is in the past, future, or today |
| 15   | `15_meeting_overlap.py`       | Checks if two meetings overlap in time |
| 16   | `16_iso_week_number.py`       | Gets the ISO week number for a given date |
| 17   | `17_string_date_conversion.py`| Converts between date strings and date objects |
| 18   | `18_time_zone_difference.py`  | Calculates the time difference between two time zones |
| 19   | `19_alarm_clock.py`           | Sets a simple alarm based on a specified time |
| 20   | `20_working_days.py`          | Counts the number of working days (Mon–Fri) between two dates |

---

## ▶️ Usage

### Run a Script
Each script is standalone. Use the terminal or command prompt:

```bash
python 5_date_difference.py
````

### Requirements

All scripts use standard Python libraries **except**:

* `18_time_zone_difference.py` requires `pytz`:

  ```bash
  pip install pytz
  ```

---

## 🧩 Folder Structure

```
date_time_practical/
│
├── 1_current_datetime.py
├── 2_age_calculator.py
├── ...
├── 20_working_days.py
└── README.md
```

---

## 📌 Notes

* Date inputs follow the format: `YYYY-MM-DD`
* Time inputs use either:

  * `HH:MM` (24-hour)
  * `HH:MM AM/PM` (12-hour)
* Scripts include validation and interactive prompts

---

## 👨‍💻 Author

Created by \Rao Shreepal

---

## 📝 License

This project is open-source and free to use under the [MIT License](LICENSE).



---

