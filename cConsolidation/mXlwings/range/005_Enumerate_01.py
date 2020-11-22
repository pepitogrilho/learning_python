# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]


e=enumerate(sh.range("A1:D4"))
print(list(e))


#wb.close()
