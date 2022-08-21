# 
# Example file for variables
#

# Declare a variable and initialize it
f=1
print(f)


# re-declaring the variable works
f="abc"
print(f)


# ERROR: variables of different types cannot be combined
print("this is a string " + str(123))
print("this is a string " + "1243")

# Global vs. local variables in functions
var = 0

def someFunction():
    global var
    var="abc"
    print(f)
    
someFunction()
print(var)

#del f
#print(f)