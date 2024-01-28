import pandas as pd

# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

# Return the result table in any order.

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    ad = actor_director.drop(columns = ['timestamp'])
    ad = ad.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')


    return ad.loc[ad['cooperation_count'] >= 3, ['actor_id', 'director_id']]
