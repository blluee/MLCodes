import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer and model 
with open('twitterProj/saved_models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = tf.keras.models.load_model('twitterProj/saved_models/sentiments_model.h5')

def predict_sentiment(tweet):
    new_sequence = tokenizer.texts_to_sequences([tweet])  # Tokenize the tweet
    new_padded_sequence = pad_sequences(new_sequence, maxlen=50, padding='post')  # Pad sequence

    # Get prediction probabilities
    prediction_probabilities = model.predict(new_padded_sequence)
    
    # Get the predicted class and confidence
    predicted_class = np.argmax(prediction_probabilities, axis=-1)[0]
    confidence = prediction_probabilities[0][predicted_class]
    
    sentiment_labels = {0: 'Negative', 1: 'Neutral', 2: 'positive'}
    
    return sentiment_labels[predicted_class], confidence
