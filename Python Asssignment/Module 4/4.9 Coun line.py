'''Write a Python program to count the number of lines in a text file.'''


# fl=open('countline.txt','w')
# fl.write('Hello...\n')
# fl.write("I'm Parth Chavda\n")
# fl.write('I from Halvad\n')
# fl.write('Thank You !!!\n')

# fl=open('countline.txt','r')
# #count line
# cl=len(fl.readlines())
# print(cl)


#------User Input------#
fl=open('countline2.txt','w')
n=int(input('Enter number of Range:'))

for i in range(n):
    data=input('Enter Data:')
    fl.write(data +'\n')

fl=open('countline2.txt','r')
cl=len(fl.readlines())
print('Lines:',cl)