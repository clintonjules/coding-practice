import pandas as pd
# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.loc[views['author_id'] == views['viewer_id'], ['viewer_id']]

    return views.drop_duplicates().rename(columns = {'viewer_id': 'id'}).sort_values('id', ascending=True)
