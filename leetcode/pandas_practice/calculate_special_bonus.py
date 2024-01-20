import pandas as pd

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0

    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M'), ['bonus']] = employees['salary']

    return employees[['employee_id', 'bonus']].sort_values('employee_id')
