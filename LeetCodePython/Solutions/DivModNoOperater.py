def divmod(a, b):
  q = 0
  r = 0
  while a >= b:
    a -= b
    q += 1
  r = a
  return q, r


a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
print(divmod(a, b))
