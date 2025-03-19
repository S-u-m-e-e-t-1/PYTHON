a=int(input("a="))
s=0
r=0
a1=a
while a!=0:
 r=a%10
 s=s*10+r
 a//=10
if s==a1:
 print(a1,"is palindrome")
else:
 print(a1,"is not palindrome")
