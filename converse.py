import sounddevice as sd
import vosk
import numpy as np
from gpiozero import LED
import json

# Initialize the GPIO control
led = LED(17)  # GPIO pin number

# Load the Vosk model
model = vosk.Model("/app/vosk-model")  # Ensure the model is correctly located in /app/vosk-model
recognizer = vosk.KaldiRecognizer(model, 16000)

# Function to listen and transcribe speech
def listen():
    led.on()  # Turn on the LED to indicate listening has started
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...", flush=True)
        while True:
            # Read from the audio stream
            data = stream.read(4000)
            
            # Check if enough data is collected to make a prediction
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get('text', '')
                
                if text:
                    print("You said:", text, flush=True)
                    
            # Optionally, clear the buffer or manage continuous listening here
    led.off()  # Turn off the LED when finished listening (if the loop ever breaks)

# Run the listening function
listen()
