#
# Example file for working with loops
#

def main():
  x = 1

  # define a while loop
  # while (x <= 5):
  #   print(x)
  #   x = x+1

  # define a for loop
  # for i in range (1,10):
  #   print(i)

  # use a for loop over a collection
  days=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
  for i in days:
    print(i)
  
  # use the break and continue statements


  #using the enumerate() function to get index 
  days=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
  for i, d in enumerate(days):
    print(i, d)

if __name__ == "__main__":
  main()
