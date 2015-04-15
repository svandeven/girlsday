#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time
from girlsday import *
from minion import *
from sun import *



i = 0
while i < 1000:
    clear()
    print minion
    sleep(0.1)

    clear()
    print minion2
    sleep(0.1)

    clear()
    print minion
    sleep(0.1)

    clear()
    print minion3
    sleep(0.1)
    i = i + 100

i = 0
while i < 1000:
    clear()
    print sun1
    sleep(0.1)

    clear()
    print sun2
    sleep(0.1)
    
    clear()
    print sun3
    sleep(0.1)
    
    clear()
    moveDown(sun3, 1)
    sleep(0.1)
    
    clear()
    moveDown(sun3, 2)
    sleep(0.1)
    
    clear()
    moveDown(sun3, 3)
    sleep(0.1)
    
    clear()
    moveUp(sun3, 1)
    sleep(0.1)

    clear()
    moveUp(sun3, 2)
    sleep(0.1)

    clear()
    moveUp(sun3, 3)
    sleep(0.1)

    clear()
    moveRight(sun3, 1)
    sleep(0.1)

    clear()
    moveRight(sun3, 2)
    sleep(0.1)

    clear()
    moveRight(sun3, 3)
    sleep(0.1)    
    
    i = i + 100
