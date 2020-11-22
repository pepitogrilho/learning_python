# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np


app = xw.apps.active

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\CaseStudy_1.xlsx"
wb = xw.Book(path_01)

sheetName = "Sheet1"

for sh in wb.sheets:
  if sh.name == sheetName:
    sheet0 = sh

sheet0.range("B1").name = "Saving"
sheet0.range("B2").name = "Interest_Rate"
sheet0.range("B3").name = "Periods"
sheet0.range("B4").name = "Future_Value"

fv = -np.fv(rate = sheet0.range("Interest_Rate").value,
            nper = sheet0.range("Periods").value,
            pmt = 0,
            pv = sheet0.range("Saving").value
            )

#print("fv = {:.2f}".format(fv))
sheet0.range("Future_Value").value = fv

#wb.close()
