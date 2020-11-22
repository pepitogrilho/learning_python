# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:50:51 2020

@author: RICARDO
"""


# SHOW (index)+(value) with ENUMERATE
nums=[55,44,33,22,11]
for n in enumerate(nums):
    print(n)

#is X in list? ...................................
words_01=["spam", "egg", "spam", "sausage"]
print("list of works:",end=''); print(words_01)

b01 = "spam" in words_01
print("Is \"spam\" in words?:" + str(b01))

b02 = "SPAM" not in words_01
print("Is NOT \"SPAM\" in words?:" + str(b02))

# ALL members fit the condition?
nums=[55,44,33,22,11]
if all([i>10 for i in nums]):
    print("All larger than ",10)

# ANY member fits the condition?
nums=[55,44,33,22,11]
if any([i>50 for i in nums]):
    print("At least one larger than ",50)
