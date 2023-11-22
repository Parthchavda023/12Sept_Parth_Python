import re
# To match only the beginning of the string

sp='Hello My Name is Parth Chavda'
c1=re.match('Hello',sp)
c2=re.match('hello',sp)
c3=re.match('Parth',sp)
print(c1)
print(c2)
print(c3)