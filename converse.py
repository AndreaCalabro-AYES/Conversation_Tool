import stt
import numpy as np
import sounddevice as sd
from gpiozero import LED

# Initialize the GPIO control
led = LED(17)  # GPIO pin number

# Coqui STT setup
model_file_path = '/app/coqui-stt-model/model.tflite'  # Path to the model file
scorer_file_path = '/app/coqui-stt-model/large_vocabulary.scorer'  # Path to the scorer file

model = stt.Model(model_file_path)
model.enableExternalScorer(scorer_file_path)

# Function to listen and transcribe speech
def listen():
    led.on()  # Turn on the LED to indicate listening has started
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...", flush=True)
        audio_data = []
        while True:
            # Read from the audio stream
            data = stream.read(4000)
            audio_data.extend(data[0])
            
            # Check if enough data is collected to make a prediction
            if len(audio_data) >= 16000:
                # Convert the audio data to numpy array
                np_audio = np.array(audio_data, dtype=np.int16)
                text = model.stt(np_audio)
                
                if text:
                    print("You said:", text, flush=True)
                
                # Clear the audio data buffer after processing
                audio_data = []
    led.off()  # Turn off the LED when finished listening (if the loop ever breaks)

# Run the listening function
listen()
