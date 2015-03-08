__author__ = 'Richard'
"""
This is the server using socketserver
"""

from socketserver import TCPServer as TCP
from socketserver import StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from', self.client_address)
        receive_data = self.rfile.readline().decode().strip()
        affiliated_receive_data = '[%s] %s'%(ctime(), receive_data)
        print(self.client_address[0],"wrote:")
        print(affiliated_receive_data)
#        self.wfile.write(output_data.encode())
        if receive_data != "exit()":
            send_data = input("Please input a message to send> ")
            self.wfile.write(send_data.encode())
        else:
            #self.finish()
            print("Disconnected from", self.client_address)

tcpServ = TCP(ADDR, MyRequestHandler)
print('Waiting for connection...')
tcpServ.serve_forever()
