"""
This server can chat with the client full duplex
"""

from socket import *
from time import ctime
import threading

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

def receive_message(sock, exit_flag, addr):
    try: # judge if the receive have error
        while not exit_flag:
            data = sock.recv(BUFSIZE)
            receive_data = data.decode()
            if receive_data == 'exit()':
                exit_flag = True
            print('[{}]{}'.format(addr, receive_data))
    except ConnectionResetError:
        print('Client', addr, 'is offline')
        return exit_flag
    return exit_flag

def send_message(sock, exit_flag):
    try: # judge if the send have error:
        while not exit_flag:
            data = input("Please input data >")
            if data == 'exit()':
                exit_flag = True
            send_data = '[Server@{}]{}'.format(ctime(), data)
            sock.send(send_data.encode())
    except ConnectionResetError:
        print('Client',  'is offline')
        return exit_flag
    return exit_flag

def main():
    threads = []

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        try:
            print('Waiting for connection...')
            tcpCliSock, addr = tcpSerSock.accept()
            print('...connected from:', addr)

            # 2 threads, 1 for receiving, 1 for sending
            exit_flag = False
            t = threading.Thread(target=receive_message, args=(tcpCliSock, exit_flag, addr), name='Thread-R')
            threads.append(t)
            t = threading.Thread(target=send_message, args=(tcpCliSock, exit_flag), name='Thread-S')
            threads.append(t)

            event = threading.Event

            for i in range(len(threads)):
                threads[i].start()

            for i in range(len(threads)):
                threads[i].join()
            tcpCliSock.close()
        except ConnectionResetError: # if the client just terminate by it self without using exit()
            print('Client [{}] is offline', addr)
    tcpSerSock.close()

if __name__ == '__main__':
    main()