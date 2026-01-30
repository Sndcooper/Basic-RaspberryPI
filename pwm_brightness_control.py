"""
PWM Brightness Control
======================
Description: Control LED brightness using PWM with two pushbuttons. Button 1 increases brightness, 
Button 2 decreases brightness in 10% increments. PWM frequency: 10Hz.

Hardware Requirements:
- LED on GPIO 11 (BOARD mode)
- Pushbutton 1 on GPIO 12 (with pull-up)
- Pushbutton 2 on GPIO 18 (with pull-up)

Author: Vilas
"""

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
prevB1 = 1
prevB2 = 1
freq = 10
duty = 50
pwm1 = GPIO.PWM(11, freq)
pwm1.start(duty)
try:
	while True:
		B1 = GPIO.input(12)
		B2 = GPIO.input(18)
		if B1 == 1 and prevB1==0:
			duty+=10
		if B2 == 1 and prevB2==0:
			duty-=10
		if duty>99: 
			duty=99
		if duty<0:
			duty = 0
		pwm1.ChangeDutyCycle(duty)
		prevB1 = B1
		prevB2 = B2

except KeyboardInterrupt:
	GPIO.cleanup()
	print("gpio is cleaned")
