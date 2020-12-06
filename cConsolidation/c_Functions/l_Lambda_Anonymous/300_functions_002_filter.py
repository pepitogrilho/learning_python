# -*- coding: utf-8 -*-
"""
#Program to filter out only the even items from a list
"""



nums = [1,5,4,6,8,11,3,12]
nums_filtered = list(filter(lambda x:(x%2 == 0), nums))
print(nums_filtered)

