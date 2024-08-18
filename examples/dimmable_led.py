import time
from simplesp import DimmableLED  # Import the DimmableLED class from the SimplESP library

# Initialize the DimmableLED object
led = DimmableLED(pin_number=2)

# Set brightness to 50%
led.set_brightness(512)
print(f"LED brightness set to {led.get_brightness()}")
time.sleep(2)

# Set brightness to 100% (full brightness)
led.on()
print(f"LED brightness set to {led.get_brightness()}")
time.sleep(2)

# Dim the LED in a loop
print("Dimming the LED")
for level in range(1023, -1, -102):  # Gradually dim the LED
    led.set_brightness(level)
    print(f"LED brightness set to {led.get_brightness()}")
    time.sleep(0.5)

# Breathing effect: smoothly increase and decrease brightness 5 times
print("Starting the breathing effect")
b = 0
sign = 1

for _ in range(5):  # Repeat the breathing effect 5 times
    for _ in range(2046):  # 1023 two times, once up and once down
        b = b + sign
        if b == 1023 or b == 0:
            sign = -1 * sign
        led.set_brightness(b)
        time.sleep(0.001)

# Turn the LED off
led.off()
print("LED is OFF")
