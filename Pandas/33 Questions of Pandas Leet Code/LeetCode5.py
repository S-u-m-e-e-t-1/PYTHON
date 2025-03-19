import pandas as suraj

data = {
    'tweet_id': [1, 2],
    'content': [
        'Vote for Biden',
        'Let us make America great again!'
    ]
}

df = suraj.DataFrame(data)
for i in range(len(df)):
    if len(df['content'].iloc[i])>15 :
        print(df['tweet_id'].iloc[i])
