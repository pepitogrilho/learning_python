# -*- coding: utf-8 -*-

"""
"""

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")    
 ]


users_dict = {user[1]: user[2] for user in users}