'''Write a Python program to read a file line by line and store it into a list.'''


# fl=open('Readlist.txt','w')

# fl.write("Hello...\n")
# fl.write("I'm Parth Chavda\n")
# fl.write("I From Halvad\n")
# fl.write('How are you???')

# print('Read File:-')
# fl=open('Readlist.txt','r')
# print(fl.read())

# print('Store in a List:-')
# fl=open('Readlist.txt','r')
# print(fl.readlines())


#------user input-------#
fl=open('Readlist2.txt','w')
n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    fl.write(f'{id}-{nm}\n')

print('Read file:-')
fl=open('Readlist2.txt','r')
print(fl.read())

print('Store in a List:-')
fl=open('Readlist2.txt','r')
print(fl.readlines())