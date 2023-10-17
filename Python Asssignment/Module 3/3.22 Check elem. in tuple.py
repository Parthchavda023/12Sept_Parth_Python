'''Write a Python program to check whether an element exists within a tuple.'''


# p=(10,'Parth',20,'Sanjay',103,'Vipul')

# if 'Parth' in p:
#     print("The element is in the Tuple")
# else:
#     print('The element is not in the Tuple')

#-----user input------#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=input("Enter Elements:")
    p.append(s)

print(tuple(p))

sp=input("Enter Check Elements=")

if sp in p:
    print('The element is in the Tuple')
else:
    print('The element is not in the Tuple')