import pandas as suraj

employee = {'name': ['a', 'b', 'c', 'd', 'e'], 'sal': [123, 1234, 12345, 123456, 1234567]}
df = suraj.DataFrame(employee)
print(df)
df['sal'] = [1, 2, 3, 4, 5]
print(df)
