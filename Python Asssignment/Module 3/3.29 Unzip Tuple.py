'''Write a Python program to unzip a list of tuples into individual lists.

like:-
input:[(101,'Parth'),(102,'Sanjay'),(103,'Vipul')]
output:
Id=[101,102,103]
Name=['Parth'.'Sanjay','Vipul']
'''


# p=[(101,'Parth'),(102,'Sanjay'),(103,'Vipul')]

# print(p)

# id,nm=zip(*p)
# print("Id=",id)
# print("Name",nm)

#-----Using Input-----#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    id=int(input('Enter ID='))
    nm=str(input('Enter Name='))
    p.append((id,nm))

print(tuple(p))

Id,Nm=zip(*p)
print("ID=",Id)
print("Name=",Nm)
