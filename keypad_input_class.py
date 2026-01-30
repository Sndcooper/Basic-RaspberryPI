"""
Keypad Input Class
==================
Description: Object-oriented keypad handler class. Builds input string from key presses until 
return character is detected. Returns complete string when specified character (e.g., 'd') is pressed.

Hardware Requirements:
- 4x4 matrix keypad
- Rows connected to GPIO: 37, 35, 33, 31 (BOARD mode)
- Columns connected to GPIO: 38, 40, 36, 32 (BOARD mode)

Usage Example:
    kp = keypad(rows, cols, keys, 'd')
    value = kp.get_val()

Author: Vilas
"""

rows = [37, 35, 33, 31]
cols = [38, 40, 36, 32]
keys = [['d', '#', 0, '*'], ['c',9,8,7], ['b', 6,5,4],['a',3,2,1]]
value = 0
pastValue = 0

import RPi.GPIO as gpio
from time import sleep

class keypad():
    def __init__(self, rows, cols, keys, retchar):
        self.rows = rows
        self.cols = cols
        self.keys = keys
        self.retchar = retchar
        self.key = "" 
        gpio.setmode(gpio.BOARD)
        for i in self.rows:
            gpio.setup(i, gpio.OUT)
        for i in self.cols:
            gpio.setup(i, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    def get_val(self):
        while True:
            for i in range(4):
                for j in range(4):
                    gpio.output(self.rows[i], 1)
                    value = gpio.input(self.cols[j])
                    gpio.output(self.rows[i], 0)
                    if value == 1 and pastValue == 0:
                        if self.keys[j][i] == self.retchar:
                            print(self.key)
                            return self.key

                        self.key += str(self.keys[j][i])
                        pastValue = 1
                        sleep(0.325)
                    elif value==0:
                        pastValue = 0


