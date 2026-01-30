"""
Ultrasonic Distance Sensor
===========================
Description: Measures distance using HC-SR04 ultrasonic sensor. Sends trigger pulse and calculates 
distance from echo time. Displays distance in centimeters with 0.2s refresh rate.

Hardware Requirements:
- HC-SR04 ultrasonic sensor
- Trigger pin on GPIO 31 (BOARD mode)
- Echo pin on GPIO 29 (BOARD mode)
- IR LED on GPIO 11 (BOARD mode)

Author: Vilas
"""

from time import sleep, time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
trig = 31
echo = 29
ir = 11

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(ir, gpio.OUT)

try:
    while True:
        gpio.output(trig, 0)
        sleep(2e-6)
        gpio.output(trig, 1)
        sleep(10e-6)
        gpio.output(trig, 0)
        while gpio.input(echo)==0:
            pass
        sT = time()
        while gpio.input(echo)==1:
            pass
        eT = time()
        dt = eT-sT
        cm = dt*1000000/29.155
        print(cm)
        sleep(0.2)
except KeyboardInterrupt:
    gpio.cleanup()
