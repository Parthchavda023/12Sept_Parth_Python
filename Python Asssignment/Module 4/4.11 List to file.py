'''Write a Python program to write a list to a file.'''


p=[]
n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    p.append(f'{id}-{nm}')

print(p)
fl=open('Listwrite.txt','w')
for i in p:
    fl.write(i+"\n")