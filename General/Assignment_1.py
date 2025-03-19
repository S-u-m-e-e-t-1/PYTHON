"""Python assignment 1.1
limit = int(input("Enter the limit: "))
x=0
y=1
i=0
sum=0
print(x,y,end=",")
while (sum<=limit):
  sum=x+y
  x=y
  y=sum
  print(sum,end=',')"""

"""Python assignment 1.3
dice1 = 1
while dice1 <= 6:
    dice2 = 1
    while dice2 <= 6:
        dice3 = 1
        while dice3 <= 6:
            if dice1 + dice2 + dice3 == 15:
                print((dice1, dice2, dice3))
            dice3 += 1
        dice2 += 1
    dice1 += 1
"""
"""Python assignment 1.4
number = int(input("Enter a number: "))
sum = 0
while number > 0:
  sum=sum*10+number%10
  number=number//10
print("Reversed number is: ",sum)
"""
"""Python assignment 1.5"""
number = int(input("Enter a number: "))
sum = 0
temp = number
while temp > 0:
  sum=sum*10+temp%10
  temp //= 10
if number == sum:
  print("The number is a palindrome")
else:
  print("The number is not a palindrome")
