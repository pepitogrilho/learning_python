# -*- coding: utf-8 -*-
"""
map(function,list)
-> map apply the function to the list
"""


#............................................

def add_five(x):
    return x+5

nums=[11,22,33,44,55]

nums_plus_5_map = map(add_five,nums)

nums_plus_5_list = list(nums_plus_5_map); print(nums_plus_5_list)
#............................................

nums=[11,22,33,44,55]

nums_plus_5 = list(map(lambda x:(x + 5), nums))

print(nums_plus_5)

