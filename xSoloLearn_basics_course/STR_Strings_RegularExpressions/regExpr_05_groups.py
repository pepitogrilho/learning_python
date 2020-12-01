# -*- coding: utf-8 -*-
"""
Groups can be created by surrounding part of a regular expression with parentheses
"""


import re

pattern = r"a(bc)(de)(f(g)h)i"

test_string = "abcdefghijklmnop"

match = re.match(pattern, test_string)

if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.groups())
