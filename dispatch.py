import os, sys
import socket
import multiprocessing
import threading
from conn import Connection, IPC
from event import EventModule
import mod_comm 
class CommConn(Connection):
    def __init__(self, sock):
        self.sock = sock
    def handleRead(self):
        Connection.handleRead(self)
        print("cmd is {0}".format(self.cmd))
        mod = mod_comm.getModule(self.cmd)
        return mod.handle(self, self.buf)
#         head = self.read(8)
#         try:
#             self.h = struct.unpack('!ii', head)
#         except struct.error as e:
#             return False
#         buff = self.read(self.h[0])
        
    

    
class Routine:
    def __init__(self, fd):
        self.pid = os.getpid()
        self.em = EventModule()
        self.fd = fd
#         self.cond = threading.Condition()
#         self.rfd, self.wfd = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)

#         self.ipc = IPC((self.em.addConn, self), fd)
#         self.em.addConn(self.ipc)

#     def __setstate__(self, state):
#         """ This is called while unpickling. """
#         self.__dict__.update(state)
#         
#     def __getstate__(self):
#         """ This is called before pickling. """
#         state = self.__dict__.copy()
# #         del state['rfd']
# #         del state['wfd']
# #         del state['thr']
#         return state    
    
    def run(self):
        while True:
            print("thread.................")
            self.em.process()
    def recvHandler(self):
        self.rfd, self.wfd = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.thr = threading.Thread(target = self.run)
        self.em.addConn(IPC(self.rfd))
        self.thr.start()
        while True:
            cli = multiprocessing.reduction.recv_handle(self.fd)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno = cli)
            conn = CommConn(sock)
#             conn = LoginConn(sock)
#             conn = findConn(sock)
            self.em.addConn(conn)
            self.wfd.send(b'hehe')
            print("send done...")
#             if len(self.em.socks) > 0:
#                 self.em.process()

class Dispatch:
    def __init__(self, pidCnt):
        self.cnt = pidCnt
        self.routines = []
        self.pipes = []
        self.fds = dict()
        for i in range(0, pidCnt):
            pipe, child = multiprocessing.Pipe()
            r = Routine(child)
            self.routines.append(r)
            self.pipes.append(pipe)
    def start(self):
        for i in range(0, self.cnt):
            p = multiprocessing.Process(target = self.routines[i].recvHandler)
            p.start()
    def dispatch(self, cli):
        idx = cli.fileno() % self.cnt
        multiprocessing.reduction.send_handle(self.pipes[idx],cli.fileno(), self.routines[idx].pid)
    