import pandas as suraj


data = {
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
    'salary': [3000, 3800, 7400, 6100, 7700]
}

df = suraj.DataFrame(data)
df['bonus'] = 0
df.loc[(df['employee_id'] % 2 != 0) & ~(df['name'].str.startswith('M')), 'bonus'] = df['salary']
print(df[['employee_id', 'bonus']])
