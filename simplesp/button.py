from machine import Pin
import time

class Button:
    def __init__(self, pin_number, callback=None, debounce=200):
        """Initialize the Button on a specific GPIO pin.

        Args:
            pin_number (int): The GPIO pin number where the button is connected.
            callback (function, optional): A function to call when the button is pressed.
            debounce (int, optional): Minimum time (in milliseconds) between successive calls to the callback.
        """
        self.button = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.callback = callback
        self.debounce = debounce / 1000  # Convert milliseconds to seconds
        self.last_press_time = 0

        if self.callback:
            self.button.irq(trigger=Pin.IRQ_FALLING, handler=self._handle_press)

    def _handle_press(self, pin):
        """Internal method to handle button press interrupt."""
        current_time = time.time()
        if (current_time - self.last_press_time) >= self.debounce:
            self.last_press_time = current_time
            if self.callback:
                self.callback(pin)

    def is_pressed(self):
        """Check if the button is pressed.

        Returns:
            bool: True if the button is pressed, False otherwise.
        """
        return not self.button.value()  # Active low (0 means pressed)
