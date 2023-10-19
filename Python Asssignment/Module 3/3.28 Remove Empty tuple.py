'''Write a Python program to remove an empty tuple(s) from a list of tuples.'''


# p=[(1,2),(),(3,4),(),(5,6),('Parth','Sanjay'),('')]

# print('Original list:',p)

# for i in p:
#     if not i:
#         p.remove(i)

# print('Remove Empty Tuple:',tuple(p))

#-----Using input-----#

p=[]
n=int(input('Enter Number of Range:'))

for i in range(n):
    s=input('Enter Data:')
    p.append(s)


print(tuple(p))

for i in p:
    if not i:
        p.remove(i)

print(tuple(p))