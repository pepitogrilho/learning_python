# -*- coding: utf-8 -*-

"""
The None object represent absence of a value = NULL
"""

if None==None:
    print("Nooooone1 !")

if ""==None:
    print("Nooooone2 !")

if []==None:
    print("Nooooone3 !")

None

print(None)



"""
The None object is returned by a function that doesn't return anything
"""

def hello():
    print("hello")
    
hello_output = hello()
if hello_output == None:
    print("NooooOoooone!")
