# -*- coding: utf-8 -*-
"""
cont counts up infinitely from a value
"""

from itertools import count

for i in count(3):
  print(i)
  if i >=11:
      break

