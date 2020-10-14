# -*- coding: utf-8 -*-

path = "C:\\GitHub\\learning_python\\files\\files_01_text_file_example.txt"

#Put text into a STRING
f = open(path, "r")
str_f_lines = f.read()
print(str_f_lines)
f.close()

#Put text lines into a LIST
f = open(path, "r"); print(type(f))
list_f_lines = f.readlines()
for line in list_f_lines:
    print(line)
f.close()

#Read line by line
f = open(path, "r"); print(type(f))
for line in f:
    print(line)
f.close()

#Read char by char
f = open(path, "r")
text = f.read()
for char in text:
    print(char)
f.close()

