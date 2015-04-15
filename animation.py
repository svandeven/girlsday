#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time
from girlsday import *
from minion import *
from sun import *



i = 0
while i < 1000:

    show(minion)
    sleep(0.1)

    show(minion2)
    sleep(0.1)

    show(minion)
    sleep(0.1)

    show(minion3)
    sleep(0.1)
    i = i + 100

i = 0
while i < 5:
    i = i + 1
    
    show(sun1)
    sleep(0.1)

    show(sun2)
    sleep(0.1)
    
    show(sun3)
    sleep(0.1)
    
    moveDown(sun3, 1)
    sleep(0.1)

    moveDown(sun3, 2)
    sleep(0.1)

    moveDown(sun3, 3)
    sleep(0.1)

    moveUp(sun1, 1)
    sleep(0.1)

    moveUp(sun2, 2)
    sleep(0.1)

    moveUp(sun3, 3)
    sleep(0.1)

    moveRight(sun1, 10)
    sleep(0.1)

    moveRight(sun2, 20)
    sleep(0.1)

    moveRight(sun3, 30)
    sleep(0.1)  
    
    moveRight(sun3, 40)
    sleep(0.1)  
    
    moveRight(sun3, 50)
    sleep(0.1)
    
    moveRight(sun3, 40)
    sleep(0.1)
    
    moveRight(sun3, 30)
    sleep(0.1)
    
    moveRight(sun2, 20)
    sleep(0.1)
    
    moveRight(sun1, 10)
    sleep(0.1)
    
    moveLeft(sun1, 1)
    sleep(0.1)

    moveLeft(sun2, 2)
    sleep(0.1)
    
    moveLeft(sun3, 3)
    sleep(0.1)
    

