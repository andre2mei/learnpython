#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=25,hours=6, minutes=25))

# print today's date
now = datetime.now()
print("Today is : ", str(now))

# print today's date one year from now
print("One year from now will be : ", str(now+timedelta(days=360)))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
tformated=t.strftime("%A, %B %d, %Y")
print("One week ago is : ", tformated)

### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

