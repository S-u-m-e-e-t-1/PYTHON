import pandas as pd

data = {
    "account_id": [3, 2, 8, 6],
    "income": [108939, 12747, 87709, 91796]
}
df = pd.DataFrame(data)

filtered_df = pd.DataFrame()

c1 = len(df[df["income"] < 20000])
c2 = len(df[(df["income"] >= 20000) & (df["income"] <= 50000)])
c3 = len(df[df["income"] > 50000])

filtered_df['low'] = [c1]
filtered_df['mid'] = [c2]
filtered_df['high'] = [c3]

# print(filtered_df)
print(type(c1))