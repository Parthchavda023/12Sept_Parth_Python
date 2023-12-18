'''Write a Python program to get the Factorial number of given number
Factorial 5=120 (5*4*3*2*1)'''


#--------Using While loop------#
# p=int(input("Enter Number:"))
# fac=1

# while(p>0):
#     fac=fac*p
#     p=p-1
# print(f"Factorial {p} = {fac}")


#--------Using For loop------#
# p=int(input("Enter Number:"))
# fac=1

# for i in range(1,p+1):
#     fac=i*fac
# print(f"Factorial {p} = {fac}")


#-----impotr Factorial Module------#
import math

s=int(input("Enter Numbe:"))
p=math.factorial(s)
print('Factorial=',p)