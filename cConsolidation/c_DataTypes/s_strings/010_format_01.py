# -*- coding: utf-8 -*-

"""
the string "format" method
"""
l01=[4,5,6]
msg="numbers: {0},{1},{2}".format(l01[2],l01[1],l01[0])
print(msg)

#
print("{0}{1}{0}".format("abra","cad"))

#
print("{x},{y}".format(x=5,y=6))

#
print("{c},{b},{a}".format(a=5,b=9,c=7))

#
friend="Juan"
print(f"{friend} is my friend")

#
friend="Juan"
print(f"{friend!r} is my friend")