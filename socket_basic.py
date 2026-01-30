"""
Socket Basic
============
Description: Basic socket communication server. Listens for UDP messages, displays client address, 
and responds. Demonstrates fundamental socket programming concepts with GPIO integration.

Configuration:
- Server IP: 10.254.34.67
- Server Port: 1234
- GPIO Pin: 11 (BOARD mode, input)

Commands: 'TEMP' - reads GPIO and responds

Author: Vilas
"""

import socket
from time import sleep, time
import RPi.GPIO as gp

gp.setmode(gp.BOARD)
pin = 11
gp.setup(pin, gp.IN)

bufferSize = 1024
ServerIP = '10.254.34.67'
ServerPort = 1234
RPIServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIServer.bind((ServerIP, ServerPort))
print('Server is running')

while True:
    cmd ,address = RPIServer.recvfrom(bufferSize)
    cmd = cmd.decode('utf-8')
    print(cmd)
    if cmd == 'TEMP':
        result = gp.input(pin)
        while result.is_valid()==False:
            print('bad readin')
            result=gp.input(pin)
        data=cmd+':'+str(result)
        data= data.encode('utf-8')
        RPIServer.sendto(data, address)
    if cmd != 'HUM' and cmd != 'TEMP':
        data = cmd+':'+'null'
        data = data.encode('utf-8')
