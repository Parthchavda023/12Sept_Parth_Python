import re

#A,Z D-d, S-s, W-w

sp="ParthChavda022@ gmail.COM!!!333"
A=re.findall('\AParth',sp)   # Match only at the start of the string
print("A=",A)

Z=re.findall('33\Z',sp)   # Match only at the end of the string
print("Z=",Z)

D=re.findall('\D',sp)   # Not match(Ignore) Digital number
d=re.findall('\d',sp)   # Match(Print) only Digital number  
print("D=",D)
print("d=",d)

S=re.findall('\S',sp)   #Not match(Ignore) Space
s=re.findall('\s',sp)   # Match (Print) Space
print("S=",S)
print("s=",s)

W=re.findall('\w',sp)   # Not match(Ignore) special character
w=re.findall('\W',sp)   # Match(Print) Special character
print("W=",W)
print("w=",w)