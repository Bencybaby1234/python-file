# progrma to demonstrate use of regular expresion
import re

txt = "The rain in Spain"
# search the string to see  if it start  with 'the' and with spain
x = re.search("^The.*Spain$", txt)
print("search: " + str(x))

# print a lsit of all matches
x = re.findall("ai", txt)
print("FInd all: " + str(x))

# return an empty list if match found
x = re.findall("partugal", txt)
print("FInd all: " + str(x))

x = re.split(r"\s", txt)
print("Split:" + str(x))

# replace white space with character
x = re.sub(r"\s", "9", txt)
print("replace", x)

# replace 1st two occurence
x = re.sub(r"\s", "9", txt, 2)
print("replace", x)
