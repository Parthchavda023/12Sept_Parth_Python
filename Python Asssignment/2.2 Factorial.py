'''Write a Python program to get the Factorial number of given number
Factorial 5=120 (5*4*3*2*1)'''


p=int(input("Enter Number:"))
fac=1

while(p>0):
    fac=fac*p
    p=p-1

print(f"Factorial {p} = {fac}")

# for i in range(1,p+1):
#     fac=i*fac

# print(f"Factorial {p} = {fac}")