'''Write a Python program to convert a list of tuples into a dictionary.'''


# p=[(101,'Parth'),(102,'Sanjay'),(103,'Vipul')]

# print(p)
# print(type(p))

# s=tuple(p)
# print(s)
# print(type(s))

# sp=dict(p)
# print(sp)
# print(type(sp))

#-----User inout----#
# p=[]
# n=int(input("Enter Number of Range:"))

# for i in range(n):
#     s=input("Enter Id=")
#     S=input("Enter Name=")
#     p.append((s,S))

# print(p)
# print(type(p))

# sp=tuple(p)
# print(sp)
# print(type(sp))

# csp=dict(zip(*zip(*p)))
# print(csp)
# print(type(csp))

#------User input with key & items Methods-----#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=input("Enter Id=")
    S=input("Enter Name=")
    p.append((s,S))

sp=(dict(p))
print(sp[key]=value)
