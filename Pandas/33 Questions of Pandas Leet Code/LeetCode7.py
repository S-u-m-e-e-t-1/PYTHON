import pandas as pd


data = {
    'user_id': [1, 2],
    'name': ['aLice', 'bOB']
}

df = pd.DataFrame(data)


df['name'] = df['name'].str.title()


print(df)
