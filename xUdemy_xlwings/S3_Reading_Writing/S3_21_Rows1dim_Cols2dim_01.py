# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#(python-list) > (an excel-vertical-range)
m1 = [["1.1", "1.2", "1.3"],
      ["2.1", "2.2", "2.3"],
      ["3.1", "3.2", "3.3"]]
sh.range("A1").value = m1

# (horiz-range) + (ndim=1) > (row)
r1 = sh.range("A1:C1").options(ndim = 1).value
print(r1)

# (vert-range) + (ndim=2) > (col)
c1 = sh.range("A1:A3").options(ndim = 2).value
print(c1)

# (vert-range) + (ndim=1) > (row)
l3 = sh.range("A1:A3").options(ndim = 1).value
print(l3)

# (horiz-range) + (ndim=2) > (???)
l4 = sh.range("A1:C1").options(ndim = 2).value
print(l4)


#wb.close()
