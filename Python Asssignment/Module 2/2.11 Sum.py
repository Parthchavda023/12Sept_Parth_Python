'''Write a python program to sum of the first n positive integers.'''



p=int(input("Enter Number:"))
sum=0
for i in range(1,p+1):
    if p>0:
        sum+=i
    else:
        print('Enter Positive Number')

print("Sum is=",sum)



# -------------------------------#
# p=int(input("Enter Number:"))
# sum=(p*(p+1))/2

# if p<=0:
#     print("Plz enter positive number")
# else:
#     print("Sum is=",sum)