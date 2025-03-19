import pandas as pd


data = {
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)


grouped = df.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index().rename(columns={'timestamp': 'cnt'})

# Find the row with the maximum count
max_row = grouped[grouped['cnt'] == grouped['cnt'].max()]

print(max_row)
