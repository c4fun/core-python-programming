"""
This client returns a port number from a service name and a protocol name
"""

__author__ = 'Richard'
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

port = None

while True:
    #TODO QUESTION send a dummy message to WHERE?
    data = 'dummy message'
    #udpCliSock.sendto(data.encode(), ADDR)
    port = getservbyname('daytime', 'udp')
    if port:
        break;

print("The port for daytime is:", port)

udpCliSock.close()