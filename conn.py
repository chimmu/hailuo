# import socket
# import select
# import dispatch
import socket
import errno
class Connection:
    def __init__(self):
#         self.buf = bytes()
        pass
    def disconnect(self):
        self.sock.close()
        
    def read(self, size):
        try:
            return self.sock.recv(size)
        except socket.error as e:
            if e.args[0] != errno.EAGAIN:
                self.disconnect()
            print("conn read exception")
            return None
    def write(self, buf):
        try:
            print("send sock {0}".format(self.sock))    
            return self.sock.send(buf)
        except Exception as e:
            print(e)
            return None
    def handleRead(self):
        self.buf = self.read(2048)
        print("Connection: {0}".format(self.buf))
        ret = True
        if self.buf == None:
            ret = False
        return ret
    
