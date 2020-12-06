# -*- coding: utf-8 -*-

"""
"""

def double(x):
    return x*2

l=[1,2,3,4,5]

l2_c = [double(x) for x in l]  ; print(l2_c)

l2_m = map(double,l)           ; print(list(l2_m))
