from conn import Connection
class LoginConn(Connection):
    def __init__(self, cli):
        self.sock = cli
    def handleRead(self):
        print("loginConn")
        Connection.handleRead(self)
        print(self.buf)
        self.write(self.buf)