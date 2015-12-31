import select 
class EventModule:
    def __init__(self):
        self.socks = []
        self.conns = dict()
         
    def addConn(self, conn):
#         self.conns[conn.sock] = conn
        self.socks.append(conn.sock)
        self.conns[conn.sock] = conn
#         print("add done")
        
    def delConn(self, conn):
        print("delete conn {0}".format(conn))
        self.socks.remove(conn.sock)
        self.conns[conn.sock] = None
        
    def process(self):
        if len(self.socks) <= 0:
            return
#         print(self.socks)
        rfds, wfds, efds = select.select(self.socks, [], [])
        for fd in rfds:
            ret = self.conns[fd].handleRead()
            if ret == False:
                self.delConn(self.conns[fd])
        for efd in efds:
            print("exception event****************")
            print(efd)