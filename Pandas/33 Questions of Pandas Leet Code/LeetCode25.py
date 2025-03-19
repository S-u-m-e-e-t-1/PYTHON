import pandas as pd

orders_data = {
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3]
}

df = pd.DataFrame(orders_data)

print(df.groupby('customer_number')['order_number'].count().reset_index().rename(columns={'order_number': 'cnt'}).max())