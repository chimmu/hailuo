from conn import IPC
from copy import deepcopy
import socket
MOD_LOGIN = 0
MOD_MSG = 1

# REQ_TYPE_IPC  = 0
# REQ_TYPE_SOCKET = 1
g_mods = dict()
class Mods:
    def __init__(self, cmd, mod, buf = None):
        self.cmd, self.mod = cmd,mod
        self.buf = buf

class IpcMsg:
    def __init__(self, reqfrom, reqcmd, msg):
        self.reqfrom = reqfrom
        self.reqcmd = reqcmd
        self.msg = msg
#todo
class ModsIPC(IPC):
    def __init__(self, cmd, mod):
        self.cmd = cmd
        self.mod = mod
        self.rfd, self.wfd = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
        IPC.__init__(self, self.wfd)
    def handleRead(self):
        IPC.handleRead(self)
        self.buf = getModuleBuf(self.cmd)
        self.mod.handleIPC(self.buf)
#         return self.mod.handle(REQ_TYPE_IPC, self, self.buf)
        print("read buf: {0}".format(self.buf))
        return True
    def write(self, buf):
        try:
            self.rfd.send(buf)
            return True
        except socket.error as e:
            print(e)
            return False
class Module:
    def __init__(self, cmd):
        self.ipc = ModsIPC(cmd, self)

    def write(self, buf):
        return self.ipc.write(buf)
    def handleIPC(self, msg):
        pass
    def handle(self, conn, data):
        pass
    
def registerModule(mod, cmd):
    g_mods[cmd] = Mods(cmd, mod)
    
def getModule(cmd):
    return g_mods[cmd].mod

def delModule(cmd):
    g_mods[cmd] = None
    
def sendModuleBuf(cmd, buf):
    g_mods[cmd].buf = buf
    g_mods[cmd].mod.write(b'fuck')
    
def getModuleBuf(cmd):
    return g_mods[cmd].buf 

def getIpcs():
    for (cmd, value) in g_mods.items():
        yield value.mod.ipc
        
    