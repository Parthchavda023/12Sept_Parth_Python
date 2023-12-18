'''Write a Python program to write a list to a file.'''



# p=['101-','Parth','102-','Sanjay','103-','Vipul']
# fl=open('Listwrite.txt','w')
# fl.write(' '.join(p))

# fl=open('Listwrite.txt','r')
# data=fl.read()
# p=data.split()
# print(p)

#--------User Input---------#

p=[]
n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    p.append(f'{id}-{nm}')

print(p)
fl=open('Listwrite2.txt','w')
for i in p:
    fl.write(i+"\n")

fl=open('Listwrite2.txt','r')
print(fl.read())