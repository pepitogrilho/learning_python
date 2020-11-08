# -*- coding: utf-8 -*-
"""
"""

name = "Bob"
print(f"Hello, {name}")
name = "Joe"
print(f"Hello, {name}")


greeting="Hello, {}"
print(greeting.format("Cris"))
name = "Jane"
print(greeting.format(name))


stringTemplate="{}x{}={}"
stringTemplate.format(str(5),str(4),str(5*4))
print(stringTemplate.format(str(5),str(4),str(5*4)))