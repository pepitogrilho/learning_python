# -*- coding: utf-8 -*-

"""
List comprehensions obey a simple rules
"""

#evens_v1
evens_0_10 = [i*2 for i in range(6)]
print(evens_0_10)

#exponential
cubes_0_4 = [i**3 for i in range(5)]
print(cubes_0_4)

#evens_v1
evens_0_10_v2 = [i for i in range(11) if i%2==0]
print(evens_0_10_v2)

#multiples_of_3
multiples_of_3 = [i for i in range(21) if i%3==0]
print(multiples_of_3)
