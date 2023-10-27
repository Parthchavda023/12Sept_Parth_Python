'''Write a Python program to read a random line from a file.'''


import random
fl=open('Datetime.txt','r')
s=fl.read()
sp=list(map(str,s.split(',')))
csp=random.choice(sp)
print("Random line from file:",csp)

# p=[]
# n=int(input("Enter Number of Range:"))
# for i in range(n):
#     x=input("Enter File Data:")
#     p.append(x)

# fl=open('randomfile.txt','w')
# fl.write(str(p))

# import random
# fl=open('randomfile.txt','r')
# s=fl.read()
# sp=list(map(str,s.split(',')))
# csp=random.choice(sp)
# print("Random line from file:",csp)