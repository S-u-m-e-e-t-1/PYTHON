import pandas as pd

# Creating the dataframe
data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}

df = pd.DataFrame(data)
cf1=df.groupby('class')['student'].count().reset_index()

print(cf1[cf1['student']>=5][['class']])
