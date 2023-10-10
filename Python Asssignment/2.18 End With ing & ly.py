"""Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged."""


p=input("Enter Sring:")

#-------Nested Statement---------#
if len(p)>2:
    if p.endswith("ing"):
        p += 'ly'
    else:
       p +='ing'

print(p)

#--------If else Statement-------#
# if len(p)<3:
#     print(p)
# elif p[-3:]=='ing':
#     print(p+'ly')
# else :
#     print(p+'ing')