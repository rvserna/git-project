"""examples continued"""

import re

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt, re.IGNORECASE)
print(res)

txt = 'The rain in Spain'
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\s", txt)

print(x)

txt = 'The rain in Spain'
x = re.sub('\s', '9', txt)

print(x)

txt = "The rain in Spain"
x = re.search('ai', txt)
print(x)

txt = 'The rain in Spain'
x = re.search(r'\bS\w+', txt)
print(x.string)

x = re.search(r'\bS\w+', txt)
print(x.group())
