#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time
from girlsday import *
from minion import *
from sun import *



i = 0
while i < 10:
    i = i + 1
    show(minion)
    show(minion2)
    show(minion)
    show(minion3)

i = 0
while i < 5:
    i = i + 1
    
    show(sun1)
    show(sun2)
    show(sun3)    
    moveDown(sun3, 1)
    moveDown(sun3, 2)
    moveDown(sun3, 3)
    moveUp(sun1, 1)
    moveUp(sun2, 2)
    moveUp(sun3, 3)
    moveRight(sun1, 10)
    moveRight(sun2, 20)
    moveRight(sun3, 30)
    moveRight(sun2, 40)
    moveRight(sun3, 50)
    moveRight(sun2, 40)
    moveRight(sun3, 30)
    moveRight(sun2, 20)
    moveRight(sun1, 10)
    moveLeft(sun1, 1)
    moveLeft(sun2, 2)
    moveLeft(sun3, 3)