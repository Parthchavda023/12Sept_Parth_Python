import re 

sp="Hello I'm Parth Chavda022"
c1=re.findall('P...h',sp)
c2=re.findall('Pa..h',sp)
c3=re.findall('PARTH|Parth',sp)
c4=re.findall('[A-Z]|[a-z]|[0-9]',sp)
c5=re.findall('[A-Z]|[a-z]',sp)
print('P...h=',c1)
print('Pa..h=',c2)
print('PARTH|Parth=',c3)
print('[A-Z]|[a-z]|[0-9]=',c4)
print('[A-Z]|[a-z]',c5)