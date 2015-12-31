from db import g_dbConn
class User:
    def __init__(self, conn):
        self.id = 0
        self.name = ""
        self.passwd = ""
        self.isLogin = False
        self.conn = conn
    def getUser(self, user):
        self.id, self.name, self.passwd = g_dbConn.getUserInfo(user)
        