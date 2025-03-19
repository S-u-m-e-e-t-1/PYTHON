import pandas as suraj

data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

df = suraj.DataFrame(data)

print(df[df['weight']>100].sort_values(by='weight',ascending=False)[['name']])
