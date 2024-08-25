import os
import sys
import queue
import sounddevice as sd
import vosk
import pyttsx3
import json
import random
from sentiment_analysis import download_lexicon, analyze_sentiment, define_sentiment_class, react_based_on_sentiment

# Importing sentences
with open('json_files/questions.json') as json_file:
    question_list = json.load(json_file)
with open('json_files/how_are_you_reactions.json') as json_file:
    how_are_you_reactions = json.load(json_file)
with open('json_files/continue_conversation_reactions.json') as json_file:
    continue_conversation_reactions = json.load(json_file)

# Initialize Vosk model for STT
vosk.SetLogLevel(-1)  # Suppress Vosk logs
model = vosk.Model("model")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate if needed

# Keyword to stop the chatbot
STOP_KEYWORD = "stop"

# Function to perform TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to perform STT
def recognize_speech():
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening... (Say 'stop' to exit)")
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result)["text"]
                if text:
                    return text

# Main loop to handle STT -> Sentiment Analysis -> TTS
def main():
    # Download the VADER lexicon
    download_lexicon()

    while True:
        try:
            
            # First question - how are you
            speak(random.choice(question_list["how_are_you"]))
            print("Please, say STOP to end the conversation")
            
            # Perform Speech-to-Text (STT)
            recognized_text = recognize_speech()
            print(f"You said: {recognized_text}")

            # Check if the STOP_KEYWORD is in the recognized text
            if STOP_KEYWORD in recognized_text.lower():
                speak("Goodbye!")
                print("Stopping the chatbot.")
                break

            # Analyze sentiment
            sentiment_scores = analyze_sentiment(recognized_text)
            sentiment_class = define_sentiment_class(sentiment_scores)

            # Get reaction based on sentiment
            response_text = react_based_on_sentiment(sentiment_class, how_are_you_reactions)
            print(f"Bot says: {response_text}")

            # Perform Text-to-Speech (TTS)
            speak(response_text)
            
            
            # Second question - OK to continue chatting
            speak(random.choice(question_list["is_it_ok_to_continue"]))
            
            # Perform Speech-to-Text (STT)
            recognized_text = recognize_speech()
            print(f"You said: {recognized_text}")

            # Check if the STOP_KEYWORD is in the recognized text
            if STOP_KEYWORD in recognized_text.lower():
                speak("Goodbye!")
                print("Stopping the chatbot.")
                break

            # Analyze sentiment
            sentiment_scores = analyze_sentiment(recognized_text)
            sentiment_class = define_sentiment_class(sentiment_scores)

            # Get reaction based on sentiment
            response_text = react_based_on_sentiment(sentiment_class, how_are_you_reactions)
            print(f"Bot says: {response_text}")

            # Perform Text-to-Speech (TTS)
            speak(response_text)
            

        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
