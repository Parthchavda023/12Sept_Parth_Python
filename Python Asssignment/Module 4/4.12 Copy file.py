'''Write a Python program to copy the contents of a file to another file.'''


# fl=open('Copyfile.txt','w')
# fl.write('Hello...\n')
# fl.write("I'm Parth Chavda\n")
# fl.write('How are you???\n')

# fl=open('Copyfile.txt','r')
# #Copy file
# fl2=open('Copyfile2.txt','w')
# fl2.write(fl.read())


#-----user input------#
fl=open('Copyfile3.txt','w')
n=int(input("Enter number of Range:"))
for i in range(n):
    c=input('Enter Data:')
    fl.write(f'{c}\n')


fl=open('Copyfile3.txt','r')
fl2=open('Copyfile4.txt','w')
fl2.write(fl.read())