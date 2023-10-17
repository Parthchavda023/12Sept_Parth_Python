'''Write a Python function to get the largest number, smallest num and sum
of all from a list'''


# num=[10,20,30,40,50]

# l=max(num)
# s=min(num)
# sum=l+s

# print('Largest Number:',l)
# print('Smallest Number:',s)
# print('total=',sum)

#------------User Get Number----------#
# num=input("Enter Number(Press Space Button):").split()

# l=max(num)
# s=min(num)
# sum=int(l)+int(s)

# print('Largest Number:',l)
# print('Smallest Number:',s)
# print('total=',sum)

#---------With loop---------#
n=int(input('Enter Number of Range:'))
p=[]
sum=0

for i in range(n):
    s=int(input('Enter Number:'))
    p.append(s)

print(p)
p.sort()
print(p)
print('Small Number=',p[0])
print('Large Number=',p[-1])

for i in p:
    sum=sum+i

print('Sum of all elements in a list',sum)