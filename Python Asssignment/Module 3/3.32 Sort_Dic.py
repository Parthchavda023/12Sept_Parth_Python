'''Write a Python script to sort (ascending and descending) a dictionary by value.'''


'''
p={103:'Parth',101:'Sanjay',102:'Vipul'}

print('Original Dictionary:',p)

#----sorting in ascending--#
s=dict(sorted(p.items()))
print('Ascending=',s)

#---sorting in descending---#
# sp=dict(reversed(s.items()))    #jo pahela thi j dictionary ne sort kri hoy tyare
sp=dict(sorted(p.items()))        # nahitar pahela dic ne sort kri ne reversed krvi
csp=dict(reversed(sp.items()))
print('Descending=',csp)
'''

#-----User input----#
p={}
n=int(input('Enter Number of Range:'))

for i in range(n):
    id=int(input('Enter Id Number:'))
    nm=str(input('Enter Name:'))
    p[id]=nm

print('Original Dictionary=',p)

#----sorting in ascending--#
s=dict(sorted(p.items()))
print('Ascending=',s)

#---sorting in descending---#
sp=dict(reversed(s.items()))
print('Discending=',sp)