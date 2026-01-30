"""
IR Brightness Control via Arduino
==================================
Description: Controls IR LED brightness using PWM based on Arduino ADC readings via serial. 
Reads potentiometer values (0-1024) from Arduino and converts to PWM duty cycle (0-100%).

Hardware Requirements:
- IR LED on GPIO 11 (BOARD mode)
- Arduino connected via USB (/dev/ttyACM0 or /dev/ttyUSB0)
- Potentiometer on Arduino A0

Author: Vilas
"""

from time import sleep
import RPi.GPIO as gpio
import serial

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
    ser.reset_input_buffer()
except:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)

#pwm
pwm1 = gpio.PWM(11, 10000)
pwm1.start(1)

try:
    while True:
        value = ser.readline().decode('utf-8', errors='ignore').rstrip()
        if not value:
            continue
        adcVal = int(value)
        adcVal *=100/1024
        pwm1.ChangeDutyCycle(adcVal)

except KeyboardInterrupt:
    gpio.cleanup()
    print("gpio cleansed")
