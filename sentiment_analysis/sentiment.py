import numpy as np
import re
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import streamlit as st
import random

# load tokenizer 
with open('sentiment analysis/saved_models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load saved model 
model = tf.keras.models.load_model('sentiment analysis/sentiments_model.h5')

# Function to clean the input text
def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    return tweet

# Streamlit App
st.title('Sentiment Analysis AI')
st.write("Enter a sentence below, and this AI will predict its sentiment!")

# Get user input
user_input = st.text_input("Enter a sentiment:")
if user_input:
    # Clean and preprocess input
    new_tweet_cleaned = [clean_tweet(user_input)]
    new_sequence = tokenizer.texts_to_sequences(new_tweet_cleaned)
    new_padded_sequence = pad_sequences(new_sequence, maxlen=50, padding='post')
    
    # Get prediction
    prediction_probabilities = model.predict(new_padded_sequence)
    predicted_class = np.argmax(prediction_probabilities, axis=-1)[0]
    confidence = prediction_probabilities[0][predicted_class]
    sentiment_labels = {0: 'looking bad', 1: 'Neutral', 2: 'sounding good'}

    # Confidence levels for output
    if confidence > 0.85:
        sentence_starters = [
            "I am sure this news is", 
            "Without a doubt, this news is", 
            "I can confidently say this news is"
        ]
    elif 0.60 < confidence <= 0.85:
        sentence_starters = [
            "This news seems to be", 
            "It is likely this news is", 
            "I am fairly sure this news is"
        ]
    else:
        sentence_starters = [
            "This news might be", 
            "After scanning, it could be that this news is", 
            "I am not entirely sure, but this news appears to be"
        ]

    selected_sentence = random.choice(sentence_starters)
    st.write(f"{selected_sentence} {sentiment_labels[predicted_class]} with {confidence * 100:.2f}% confidence level.")
