'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.'''

a=int(input("Enter Value Of A:"))
b=int(input("Enter Value Of B:"))
c=int(input("Enter Value Of C:"))

if a==b or b==c or c==a:
    print("Two value are equal so sum will be 0")
else :
    print(f"Sum is {a}+{b}+{c}={a+b+c}")