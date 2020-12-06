# -*- coding: utf-8 -*-
"""
"""

from itertools import product, permutations

#product
letters_A_B=("A", "B")
product_A_B=product(letters_A_B, range(2))
print(list(product_A_B))

#permutations
letters_A_B=("A", "B")
permutations_A_B=permutations(letters_A_B)
print(list(permutations_A_B))