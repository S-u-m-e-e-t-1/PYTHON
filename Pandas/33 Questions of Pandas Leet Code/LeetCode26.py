import pandas as pd

data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
}

df = pd.DataFrame(data)

print(df.groupby('sell_date')['product'].count().reset_index().rename(columns={'product':'cnt'}))
# print(df.groupby('sell_date').agg(
#     cnt=('product', 'count'),
#     products=('product', lambda x: ', '.join(x))
# ).reset_index())