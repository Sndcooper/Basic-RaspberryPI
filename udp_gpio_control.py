"""
UDP GPIO Control
================
Description: UDP server for remote GPIO control. Receives commands via UDP socket and controls 
GPIO based on commands. Demonstrates network-based hardware control.

Configuration:
- Server IP: 10.254.34.67
- Server Port: 2233
- GPIO Pin: 11 (BOARD mode, input)

Commands: 'GO' - reads GPIO input and responds with result

Author: Vilas
"""

import socket
from RPi.GPIO import *
from time import time, sleep

setmode(BOARD)
bufferSize = 1024
ServerIP = '10.254.34.67'
ServerPort = 2233
RPIServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIServer.bind((ServerIP, ServerPort))
print('Server up..')
while True:
    cmd, address=RPIServer.recvfrom(bufferSize)
    cmd = cmd.decode('utf-8')
    print(cmd)
    print('Client address, address[0])
    if cmd =='GO':
        result=input(11)
