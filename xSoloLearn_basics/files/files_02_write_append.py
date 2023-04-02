# -*- coding: utf-8 -*-

#When a file is opened in write mode, the file's content is DELETED!

file_path = "C:\\GitHub\\learning_python\\pepe.txt" 

#re-write content
f_write = open(file_path, "w")
count=f_write.write("eeeeeeeeoooooooooo\n")
f_write.close()
f_read = open(file_path, "r")
print(f_read.read())
f_read.close()
print(count," bytes written")

#re-write content
f_write = open(file_path, "w")
f_write.writelines(["xxxxxx\n","yyyyyy\n","zzzzzz\n"])
f_write.close()
f_read = open(file_path, "r")
print(f_read.read())
f_read.close()

#append content
f_append = open(file_path, "a")
f_append.write("eeeeeeeooooooooo")
f_append.close()
f_read = open(file_path, "r")
print(f_read.read())
f_read.close()
