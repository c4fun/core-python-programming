__author__ = 'Richard'
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

def udpCliSockAddr(host = HOST, port = PORT):
    #enable the socket to connect to a certain address
    #cliSock.connect((host, port))
    #应该有比下面更好的调用时的方法，可以让在调用的时候遇见空就取默认值
    if host =='': host = HOST
    port = PORT if port =='' else int(port)
    return (host, port)

host = input('Input a host: an IPv4 address. e.g. localhost, 127.0.0.1 >')
port = input('Input a port: an integer in 65535. e.g. 17548 >')
address = udpCliSockAddr(host, port)
print(address)

while True:
    data = input("> ")
    if not data:
        break
    udpCliSock.sendto(data.encode(), address)
    data, address = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break;
    print(data.decode())

udpCliSock.close()