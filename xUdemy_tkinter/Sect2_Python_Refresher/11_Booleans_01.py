# -*- coding: utf-8 -*-
"""
"""

stringA = ["a", "b"]
stringB = ["a", "b"]

print(stringA == stringB)
print(stringA is stringA)

print(stringA is stringB)
stringB = stringA
print(stringA is stringB)
