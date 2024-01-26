import pandas as pd

# Write a solution to find the first login date for each player.

# Return the result table in any order.

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[['player_id', 'event_date']].sort_values('event_date')
    df = df.rename(columns = {'event_date': 'first_login'})
    
    return df.groupby('player_id')['first_login'].min().reset_index()
