import os

# Specify the directory where you want to create the files
directory = 'C:\\Users\\ASUS\\IdeaProjects\\DataAnalysis\\venv\\Pandas\\New folder'

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Create 30 files
for i in range(1, 35):
    file_path = os.path.join(directory, f'LeetCode{i}.py')
    with open(file_path, 'w') as file:
        file.write(f'This is Problem number {i}\n import pandas as pd ')

print('4 files created successfully')
