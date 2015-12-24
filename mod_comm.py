from conn import IPC
import socket
MOD_LOGIN = 0
MOD_MSG = 1
g_mods = dict()
class Mods:
    def __init__(self, cmd, mod):
        self.cmd, self.mod = cmd,mod
        self.buf = None

#todo
class ModsIPC(IPC):
    def __init__(self, cmd):
        self.cmd = cmd
        self.rfd, self.wfd = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
        IPC.__init__(self, self.wfd)
    def handleRead(self):
        IPC.handleRead(self)
        self.buf = getModuleBuf(self.cmd)
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
        self.ipc = ModsIPC(cmd)
        pass
    def write(self, buf):
        return self.ipc.write(buf)
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
        print("***********cmd: {0}, value:{1}*******".format(cmd, value))
        print(value.mod.ipc)
         
        print("returnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        yield value.mod.ipc
        
    