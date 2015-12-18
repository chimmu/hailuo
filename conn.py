# import socket
# import select
# import dispatch
class Connection:
        
    def disconnect(self):
        self.sock.close()
        
    def read(self, size):
        try:
            return self.sock.recv(size)
        except Exception as e:
            print(e)
            return None
    def write(self, buf):
        try:    
            return self.sock.send(buf)
        except Exception as e:
            print(e)
            return None
    def handleRead(self):
        self.buf = self.read(2048)
        print("Connection: {0}".format(self.buf))
 
    
