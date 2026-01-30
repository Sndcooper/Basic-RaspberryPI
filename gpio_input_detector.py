"""
GPIO Input Detector
===================
Description: Detects GPIO input on pin 27 (BCM mode) and controls LED on pin 17. When input 
is detected (LOW), LED briefly turns off then on again.

Hardware Requirements:
- LED on GPIO 17 (BCM mode)
- Input sensor on GPIO 27 (BCM mode) with pull-up resistor

Author: Vilas
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(17, 1)
try:
	while True:
		detect = GPIO.input(27)
		print(detect)
		if detect == 0:
			print("detected")
			GPIO.output(17, 0)
			GPIO.output(17, 1)
		else :
			continue

except KeyboardInterrupt:
	GPIO.cleanup()
	print("cleaned")
