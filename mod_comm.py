MOD_LOGIN = 0
g_mods = dict()
class Module:
    def __init__(self):
        pass
    def handle(self, conn, data):
        pass
    
def registerModule(mod, cmd):
    g_mods[cmd] = mod
    
def getModule(cmd):
    return g_mods[cmd]

def delModule(cmd):
    g_mods[cmd] = None