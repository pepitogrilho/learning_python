# -*- coding: utf-8 -*-
"""
"""

name = input("Enter your name:")
print("Hello {}".format(name))
print(f"Hello {name}")


size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print("Your house is {} square metres.".format(square_metres))
print(f"Your house is {square_metres} square metres.")
print(f"Your house is {square_metres:.2f} square metres.")
