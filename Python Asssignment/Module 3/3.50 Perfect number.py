'''Write a Python function to check whether a number is perfect or not.

    ->First of all,a perfect number is a positive integer that is equal to the sum 
of its proper positive divisors, that is the sum of its positive divisors excluding 
the number itself.
    ->a perfect number is a number that is half the sum of all of its positive divisors.
Example :
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors,
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its 
positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is
28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128
'''

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum=sum+i
    return sum

n =int(input("Enter a Number:-"))
s=perfect(n)
if n == s:
    print(f"{n} Number Is Perfect ...")
else:
    print(f"{n} Number Is not Perfect......")
