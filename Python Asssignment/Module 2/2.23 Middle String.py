''' Write a Python function to insert a string in the middle of a string.'''

a=input("enter str:")
b=input("Enter Second(middle) str:")

if len(a):
    print(a[:2] +b+ a[2:])
else:
    print("sorry...!")