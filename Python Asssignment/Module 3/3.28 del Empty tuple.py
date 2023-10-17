'''Write a Python program to remove an empty tuple(s) from a list of tuples.'''


p=[(1),(2),(14),(''),(10)]

# print(tuple(p)) 
# print(p)

for i in p:
    if len(p)==0:
     del p

print(tuple(p))
