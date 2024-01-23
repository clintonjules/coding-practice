import pandas as pd

# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates()

    sorted_sal = unique.sort_values(ascending=False)

    if len(sorted_sal) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    nth = sorted_sal.iloc[1]

    return pd.DataFrame({'SecondHighestSalary': [nth]})
