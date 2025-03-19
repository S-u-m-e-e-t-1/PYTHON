"""Python Assignment 1
Find the sum of all even numbers and sum of odd numbers from 1 to a given number.

num = int(input("Enter a number: "))
i = 0
even_sum = 0
odd_sum = 0
while i <= num:
  if i % 2 == 0:
    even_sum += i
  else:
    odd_sum += i
  i += 1
print("Sum of even numbers is: ", even_sum)
print("Sum of odd numbers is: ", odd_sum)
"""

"""Python Assignment 2
Print the multiplication table of a given number

num = int(input("Enter a number: "))
i = 1
for i in range(11) :
  print(num, "x", i, "=", num * i)
  """

"""Python Assignment 3
 Count the total number of digits in a number and also print the sum of those digits.
 
num = int(input("Enter a number: "))
rem = 0
sum = 0
countdig = 0
while num > 0:
  rem = num % 10
  sum = sum + rem
  num = num // 10
  countdig+=1
print("Sum of digits is: ", sum)
print("Count of digits is: ", countdig)
   """

"""Python Assignment 4
 Check if the given string is a palindrome
 
str = input("Enter a string: ")
if str == str[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
    """
"""Python Assignment 5
Check if a given number is an Armstrong number

num = int(input("Enter a number: "))
remdig = 0
sum = 0
temp = num
while temp > 0:
  remdig = temp % 10
  sum += remdig ** 3
  temp //= 10
if num == sum:
  print(num, "is an Armstrong number")
else:
  print(num, "is not an Armstrong number")
"""
"""Python Assignment 6
 Display all numbers within a range except the prime numbers.
 
start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
              print(num)
              break
"""
"""Python Assignment 7
Accepts a string and calculates the number of digits and letters.

str = input("Enter a string: ")
digit = 0
letter = 0
for i in str:
   if i in range(0,9):
     digit += 1
   else:
     letter += 1
print("Number of digits is: ", digit)
print("Number of letters is: ", letter)
"""
"""Python Assignment 8
Print the below pattern:
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        
for i in range(1,6):
  for j in range(1,i+1):
    print(j, end=" ")
  print()
"""
"""Python Assignment 9
Print the below pattern:
        1 2 3 4 5
        1 2 3 4
        1 2 3 4
        1 2
        1
        
for i in range(5,0,-1):
  for j in range(1,i+1):
    print(j, end=" ")
  print()
"""
"""Python Assignment 10
Print the below pattern:            
                *
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
      * * * * * * * * * * *
   
rows = 6
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    for l in range(1, i):
        print("*", end="")
    print()
    """
"""Python Assignment 11. 
Print the below pattern:
    1 
    2 1 
    3 2 1 
    4 3 2 1 
    5 4 3 2 1
    
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    """
"""Python Assignment 12. 
Print the below pattern:
        1
        3 2
        6 5 4
        10 9 8 7

        num = 1
for i in range(1, 5):
    for j in range(i, 0, -1):
        print(num, end=" ")
        num += 1
    print()
"""
"""Python Assignment 13.
Print the below pattern:
              1 
            1 2 
          1 2 3 
        1 2 3 4 
      1 2 3 4 5
      
num = 1
for i in range(1, 5):
    for j in range(i, 0, -1):
        print(num, end=" ")
        num += 1
    print()
      """
"""Python Assignment 14. 
Print the below pattern:
        1  
        2  4  
        3  6  9  
        4  8  12  16  
        5  10  15  20  25  
        6  12  18  24  30  36  
        7  14  21  28  35  42  49  
        8  16  24  32  40  48  56  64
        
for i in range(1, 9):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
"""
"""Python Assignment 15.
Print the below pattern:
        * 
        * * 
        * * * 
        * * * * 
        * * * * *
        
for i in range(1, 6):
    print("* " * i)
"""
"""Python Assignment 16.
Print the below pattern:
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
        * * * * 
        * * * 
        * * 
        *

for i in range(1, 6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)
"""
"""Python Assignment 17.
Print all the combinations to generate 15 while roll 3 dices

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
"""Python Assignment 18.
Check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 8
Maximum length of transaction password: 20
import re
password = input("Enter a password: ")
flag = 0
while True:
    if (len(password) < 8or len(password) > 20):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[$#@]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
if flag == -1:
    print("Not a Valid Password")
"""
"""Python Assignment 19.
Take seven colors in a sequence. Check each color and comeout of the loop if the color is GREEN.

colors = ["RED", "GREEN", "BLUE", "YELLOW", "WHITE", "BLACK", "PERL"]
for color in colors:
    if color == "GREEN":
        print("We found the color we were looking for")

"""
"""Python Assignment 20. 
Find the factorial of a given number.

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
    
"""
"""Python Assignment 21. 
Create groups and add people to the groups. Check each persons and in the group and prin

group1 = ["John", "Jane", "Jim"]
group2 = ["Jack", "Jill", "Joe"]
group3 = ["Jessica", "Jess", "Jessy"]
person = input("Enter a person's name: ")
if person in group1:
    print(person, "is in group 1")
elif person in group2:
    print(person, "is in group 2")
elif person in group3:
    print(person, "is in group 3")
else:
    print(person, "is not in any group")

"""
"""Python Assignment 22.
Enter a string and print the whole except e and s

str = input("Enter a string: ")
new_str = ""
for i in str:
    if i != "e" and i != "s":
        new_str += i
print("New string is: ", new_str)

"""