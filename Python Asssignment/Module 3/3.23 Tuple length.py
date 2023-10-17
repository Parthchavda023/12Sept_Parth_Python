''' Write a Python program to find the length of a tuple. '''


# p=(101,'Parth',102,'Sanjay',103,'Vipul')

# print(p)
# print('Length=',len(p))

#---User Input----#
p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=input('Enter Value:')
    p.append(s)

print(tuple(p))
print(len(p))
