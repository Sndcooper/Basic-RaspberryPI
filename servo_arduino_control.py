"""
Servo Control via Arduino
==========================
Description: Controls servo motor angle using potentiometer connected to Arduino. Reads ADC values 
via serial and converts to servo PWM duty cycle (2-13.5%). 50Hz PWM signal for servo control.

Hardware Requirements:
- Servo motor on GPIO 16 (BOARD mode)
- LED on GPIO 11 (BOARD mode)
- Arduino with potentiometer connected via USB

Author: Vilas
"""

import RPi.GPIO as gpio
from time import sleep
import serial

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(16, gpio.OUT)
pwm = gpio.PWM(16, 50)
pwm.start(0)
lastDC = 0

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

except:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            value = ser.readline().decode('utf-8', errors = 'ignore').rstrip()
            if not value:
                continue
            adc = int(value)
            angle = adc*11.5/1024
            angle +=2
            if lastDC != angle:
                lastDC = angle
                pwm.ChangeDutyCycle(int(angle))
                print(angle)

except KeyboardInterrupt:
    gpio.cleanup()
    pwm.stop()
    print('cleansed')
