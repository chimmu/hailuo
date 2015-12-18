import os, sys
import socket
import multiprocessing
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
            self.cb(self.cb_args, conn)
            return conn
        except Exception as e:
            print(e)
            return None
    
class Routine:
    def __init__(self, fd):
        self.pid = os.getpid()
        self.em = EventModule()
        self.ipc = IPC((self.em.addConn, self), fd)
        self.em.addConn(self.ipc)
    def run(self):
        while True:
            self.em.process()
            
class Dispatch:
    def __init__(self, pidCnt):
        self.cnt = pidCnt
        self.routines = []
        self.pipes = []
        for i in range(0, pidCnt):
            pipe, child = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
            r = Routine(child)
            self.routines.append(r)
            self.pipes.append(pipe)
    def start(self):
        for i in range(0, self.cnt):
            p = multiprocessing.process(self.routines[i].run, args=(self.routines[i]))
            p.start()
    def dispatch(self, cli):
        conn = LoginConn(cli)
        idx = conn.sock.fileno() % self.cnt
        self.pipes[idx].send(conn)
    