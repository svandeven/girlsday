import subprocess as sp
import time

def clear():
    sp.call('clear',shell=True)
def sleep(sec):
    time.sleep(sec)
    
def moveDown(frame, delta):
    clear()
    for l in range (0, delta):
        print ""
    print frame
    
def moveUp(frame, delta):
    clear()