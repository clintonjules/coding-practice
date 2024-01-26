import pandas as pd

# Write a solution to calculate the number of unique subjects each teacher teaches in the university.

# Return the result table in any order.

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.drop(columns = ['dept_id'])
    df = df.groupby('teacher_id')['subject_id'].nunique().reset_index()

    return df.rename(columns = {'subject_id': 'cnt'})
