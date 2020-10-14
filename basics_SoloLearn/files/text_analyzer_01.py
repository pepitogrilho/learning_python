# -*- coding: utf-8 -*-

"""
v1
"""
filepath = "C:\\GitHub\\learning_python\\files\\text_analyzer_01_file_example.txt"

with open(filepath) as f:
    text = f.read()
    
print(text)



"""
v2
"""
def count_char(text, char):
    count=0
    for c in text:
        if c == char:
            count+=1
    return count


filepath = "C:\\GitHub\\learning_python\\files\\text_analyzer_01_file_example.txt"
with open(filepath) as f:
    text = f.read()

num_veces_01 = count_char(text,"e")    
print(num_veces_01)

"""
v3
"""
def count_char(text, char):
    count_all=0
    count_found=0
    for c in text:
        count_all+=1
        if c == char:
            count_found+=1
    return 100*(count_found/count_all)


filepath = "C:\\GitHub\\learning_python\\files\\text_analyzer_01_file_example.txt"
with open(filepath) as f:
    text = f.read()

num_veces_01 = count_char(text,"e")    
print(num_veces_01)
