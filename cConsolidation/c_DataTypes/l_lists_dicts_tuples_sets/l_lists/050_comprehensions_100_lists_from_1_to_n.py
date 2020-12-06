# -*- coding: utf-8 -*-

"""
"""


l04 = list(range(5))                         ;print(l04)    

l15 = [(lambda x:x+1)(x) for x in l04]       ;print(l15)



l15 = [(lambda x:x+1)(x) for x in range(5)]  ;print(l15)