import math
print("Enter three side of triangle")
a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))    
print("Area of triangle=",area)
print("perimeter of triangle=",a+b+c)