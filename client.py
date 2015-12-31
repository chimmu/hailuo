import socket
from time import sleep
import struct
from event import EventModule
from conn import Connection
import mod_comm
import threading
class Client(Connection):
    def __init__(self, cid):
        self.id = int(cid)
        Connection.__init__(self)
    def connect(self, ip, port, timeout = 1000):
        try: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
#             self.sock.settimeout(timeout)
            self.sock.connect((ip, port))
            return self.sock
        except Exception as e:
            print(e)
            return None
#     def write(self, buf):
#         try:    
#             return self.sock.send(buf)
#         except Exception as e:
#             print(e)
#             return None
#     def recv(self):
#         try:
#             buf = self.sock.recv(1024)
#             print(buf) 
#         except Exception as e:
#             print(e) 
#             exit(1) 
        
    def handleRead(self):
        Connection.handleRead(self)
        print("recieved:")
        print(self.buf)
        return True

def task(conn):
    while True:
        msg = input('input>>>>')
        buff = '{"to":' + str(conn.id) + ', "msg":"' + msg + '"}'
        conn.write(mod_comm.MOD_MSG, buff.encode(encoding='utf_8', errors='strict'))
if __name__ == '__main__':
    cid = input('input the id')
    cli = Client(cid)
    cli.connect("127.0.0.1", 9527)
#     for i in range(0, 10):
    if int(cid) == 2:
        msg = '{"username": "test", "passwd": "1234"}'
    else:
        msg = '{"username": "test2", "passwd": "asdfg"}'
    cli.write(mod_comm.MOD_LOGIN, msg.encode(encoding='utf_8', errors='strict'))
#     head = struct.pack('!ii',len(msg), mod_comm.MOD_LOGIN)
#     cli.write(head)
#     cli.write(msg.encode(encoding='utf_8', errors='strict'))
#     sleep(1)
#     cli.recv()
    em = EventModule()
    em.addConn(cli)
    thr = threading.Thread(target=task, args=(cli,))
    thr.start()
    while True:
        print("cli processing...")
        em.process()
    
    
