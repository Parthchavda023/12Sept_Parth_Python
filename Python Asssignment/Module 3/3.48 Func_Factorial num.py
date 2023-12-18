'''Write a Python function to calculate the factorial of a number (a nonnegative integer)'''

# def fact():
#     p=int(input("Enter Number:"))
#     fac=1

#     if p>=1:
#         for i in range(1,p+1):
#             fac=i*fac
#         print(f'The factorial of {p} is {fac}')
#     elif p==0:
#         print("The factorial of 0 is 1")
#     else:
#         print("Error, factorial does not exit for negative numbers")

# fact()


#-----impotr Math Module------#
def fact():
    p=int(input("Enter Number:"))
    if p>=1:
        import math
        s=math.factorial(p)
        print(f'The factorial of {p} is {s}')
    elif p==0:
        print("The factorial of 0 is 1")
    else:
        print("Error, factorial does not exit for negative numbers")

fact()