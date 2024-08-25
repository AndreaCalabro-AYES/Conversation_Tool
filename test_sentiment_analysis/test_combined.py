from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure that the VADER lexicon is downloaded
nltk.download('vader_lexicon')

def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def analyze_sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    return sentiment

def main():
    print("Combined Sentiment Analysis (TextBlob & VADER) is ready for testing.")
    while True:
        user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # Analyze sentiment using TextBlob
        tb_sentiment = analyze_sentiment_textblob(user_input)
        print(f"TextBlob Sentiment: Polarity={tb_sentiment.polarity}, Subjectivity={tb_sentiment.subjectivity}")

        # Analyze sentiment using VADER
        vader_sentiment = analyze_sentiment_vader(user_input)
        print(f"VADER Sentiment: {vader_sentiment}")

if __name__ == "__main__":
    main()
