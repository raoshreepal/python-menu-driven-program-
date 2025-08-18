from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

diff = abs((d2 - d1).days)
print("Difference in days:", diff)
# what is abs
# The abs() function returns the absolute value of a number, which means it converts negative values to positive.
# In this context, it ensures that the difference in days is always a non-negative value, regardless of the order of the dates entered.