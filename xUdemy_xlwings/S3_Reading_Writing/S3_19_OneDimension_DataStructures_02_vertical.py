# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#(1 value) > (an excel-vertical-range)
v1 = "eeoo"
sh.range("A1:A4").value = v1

#(an excel-vertical-range) > (list)
vl1 = sh.range("A1:A4").value
print(vl1)





#wb.close()
