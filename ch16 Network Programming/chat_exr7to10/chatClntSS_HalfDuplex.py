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
    exit_flag = False
    #If input != '' then continue input is needed, then we add another loop starting from here

    send_data = input('> ')
    if send_data == "exit()":
        exit_flag = True
    send_data = '%s\r\n'%(send_data)
    tcpCliSock.send(send_data.encode())
    if exit_flag:
        break
    # If just using indention, then there will be a problem.
    # ConnectionAbortedError: [WinError 10053] 您的主机中的软件中止了一个已建立的连接。
    data = tcpCliSock.recv(BUFSIZE)
    receive_data =data.decode().strip()
    if receive_data == "exit()":
        exit_flag = True
        break;
    print("Server wrote:")
    print(receive_data)
    tcpCliSock.close()
