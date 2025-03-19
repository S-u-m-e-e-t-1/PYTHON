import pandas as pd

# Creating the Employees DataFrame
employees_data = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}

employees_df = pd.DataFrame(employees_data)

# Creating the EmployeeUNI DataFrame
employee_uni_data = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}

employee_uni_df = pd.DataFrame(employee_uni_data)

print(pd.merge(employees_df,employee_uni_df,on='id',how="left"))