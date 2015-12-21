from conn import Connection
class LoginConn(Connection):
    def __init__(self, cli):
        self.sock = cli
    def handleRead(self):
        ret = Connection.handleRead(self)
        if ret == False:
            return False
        ret = self.write(self.buf)
        if ret == None:
            return False
        return True