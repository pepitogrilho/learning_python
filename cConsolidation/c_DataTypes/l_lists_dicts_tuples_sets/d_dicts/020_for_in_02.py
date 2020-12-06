# -*- coding: utf-8 -*-

"""
"""

#Update the same way as lists: 
ages={"Dave":24, "Mary":42, "John":58}

stuCheck = "Bob"
#stuCheck = "Dave"

if stuCheck in ages:
    print(f"{stuCheck}: {ages[stuCheck]} is registered")
else:
    print(f"{stuCheck} is NOT registered")
    