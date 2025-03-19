import pandas as pd

# Creating Students DataFrame
students = pd.DataFrame({
    'student_id': [1, 2, 13, 6],
    'student_name': ['Alice', 'Bob', 'John', 'Alex']
})

# Creating Subjects DataFrame
subjects = pd.DataFrame({
    'subject_name': ['Math', 'Physics', 'Programming']
})

# Creating Attendance DataFrame (assuming this data)
examinations = pd.DataFrame({
    'student_id': [1, 1, 2, 2, 13, 13, 6, 1, 2, 13, 1],
    'subject_name': ['Math', 'Physics', 'Math', 'Programming', 'Physics', 'Math', 'Programming', 'Math', 'Programming',
                     'Physics', 'Math']
})

examination_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

student_subject = pd.merge(students, subjects, how='cross')

result_df = pd.merge(student_subject, examination_count, on=['student_id', 'subject_name'], how='left')

# result_df = result_df[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(
#     by=['student_id', 'subject_name'])

# result_df['attended_exams'] = result_df['attended_exams'].fillna(0)

print(result_df)