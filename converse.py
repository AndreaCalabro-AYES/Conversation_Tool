from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import sounddevice as sd
import numpy as np
from gpiozero import LED

# Initialize the GPIO control
led = LED(17)  # GPIO pin number

# Load the Wav2Vec2 model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

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
                np_audio = np.array(audio_data, dtype=np.float32) / 32768.0  # Normalize audio to [-1, 1]
                
                # Process the audio data
                inputs = processor(np_audio, sampling_rate=16000, return_tensors="pt", padding=True)
                with torch.no_grad():
                    logits = model(inputs.input_values).logits
                
                # Decode the predicted text
                predicted_ids = torch.argmax(logits, dim=-1)
                text = processor.batch_decode(predicted_ids)[0]
                
                if text:
                    print("You said:", text, flush=True)
                
                # Clear the audio data buffer after processing
                audio_data = []
    led.off()  # Turn off the LED when finished listening (if the loop ever breaks)

# Run the listening function
listen()
