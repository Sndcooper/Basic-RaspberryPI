"""
4x4 Matrix Keypad
=================
Description: Reads input from 4x4 matrix keypad. Scans rows and columns to detect key presses 
and displays the pressed key. Includes debouncing with 0.3s delay.

Hardware Requirements:
- 4x4 matrix keypad
- Rows connected to GPIO: 37, 35, 33, 31 (BOARD mode)
- Columns connected to GPIO: 38, 40, 36, 32 (BOARD mode)

Key Layout: [['d', '#', 0, '*'], ['c',9,8,7], ['b', 6,5,4], ['a',3,2,1]]

Author: Vilas
"""

from time import sleep, time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
rows = [37, 35, 33, 31]
cols = [38, 40, 36, 32]

for i in rows:
    gpio.setup(i, gpio.OUT)

for i in cols:
    gpio.setup(i, gpio.IN, pull_up_down = gpio.PUD_DOWN)

keys = [['d', '#', 0, '*'], ['c',9,8,7], ['b', 6,5,4],['a',3,2,1]]
prev = ' '
prevVal = 0
try:
    while True:
        for i in range(4):
            for j in range(4):
                gpio.output(rows[i], 1)
                val = gpio.input(cols[j])
                gpio.output(rows[i], 0)
                if val ==1 and prevVal == 0:
                    print(str(keys[j][i]))
                    prev = " "
                    prev = str(keys[j][i])
                    sleep(0.3)
                    prevVal = 1
                else :
                    if not val :
                        prevVal = 0
                    prev = " "

except KeyboardInterrupt:
    gpio.cleanup()
