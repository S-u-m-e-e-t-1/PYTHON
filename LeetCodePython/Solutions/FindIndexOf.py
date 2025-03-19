def findIndexOf(a,b):
  j=0
  for i in range(len(a)):
    if a[i]==b[0]:
      while j<len(b):
        if a[i+j]==b[j]:
          j+=1
        else:
          break
      if j==len(b):
        return i+1
  return -1
a=input("Enter the string: ")
b=input("Enter the substring: ")
print(findIndexOf(a,b))
  