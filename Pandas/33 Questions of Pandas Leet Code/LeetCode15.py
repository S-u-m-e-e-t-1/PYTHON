import pandas as pd

data = [
    {"id": 1, "email": "john@example.com"},
    {"id": 2, "email": "bob@example.com"},
    {"id": 3, "email": "john@example.com"},
]

df = pd.DataFrame(data)
df=df.drop_duplicates('email')
print(df)
# df.sort_values(by='id',ascending=True,inplace=True)
# # Drop the duplicates based on email.
# df.drop_duplicates(subset='email', keep='first', inplace=True)

