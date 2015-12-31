# import socket
# import select
# import dispatch
import socket
import errno
import json
'''
struct head{
int type;
int len;
}
'''
import struct
class Connection:
    def __init__(self):
        self.buf = bytes()
        pass
    def disconnect(self):
        self.sock.close()
        
    def read(self, size):
        try:
            return self.sock.recv(size)
        except socket.error as e:
            print(e)
            if e.args[0] != errno.EAGAIN:
                self.disconnect()
            print("conn read exception")
            return None
    def write(self, cmd, buf):
        try:
            print("send sock {0}".format(self.sock))
            h = struct.pack('!ii',len(buf), cmd)
            self.sock.send(h)    
            return self.sock.send(buf)
        except socket.error as e:
            print(e)
            return None
    def handleRead(self):
        head = self.read(8)
        if head == None:
            return False
        try:
            self.buflen, self.cmd = struct.unpack('!ii', head)
        except struct.error as e:
            return False
        buff = self.read(self.buflen)
        print(buff.decode("utf8"))
        if buff:
            self.buf = json.loads(buff.decode('utf8'))
            return True
        return False
    

class IPC(Connection):
    def __init__(self, sock):
#         fds = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
#         if mode == self.READ:
#             fds[1].close()
#             self.fd = fds[0]
#         else:
#             fds[0].close()
#             self.fd = fds[1]
        self.sock = sock
    def handleRead(self):
        try:
            print("ipc handle read...")
            buf = self.sock.recv(1024)
            if buf != None:
                return True
            return False
#             conn = struct.unpack('s', buff)
        except Exception as e:
            print(e)
            return False
#         print("Connection: {0}".format(self.buf))
    
