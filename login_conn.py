from conn import Connection
from db import g_dbConn

class LoginConn(Connection):
    def __init__(self, cli):
        self.sock = cli
    def handleRead(self):
        ret = Connection.handleRead(self)
        if ret == False:
            return False
        ret = g_dbConn.checkPasswd(self.buf['user'], self.buf['passwd'])
        if ret == False:
            print("login failed")
            return False
        print("login success")
        self.write(b'fuck')
        return True