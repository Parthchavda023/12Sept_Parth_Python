'''Write a Python function that takes a list and returns a new list with unique
elements of the first list.'''


# p=[1,1,1,2,5,3,3,4,5]
# sp=[]
# for i in p:
#     if i not in sp:
#         sp.append(i)

# print('Original List:',p)
# print('unique list:',sp)

#-------User input-------#

p=[]
sp=[]
n=int(input('Enter Number of Range:'))

for i in range(n):
    s=input('Enter Value:')
    p.append(s)

p.sort()
print('Original List:',p)

for i in p:
    if i not in sp:
        sp.append(i)

sp.sort()
print('Unique List:',sp)