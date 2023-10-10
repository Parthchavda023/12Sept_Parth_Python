'''Write a Python function that takes a list and returns a new list with unique
elements of the first list.'''


p=[1,1,1,2,5,3,3,4,5]
sp=[]
for i in p:
    if i not in sp:
        sp.append(i)

print('unique list:',sp)