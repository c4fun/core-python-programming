__author__ = 'Richard'
'''To build asynchronous handlers, use the ThreadingMixIn and ForkingMixIn classes.'''
import socket
import threading
import socketserver

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("Send from server (which is only a repeater)")+\
                   bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)
        if data != "exit()":
            send_data = input("Please input a message to send> ")
            #self.wfile.write(send_data.encode())
            self.request.sendall(bytes(send_data, 'ascii'))
        else:
            #self.finish()
            print("Disconnected from", self.client_address)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

'''
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))
    finally:
        sock.close()
'''

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 21567

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    server.shutdown()