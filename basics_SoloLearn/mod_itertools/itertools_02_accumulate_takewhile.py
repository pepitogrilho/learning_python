# -*- coding: utf-8 -*-
"""
- accumulate returns a total of values inan iterable
- takewhile takes items from an iterable while a predicate function remains true
"""

from itertools import accumulate, takewhile

#accumulate
range_8 = range(8); print(list(range_8))
acc_8 = accumulate(range_8)
list_acc_8 = list(acc_8)
print(list_acc_8)

#takewhile
takewhile_6 = takewhile(lambda x: x<=6, list_acc_8)
list_takewhile_6=list(takewhile_6)
print(list_takewhile_6)