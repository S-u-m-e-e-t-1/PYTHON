
import pandas as pd

# Create a DataFrame
data = {
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

df = pd.DataFrame(data)


df['rank'] = df['score'].rank(method='dense', ascending=False).astype(int)


df_sorted = df.sort_values(by='score', ascending=False)

# Display the result
print(df_sorted)

