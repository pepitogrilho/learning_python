# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]

############ HORIZONTAL ###########################

#(pyton-list) > (an excel-HORIZONTAL-range)
lh1 = [1, 2, 3, 4]
sh.range("A1").value = lh1

#(excel-HORIZONTAL-range) > (pyton-list)
lh2 = sh.range("A1:D1").value
print(lh2)

############ HORIZONTAL ###########################


############ VERTICAL #############################

#(python-list) > (an excel-VERTICAL-range)
lv1 = [1, 2, 3, 4]
sh.range("A1").options(transpose = True).value = lv1

#(excel-HORIZONTAL-range) > (pyton-list)
lv2 = sh.range("A1:A4").value
print(lv2)

############ VERTICAL #############################




#wb.close()
