# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#(python-list) > (an excel-vertical-range)
l1 = [1, 2, 3, 4]
sh.range("A1:A4").options(transpose = True).value = l1





#wb.close()
