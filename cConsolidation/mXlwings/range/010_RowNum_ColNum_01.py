# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]

#..............SUM.........................
f_ini=2
f=f_ini
c=4
n=10

while f < f_ini+n:
  sh.range(f,c).value = f
  f+=1

sh.range("D1").formula = "=SUM(D2:D11)"

formula01 = sh.range("D1").formula
print(formula01)
#..............SUM.........................

#wb.close()
