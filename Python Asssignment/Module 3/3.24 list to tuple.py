'''Write a Python program to convert a list to a tuple.'''


# p=[10,'Parth',102,'Sanjay',105,'Vipul']

# print(p)
# print(type(p))

# s=tuple(p)
# print(s)
# print(type(s))


#------User input-----#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=input('Enter Elements:')
    p.append(s)

print(p)
print(type(p))

sp=tuple(p)
print(sp)
print(type(sp))