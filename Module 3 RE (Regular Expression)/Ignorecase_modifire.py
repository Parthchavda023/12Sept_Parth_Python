import re

sp="PARTHchavda022@gmail.com"

c1=re.findall('[A-Z]',sp)
c2=re.findall('[a-z]',sp)
c3=re.findall('[A-Za-z]',sp)
c4=re.findall('[0-9]',sp)
c5=re.findall('[A-Za-z0-9]',sp)
print("A-Z=",c1)
print("a-z=",c2)
print("A-Za-z=",c3)
print("0-9=",c4)
print("A-Za-z0-9=",c5)