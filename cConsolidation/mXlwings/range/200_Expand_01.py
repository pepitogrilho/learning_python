# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]

#Populate
m1 = [["1.1", "1.2", "1.3"],
      ["2.1", "2.2", "2.3"],
      ["3.1", "3.2", "3.3"]]
sh.range("A1").value = m1

#Read from "A1" all cells available at the right
r1 = sh.range("A1").expand("right").value
print(r1)

#Read from "A1" all cells available downwards
c1 = sh.range("A1").options(ndim=2, expand="down").value
print(c1)

#Read from "A1" all cells available in the matrix
m1 = sh.range("A1").expand("table").value
print(m1)

#Read from "A1" all cells available in the matrix
m2 = sh.range("A1").expand().value
print(m2)

#wb.close()
