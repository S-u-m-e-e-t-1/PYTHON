a=int(input("a="))
s=0
r=0
a1=a
while a!=0:
 r=a%10
 s+=r
 a//=10
print(s)
