# -*- coding: utf-8 -*-
"""
"""

#[LISTs] are defined in squared brackets
l = ["Bob", "Rolf", "Anne"]

#(TUPLEs) 
# - difference to LISTS: canN0T be CHANGED (tuples="constant-lists")
t = ("constant-Bob", "constant-Rolf", "constant-Anne")

#{SETs} 
# - difference to LISTS: canN0T contain duplicated elements
# - difference to LISTS & TUPLEs : the order is not guaranteed 
s = {"Bob", "Rolf", "Anne"}


#Accessing: by index in Lists+Tuples, not in Sets
print(f"l[0]={l[0]}, l[1]={l[1]}, l[2]={l[2]}")
print(f"t[0]={t[0]}, t[1]={t[1]}, t[2]={t[2]}")
try:
  print(f"s[0]={s[0]}, s[1]={s[1]}, s[2]={s[2]}")
except TypeError:
  print("We got a TypeError by accessing a set like a list: s[0]")
for i in s:
  print(f"s[?]={i}")
  
  
#Adding elements
l.append("Ric"); print(l)
s.add("Ric"); print(s)

#Removing elements
l.remove("Bob"); print(l)