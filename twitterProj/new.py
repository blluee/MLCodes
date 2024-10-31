import tweepy
import time
# Replace with your own credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPLMwgEAAAAAbcXoEfUHFaOo%2FNg3Af37t9JYar8%3DJM9MeDGlB5QhnqSAgr23ArUkRTOW1oLnTTjxjq6ihlN5rjT29p'

client = tweepy.Client(bearer_token=bearer_token)


def get_openai_tweets(max_results=5):
    try:
        user = client.get_user(username='OpenAI')
        user_id = user.data.id
        response = client.get_users_tweets(id=user_id, max_results=max_results)

        if response.data:
            for tweet in response.data:
                print(tweet.text)
        else:
            print("No tweets found for OpenAI.")
    except tweepy.TooManyRequests:
        print("Rate limit exceeded. Waiting for 15 minutes...")
        time.sleep(15 * 60)  # Sleep for 15 minutes
        get_openai_tweets(max_results)  # Retry fetching tweets

get_openai_tweets(max_results=5)