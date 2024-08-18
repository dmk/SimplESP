from machine import Pin, PWM

class DimmableLED:
    def __init__(self, pin_number, frequency=1000):
        """Initialize the DimmableLED on a specific GPIO pin with a given frequency."""
        self.led = PWM(Pin(pin_number))
        self.led.freq(frequency)
        self.brightness_level = 0

    def set_brightness(self, level):
        """Set the brightness of the LED.

        Args:
            level (int): The brightness level from 0 (off) to 1023 (full brightness).
        """
        if 0 <= level <= 1023:
            self.brightness_level = level
            self.led.duty(level)
        else:
            raise ValueError("Brightness level must be between 0 and 1023.")

    def off(self):
        """Turn the LED off by setting brightness to 0."""
        self.set_brightness(0)

    def on(self):
        """Turn the LED on to full brightness (1023)."""
        self.set_brightness(1023)

    def get_brightness(self):
        """Get the current brightness level."""
        return self.brightness_level
