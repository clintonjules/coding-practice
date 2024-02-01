import pandas as pd

# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values('score', ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    return scores.drop(columns = ['id'])
