def inc(a,b=1):
    return(a+b)
a=inc(1)
#2
a=inc(a,a)
#a is 2 and a+a = 4
print(a)

print("=================")

x=1
y=2

max=x if (x>y) else y
print(max)

if (x>=y):
    max=x
else:
    max=y
print(max)


print("=================")
number=0
if (number<10000):
  print(4)
elif (number<1000):
  print(3)
elif (number<10):
  print(2)
else:
  print(1)

if (number<=10):
  print(1)
elif (number<=100):
  print(2)
elif (number<=1000):
  print(3)
else:
  print(4)

if (number>=1000):
  print(4)
elif (number>=100):
  print(3)
elif (number>=10):
  print(2)
else:
  print(1)


def Sum10th(data):
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0): sum=sum+d
  return sum
print(Sum10th())