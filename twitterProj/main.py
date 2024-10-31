import credentials
import model
import data_cleaning

def main():
    # Get tweets from Twitter
    tweets = credentials.get_tweets()  # Assume this function retrieves tweets

    # Analyze sentiment for each tweet
    for tweet in tweets:
        cleaned_tweet = data_cleaning.clean_tweet(tweets)
        sentiment, confidence = model.predict_sentiment(cleaned_tweet)
        print(f'Tweet: {cleaned_tweet}\nSentiment: {sentiment} with {confidence * 100:.2f}% confidence\n')

if __name__ == "__main__":
    main()
