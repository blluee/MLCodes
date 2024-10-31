# streamlit_app.py
import streamlit as st
import credentials
import model
from data_cleaning import clean_tweet
import matplotlib.pyplot as plt
import pandas as pd

# Function to plot sentiment trends
def plot_sentiment_trends(sentiment_data):
    # Convert the sentiment data to a DataFrame
    df = pd.DataFrame(sentiment_data)
    
    # Count sentiment occurrences
    sentiment_counts = df['sentiment'].value_counts().reindex(['looking bad', 'Neutral', 'sounding good'], fill_value=0)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=['red', 'yellow', 'green'])
    plt.title("Sentiment Trends Over Days")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot(plt)

# Set the title of the Streamlit app
st.title("Sentiment Analysis Dashboard")

# User input for tweets
user_input = st.text_area("Enter a tweet or text to analyze:", "")

# Button to analyze the sentiment
if st.button("Analyze"):
    if user_input:  # Check if the user has entered any text
        # Clean the user input
        cleaned_tweet = clean_tweet(user_input)

        # Predict sentiment using the model
        sentiment, confidence = model.predict_sentiment(cleaned_tweet)

        # Display the results
        st.write(f"**Tweet:** {cleaned_tweet}")
        st.write(f"**Sentiment:** {sentiment} with {confidence * 100:.2f}% confidence")
    else:
        st.warning("Please enter a tweet or text.")

# Optional: Add functionality to fetch tweets based on a search term
search_term = st.text_input("Search for tweets on Twitter:")
if st.button("Fetch Tweets"):
    if search_term:  # Check if the user has entered a search term
        tweets = credentials.get_tweets(query=search_term, count=5)
        st.write("**Fetched Tweets:**")
        
        # Placeholder for sentiment data
        sentiment_data = []

        for tweet in tweets:
            st.write(tweet)
            # Clean and analyze each fetched tweet
            cleaned_tweet = clean_tweet(tweet)
            sentiment, confidence = model.predict_sentiment(cleaned_tweet)
            sentiment_data.append({'tweet': cleaned_tweet, 'sentiment': sentiment})

        # If there are sentiment data, plot trends
        if sentiment_data:
            plot_sentiment_trends(sentiment_data)

    else:
        st.warning("Please enter a search term.")
