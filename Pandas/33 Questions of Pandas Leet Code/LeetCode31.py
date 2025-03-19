import pandas as pd

# Data for employees
employee_data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [None, 101, 101, 101, 101, 101]
}

# Create DataFrame
df = pd.DataFrame(employee_data)

# Group by managerId and count the number of employees
manager_counts = df.groupby('managerId').size().reset_index(name='employee_count')
report=manager_counts[manager_counts['employee_count'] >= 5]

# Display the result
print(df[df['id'].isin(report['managerId'])].fillna(0))
