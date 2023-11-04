'''Write a Python program to read a file line by line store it into a variable.'''


# fl=open('Readlinebyline.txt','w')
# fl.write('Hello...\n')
# fl.write("I'm Parth Chavda\n")
# fl.write('How are you???\n')

# fl=open('readlinebyline.txt','r')
# print(fl.read())


#----User input-----#
fl=open('Readlinebyline2.txt','w')
n=int(input('Enter Number of Range:'))
for i in range(n):
    p=input(f'Enter Line{[i+1]}:')
    fl.write(f'{p}\n')

fl=open('Readlinebyline2.txt','r')
print(fl.read())