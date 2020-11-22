# -*- coding: utf-8 -*-

"""
Tuples are like lists, but cannot be changed
Tuples = Constant/Immutable lists
Tuples are faster than lists, but cannot be changed
"""

words=("spam", "eggs", "sausages")
print(words)
print(words[0])

#TypeError:
words[0]="Spam"

"""
Tuples can be created without parenthesis:
"""
wordss="ssppaamm", "eeggggss", "ssaauussaaggeess"
print(wordss)
print(wordss[0])