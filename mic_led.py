from gpiozero import SmoothedInputDevice, LED
import time

# Initialize the microphone connected to GPIO pin 18
mic = SmoothedInputDevice(pin=18, threshold=0.5, queue_len=5, sample_wait=0.1)

# Initialize the LED connected to GPIO pin 18
led = LED(17)

try:
    print("Starting microphone detection...", flush=True)
    print(f"Microphone initialized on GPIO pin 18 with threshold={mic.threshold}, queue_len={mic.queue_len}", flush=True)
    print(f"LED initialized on GPIO pin 17", flush=True)
    
    while True:
        mic_value = mic.value  # Get the current smoothed value
        print(f"Mic value: {mic_value:.2f}", flush=True)  # Debugging mic value
        
        if mic.is_active:
            led.on()  # Turn on the LED when sound is detected
            print("Sound detected! LED is ON.", flush=True)
        else:
            led.off()  # Turn off the LED when no sound is detected
            print("No sound detected. LED is OFF.", flush=True)
        
        time.sleep(0.1)  # Small delay to prevent too rapid switching

except KeyboardInterrupt:
    print("Exiting program due to keyboard interrupt.", flush=True)
finally:
    led.off()  # Ensure the LED is turned off when the script exits
    print("LED turned OFF, exiting program.", flush=True)
