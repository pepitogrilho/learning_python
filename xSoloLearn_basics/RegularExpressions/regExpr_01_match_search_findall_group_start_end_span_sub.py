# -*- coding: utf-8 -*-
"""
To avoid any confusion while working with regular expressions,
we would use RAW STRINGS as ...
... r"expression"
"""

import re

pattern = r"spam"
print(re.match(pattern, "spamspamspam"))

pattern = r"pam"
print(re.match(pattern, "spamspamspam"))

#........................................

pattern = r"pam"
print(re.search(pattern, "eggsspamsausagespam"))

#........................................

pattern = r"pam"
print(re.findall(pattern, "eggsspamsausagespam"))

#........................................

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())
   
#........................................

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)