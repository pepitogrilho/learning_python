# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#############################################################
#(python-list) > (an excel-VERTICAL-range)
lv1 = [1, 2, 3, 4]
sh.range("A1").options(transpose = True).value = lv1
#(excel-HORIZONTAL-range) > (pyton-list)
lv2 = sh.range("A1:A4").value
print(lv2)
#(excel-HORIZONTAL-range) > (pyton-list)
lv3 = sh.range("A1:A4").options(ndim=2).value
print(lv3)
#############################################################

#############################################################
#(python-list) > (an excel-VERTICAL-range)
lv4 = [[7], [8], [9], [10]]
sh.range("A7").value = lv4
#############################################################






#wb.close()
