# -*- coding: utf-8 -*-
"""
"""

import time
import pyautogui as auto

#auto.moveTo(100, 100, duration=1)

time.sleep(10)

i = 1
while i > 0:
    print(i)
    auto.dragRel(10, 0, duration=1)
    auto.dragRel(0, 10, duration=1)
    auto.dragRel(-10, 0, duration=1)
    auto.dragRel(0, -10, duration=1)
    time.sleep(10)
    i+=1 
    