'''Write a Python program to reverse a tuple.'''

# p=('Parth',101,'Sanjay',103)

# print(p)
# s=p[::-1]
# print(s)

#------User Input-----#

p=[]
n=int(input('Enter NUmber of Range:'))

for i in range(n):
    s=input('Enter Data:')
    p.append(s)

# print(tuple(p))
# sp=p[::-1]
# print(sp)

print(p)
p.reverse()
sp=(tuple(p))
print(sp)