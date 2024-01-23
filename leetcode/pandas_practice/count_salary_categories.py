import pandas as pd

# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.

# Return the result table in any order.

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts.loc[accounts['income'] < 20000, ['income']]
    avg = accounts.loc[(accounts['income'] >= 20000) & (accounts['income'] < 50000), ['income']]
    high = accounts.loc[accounts['income'] > 50000, ['income']]


    return pd.DataFrame({'category': ['High Salary','Average Salary','Low Salary'], 'accounts_count': [len(high), len(avg), len(low)]})
