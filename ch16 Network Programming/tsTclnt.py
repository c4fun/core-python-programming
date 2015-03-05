"""
This client send data to server, then receive data from server
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
#经过实测，如果data超过这个bufsize，客户端会自动退出。
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()
