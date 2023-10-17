'''Write a Python program to get unique values from a list'''


n=int(input("Enter Range of Number:"))
p=[]

for i in range(n):
    x=input("Enter value:")
    if x not in p:
        p.append(x)
    
print('unique list name:-',p)