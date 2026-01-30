"""
Security System
===============
Description: Integrated security system with keypad authentication, ultrasonic sensor for object 
detection, and servo-controlled lock. Multi-threaded keypad input and distance monitoring.

Hardware Requirements:
- 4x4 matrix keypad (GPIO 37,35,33,31 for rows; 38,40,36,32 for cols)
- HC-SR04 ultrasonic sensor (Trigger: GPIO 11, Echo: GPIO 13)
- Servo motor on GPIO 15 (BOARD mode)

Features: Password entry, distance-based object detection, automated servo lock control

Author: Vilas
"""

import RPi.GPIO as gp
from time import sleep, time
from os import getcwd
import keypadClass
from threading import Thread

gp.setmode(gp.BOARD)

trig = 11
echo = 13
servo = 15

object =0
strInput = ""

gp.setup(trig, gp.OUT)
gp.setup(servo, gp.OUT)
gp.setup(echo, gp.IN)

servoC = gp.PWM(servo, 50)
servoC.start(2)

rows = [37, 35, 33, 31]
cols = [38, 40, 36, 32]
keys = [['d', '#', 0, '*'], ['c',9,8,7], ['b', 6,5,4],['a',3,2,1]]
keypad1 = keypadClass.keypad(rows, cols, keys, 'd')

def readKeypad():
    global strInput
    while strInput != '*':
        strInput = keypad1.get_val()
        sleep(.2)
        if len(strInput)>6:
            strInput = ''

def trigger():
    global object
    while True:
        gp.output(trig, 0)
        sleep(2e-6)
        gp.output(trig, 1)
        sleep(10e-6)
        gp.output(trig, 0)
        while gp.input == 0:
            continue
        sTime = time()
        while gp.input == 1:
            continue
        eTime = time()
        dt = sTime-eTime
        if dt == 2000:
            object= 1

try:
    t1 = Thread(target = trigger, daemon = True)
    t2 = Thread(target = readKeypad, daemon = True)
    t1.start()
    t2.start()
    while True:
        rows = [37, 35, 33, 31]
        cols = [38, 40, 36, 32]
        if object == 1 or strInput == '1234':
            servoC.ChangeDutyCycle(12)
            print('unarmed')
            sleep(5)
            servoC.ChangeDutyCycle(2)
            print('armed')
        if strInput == '12345':
            print('verified')

except KeyboardInterrupt:
    gp.cleanup()
t1.stop()
t2.stop()
gp.cleanup()
