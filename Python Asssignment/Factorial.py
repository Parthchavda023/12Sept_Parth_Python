# Factorial 5=120 (5*4*3*2*1)

p=int(input("Enter Number:"))
fac=1

for i in range(1,p+1):
    fac=i*fac

print(f"Factorial {p} = {fac}")