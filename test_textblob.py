from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def main():
    print("TextBlob Sentiment Analysis is ready for testing.")
    while True:
        user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: Polarity={sentiment.polarity}, Subjectivity={sentiment.subjectivity}")

if __name__ == "__main__":
    main()
