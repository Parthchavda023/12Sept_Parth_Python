'''Write a Python program to get the Fibonacci series of given range.'''

p=int(input("Enter Number:"))
a=0
b=1

for i in range(p):
    if p<=0:
        print("Plz enter a positive number...")
    else:
        print(a,end=" ")
        c=a+b
        a=b
        b=c