'''Write a python program to sum of the first n positive integers.'''

p=int(input("Enter Number:"))
sum=(p*(p+1))/2

if p<=0:
    print("Plz enter positive number")
else:
    print("Sum is=",sum)