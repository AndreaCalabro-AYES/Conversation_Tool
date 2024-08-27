import pyttsx3
import sounddevice as sd
import vosk
from gpiozero import LED
import json

# Initialize the TTS engine
engine = pyttsx3.init()

# Example GPIO control
led = LED(17)  # GPIO pin number

# Function to speak text
# def speak(text):
#     led.on()  # Turn on the LED when speaking
#     engine.say(text)
#     engine.runAndWait()
#     led.off()  # Turn off the LED after speaking

# Vosk setup
model = vosk.Model("/app/vosk-model")  # Ensure the model is copied to /app
recognizer = vosk.KaldiRecognizer(model, 16000)

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...", flush=True)
        while True:
            data = stream.read(4000)
            if recognizer.AcceptWaveform(data[0]):
                result = json.loads(recognizer.Result())
                print("You said:", result['text'], flush=True)

# Test functions
# speak("Hello, this is a test from Docker container.")
listen()
