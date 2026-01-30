"""
UDP Socket Server
=================
Description: Basic UDP socket server that listens on port 2233, receives messages from clients, 
and sends acknowledgment. Demonstrates simple network communication.

Configuration:
- Server IP: 10.254.34.67
- Server Port: 2233
- Buffer Size: 1024 bytes

Author: Vilas
"""

import socket
import time
dataSize = 1024
msgRec = 'sent'
Sport = 2233
SIP = '10.254.34.67'

dataSending = msgRec.encode('utf-8')
RPIsocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((SIP, Sport))
print("server connected")
message, address = RPIsocket.recvfrom(dataSize)
message = message.decode('utf-8')
print(message)
print('client address', address[0])

RPIsocket.sendto(dataSending, address)

