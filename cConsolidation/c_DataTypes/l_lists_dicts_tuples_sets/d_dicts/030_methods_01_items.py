# -*- coding: utf-8 -*-

"""
Updating and appending
"""

#Update the same way as lists: 
ages={"Dave":24, "Mary":42, "John":58}
print(ages); print(type(ages))

ages_items = ages.items()
print(ages_items);print(type(ages_items))

ages_items_list = list(ages_items)
print(ages_items_list);print(type(ages_items_list))
print(type(ages_items_list[0]))