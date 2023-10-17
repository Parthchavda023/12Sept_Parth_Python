'''Write a Python program to replace last value of tuples in a list.'''


# p=['Parth','Sanjay','Vipul','Mehul','Pankaj','Hardik']

# print(p)

# p.pop()
# print(p)

# p.append('Prakash')
# print(p)


#------user input-------#

p=[]
n=int(input('Enter Number of Range:'))

for i in range(n):
    s=input("Enter Element:")
    p.append(s)

print(tuple(p))

p.pop()
print(p)

N=input("Enter New Element:")

p.append(N)
print(p)