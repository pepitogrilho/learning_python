# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


#(python-matrix) > (excel-matrix)
m1 = [["1.1", "1.2", "1.3"],
      ["2.1", "2.2", "2.3"],
      ["3.1", "3.2", "3.3"]]
sh.range("A1").value = m1


# (matrix-range) > (smaller matrix)
m2 = sh.range("A1:B2").value
print(m2)

# transposing matrix
m3 = sh.range("A1:B2").options(transpose = True).value
print(m3)




#wb.close()
