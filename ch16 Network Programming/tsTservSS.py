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
        print('...connected from %s', self.client_address)
        output_data = '[%s] %s'%(ctime(), self.rfile.readline())
        self.wfile.write(output_data.encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print('Waiting for connection...')
tcpServ.serve_forever()
