# -*- coding: utf-8 -*-

"""
Sets are similar to lists or dictionaries, but are
- unordered
- unidexed
"""

#1st way for creating a SET: directly
num_set = {1, 2, 3, 4, 5}
print(num_set)


#2nd way for creating a SET: list > set(list)
word_list = ["spam", "eggs", "sausage"]
word_set = set(word_list)
print(word_set)
