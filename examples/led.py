import time
from simplesp import LED  # Import the LED class from the SimplESP library

# Initialize the LED object
# Replace '2' with the GPIO pin number connected to your LED
led = LED(pin_number=2)

# Turn the LED on
led.on()
print("LED is ON")
print(led.is_on()) # will print True
time.sleep(2)  # Keep the LED on for 2 seconds

# Turn the LED off
led.off()
print("LED is OFF")
print(led.is_on()) # will print False
time.sleep(2)  # Keep the LED off for 2 seconds

# Blink the LED in a loop
print("Starting to blink the LED")
for _ in range(5):  # Blink the LED 5 times
    led.on()
    print("LED is ON")
    time.sleep(0.5)  # LED on for 0.5 seconds
    led.off()
    print("LED is OFF")
    time.sleep(0.5)  # LED off for 0.5 seconds

print("Done blinking the LED")
