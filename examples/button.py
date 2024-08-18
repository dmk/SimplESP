import time
from simplesp.button import Button  # Import the Button class from the SimplESP library

# Callback function to handle button press
def on_button_pressed(pin):
    print("Button was pressed!")

# Initialize the Button object with a callback and a debounce time of 300 ms
button = Button(pin_number=0, callback=on_button_pressed, debounce=300)

# Main loop to check button state
for _ in range(10):  # Check the button 10 times
    if button.is_pressed():
        print("Button is currently pressed")
    else:
        print("Button is not pressed")
    time.sleep(1)  # Wait for 1 second between checks
