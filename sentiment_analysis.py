import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

# Ensure that the VADER lexicon is downloaded
def download_lexicon():
    nltk.download('vader_lexicon')
    

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    return sentiment

def define_sentiment_class(sentiment_scores, VERY_THD= 0.75):
    # Extract the positive, negative, and neutral scores
    pos = sentiment_scores['pos']
    neu = sentiment_scores['neu']
    neg = sentiment_scores['neg']
    
    if (pos == neg) and (pos == neu) and (neg == neu):
        sentiment_class = "Unclear"
    elif pos >= VERY_THD:
        sentiment_class = "VeryPositive"
    elif neg >= VERY_THD:
        sentiment_class = "VeryNegative"
    elif neu >= VERY_THD:
        sentiment_class = "VeryNeutral"
    elif (pos >= neg) and (pos >= neu):
        sentiment_class = "Positive"
    elif (neg >= pos) and (neg >= neu):
        sentiment_class = "Negative"
    elif (neu >= pos) and (neu >= neg):
        if pos >= neg:
            sentiment_class = "NeutralPositive"
        else:
            sentiment_class = "NeutralNegative"
    else:
        sentiment_class = "Unclear"
    
    return sentiment_class

sentence_reaction = {
    "VeryPositive": ["This is fantastic!", "I'm thrilled too!", "Amazing!"],
    "Positive": ["This is good!", "I'm happy for you!", "Nice!"],
    "NeutralPositive": ["Okay, let's start.", "Not bad at all.", "I'm content with this."],
    "VeryNeutral": ["You are neutral.", "No strong feelings either way.", "Stay calm, you will find the flow."],
    "NeutralNegative": ["I'm not sure about this.", "It's a bit off.", "You have mixed feelings."],
    "Negative": ["This isn't great.", "You don't seem happy with this.", "Seems it could be better."],
    "VeryNegative": ["This is terrible!", "You're really disappointed.", "Awful!"],
    "Unclear": ["I don't understand.", "This is confusing.", "Can you clarify?"]
}

def react_based_on_sentiment(sentiment_class):
    # Ensure the sentiment class exists in the dictionary
    if sentiment_class in sentence_reaction:
        # Return a random sentence from the list associated with the sentiment class
        sentence = random.choice(sentence_reaction[sentiment_class])
    else:
        # Handle cases where the sentiment class is not found
        sentence = "I am sorry, I am still young and unexperienced."

    return sentence


    
    

