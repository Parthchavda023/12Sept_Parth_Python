'''Write a Python script to merge two Python dictionaries.'''

p={101:'Parth',102:'Prakash'}
s={103:'Sanjay',104:'Mehul'}
sp={}

print('Dic1:',p)
print('Dic2',s)

for i in (p,s):
    sp.update(i)

print('New Merge Dic:',sp)