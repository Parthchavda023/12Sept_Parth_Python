'''Write a Python program to read an entire text file.'''


# fl=open('Datetime.txt','r')
# print(fl.read())


#-----user input------#
fl=open('Read.txt','w')
n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    fl.write(f'{id}-{nm}\n')

print('-------------')
fl=open('Read.txt','r')
print(fl.read())