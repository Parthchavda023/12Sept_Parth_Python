import re

sp="""
    Hello friend's
    I'm Parth Chavada
    I from Halvad
    Good Morning !!!
                    """
c1=re.findall('Chavada',sp)
c2=re.findall('va',sp)
c3=re.findall('a',sp)
print(c1)
print(c2)
print(c3)