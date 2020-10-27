# -*- coding: utf-8 -*-
"""
"." > one single character
"^" > start character
"$" > start character
"""


# "." > one single character
import re

pattern = r"gr.y"

test_string = "grey"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
    
test_string = "groy"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
    

# "^" > first character
    
pattern = r"^g..."
test_string = "grey"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")


# "$" > last character
    
pattern = r"...y$"
test_string = "grey"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
    