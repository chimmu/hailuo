import socket
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
        
if __name__ == '__main__':
    cli = Client()
    cli.connect("127.0.0.1", 9527)
    cli.write("fuck".encode(encoding='utf_8', errors='strict'))