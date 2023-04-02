# -*- coding: utf-8 -*-
"""
"""

import pandas as pd


data = {
  'id': ['A','B','C'],
  'c1': [10, 11, 12],
  'c2': [20, 21, 22],
  'c3': [30, 31, 32]
      }
df1 = pd.DataFrame(data)
print(df1)

print("-"*30)

df2=df1.set_index('id')
print(df2)

print("-"*30)

print(df2[['c1','c2']])

print("-"*30)

print(df2['c1'][0:2])

print("-"*30)

print(df2.columns)