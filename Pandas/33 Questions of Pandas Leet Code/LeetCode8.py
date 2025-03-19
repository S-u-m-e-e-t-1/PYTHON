import pandas as pd
import re


data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
    'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']
}

df = pd.DataFrame(data)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0]+[a-zA-Z0-9._%+-]+@leetcode+\.[a-zA-Z]'
    return re.match(pattern, email) is not None


df['valid_email'] = df['mail'].apply(is_valid_email)


valid_emails_df = df[df['valid_email'] == True]

print(valid_emails_df)
