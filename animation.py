#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time

sun = """
       xx        xXx        xx       
       X X       X X       X X       
  xx    X X      X X      X X    xx  
  X X    X X     X X     X X    X X  
   X X    X X  XXXXXXX  X X    X X   
    X X    XXXXX     XXXXX    X X    
     X X  XX             XX  X X     
      X XX                 XX X      
       XX   XXX      XXX    XX       
 xxxxxxXX  XX XX    XX XX    Xxxxxxx 
X      X   XXXXX    XXXXX    X      X
 xxxxxxX    XXX      XXX     Xxxxxxx 
       X                     X       
       XX                    X       
      X XX     XXXXXXX      X X      
     X X  X               XX X X     
    X X    XX           XX    X X    
   X X     X XXXXXXXXXXX X     X X   
  X X     X X    X X    X X     X X  
  xx     X X     X X     X X     xx  
        X X      X X      X X        
       X X       X X       X X       
       xx        xXx        xx       
"""

sun2 = """
       xx        xXx        xx       
       X X       X X       X X       
  xx    X X      X X      X X    xx  
  X X    X X     X X     X X    X X  
   X X    X X  XXXXXXX  X X    X X   
    X X    XXXXX     XXXXX    X X    
     X X  XX             XX  X X     
      X XX                 XX X      
       XX   XXX      XXX    XX       
 xxxxxxXX  XXXXX    XXXXX    Xxxxxxx 
X      X   XX XX    XX XX    X      X
 xxxxxxX    XXX      XXX     Xxxxxxx 
       X                     X       
       XX      x     x        X       
      X XX      XXXXX      X X      
     X X  X               XX  X X     
    X X    XX           XX      X X    
   X X     X XXXXXXXXXXX X        X X   
  X X     X X    X X    X X         X X  
  xx     X X     X X     X X         xx  
        X X      X X      X X        
       X X       X X       X X       
       xx        xXx        xx       
"""

minion = """
          ███████████████
        █                 █
      █                     █
     █        ███████        █
    █        █████████        █
    █       ██▀     ▀██       █
   ███████████  █▀█  ███████████
   ███████████  ▀▀▀  ███████████
    █       ▀██     ██▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀█████████▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌███████████████████▐▓▓▌▌
   █  ▐▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓███████▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ██  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  ██
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌  █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         █████▀    ▀█████
         ▀▀▀▀        ▀▀▀▀ 
"""

minion2 = """
          ███████████████
        █                 █
      █                     █
     █        ███████        █
    █        █████████        █
    █       ██▀     ▀██       █
   ███████████    █▀████████████
   ███████████    ▀▀▀███████████
    █       ▀██     ██▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀█████████▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌███████████████████▐▓▓▌▌
   █  ▐▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓███████▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ██  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  ██
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         █████▀    ▀█████
         ▀▀▀▀        ▀▀▀▀
"""
minion3 = """
          ███████████████
        █                 █
      █                     █
     █        ███████        █
    █        █████████        █
    █       ██▀     ▀██       █
   ████████████▀█    ███████████
   ███████████▀▀▀    ███████████
    █       ▀██     ██▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀█████████▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌███████████████████▐▓▓▌▌
   █  ▐▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓███████▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ██  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  ██
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         █████▀    ▀█████
         ▀▀▀▀        ▀▀▀▀
"""

def clearScreen():
    sp.call('clear',shell=True)

i = 0
# while i < 1000:
#     clearScreen()
#     print minion
#     time.sleep(0.1)
#
#     clearScreen()
#     print minion2
#     time.sleep(0.1)
#
#     clearScreen()
#     print minion
#     time.sleep(0.1)
#
#     clearScreen()
#     print minion3
#     time.sleep(0.1)
#     i = i + 100
    
while i < 1000:
    clearScreen()
    print sun
    time.sleep(0.1)

    clearScreen()
    print sun2
    time.sleep(0.1)
    i = i + 100