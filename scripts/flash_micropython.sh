#!/bin/bash

COM_PORT=${1:-/dev/ttyUSB0}

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
source "$SCRIPT_DIR/logger.sh"

MICROPYTHON_BIN_URL="https://micropython.org/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.bin"
MICROPYTHON_BIN_PATH="$(dirname "${BASH_SOURCE[0]}")/tmp/esp32.bin"

download_firmware() {
  log-info "Downloading firmware..."
  wget $MICROPYTHON_BIN_URL -O $MICROPYTHON_BIN_PATH
}

cleanup() {
  log-info "Cleaning up the files..."
  rm -vf $MICROPYTHON_BIN_PATH
}

flash_firmware() {
  log-info "Erasing existing firmware on port ${COM_PORT}..."
  esptool.py --chip esp32 --port $COM_PORT erase_flash

  log-info "Flashing MicroPython firmware on port ${COM_PORT}..."
  esptool.py \
    --chip esp32 --port $COM_PORT --baud 460800 \
    write_flash -z 0x1000 $MICROPYTHON_BIN_PATH
}

# TODO: add check for the port

download_firmware
flash_firmware
cleanup

# TODO: add check for successful flash
log-info "MicroPython firmware installed successfully"
