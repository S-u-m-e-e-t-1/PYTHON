import pandas as suraj

costumer = {'id': [1, 2, 3, 4, 5, 6], 'name': ['a', 'b',None , 'd', 'e', 'f'],
            'email': ["abc@gmail.com", "abcd@gmail.com", "abc@gmail.com", "abcde@gmail.com", "abcdef@gmail.com",
                      "abcd@gmail.com", ]}
df = suraj.DataFrame(costumer)
print(df.dropna(subset=['name']).drop_duplicates(subset=['email']))
