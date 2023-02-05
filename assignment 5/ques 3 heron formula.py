import math
a=int(input("enter the side a of triangle"))
b=int(input("enter the side b of triangle"))
c=int(input("enter the side c of triangle"))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(x)
print(area)