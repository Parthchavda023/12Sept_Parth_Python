'''Write a Python program to read a random line from a file.'''


# fl=open('randomfile.txt','w')
# fl.write('101-Parth\n')
# fl.write('102-Sanjay\n')
# fl.write('103-Prakash\n')
# fl.write('104-Raj\n')
# fl.write('105-Om\n')
# fl.write('106-Rajveer\n')
# fl.write('107-Mehul\n')

# import random
# fl=open('randomfile.txt','r')
# s=fl.readlines()
# sp=random.choice(s)
# print("Random line from file:",sp)


#------User inpu-----#

fl=open('randomfile2.txt','w')
n=int(input("Enter Number of Range:"))
for i in range(n):
    id=input('Enter Id:')
    nm=input("Enter Name:")
    fl.write(f'{id}-{nm}\n')

import random
fl=open('randomfile2.txt','r')
s=fl.readlines()
sp=random.choice(s)
print("Random line from file:",sp)