import sentiment_analysis

sentiment_analysis.download_lexicon()

def main():
    print("VADER Sentiment Analysis is ready for testing.")
    while True:
        user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        sentiment_scores = sentiment_analysis.analyze_sentiment(user_input)
        print(f"Sentiment scores: {sentiment_scores}")
        sentiment_class = sentiment_analysis.define_sentiment_class(sentiment_scores)
        print(f"Sentiment class: {sentiment_class}")
        print(sentiment_analysis.react_based_on_sentiment(sentiment_class))

if __name__ == "__main__":
    main()
