''' Write a Python function to reverses a string if its length is a multiple of 4.'''

p=input("enter a name:")

if(len(p)%4<=0):
    print(p)
else:
    print(p[::-1])