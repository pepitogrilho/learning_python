# -*- coding: utf-8 -*-

"""
Updating and appending
"""

#Update the same way as lists: 
ages={"Dave":24, "Mary":42, "John":58}
ages["Dave"]=ages["Dave"]+1
print(ages["Dave"])

#Append in a different way
ages["Pete"]=30
print(ages["Pete"])



#is X in dict? ...................................
print("ages:",end=''); print(ages)
print("Is \"Dave\" in ages?:" + str("Dave" in ages))
print("Is NOT \"Johnny\" in ages?:" + str("Johnny" not in ages))