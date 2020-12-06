# -*- coding: utf-8 -*-
"""
"""

def firstn(n):
  num, nums = 0, []
  while num < n:
    nums.append(num)
    num += 1
  return nums

print(firstn(5))
print(sum(firstn(5)))

#............................................

def firstn(n):
  num = 0
  while num < n:
    yield num
    num += 1

print(list(firstn(5)))
print(sum(firstn(5))) 
