'''Write a Python program to select an item randomly from a list. '''



# import random
# p=["Parth",1,"mehul",2,"Prakash",5,"Pankaj"]
# print(p)

# # Select Random choice
# sp=random.choice(p)
# print("Random choice:",sp)

#-------- User input------#

import random
p=[]
n=int(input("Enter Number Of Range:"))

for i in range(n):
    s=input("Enter Value of a List:")
    p.append(s)

y="y"
while y!="n":
    print(p)
    s=random.choice(p)
    print(s)

    print('Enter "y" to Refresh and "n" to Close program')
    y=input("Refresh:")