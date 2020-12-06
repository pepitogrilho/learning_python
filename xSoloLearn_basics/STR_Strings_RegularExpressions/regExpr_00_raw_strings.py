# -*- coding: utf-8 -*-
"""
- Problem with regex (regular expressions):
For escaping special characters like "$" or " " " ...
... we use "\", but the code is difficult to read
- Solution: "raw string": r"hola$caracola"
"""

rawString = r"hola$caracola"
print(rawString)