#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time
import random

sleepTime = 0.2

colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[34m',
        '\033[32m']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    sp.call('clear',shell=True)
def sleep(sec):
    time.sleep(sec)
def colourful(frame):
    color = random.choice(colors)
    return color + frame + bcolors.ENDC
    
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