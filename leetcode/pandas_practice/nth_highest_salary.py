import pandas as pd

# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates()

    sorted_sal = unique.sort_values(ascending=False)

    if N > len(sorted_sal) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    nth = sorted_sal.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [nth]})
