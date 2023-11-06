''' Write a Python program to check if a number is positive, negative or zero. '''

p=int(input("Enter Number:"))

if p==0:
    print(f"{p} = Zero")
elif p<0:
    print(f"{p} = Negative Number")
else :
    print(f"{p} = Positive Number")