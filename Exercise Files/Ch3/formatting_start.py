#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  now = datetime.now()
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("Year : %Y month : %m date : %d | is %a %d %B %A %b"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("%c | %x | %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("%I:%M:%S %p"))
  print(now.strftime("%H:%M"))

if __name__ == "__main__":
  main();
