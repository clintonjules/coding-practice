import pandas as pd

# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# Return the result table ordered by user_id.

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()

    return users.sort_values('user_id')
