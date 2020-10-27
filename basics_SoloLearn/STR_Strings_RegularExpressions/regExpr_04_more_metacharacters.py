# -*- coding: utf-8 -*-
"""
"*" > zero or more repetitions of the previous "thing"
"?" > zero or more repetitions 
"+" > one or more repetitions of the previous "thing"
"{" and "}" > number of repetitions
"""


# "(thing)*" > ZERO or more prepetitions of "thing"
import re

pattern = r"egg(spam)*"

test_string = "egg"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "eggspam"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "eggspamspam"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

# "(thing)?" > ZERO or more prepetitions of "thing"
import re

pattern = r"egg(spam)?"

test_string = "egg"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "eggspam"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "eggspamspam"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")


# "(thing)+" > ONE or more prepetitions of "thing"
import re

pattern = r"egg(spam)+"

test_string = "egg"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "eggspam"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")


# "{}" > number of repetitions
import re

pattern = r"^9{1,3}$"

test_string = "8"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "9"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "99"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "999"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")

test_string = "9999"
if re.match(pattern, test_string):
    print(r"the pattern >"+pattern+"< matches with the string >"+test_string+"<")
