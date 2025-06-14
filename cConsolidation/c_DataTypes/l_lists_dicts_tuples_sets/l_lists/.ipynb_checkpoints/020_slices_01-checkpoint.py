# -*- coding: utf-8 -*-

#Slices can be also in tuples

"""
My first slices
"""
numbers=[0,1,2,3,4,5,6,7,8,9]

print(numbers[0:1])
print(numbers[0:2])
print(numbers[0:3])
print(numbers[0:4])

print(numbers[1:2])
print(numbers[1:3])
print(numbers[1:4])
print(numbers[1:5])

print(numbers[0:1])
print(numbers[1:2])
print(numbers[2:3])
print(numbers[3:4])


"""
negative index
"""
numbers=[0,1,2,3,4,5,6,7,8,9]

print(numbers[0:])
print(numbers[1:-1])
print(numbers[2:-2])
print(numbers[3:-3])


"""
Omitted start/end
"""
numbers=[0,1,2,3,4,5,6,7,8,9]

print(numbers[:4])
print(numbers[4:])


"""
3rd argument = step
"""
numbers=[0,1,2,3,4,5,6,7,8,9]

print(numbers[0:10:2])
print(numbers[0:10:3])
print(numbers[0:10:4])
print(numbers[0:10:5])


"""
negative 3rd argument
"""
numbers=[0,1,2,3,4,5,6,7,8,9]

print(numbers[::-1])
print(numbers[9::-1])
print(numbers[7:5:-1])
