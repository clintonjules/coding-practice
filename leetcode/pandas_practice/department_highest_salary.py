import pandas as pd

# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, how='left', left_on='departmentId', right_on='id')
    dropped = merged[['name_y', 'name_x', 'salary']].rename(columns = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    grouped = dropped.groupby(['Department']).apply(lambda x: x[x['Salary'] == x['Salary'].max()])

    return grouped
