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
import req
class ModLogin(mod_comm.Module):
    def __init__(self, cmd):
        mod_comm.Module.__init__(self, cmd)
        self.logins = dict()
    def handleIPC(self, msg):
        mod_comm.Module.handleIPC(self, msg)
        pass
    def handle(self,  conn, data):
        mod_comm.Module.handle(self, conn, data)
        user = User(conn)
        user.getUser(data['username'])
        if user.passwd == data['passwd']:
            user.isLogin = True
            conn.write(mod_comm.MOD_LOGIN, 'login success'.encode(encoding='utf_8', errors='strict'))
            mod_comm.sendModuleBuf(mod_comm.MOD_MSG, mod_comm.IpcMsg(mod_comm.MOD_LOGIN, req.REQ_USER_LOGIN, user))
        else:
            conn.write(mod_comm.MOD_LOGIN, 'login failed'.encode(encoding='utf_8', errors='strict'))
        return True

mod_comm.registerModule(ModLogin(mod_comm.MOD_LOGIN), mod_comm.MOD_LOGIN)     