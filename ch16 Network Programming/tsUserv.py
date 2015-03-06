__author__ = 'Richard'

from socket import *
from time import ctime
from random import randint

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

random_port = randint(1, 65535)
print("Port is: {}".format(random_port))
ADDR = (HOST, random_port)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("Waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    newdata = '[%s] %s'%(ctime(), data.decode())
    udpSerSock.sendto(newdata.encode(), addr)
    print("...received from and returned to:", addr)

udpSerSock.close()