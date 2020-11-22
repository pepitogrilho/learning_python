# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#(pyton-list) > (an excel-horizontal-range)
l1 = [1, 2, 3, 4]
sh.range("A1").value = l1

#(excel-horizontal-range) > (pyton-list)
l2 = sh.range("A1:D1").value
print(l2)

#(1 value) > (an excel-horizontal-range)
v1 = "eeoo"
sh.range("A2:D2").value = v1






#wb.close()
