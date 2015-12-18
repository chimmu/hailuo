from conn import Connection
class LoginConn(Connection):
    def __init__(self, cli):
        self.sock = cli
    def handleRead(self):
        print("loginConn")
        self.write(self.buf)