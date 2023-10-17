p=int(input("Enter number of Name:"))
nm=[]

for i in range(p):
    name=input("Enter Name:")
    if name in nm:
        print("Dublicae Name...")
    else:
        nm.append(name)
    
print("Name=",nm)