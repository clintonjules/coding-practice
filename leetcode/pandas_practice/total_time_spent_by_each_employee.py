import pandas as pd

# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

# Return the result table in any order.

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees.out_time - employees.in_time
    dropped = employees.drop(columns = ['in_time', 'out_time']).rename(columns = {'event_day':'day'})

    dropped = dropped[['day', 'emp_id', 'total_time']]

    return dropped.groupby(['day','emp_id']).sum().reset_index()
