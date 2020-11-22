# -*- coding: utf-8 -*-
"""
To INSTALL xlwings add-in in Excel:...
...> From anaconda-prompt:> xlwings addin install 
To REMOVE xlwings add-in in Excel:...
...> From anaconda-prompt:> xlwings addin remove 
"""

import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt


app = xw.apps.active
#Open workbook
wb = xw.Book("hello.xlsx")
inp = wb.sheets[0]



wb.close()
