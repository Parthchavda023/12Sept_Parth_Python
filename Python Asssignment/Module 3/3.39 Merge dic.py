'''Write a Python script to merge two Python dictionaries.'''

# p={101:'Parth',102:'Prakash'}
# s={103:'Sanjay',104:'Mehul'}
# sp={}

# print('Dic1:',p)
# print('Dic2:',s)

# for i in (p,s):
#     sp.update(i)

# print('New Merge Dic:',sp)


#---user input---#

p={}
s={}
sp={}
n=int(input("Enter Number of Renge1:"))

for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    p[id]=nm


N=int(input('Enter number of Range2:'))
for j in range(N):
    ID=int(input('Enter Id:'))
    NM=str(input('Enter Name:'))
    s[ID]=NM

print('Dic1=',p)
print('Dic2=',s)

for k in (p,s):
    sp.update(k)

print('New Merge dic=',sp) 