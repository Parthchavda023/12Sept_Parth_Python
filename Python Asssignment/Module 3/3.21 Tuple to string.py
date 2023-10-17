'''Write a Python program to convert a tuple to a string.'''


# p=('P','a','r','t','h')

# print(p)
# s=''.join(p)
# print(s)


#-----User input-----#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    s=input("Enter str Character:")
    p.append(s)

print(tuple(p))
print(p)

print(''.join(p))