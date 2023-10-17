'''Write a Python program to check whether a list contains a sub list'''


# p=[1,2,3,4,5,6]
# s=[1,2]

# print(s)
# p.append(s)
# print(p)

# if s in p:
#     print('Sublist in a list')
# else:
#     print('Sublist not in a list')

#------User input-------#

p=[]
s=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=input("Enter Your Data:")
    p.append(x)

print(p)

d=int(input("Enter Number of data:"))
for i in range(d):
    y=input("Enter Your Data:")
    s.append(y)

print(s)
p.append(s)
print(p)

if s in p:
    print("Sublist In List")
else:
    print("No Sub List in List")