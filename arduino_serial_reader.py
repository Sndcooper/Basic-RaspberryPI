"""
Arduino Serial Reader
=====================
Description: Reads analog values from Arduino via serial (9600 baud) and converts ADC readings 
to voltage. Displays both ADC value (0-1023) and calculated voltage (0-5V).

Hardware Requirements:
- Arduino with analog sensor
- USB connection to RPi (/dev/ttyACM0 or /dev/ttyUSB0)

Author: Vilas
"""

import serial
import time

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
except:
    ser = serial.Serial('/dev/tty/USB0', 9600, timeout=1)

print("reading...")

while True:
    if ser.in_waiting >0:
        try:
            value = ser.readline().decode('utf-8', errors='ignore').rstrip()
            if not value:
                continue
            adc_value = int(value)
            voltage = (adc_value / 1023)*5
            print(adc_value, voltage)
        except ValueError:
            pass
        except UnicodeDecodeError:
            pass

