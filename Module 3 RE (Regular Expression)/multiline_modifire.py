import re 

sp="Hey I'm Parth Chavda"
c1=re.findall('^Hey',sp)    # ^ in start \\ Match only at the start of the string
c2=re.findall('Hey$',sp)    
c3=re.findall('^[A-Z]',sp)  # 1st character capital so print 
c4=re.findall('^[a-z]',sp)  # 1st character small so print
c5=re.findall('[^a-z]',sp)  # Only capital character with space and special simbol
c6=re.findall('[^A-Z]',sp)  #Only small character with space and special simbol
c7=re.findall('Chavda$',sp) # $ in end \\ Match at the end of a line
print("1)^Hey=",c1)
print("2)Hey$=",c2)
print("3)^[A-Z]=",c3)
print("4)^[a-z]=",c4)
print("5)[^a-z]=",c5)
print("6)[^A-Z]=",c6)
print("7)chavda$=",c7)