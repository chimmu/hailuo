import mod_comm
from mod_comm import IpcMsg
from user import User
import req
#TODO
class ModMsg(mod_comm.Module):
    def __init__(self, cmd):
        mod_comm.Module.__init__(self, cmd)
        self.users = dict()
#         self.sock = sock
    def handleIPC(self, msg):
        mod_comm.Module.handleIPC(self, msg)
        if msg.reqcmd == req.REQ_USER_LOGIN:
            self.users[msg.msg.id] = msg.msg
        return True
    def handle(self,  conn, data):
        mod_comm.Module.handle(self,  conn, data)
        id = data['to']
#         print("id is {0}".format())
#         self.users[id].conn.write(mod_comm.MOD_MSG, 'gannnnnnnnnnnnnnn')
        self.users[id].conn.write(mod_comm.MOD_MSG, data['msg'].encode("utf8"))
        return True
mod_comm.registerModule(ModMsg(mod_comm.MOD_MSG), mod_comm.MOD_MSG)