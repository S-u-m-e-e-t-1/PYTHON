import pandas as pd
data = {
    'id': [1, 2, 3,4,5],
    'salary': [100,900, 200,800, 300]
}
df = pd.DataFrame(data)
a=df['salary'].tolist()
a.sort()
print(a[0])
