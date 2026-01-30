"""
Pushbutton Toggle
=================
Description: Toggle LED state using a pushbutton. Each button press switches LED between 
ON and OFF states with debouncing logic.

Hardware Requirements:
- Pushbutton on GPIO 12 (BOARD mode) with pull-up
- LED on GPIO 11 (BOARD mode)

Author: Vilas
"""

from time import sleep
import RPi.GPIO as GPIO
delay = 0.1
inPin = 12
outPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(outPin, GPIO.OUT)
prevButton = -1
currentButton = -1
prevState = 0
try:
	while True:
		currentButton = GPIO.input(inPin)
		while currentButton == 0:
#			currentButton  = GPIO.input(inPin)
			if prevState == 0:
				GPIO.output(outPin, 1)
				prevState = 1
			elif prevState == 1:
				GPIO.output(outPin, 0)
				prevState = 0
			prevButton = 1
#		sleep(delay)


except KeyboardInterrupt:
	GPIO.cleanup()
	print("\nGPIO cleaned")
