"""
PWM Basic
=========
Description: Basic PWM signal generation example on GPIO 17 (BCM mode). Demonstrates starting 
PWM at 50% duty cycle, then changing to 10% after 5 seconds.

Hardware Requirements:
- LED or servo on GPIO 17 (BCM mode)

Author: Vilas
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

myPWM = GPIO.PWM(17, 10)
myPWM.start(50)
sleep(5)
myPWM.start(10)
sleep(2)
GPIO.cleanup()

