import pandas as suraj

# Creating the DataFrame for Views table
data = {
    'article_id': [1, 1, 2, 2, 4, 3, 3],
    'author_id': [3, 3, 7, 7, 7, 4, 4],
    'viewer_id': [5, 6, 7, 6, 1, 4, 4],
    'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
}

df = suraj.DataFrame(data)
df['view_date'] = suraj.to_datetime(df['view_date'])

for i in range(len(df)):
    if df['author_id'].iloc[i] == df['viewer_id'].iloc[i]:

        print(df['author_id'].iloc[i])


