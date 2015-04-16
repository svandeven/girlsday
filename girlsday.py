#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time

sleepTime = 0.2

def clear():
    sp.call('clear',shell=True)
def sleep(sec):
    time.sleep(sec)
    
def show(frame):
    clear()
    print frame
    sleep(sleepTime)
    
def moveDown(frame, delta):
    clear()
    for l in range (0, delta):
        print ""
    print frame
    sleep(sleepTime)
    
def moveUp(frame, delta):
    clear()
    i = 1
    for l in frame.splitlines():
        if i > delta:
            print l
        i += 1
    sleep(sleepTime)
        
def moveRight(frame, delta):
    clear()
    prefix = ""
    for i in range(0,delta):
        prefix += " "
    for l in frame.splitlines(): 
        print prefix + l
    sleep(sleepTime)
        
def moveLeft(frame, delta):
    clear()
    for l in frame.splitlines(): 
        print l[delta-1:]
    sleep(sleepTime)        