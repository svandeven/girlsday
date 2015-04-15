#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import time

minion = """
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █                 █
      █                     █
     █        ▄▄▄▄▄▄▄        █
    █        █████████        █
    █       ██▀     ▀██       █
   ███████████  █▀█  ███████████
   ███████████  ▀▀▀  ███████████
    █       ▀█▄     ▄█▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀▄▄▄▄▄▄▄▄▄▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
   █  ▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ▄█  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  █▄
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌  █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         ▄████▀    ▀████▄
         ▀▀▀▀        ▀▀▀▀
"""

minion2 = """
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █                 █
      █                     █
     █        ▄▄▄▄▄▄▄        █
    █        █████████        █
    █       ██▀     ▀██       █
   ███████████    █▀████████████
   ███████████    ▀▀▀███████████
    █       ▀█▄     ▄█▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀▄▄▄▄▄▄▄▄▄▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
   █  ▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ▄█  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  █▄
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         ▄████▀    ▀████▄
         ▀▀▀▀        ▀▀▀▀
"""
minion3 = """
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █                 █
      █                     █
     █        ▄▄▄▄▄▄▄        █
    █        █████████        █
    █       ██▀     ▀██       █
   ████████████▀█    ███████████
   ███████████▀▀▀    ███████████
    █       ▀█▄     ▄█▀       █
    █         ▀█████▀         █
    █                         █
    █      ▀▄▄▄▄▄▄▄▄▄▀        █
   ▐▓▓▌                     ▐▓▓▌
   ▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
   █  ▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌  █
  █  ▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ▐  █
  █  █ ▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌ █  █
  █  █ ▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌ █  █
  █  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  █
 ▄█  █▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█  █▄
 █████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ █████
 ██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌ ██████
  ▀█▀█  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   █▀█▀
         ▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
          ▐▓▓▓▓▌  ▐▓▓▓▓▌
         ▄████▀    ▀████▄
         ▀▀▀▀        ▀▀▀▀
"""

def clearScreen():
    sp.call('clear',shell=True)

i = 0
while i < 1000:
    clearScreen()
    print minion
    time.sleep(0.1)

    clearScreen()
    print minion2
    time.sleep(0.1)
    
    clearScreen()
    print minion
    time.sleep(0.1)
    
    clearScreen()
    print minion3
    time.sleep(0.1)
    i = i + 100