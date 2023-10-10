'''Write a Python program to get unique values from a list'''


p=int(input("Enter Range of Number:"))
nm=[]
lnm=[]

for i in range(p):
    name=input("Enter Name:")
    if name not in nm:
        nm.append(name)
    
print('unique list name:-',nm)