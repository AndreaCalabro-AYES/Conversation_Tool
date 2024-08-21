import pandas as pd
import re

# Load datasets
eng_dataset = pd.read_csv('C:/internal_project/MM_Internal_Project/Conversation_Tool/train_data_sentiment_analysis/eng_dataset.csv')
imdb_dataset = pd.read_csv('C:/internal_project/MM_Internal_Project/Conversation_Tool/train_data_sentiment_analysis/IMDB Dataset.csv')
sentiment_analysis = pd.read_csv('C:/internal_project/MM_Internal_Project/Conversation_Tool/train_data_sentiment_analysis/sentiment_analysis.csv')
train_set = pd.read_csv('C:/internal_project/MM_Internal_Project/Conversation_Tool/train_data_sentiment_analysis/Train_set.txt', sep=";", header=None, names=["text", "emotion"])

# Cleaning function
def clean_text(text):
    text = text.lower()  # convert to lowercase
    text = re.sub(r'\[.*?\]', '', text)  # remove text in brackets
    text = re.sub(r'http\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation and numbers
    text = text.strip()  # remove leading/trailing whitespace
    return text

# Apply cleaning
eng_dataset['text'] = eng_dataset['content'].apply(clean_text)
imdb_dataset['text'] = imdb_dataset['review'].apply(clean_text)  # assuming 'review' is the text column
sentiment_analysis['text'] = sentiment_analysis['text'].apply(clean_text)
train_set['text'] = train_set['text'].apply(clean_text)

print(eng_dataset.columns)

# Mapping for binary sentiment (positive/negative)
def map_sentiment(label):
    return 'positive' if label in ['positive', 'joy', 'love'] else 'negative'

imdb_dataset['sentiment'] = imdb_dataset['sentiment'].apply(map_sentiment)
eng_dataset['sentiment'] = eng_dataset['sentiment'].apply(map_sentiment)
train_set['sentiment'] = train_set['emotion'].apply(map_sentiment)

# For emotion classification
# We map emotions to four categories: joy, sadness, anger, fear
def map_emotion(emotion):
    mapping = {
        'joy': 'joy',
        'sadness': 'sadness',
        'anger': 'anger',
        'fear': 'fear',
        'surprise': 'surprise',  # optional, could map to joy or another emotion
        'disgust': 'anger',  # optional, could map to anger
        # Add more mappings as needed based on your emotion categories
    }
    return mapping.get(emotion, 'neutral')  # 'neutral' for emotions not in the mapping

# train_set['emotion'] = train_set['emotion'].apply(map_emotion)

# For the other datasets, you may have to create similar mappings depending on how emotions are labeled

# Merge datasets
# Assuming that for sentiment analysis, 'sentiment' is the label, and for emotion classification, 'emotion' is the label
merged_dataset = pd.concat([
    imdb_dataset[['text', 'sentiment']],  # binary sentiment
    sentiment_analysis[['text', 'sentiment']],
    train_set[['text', 'sentiment']],
    eng_dataset[['text', 'sentiment']]  # needs appropriate labeling
], ignore_index=True)

# Save the cleaned and merged dataset
merged_dataset.to_csv('merged_dataset.csv', index=False)

print("Merged dataset saved to 'merged_dataset.csv'")