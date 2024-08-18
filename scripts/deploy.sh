#!/bin/bash

COM_PORT=${1:-/dev/ttyUSB0}

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
source "$SCRIPT_DIR/logger.sh"

run-ampy() {
  ampy --port $COM_PORT $@
}

# Function to deploy a specific file
deploy_file() {
    local file="$1"
    local target="/$1"
    if [ -f "$file" ]; then
        log-info "Deploying $file to $target"
        run-ampy put $file $target
    else
        log-error "File $file does not exist."
    fi
}

# Deploy all files in the simplesp directory
deploy_all() {
    log-info "Deploying all modules in simplesp/"

    run-ampy mkdir /simplesp 2>/dev/null || true
    for file in simplesp/*.py; do
        deploy_file "$file"
    done
}

deploy_all
