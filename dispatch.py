import os, sys
import socket
import multiprocessing
# import threading
from login_conn import LoginConn
from event import EventModule

class IPC:
    def __init__(self, callback, fd):
#         fds = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
#         if mode == self.READ:
#             fds[1].close()
#             self.fd = fds[0]
#         else:
#             fds[0].close()
#             self.fd = fds[1]
        self.sock = fd
        self.cb = callback[0]
        self.cb_args = callback[1]
    
    def handleRead(self):
        try:
            conn = self.sock.recv(1024)
#             conn = struct.unpack('s', buff)
            self.cb(self.cb_args, conn)
            return conn
        except Exception as e:
            print(e)
            return None
    
class Routine:
    def __init__(self, fd):
        self.pid = os.getpid()
        self.em = EventModule()
        self.fd = fd
#         self.ipc = IPC((self.em.addConn, self), fd)
#         self.em.addConn(self.ipc)
    def run(self):
        while True:
            self.em.process()
    def recvHandler(self):
        while True:
            cli = multiprocessing.reduction.recv_handle(self.fd)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno = cli)
            conn = LoginConn(sock)
            self.em.addConn(conn)
            if len(self.em.socks) > 0:
                self.em.process()
class Dispatch:
    def __init__(self, pidCnt):
        self.cnt = pidCnt
        self.routines = []
        self.pipes = []
        for i in range(0, pidCnt):
            pipe, child = multiprocessing.Pipe()
            r = Routine(child)
            self.routines.append(r)
            self.pipes.append(pipe)
    def start(self):
        for i in range(0, self.cnt):
            p = multiprocessing.Process(target = self.routines[i].recvHandler)
#             p = threading.Thread(target = self.routines[i].run)
            p.start()
    def dispatch(self, cli):
        
#         conn = LoginConn(cli)
        idx = cli.fileno() % self.cnt
        multiprocessing.reduction.send_handle(self.pipes[idx],cli.fileno(), self.routines[idx].pid)
#         buf = struct.pack('s', conn)
#         self.pipes[idx].send_
    