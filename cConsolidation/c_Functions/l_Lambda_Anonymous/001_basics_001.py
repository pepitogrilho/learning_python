# -*- coding: utf-8 -*-
"""
Python Anonymous/Lambda Functions
-> Defined without a name
-> lambda arguments: expression
-> We use lambda functions when we need a nameless function for a short period of time
"""


double = lambda x: x * 2
double_of_3 = double(3); print(double_of_3)


mult = lambda x,y: x * y
mult_2_3 = mult(2,3); print(mult_2_3)


mult_2_3 = (lambda x,y: x*y)(2,3); print(mult_2_3)