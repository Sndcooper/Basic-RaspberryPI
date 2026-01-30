"""
PIR Motion Sensor
=================
Description: Reads and displays PIR (Passive Infrared) motion sensor state on GPIO 33 (BOARD mode). 
Continuously monitors for motion detection.

Hardware Requirements:
- PIR sensor on GPIO 33 (BOARD mode)

Output: Prints 1 when motion detected, 0 otherwise

Author: Vilas
"""

import RPi.GPIO as gpio
from time import sleep, time

gpio.setmode(gpio.BOARD)
gpio.setup(33, gpio.OUT)

try:
    while True:
        pir = gpio.input(33)
        print(pir)

except KeyboardInterrupt:
    gpio.cleanup()

