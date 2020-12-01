# -*- coding: utf-8 -*-
"""
A character class is created by putting the characters it matches inside square brackets
"""

import re


# "[aeiou]" > one single character

pattern = r"[aeiou]"
test_string = "grey"
if re.search(pattern, test_string):
    print(r"the pattern >"+pattern+"< is found (search) in the string >"+test_string+"<")
    
    
pattern = r"gr[aeiou]y"
test_string = "groy"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
    


# "[a-z]" > lower case
pattern = r"@[a-z]@"
test_string = "@x@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

# "[A-Z]" > upper case
pattern = r"@[A-Z]@"
test_string = "@X@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

# "[a-zA-Z]" > upper case
pattern = r"@[a-zA-Z]@"
test_string = "@X@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
test_string = "@x@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

# "[0-9]" > number
pattern = r"@[0-9]@"
test_string = "@3@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

# "[^0-9]" > number (^is like "not") > "characters different to "0-9"
pattern = r"@[^0-9]@"
test_string = "@3@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
test_string = "@x@"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
