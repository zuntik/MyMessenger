import socket
from threading import Thread

PORT=12345


def clientlistener(socket,mlist):
    """Deals with receiving text"""
    while True:
        data = socket.recv(1024)
        mlist.append(data.decode())
        if not data: break
    mlist.append("Someone has become offline")




def sender(clist,mlist):
    """Deals with sending text to everyone"""
    while True:
        if len(mlist) != 0:
            m = mlist.pop(0)
            for c in clist:
                c.send(m)







serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), PORT))
serversocket.listen(200)

clientlist=list()
messagequeue=list()

Thread(target=sender(clientlist,messagequeue)).start()

while True:

    clientsocket, address = serversocket.accept()
    
    Thread(target=clientlistener(clientsocket,messagequeue)).start()

    


