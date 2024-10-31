import re

def clean_tweet(tweet):
    if isinstance(tweet, str):  # Check if tweet is a string
        tweet = tweet.lower()  # Lowercase the text
        tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)  # Remove URLs
        tweet = re.sub(r'\@\w+|\#', '', tweet)  # Remove mentions and hashtags
        # Add any other cleaning steps you want here
    else:
        tweet = ''  # Handle non-string input as needed
    return tweet
