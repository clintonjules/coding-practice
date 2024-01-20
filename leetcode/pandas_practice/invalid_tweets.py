import pandas as pd

# Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Return the result table in any order.

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets.loc[tweets['content'].apply(len) > 15, ['tweet_id']]

    return tweets
