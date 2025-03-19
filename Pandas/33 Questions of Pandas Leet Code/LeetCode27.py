import pandas as pd

# Creating the DataFrame
data = {
    'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7',
                '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
    'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota',
                  'honda', 'honda', 'honda', 'honda', 'honda'],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
}

df = pd.DataFrame(data)
print(df.groupby(['date_id', 'make_name']).agg(
    count=('date_id', 'size'),
    lead_ids=('lead_id', lambda x: ', '.join(x.astype(str))),
    partner_ids=('partner_id', lambda x: ', '.join(x.astype(str)))
).reset_index())