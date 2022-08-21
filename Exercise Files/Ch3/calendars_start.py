#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st= c.formatmonth(2022, 8, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
htmlcal=hc.formatmonth(20222,8)
print(htmlcal)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
cal = calendar.TextCalendar(calendar.SUNDAY)
for i in cal.itermonthdays(2022,8):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meeting will be every Friday on the first week of the month : ")
for m in range(1,13):
    calen = calendar.monthcalendar(2022, m)
    weekone=calen[0]
    weektwo=calen[1]

    if weekone[calendar.SUNDAY] != 0:
        meetday = weekone[calendar.SUNDAY]
    else:
        meetday = weektwo[calendar.SUNDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))