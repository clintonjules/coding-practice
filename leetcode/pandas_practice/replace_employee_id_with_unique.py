import pandas as pd

# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

# Return the result table in any order.

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, employee_uni, how='left', on='id')

    return merged.drop(columns = ['id'])
