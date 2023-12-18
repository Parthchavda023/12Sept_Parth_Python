'''Write a Python program to remove duplicates from a list.'''


p=int(input("Enter number of Name:"))
nm=[]

for i in range(p):
    s=input("Enter Name:")
    if s in nm:
        print("Dublicae Name...")
    else:
        nm.append(s)
    
print("Name=",nm)