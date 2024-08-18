#!/bin/bash

# Define color codes
BOLD="\033[1m"
RESET="\033[0m"
INFO_COLOR="\033[1;34m"   # Bold Blue
WARN_COLOR="\033[1;33m"   # Bold Yellow
ERROR_COLOR="\033[1;31m"  # Bold Red

# Info function
log-info() {
    echo -e "${INFO_COLOR}${BOLD}[INFO]${RESET} $1"
}

# Warn function
log-warn() {
    echo -e "${WARN_COLOR}${BOLD}[WARN]${RESET} $1"
}

# Error function
log-error() {
    echo -e "${ERROR_COLOR}${BOLD}[ERROR]${RESET} $1"
}
