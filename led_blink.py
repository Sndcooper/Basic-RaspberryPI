"""
LED Blink
==========
Description: Simple LED blinking program using RPi.GPIO. Blinks an LED connected to GPIO pin 11 
for a user-specified number of repetitions with 1-second intervals.

Hardware Requirements:
- LED on GPIO pin 11 (BOARD mode)
- 220Ω resistor

Author: Vilas
"""

import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

repeat = int(input("number of time running: "))
for i in range(0, repeat):
	GPIO.output(11, 1)
	sleep(1)
	GPIO.output(11, 0)
	sleep(1)

GPIO.cleanup()
