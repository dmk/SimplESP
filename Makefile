PORT ?= /dev/ttyUSB0

setup-python:
	pip install -r requirements.txt

flash:
	bash scripts/flash_micropython.sh $(PORT)

deploy:
	bash scripts/deploy.sh $(PORT)

shell:
	picocom $(PORT) -b 115200
