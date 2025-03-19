""" transpose of an matrix
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        y[j][i]=x[i][j]
for r in y:
    print(r)
"""
"""
1. Write a menu driven program to convert the given temperature from Fahrenheit to Celsius value 1 and vice versa value 2 depending upon users’ choice.
choice=int(input("Enter your choice: "))
if choice==1:
    temp=int(input("Enter the temperature in Fahrenheit: "))
    celsius=(temp-32)*5/9
    print("Temperature Celsius:",celsius)
elif choice==2:
    temp=int(input("Enter the temperature in Celsius: "))
    fahrenheit=(temp*9/5)+32
    print("Temperature Fahrenheit:",fahrenheit)
"""
"""
2. Write a Program to calculate total marks, percentage and grade of a student. Marks obtained in each of the three subjects are to be input by the user. Assign grades according to the following criteria:
Grade A: Percentage >=80
Grade B: Percentage>=70 and <80 Grade C: Percentage>=60 and <70 Grade D: Percentage>=40 and <60 Grade E: Percentage<40
li=[]
sum=0
avg=0
for i in range(6):
    marks=int(input("Enter the marks: "))
    li.append(marks)
    sum+=marks
avg=sum/6
if avg>=80:
    print("Grade A")
elif avg>=70 and avg<80:
    print("Grade B")
elif avg>=60 and avg<70:
    print("Grade C")
elif avg>=40 and avg<60:
    print("Grade D")
else:
    print("Grade E")

"""
"""
3. Write a menu-driven program, using user-defined functions to find the area of rectangle, square, circle and triangle by accepting suitable input parameters from user.
"""
"""
4. Write a Program to display the first n terms of Fibonacci series.
num=int(input("Enter the number of terms: "))
n1,n2=0,1
count=0
if num<=0:
    print("Please enter a positive integer")
elif num==1:
    print("Fibonacci sequence upto",num,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
"""
"""
5. Write a Program to find factorial of the given number.
num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)
"""
"""
6. Write a Program to find sum of the following series for n terms: 1 – 2/2! + 3/3! -------- n/n!
sum=0
n=int(input("Enter the number:"))
for i in range(1,n+1):
  fact=1
  for j in range(1,i+1):
    fact=fact*j
  sum=sum+i/fact
print(sum)
"""
"""
7. Write a Program to calculate the sum and product of two compatible matrices.
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
sum=[[0,0,0],[0,0,0],[0,0,0]]
product=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        sum[i][j]=x[i][j]+y[i][j]
print("Sum of the matrices:")
for r in sum:
    print(r)
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            product[i][j] += x[i][k] * y[k][j]
print("Product of the matrices:")
for r in product:
    print(r)

"""