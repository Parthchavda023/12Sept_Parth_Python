'''Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers.'''


# #-----sort() method------#
# dcnum=[11.5,0.05,1.05,1.10,63.65,6.60,1.0]
# print(dcnum)

# dcnum.sort()
# print('Sort list=',dcnum)
# print('Min. number:',dcnum[0])
# print('Max number:',dcnum[-1])


# #-----max,min fuction----#
# dcnum=[11.5,0.05,1.05,1.10,63.65,6.60,1.0]
# print(dcnum)
# print('Min. Number=',min(dcnum))
# print('Max Number=',max(dcnum))


#----user input-----
p=[]
n=int(input('Enter Number of Range:'))

for i in range(n):
    s=float(input('Enter Decimal Number:'))
    p.append(s)

print(p)
print('#-----with sort()----#')
p.sort()
print(p)
print('Min. number:',p[0])
print('Max number:',p[-1])
#----------------------------------#
print('#----max,min function-----#')
print('Min. Number=',min(p))
print('Max Number=',max(p))
