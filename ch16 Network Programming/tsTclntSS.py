__author__ = 'Richard'
"""
This is the client using socketserver
But actually, the client does not need to use socketserver at all
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    output_data = '%s\r\n'%(data)
    tcpCliSock.send(output_data.encode())
    recv_data = tcpCliSock.recv(BUFSIZE)
    if not recv_data:
        break
    print(recv_data.decode().strip())
    tcpCliSock.close()
