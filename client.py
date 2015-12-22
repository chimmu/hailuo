import socket
from time import sleep
import struct
class Client:
    def connect(self, ip, port, timeout = 1000):
        try: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            self.sock.settimeout(timeout)
            self.sock.connect((ip, port))
            return self.sock
        except Exception as e:
            print(e)
            return None
    def write(self, buf):
        try:    
            return self.sock.send(buf)
        except Exception as e:
            print(e)
            return None
    def recv(self):
        try:
            buf = self.sock.recv(1024)
            print(buf) 
        except Exception as e:
            print(e) 
            exit(1) 
if __name__ == '__main__':
    cli = Client()
    cli.connect("127.0.0.1", 9527)
#     for i in range(0, 10):
    msg = '{"username": "test", "passwd": "1234"}'
    head = struct.pack('!ii',len(msg), 0)
    cli.write(head)
    cli.write(msg.encode(encoding='utf_8', errors='strict'))
#     sleep(1)
    cli.recv()
