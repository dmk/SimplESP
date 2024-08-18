# SimplESP

**SimplESP** is a simple and easy-to-use MicroPython library for the ESP32, providing
basic interfaces for common components such as LEDs, PWM-controlled LEDs, buttons, and
various sensors. This library is designed to be accessible for beginners.

## Features

- **LED Control**: Turn an LED on or off with simple commands.

More features coming later

## Getting Started

### Prerequisites

To get started with SimplESP, you'll need:

- An ESP32 board.
- MicroPython firmware installed on your ESP32.
- Python 3.x installed on your computer.
- Required Python packages listed in `requirements.txt`.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dmk/SimplESP.git
   cd SimplESP
   ```

2. Set up Python environment:

   ```bash
   make setup-python
   ```

3. Flash MicroPython to the ESP32:

   If you haven't already flashed MicroPython onto your ESP32, you can use the following command:

   ```bash
   make flash
   ```

   This will run the `scripts/flash_micropython.sh` script to erase and flash the firmware onto your ESP32.

4. Deploy the SimplESP Library:

   TBD

