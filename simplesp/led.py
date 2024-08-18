from machine import Pin

class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

    def is_on(self):
        """Check if the LED is on."""
        return self.led.value() == 1
