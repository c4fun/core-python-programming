"""
This client send data to server, then receive data from server
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
#经过实测，如果data超过这个bufsize，客户端会自动退出。
ADDR = (HOST, PORT)

def tcpCliSockAddr(host = HOST, port = PORT):
    #enable the socket to connect to a certain address
    #cliSock.connect((host, port))
    #应该有更好的调用时的方法，可以让在调用的时候遇见空就取默认值
    if host =='': host = HOST
    if port =='': port = PORT
    return (host, port)

print(ADDR)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
host = input('host: an IPv4 address. e.g. localhost, 127.0.0.1')
port = input('port: an integer in 65535. e.g. 17548')
address = tcpCliSockAddr(host, port)
print(address)
tcpCliSock.connect(address)

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
