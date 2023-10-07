p=int(input("Enter Nimber of range:"))
nm=[]
for i in range(p):
    name = input("Enter Name: ")
    if name in nm:
        print("Duplicate Name!!! Plz enter different name...")
        
    else:
        nm.append(name)

print("Name=",nm)