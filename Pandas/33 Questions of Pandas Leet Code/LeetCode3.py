import pandas as suraj


customers_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}

orders_data = {
    'id': [1, 2],
    'customerId': [3, 1]
}

customers_df = suraj.DataFrame(customers_data)
orders_df = suraj.DataFrame(orders_data)

l1=customers_df['id'].tolist()
l2=orders_df['customerId'].tolist()

print([item for item in l1 if item in l2])