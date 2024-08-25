import sentiment_analysis
import json
import random

sentiment_analysis.download_lexicon()

# Importing sentences
with open('json_files/questions.json') as json_file:
    question_list = json.load(json_file)
with open('json_files/how_are_you_reactions.json') as json_file:
    how_are_you_reactions = json.load(json_file)
with open('json_files/continue_conversation_reactions.json') as json_file:
    continue_conversation_reactions = json.load(json_file)


def main():
    print("VADER Sentiment Analysis is ready for testing.")
    while True:
        how_are_you = input(random.choice(question_list["how_are_you"])+" (type 'exit' to quit): ")
        if how_are_you.lower() == 'exit':
            break
        
        sentiment_scores_q1 = sentiment_analysis.analyze_sentiment(how_are_you)
        print(f"Sentiment scores: {sentiment_scores_q1}")
        sentiment_class_q1 = sentiment_analysis.define_sentiment_class(sentiment_scores_q1)
        print(f"Sentiment class: {sentiment_class_q1}")
        print(sentiment_analysis.react_based_on_sentiment(sentiment_class_q1, how_are_you_reactions))
        
        continue_conversation = input(random.choice(question_list["is_it_ok_to_continue"])+" (type 'exit' to quit): ")
        if continue_conversation.lower() == 'exit':
            break
        
        sentiment_scores_q2 = sentiment_analysis.analyze_sentiment(continue_conversation)
        print(f"Sentiment scores: {sentiment_scores_q2}")
        sentiment_class_q2 = sentiment_analysis.define_sentiment_class(sentiment_scores_q2)
        print(f"Sentiment class: {sentiment_class_q2}")
        print(sentiment_analysis.react_based_on_sentiment(sentiment_class_q2, continue_conversation_reactions))

if __name__ == "__main__":
    main()
