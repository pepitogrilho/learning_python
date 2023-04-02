# -*- coding: utf-8 -*-
"""
"""

import pandas as pd


data = {
  'c1': [10, 11, 12],
  'c2': [20, 21, 22],
  'c3': [30, 31, 32]
      }
df1 = pd.DataFrame(data)
print(df1)

print("-"*50)

df2 = pd.DataFrame(data,index=['A','B','C'])
print(df2)

