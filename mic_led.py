from gpiozero import LED
import pyaudio
import numpy as np
import time

# Define GPIO pins
ledPin = 17

# Initialize LED
led = LED(ledPin)

# Setup PyAudio
CHUNK = 1024  # Number of audio samples per buffer
RATE = 44100  # Sampling rate

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def detect_sound(threshold=1000):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data))
    print(f"Detected peak: {peak}", flush=True)
    return peak > threshold

def loop():
    print("Entering main loop...", flush=True)
    while True:
        print("Listening for sound...", flush=True)
        if detect_sound():
            print("Sound detected!", flush=True)
            led.on()
            print("LED turned ON", flush=True)
        else:
            print("No sound detected", flush=True)
            led.off()
            print("LED turned OFF", flush=True)
        time.sleep(0.1)
        print("Loop iteration completed", flush=True)

def destroy():
    print("Cleaning up resources...", flush=True)
    led.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Resources cleaned up", flush=True)

if __name__ == '__main__':
    print("Program is starting...", flush=True)
    try:
        loop()
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, ending program...", flush=True)
        destroy()
        print("Program terminated", flush=True)
