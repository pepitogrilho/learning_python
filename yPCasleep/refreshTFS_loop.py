# -*- coding: utf-8 -*-
"""
"""

import time
import pyautogui as auto

auto.moveTo(1750, 250, duration=1)

i_sleep = 5
i_slept = 0
i_max = 60*60
while i_slept < i_max:
    #auto.dragRel(10, 0, duration=1)
    #auto.dragRel(0, 10, duration=1)
    #auto.dragRel(-10, 0, duration=1)
    #auto.dragRel(0, -10, duration=1)
    auto.click()
    time.sleep(i_sleep)
    i_slept+=i_sleep 
    print(i_slept)
    