"""
This client send data to server, then receive data from server
"""

from socket import *
import threading
from time import ctime
from MyThread import MyThread

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

def receive_message(sock, exit_flag):
    while not exit_flag:
        data = sock.recv(BUFSIZE)
        receive_data = data.decode()
        if receive_data == 'exit()':
            exit_flag = True
        print(receive_data)
    return exit_flag

def send_message(sock, exit_flag):
    while not exit_flag:
        data = input("Please input data >")
        if data == 'exit()':
            exit_flag = True
        send_data = '[{}]{}'.format(ctime(), data)
        sock.send(send_data.encode())
    return exit_flag


def main():
    threads = []
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    # 2 threads, 1 for receiving, 1 for sending
    exit_flag = False
    t = MyThread(receive_message, (tcpCliSock, exit_flag), receive_message.__name__)
    threads.append(t)
    t = MyThread(send_message, (tcpCliSock, exit_flag), send_message.__name__)
    threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    tcpCliSock.close()


if __name__ == '__main__':
    main()