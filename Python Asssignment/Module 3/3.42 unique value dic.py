'''Write a Python program to print all unique values in a dictionary.'''



p={'a':1,'b':2,'c':3,'d':1,'e':3,'f':4}

print(p)
print(set(p.values()))


#-------User input-----#

p={}
n=int(input('Enter Number of Range:'))

for i in range(n):
    a=input('Enter Key:')
    b=input("Entee Value:")
    p[a]=b

print(p)
print(set(p.values()))