# -*- coding: utf-8 -*-

"""
List comprehensions obey a simple rules
"""

#from 1 to 6
from_1_to_6 = [i+1 for i in range(6)]
print(from_1_to_6)

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
