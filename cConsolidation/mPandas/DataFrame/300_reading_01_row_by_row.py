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
df2=df1.set_index('id')
print(df2)

for index, row in df2.iterrows():
    print(index, row['c1'], row['c2'])