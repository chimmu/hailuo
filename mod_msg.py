import mod_comm

#TODO
class ModMsg(mod_comm.Module):
    def __init__(self, cmd):
        mod_comm.Module.__init__(self, cmd)
#         self.sock = sock
    def handle(self, conn, data):
        mod_comm.Module.handle(self, conn, data)
        
mod_comm.registerModule(ModMsg(mod_comm.MOD_MSG), mod_comm.MOD_MSG)