import pandas as pd

# Creating the dataframe
data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Display the dataframe
print(df.groupby('teacher_id')['subject_id'].nunique())
