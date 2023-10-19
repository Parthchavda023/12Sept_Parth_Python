'''Write a Python program to find the repeated items of a tuple.'''


# p=(1,2,2,3,4,4,5,5,6,6,7)   # output=(2,4,5,6)
# s=[]

# print('Original Number:',p)

# for i in p:
#     if p.count(i)>1:
#         if i not in s:
#             s.append(i)

# print("Repeat Number:",tuple(s))


#----User input-----#

p=[]
s=[]
n=int(input('Enter number of range:'))

for i in range(n):
    sp=input("Enter Number:")
    p.append(sp)

print(tuple(p))

for j in p:
    if p.count(j)>1:
        if j not in s:
            s.append(j)
        
print(tuple(s))