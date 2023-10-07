'''Write a python program to sum of the first n positive integers.'''

p=int(input("Enter Number of Range:"))
sum=0

for i in range(p):
    n=int(input("Enter Number of Value:"))
    sum+=n

print("Sum is=",sum)