'''Write a Python program to remove duplicates from a list'''


s=[]

n=int(input("Enter Number of Range:-"))
for i in range(n):
    x=input("Enter Value:-")
    if x not in s:
        s.append(x)

print(s)