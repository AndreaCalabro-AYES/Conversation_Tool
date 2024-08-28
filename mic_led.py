from gpiozero import SmoothedInputDevice, LED
import time

# Initialize the microphone connected to GPIO pin 18
mic = SmoothedInputDevice(pin=18, threshold=0.5, queue_len=5, sample_wait=0.1)

# Initialize the LED connected to GPIO pin 17
led = LED(17)

try:
    while True:
        if mic.is_active:
            led.on()  # Turn on the LED when sound is detected
            print("Sound detected!")
        else:
            led.off()  # Turn off the LED when no sound is detected
        
        time.sleep(0.1)  # Small delay to prevent too rapid switching
except KeyboardInterrupt:
    pass
finally:
    led.off()  # Ensure the LED is turned off when the script exits
