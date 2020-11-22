# -*- coding: utf-8 -*-
"""
"""

#[LISTs] are defined in squared brackets
friends = ["Bob", "Rolf", "Anne"]

#{SETs} 
# - difference to LISTS: canN0T contain duplicated elements
# - difference to LISTS & TUPLEs : the order is not guaranteed 
friends = {"Bob", "Rolf", "Anne"}


#Differece
friends_boys = {"Bob", "Rolf"}
friends_girls = friends.difference(friends_boys)
print(friends_girls)

#Union
friends = friends_boys.union(friends_girls)
print(friends)

#Intersection
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

art_and_science = art.intersection(science)
print(art_and_science)