'''Write a Python function that takes two lists and returns true if they have
at least one common member. '''



# p=['Parth','Sanjay','Vipul']
# s=['Mehul','Pankaj','Parth']

# for i in p:
#     if i in s:
#         print("True...")
#         break
#     else:
#         print('False..')
#         break

#-----User Input------#

#List - 1
p=[]
n=int(input("Enter Number of Range(List 1):"))
for i in range(n):
    a=input("Enter Value of a list 1:")
    p.append(a)

#List - 2
s=[]
N=int(input("Enter Number of Range(List 2):"))
for j in range(N):
    b=input("Enter Value of a list 2:")
    s.append(b)

print(p)
print(s)

for i in p:
    if i in s:
        print('True')
        break
    else:
        print("False")
        break

