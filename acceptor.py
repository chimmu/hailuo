from conn import Connection
import dispatch
import socket
class Acceptor(Connection):
    def __init__(self, port):
        self.dispatcher = dispatch.Dispatch(2)
        self.dispatcher.start()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.bind(("127.0.0.1", port))
        self.sock.listen(1024)
    def handleRead(self):
        cli, addr = self.sock.accept()
        self.dispatcher.dispatch(cli)