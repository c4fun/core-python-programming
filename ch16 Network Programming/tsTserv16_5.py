"""
This server returns timestamps
16-5: The server recognizes the following 3 commands: date, os, ls
"""

from socket import *
from time import ctime
import os

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

def is_command(data_str):
    if (data_str == 'date'):
        return ctime()
    if (data_str == 'os'):
        return os.name
    if (data_str == 'ls'):
        return ("The current directory {0} has the following files: {1}"
                .format(os.curdir, os.listdir()))
    else:
        return False

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        data_str = data.decode()
        sendData = '[%s] %s'%(ctime(), data_str) if not is_command(data_str) \
            else is_command(data_str)
        tcpCliSock.send(sendData.encode())

    tcpCliSock.close()
tcpSerSock.close()
