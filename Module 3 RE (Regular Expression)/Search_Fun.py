import re

sp="Hello, I'm Parth Chavda"
# c1=re.search('Parth',sp)
# c2=re.search('arth',sp)
# c3=re.search('parth',sp)
# print(c1)
# print(c2)
# print(c3)

# ------------------------
# c=re.search('Parth',sp)
c=re.search('parth',sp)
print(c)

if c:
    print("True") 
else:
    print("False")