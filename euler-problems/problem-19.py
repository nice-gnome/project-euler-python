"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime as dt

def sunday_count(start, end):
    sundays = 0
    current = start
    while current <= end:
        print(current.weekday())
        if current.weekday() == 6 and current.day == 1:
            sundays += 1
        current += dt.timedelta(1)
    return sundays

# solution
print(sunday_count(dt.date(1901, 1, 1), dt.date(2000, 12, 31)))