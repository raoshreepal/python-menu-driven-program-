# 15_meeting_overlap.py
from datetime import datetime

def main():
    start1 = input("Enter Meeting 1 start time (HH:MM): ")
    end1 = input("Enter Meeting 1 end time (HH:MM): ")
    start2 = input("Enter Meeting 2 start time (HH:MM): ")
    end2 = input("Enter Meeting 2 end time (HH:MM): ")

    s1 = datetime.strptime(start1, "%H:%M")
    e1 = datetime.strptime(end1, "%H:%M")
    s2 = datetime.strptime(start2, "%H:%M")
    e2 = datetime.strptime(end2, "%H:%M")

    if s1 < e2 and s2 < e1:
        print("Meetings overlap.")
    else:
        print("Meetings do not overlap.")

if __name__ == "__main__":
    main()
# This script checks if two meeting times overlap.
# It uses the datetime module to convert the meeting times to datetime objects and then compares them to determine if they 
# overlap.
# The input should be in the format "HH:MM", and the output will indicate whether the meetings overlap or not.
# If the start time of one meeting is before the end time of the other meeting, they overlap.