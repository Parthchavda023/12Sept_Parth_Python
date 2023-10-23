'''Write a Python script to concatenate following dictionaries to create a new one'''


# p={101:'Parth',102:'Sanjay'}
# s={103:'vipul',104:'Pankaj'}
# sp={}

# print('Dic1:',p)
# print('Dic2',s)

# for i in (p,s):
#     sp.update(i)

# print('New Dic:',sp)


#----User Input-----#

p={}
s={}
sp={}
n=int(input("Enter Number of Renge1:"))

for i in range(n):
    id=int(input('Enter Id='))
    nm=str(input('Enter Name='))
    p[id]=nm


N=int(input('Enter number of Range2:'))
for j in range(N):
    ID=int(input('Enter Id='))
    NM=str(input('Enter Name='))
    s[ID]=NM

print('Dic1',p)
print('Dic2=',s)

for k in (p,s):
    sp.update(k)

print('New dic=',sp) 