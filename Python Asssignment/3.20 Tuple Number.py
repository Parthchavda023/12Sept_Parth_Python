'''Write a Python program to create a tuple with numbers.'''

# p=(10,20,30,40)

# print(p)

#-----User input----#

p=[]
n=int(input("Enter number of Range:"))

for i in range(n):
    s=int(input("Enter Only number:"))
    p.append(s)

print(tuple(p))