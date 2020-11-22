# -*- coding: utf-8 -*-

#It is good practice make sure that files are closed after used

path = "C:\\GitHub\\learning_python\\files\\files_03_text_file_example.txt"

# way 1: try+finally
try:
  f = open(path, "r")
  str_f_lines = f.read()
  print(str_f_lines)
finally:
  f.close()

# way 2: "with" statement
with open(path) as f:
  print(f.read())
