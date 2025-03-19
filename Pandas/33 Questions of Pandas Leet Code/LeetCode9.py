import pandas as suraj

# Create a DataFrame
data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
    'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}

df = suraj.DataFrame(data)
df['diab'] = df['conditions'].str.contains("DIAB1")
df_diab = df[df['diab'] == True]
print(df_diab)
