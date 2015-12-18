from acceptor import Acceptor
from event import EventModule
if __name__ == '__main__':
    acc = Acceptor(9527)
    em = EventModule()
    em.addConn(acc)
    while True:
        print("running...")
        em.process()
        print("**********")