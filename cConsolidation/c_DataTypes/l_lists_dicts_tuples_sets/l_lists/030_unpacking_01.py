# -*- coding: utf-8 -*-

"""
"""

#unpacking
t = 5, 10
x, y = t
print(x, y)

#unpacking
numbers=[1,2,3,4,5,6,7,8,9]
a,b,*c,d=numbers
print(a,b,c,d)
a,b,c,*d,e=numbers
print(a,b,c,d,e)


