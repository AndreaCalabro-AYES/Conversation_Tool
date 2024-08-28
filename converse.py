import sounddevice as sd
import ctypes
import os

import os
# os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib/python3.9/site-packages/vosk:'

# Print the LD_LIBRARY_PATH to verify it's correctly set
print("LD_LIBRARY_PATH:", os.environ.get('LD_LIBRARY_PATH'), flush=True)

# Explicitly load the libvosk.so shared library
ctypes.cdll.LoadLibrary('/usr/local/lib/python3.9/site-packages/vosk/libvosk.so')

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
