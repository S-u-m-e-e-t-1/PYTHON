
import pandas as pd

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}
df = pd.DataFrame(data)
n = 2
df_sorted = df.sort_values(by='salary', ascending=False)
nth_highest_salary = df_sorted.iloc[n-1]['salary']


result_df = pd.DataFrame({'getNthHighestSalary({})': [nth_highest_salary]})
print(result_df)
