import pandas as suraj

player_info = {'player_id': [1, 2, 3, 4, 5], 'name': ["sumeet", "balaji", "subham", "krushna", "raja"],
               "age": [21, 22, 23, 24, 25], "position": ["x", "y", "z", "w", "v"], 'team': ['j', 'k', 'l', 'm', 'n']}
df = suraj.DataFrame(player_info)
a = df.iloc(player_info['player_id'] == 4), ['name', 'age', 'position', 'team']
print(a)
