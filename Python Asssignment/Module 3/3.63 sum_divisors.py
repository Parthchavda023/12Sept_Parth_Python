'''Write a Python program to returns sum of all divisors of a number'''



p=[1]
n=int(input("Enther Number:-"))
for i in range(2,n):
    if (n % i) == 0:
        p.append(i)
        
print(sum(p))