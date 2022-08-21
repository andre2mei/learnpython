#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  print ("Today's date is ", today)
 
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class


  # print out the date's individual components
  print("Date component ", today.year, today.month, today.day)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Date index today is : ", today.weekday())
  days=["mon","tue","wed","thu","fri","sat","sun"]
  print("Today's day is : ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("date and time today", datetime.now())
  
  # Get the current time
  print("Print time only : ", datetime.time(datetime.now()))

 

  
if __name__ == "__main__":
  main();
  