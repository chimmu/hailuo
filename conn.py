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
#         self.buf = bytes()
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
    def write(self, buf):
        try:
            print("send sock {0}".format(self.sock))    
            return self.sock.send(buf)
        except socket.error as e:
            print(e)
            return None
    def handleRead(self):
        head = self.read(8)
        try:
            self.h = struct.unpack('!ii', head)
        except struct.error as e:
            return False
        buff = self.read(self.h[0])
        print(self.h)
        if buff:
            self.buf = json.loads(buff.decode('utf8'))
            return True
        return False
#         print("Connection: {0}".format(self.buf))
    
