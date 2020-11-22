# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]

#(python-matrix) > (excel-matrix)
m1 = [["1.1", "1.2", "1.3", "1.4"],
      ["2.1", "2.2", "2.3", "2.4"],
      ["3.1", "3.2", "3.3", "3.4"],
      ["4.1", "4.2", "4.3", "4.4"]]
sh.range("A1").value = m1

r1 = sh.range("A1:D1")[0].value; print(r1)
r2 = sh.range("A1:D1")[3].value; print(r2)

r3 = sh.range("A1:D1")[0:2].value; print(r3)
r4 = sh.range("A1:D1")[0:1].value; print(r4)
r5 = sh.range("A1:D1")[0:3].value; print(r5)

r6 = sh.range("A1:D1")[-2:].value; print(r6)

r7 = sh.range("A1:D4")[0].value; print(r7)
r8 = sh.range("A1:D4")[4].value; print(r8)
r9 = sh.range("A1:D4")[8].value; print(r9)
r10 = sh.range("A1:D4")[12].value; print(r10)


r11 = sh.range("A1:D4")[0, 0].value; print(r11)
r12 = sh.range("A1:D4")[3, 3].value; print(r12)

r13 = sh.range("A1:D4")[0, :].value; print(r13)
r14 = sh.range("A1:D4")[2, :].value; print(r14)

r15 = sh.range("A1:D4")[:, 0].value; print(r15)

r16 = sh.range("A1:D4")[:2, 0].value; print(r16)

r17 = sh.range("A1:D4")[-2:, 0].value; print(r17)

#wb.close()
