'''Write a Python program to find the second smallest number in a list. '''


# p=[10,20,60,40,80,5,2,3,90]
# print(p)

# p.sort()
# print(p)
# print(f'{p[1]} is Second Smallest number')

#-----User input-----#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=int(input('Enter Number:'))
    p.append(s)

p.sort()
print(p)
print(f'{p[1]} is second Smallets numbe in a list')