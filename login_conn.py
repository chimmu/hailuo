# from conn import Connection
# from db import g_dbConn

# class LoginMod(Connection):
#     def __init__(self, cli):
#         self.sock = cli
#     def handleRead(self):
#         ret = Connection.handleRead(self)
#         if ret == False:
#             return False
#         ret = g_dbConn.checkPasswd(self.buf['user'], self.buf['passwd'])
#         if ret == False:
#             print("login failed")
#             return False
#         print("login success")
#         self.write(b'fuck')
#         return True

from user import User
import mod_comm 
class ModLogin(mod_comm.Module):
    def __init__(self):
        pass
    def handle(self, conn, data):
        mod_comm.Module.handle(self, conn, data)
        user = User()
        user.getUser(data['username'])
        if user.passwd == data['passwd']:
            conn.write(b'login success')
        else:
            conn.write(b'login failed')
        return True

mod_comm.registerModule(ModLogin(), mod_comm.MOD_LOGIN)     