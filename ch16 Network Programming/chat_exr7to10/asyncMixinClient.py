__author__ = 'Richard'
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
    exit_flag = False

    send_data = input('> ')
    if send_data == "exit()":
        exit_flag = True
    send_data = '%s\r\n'%(send_data)

    tcpCliSock.sendall(bytes(send_data, 'ascii'))
    response = str(tcpCliSock.recv(BUFSIZE), 'ascii')
    print("Received: {}".format(response))

    if not data:
        break
    print(data.decode())

tcpCliSock.close()
